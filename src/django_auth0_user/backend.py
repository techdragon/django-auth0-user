from social_core.backends.open_id_connect import OpenIdConnectAuth
from django.conf import settings
from social_core.exceptions import AuthCanceled, AuthTokenError, AuthFailed
import base64, json, hmac, hashlib
from calendar import timegm
from datetime import datetime
import logging


log = logging.getLogger(__name__)


class Auth0OpenId(OpenIdConnectAuth):
    """Auth0 OpenID authentication backend"""
    name = 'auth0'
    # TODO: Fetch this from Django Settings.
    OIDC_ENDPOINT = getattr(settings, 'AUTH0_OIDC_URL')
    ID_TOKEN_ISS = getattr(settings, 'AUTH0_OIDC_URL') + "/"
    USERNAME_KEY = 'user_id'

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token, token_type, and extra defined names to store in
            extra_data field"""
        data = super(Auth0OpenId, self).extra_data(user, uid, response, details=details, *args, **kwargs)
        # TODO work out why the id_token here has not been decyphered because that may be a better place to do this.
        data['token_type'] = response.get('token_type') or kwargs.get('token_type')
        data['id_token_payload'] = self.id_token
        return data
