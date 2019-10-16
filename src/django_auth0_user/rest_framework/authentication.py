# -*- coding: utf-8 -*-
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
from rest_framework import HTTP_HEADER_ENCODING
from social_core.exceptions import MissingBackend
from social_core.exceptions import AuthForbidden
from social_core.utils import requests
from social_django.views import NAMESPACE
from social_django.utils import load_backend
from social_django.utils import load_strategy
import jwt
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.authentication import get_user_model
from rest_framework_jwt.authentication import jwt_get_username_from_payload
from rest_framework_jwt.authentication import jwt_decode_handler


class FastAuth0Authentication(JSONWebTokenAuthentication):
    """
    A fast django rest framework authentication class powered by djangorestframework-jwt.

    This only performs JWT validation and user lookup, it will not work for new
    users which is why it needs to be used along with the full drf auth class
    and must be placed before the full class in the DRF auth classes list.
    Clients authenticate using the token key in the "Authorization" HTTP header. For example:

        Authorization: Bearer g87ewgbgg78wegpngxgfoawgbo78aegnafxngfe
    """
    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()
        username = jwt_get_username_from_payload(payload)

        if not username:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            return  # Fallthru

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        jwt_value = self.get_jwt_value(request)
        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)

        if not user:
            return  # Fall-Through to next auth system

        return user, jwt_value


class FullAuth0Authentication(BaseAuthentication):
    """
    A full django rest framework authentication class powered by `python-social-auth`.

    This completes the full authentication process using PSA. This includes
    fetching profile details etc, from Auth0, as a consequence this can take
    a second or two to complete the full round trip.
    Clients authenticate using the token key in the "Authorization" HTTP header. For example:

        Authorization: Bearer g87ewgbgg78wegpngxgfoawgbo78aegnafxngfe
    """
    # TODO: This should probably be configured via a setting key.
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        """
        Authenticate the request and return a two-tuple of (user, token).
        """
        auth_header = get_authorization_header(request).decode(HTTP_HEADER_ENCODING)

        auth_parts = auth_header.split()

        if len(auth_parts) == 0:
            # No authentication header means we have nothing to work with.
            return None
        elif len(auth_parts) == 1:
            msg = 'Invalid token header. Credentials not provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth_parts) > 2:
            msg = 'Invalid token header. The token string cannot contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        auth_type, auth_token = auth_parts[0], auth_parts[1]

        if auth_type.lower() != 'bearer':
            msg = 'Invalid authentication header type. Only Bearer tokens are currently supported..'
            raise exceptions.AuthenticationFailed(msg)

        strategy = load_strategy(request=request)

        try:
            backend = load_backend(strategy, 'auth0', reverse(NAMESPACE + ":complete", args=('auth0',)))
        except MissingBackend:
            msg = 'Either token header is invalid or the backend could not be loaded.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = backend.do_auth(access_token=auth_token)
        except AuthForbidden as err:
            raise exceptions.AuthenticationFailed(err)
        except requests.HTTPError as e:
            msg = e.response.text
            raise exceptions.AuthenticationFailed(msg)

        if not user:
            msg = 'Unable to authenticate these credentials.'
            raise exceptions.AuthenticationFailed(msg)
        return user, auth_token

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return 'Bearer realm="%s"' % self.www_authenticate_realm
