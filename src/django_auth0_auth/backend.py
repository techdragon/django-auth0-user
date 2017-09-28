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

    # def get_user_id(self, details, response):
    #     """
    #     Return user unique id provided by service. For openSUSE
    #     the nickname is original.
    #     """
    #     return details['nickname']

    # def user_data(self, access_token, *args, **kwargs):
    #     """Loads user data from service. Implement in subclass"""
    #     user_info = {}
    #
    #     # id_token decode and check
    #     id_token = kwargs['response'].get('id_token')
    #     if id_token:
    #         client_id, client_secret = self.get_key_and_secret()
    #         payload = self._jwt_decode(id_token, client_secret)
    #
    #         if payload['iss'] != self.ID_TOKEN_ISS:
    #             log.warning("payload['iss'] = {}".format(payload['iss']))
    #             log.warning("self.ID_TOKEN_ISS = {}".format(self.ID_TOKEN_ISS))
    #             raise AuthTokenError(self, 'Incorrect id_token : iss')
    #
    #         if payload['aud'] != client_id:
    #             raise AuthTokenError(self, 'Incorrect id_token : aud')
    #
    #         utc_timestamp = timegm(datetime.utcnow().utctimetuple())
    #
    #         if payload['exp'] < utc_timestamp:
    #             raise AuthTokenError(self, 'Incorrect id_token : exp')
    #
    #         if payload['iat'] < (utc_timestamp - 600):
    #             raise AuthTokenError(self, 'Incorrect id_token : iat')
    #
    #         nonce_obj = self._get_nonce(payload['nonce'])
    #         if nonce_obj:
    #             self._remove_nonce(nonce_obj.id)
    #         else:
    #             raise AuthTokenError(self, 'Incorrect id_token : nonce')
    #
    #         user_info['id_token_payload'] = payload
    #
    #     # UserInfo Request
    #     json = self.get_json(
    #         self.USERINFO_URL,
    #         params={'schema': 'openid'},
    #         headers={'Authorization': 'Bearer ' + access_token}
    #     )
    #     user_info.update(json)
    #     return user_info

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token, token_type, and extra defined names to store in
            extra_data field"""
        data = super(Auth0OpenId, self).extra_data(user, uid, response, details=details, *args, **kwargs)
        # TODO work out why the id_token here has not been decyphered because that may be a better place to do this.
        data['token_type'] = response.get('token_type') or kwargs.get('token_type')
        data['id_token_payload'] = self.id_token
        return data

    def _get_nonce(self, nonce):
        # server_url = self.AUTHORIZATION_URL  # handled by the authorization_url method.
        try:
            return self.strategy.storage.association.get(server_url=self.authorization_url(), handle=nonce)[0]
        except:
            return None

    def _remove_nonce(self, id):
        try:
            self.strategy.storage.association.remove([id])
        except:
            return None

    def _jwt_decode(self, jwt, key=''):
        try:
            signing_input, crypto_segment = str(jwt).rsplit('.', 1)
            header_segment, payload_segment = signing_input.split('.', 1)
        except ValueError:
            raise AuthTokenError(self, 'Incorrect id_token : Not enough segments')

        try:
            header = json.loads(self._base64url_decode(header_segment))
        except TypeError:
            raise AuthTokenError(self, 'Incorrect id_token : Invalid header padding')
        except ValueError as e:
            raise AuthTokenError(self, 'Incorrect id_token : Invalid header string: %s' % e)

        try:
            payload = json.loads(self._base64url_decode(payload_segment))
        except TypeError:
            raise AuthTokenError(self, 'Incorrect id_token : Invalid payload padding')
        except ValueError as e:
            raise AuthTokenError(self, 'Incorrect id_token : Invalid payload string: %s' % e)

        try:
            signature = self._base64url_decode(crypto_segment)
        except TypeError:
            raise AuthTokenError(self, 'Incorrect id_token : Invalid crypto padding')

        try:
            sign = self._jwt_sign[header['alg']](signing_input, key)
        except KeyError:
            raise AuthTokenError(self, 'Incorrect id_token : Algorithm not supported')
        if signature != sign:
            raise AuthTokenError(self, 'Incorrect id_token : Signature verification failed')

        return payload

    _jwt_sign = {
        'HS256': lambda msg, key: hmac.new(key.encode(), msg.encode(), hashlib.sha256).digest(),
        'HS384': lambda msg, key: hmac.new(key.encode(), msg.encode(), hashlib.sha384).digest(),
        'HS512': lambda msg, key: hmac.new(key.encode(), msg.encode(), hashlib.sha512).digest(),
    }

    def _base64url_decode(self, input):
        rem = len(input) % 4
        if rem > 0:
            input += '=' * (4 - rem)
        try:
            return base64.urlsafe_b64decode(input.encode()).decode()  # return str
        except UnicodeDecodeError:
            return base64.urlsafe_b64decode(input.encode())  # return byte
