from social_core.backends.open_id_connect import OpenIdConnectAuth
import logging
from six.moves.urllib_parse import urlencode, unquote
from django_auth0_user.settings import AUTH0_OIDC_ENDPOINT

from jose import jwk, jwt
from jose.utils import base64url_decode

# from django.conf import settings
# from social_core.exceptions import AuthCanceled, AuthTokenError, AuthFailed
# import base64, json, hmac, hashlib
# from calendar import timegm
# from datetime import datetime

log = logging.getLogger(__name__)


# TODO: Handle both OpenID Compliant and non-OpenID compliant Auth0 clients!
# ^ This may need some clever test setup to test against 2 sets of Auth0 client details.

# TODO: Add an option to ensure that metadata is returned via rules, using the Management API to set them up for users.
# https://auth0.com/docs/api/management/v2#!/Rules/get_rules

# TODO: Use Django's checks framework/tools to warn about misconfiguration.
#       e.g. OIDC Compliance + No Rule to include Metadata + Some future feature that depends on metadata.


# Valid Lock v10 Configuration Parameters via Query String Arguments
# http://auth0.com/docs/libraries/lock/v10/configuration
AUTH0_ALLOWED_URL_PARAMETERS = (
    # Display
    'allow_autocomplete',
    'allowed_connections',
    'allow_show_password',
    'autoclose',
    'autofocus',
    'avatar',
    'closable',
    'container',
    'language',
    'language_dictionary',
    'popup_options',
    'remember_last_login',

    # Theming
    'theme',
    'auth_buttons',
    'labeled_submit_button',
    'logo',
    'primary_color',

    # Social
    'social_button_style',

    # Authentication
    'auth'
    'audience',
    'auto_parse_hash',
    'connection_scopes',
    'params',
    'redirect_url',
    'response_mode',
    'response_type',
    'sso',

    # Database
    'additional_sign_up_fields',
    'allow_login',
    'allow_forgot_password',
    'allow_sign_up',
    'default_database_connection',
    'initial_screen',
    'login_after_sign_up',
    'forgot_password_link',
    'must_accept_terms',
    'prefill',
    'sign_up_link',
    'username_style',

    # Enterprise
    'default_enterprise_connection',

    # Other
    'oidc_conformant',
    'client_base_url',
    'language_base_url',
    'hash_cleanup',
    'leeway',
)


class Auth0OpenId(OpenIdConnectAuth):
    """Auth0 OpenID authentication backend"""
    name = 'auth0'

    OIDC_ENDPOINT = AUTH0_OIDC_ENDPOINT
    ID_TOKEN_ISS = AUTH0_OIDC_ENDPOINT + "/"
    # Under some circumstances we wont have the 'user_id' in the response during get_user_details.
    # One option is to re-implement this function here in our backend
    # for completeness and ease of documenting how this all works...
    # The other is setting USERNAME_KEY = 'sub' instead of the more obvious USERNAME_KEY = 'user_id',
    # were going with the other for now to keep things simple.
    USERNAME_KEY = 'sub'

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token, token_type, and extra defined names to store in
            extra_data field"""
        data = super(Auth0OpenId, self).extra_data(user, uid, response, details=details, *args, **kwargs)
        # TODO work out why the id_token here has not been decoded
        #  because there may be a better place to do this...
        #  https://github.com/python-social-auth/social-core/issues/127
        # TODO: Don't just store everything here, be more selective.
        data['id_token_payload'] = self.id_token
        return data

    def auth_url(self):
        """Return redirect url"""
        state = self.get_or_create_state()
        params = self.auth_params(state)
        params.update(self.get_scope_argument())
        params.update(self.auth_extra_arguments())
        params.update({_key: self.data[_key] for _key in self.data.keys() if _key in AUTH0_ALLOWED_URL_PARAMETERS})
        params = urlencode(params)
        if not self.REDIRECT_STATE:
            # redirect_uri matching is strictly enforced, so match the
            # providers value exactly.
            params = unquote(params)
        return '{0}?{1}'.format(self.authorization_url(), params)
