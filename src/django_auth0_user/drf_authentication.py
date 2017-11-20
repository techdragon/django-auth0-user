# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
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


class SocialAuthentication(BaseAuthentication):
    """
    `python-social-auth` based django rest framework authentication.

    Clients authenticate using the token key in the "Authorization"
    HTTP header. For example:

        Authorization: Bearer g87ewgbgg78wegpngxgfoawgbo78aegnafxngfe
    """
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
