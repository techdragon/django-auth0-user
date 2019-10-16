import json
import pytest

from social_core.tests.backends.oauth import OAuth2Test
from social_core.tests.backends.open_id_connect import OpenIdConnectTestMixin


@pytest.mark.skip
class FirstOpenIdConnectTest(OpenIdConnectTestMixin, OAuth2Test):
    backend_path = 'django_auth0_user.backend.Auth0OpenId'
    issuer = 'https://foobar.auth0.com/'

    openid_config_body = json.dumps({
        'issuer': 'https://auth.globus.org',
        'authorization_endpoint': 'https://auth.globus.org/v2/oauth2/authorize',
        'userinfo_endpoint': 'https://auth.globus.org/v2/oauth2/userinfo',
        'token_endpoint': 'https://auth.globus.org/v2/oauth2/token',
        'revocation_endpoint': 'https://auth.globus.org/v2/oauth2/token/revoke',
        'jwks_uri': 'https://auth.globus.org/jwk.json',
        'response_types_supported': [
            'code',
            'token',
            'token id_token',
            'id_token'
        ],
        'id_token_signing_alg_values_supported': [
            'RS512'
        ],
        'scopes_supported': [
            'openid',
            'email',
            'profile'
        ],
        'token_endpoint_auth_methods_supported': [
            'client_secret_basic'
        ],
        'claims_supported': [
            'at_hash',
            'aud',
            'email',
            'exp',
            'name',
            'nonce',
            'preferred_username',
            'iat',
            'iss',
            'sub'
        ],
        'subject_types_supported' : ['public']
    })


@pytest.mark.skip
class SecondOpenIdConnectTest(OpenIdConnectTestMixin, OAuth2Test):
    backend_path = 'django_auth0_user.backend.Auth0OpenId'
    issuer = 'https://login.elixir-czech.org/oidc/'
    openid_config_body = """
    {
        "claims_supported": [
            "sub",
            "name",
            "preferred_username",
            "given_name",
            "family_name",
            "middle_name",
            "nickname",
            "profile",
            "picture",
            "website",
            "gender",
            "zoneinfo",
            "locale",
            "updated_at",
            "birthdate",
            "email",
            "email_verified",
            "phone_number",
            "phone_number_verified",
            "address"
        ],
        "op_policy_uri": "https://login.elixir-czech.org/oidc/about",
        "subject_types_supported": [
            "public",
            "pairwise"
        ],
        "request_parameter_supported": true,
        "userinfo_signing_alg_values_supported": [
            "HS256",
            "HS384",
            "HS512",
            "RS256",
            "RS384",
            "RS512",
            "ES256",
            "ES384",
            "ES512",
            "PS256",
            "PS384",
            "PS512"
        ],
        "revocation_endpoint": "https://login.elixir-czech.org/oidc/revoke",
        "issuer": "https://login.elixir-czech.org/oidc/",
        "id_token_encryption_enc_values_supported": [
            "A256CBC+HS512",
            "A256GCM",
            "A192GCM",
            "A128GCM",
            "A128CBC-HS256",
            "A192CBC-HS384",
            "A256CBC-HS512",
            "A128CBC+HS256"
        ],
        "require_request_uri_registration": false,
        "grant_types_supported": [
            "authorization_code",
            "implicit",
            "urn:ietf:params:oauth:grant-type:jwt-bearer",
            "client_credentials",
            "urn:ietf:params:oauth:grant_type:redelegate",
            "urn:ietf:params:oauth:grant-type:device_code"
        ],
        "token_endpoint": "https://login.elixir-czech.org/oidc/token",
        "request_uri_parameter_supported": false,
        "service_documentation": "https://login.elixir-czech.org/oidc/about",
        "registration_endpoint": "https://login.elixir-czech.org/oidc/register",
        "jwks_uri": "https://login.elixir-czech.org/oidc/jwk",
        "userinfo_encryption_alg_values_supported": [
            "RSA-OAEP",
            "RSA-OAEP-256",
            "RSA1_5"
        ],
        "scopes_supported": [],
        "token_endpoint_auth_methods_supported": [
            "client_secret_post",
            "client_secret_basic",
            "client_secret_jwt",
            "private_key_jwt",
            "none"
        ],
        "userinfo_encryption_enc_values_supported": [
            "A256CBC+HS512",
            "A256GCM",
            "A192GCM",
            "A128GCM",
            "A128CBC-HS256",
            "A192CBC-HS384",
            "A256CBC-HS512",
            "A128CBC+HS256"
        ],
        "claim_types_supported": [
            "normal"
        ],
        "request_object_encryption_enc_values_supported": [
            "A256CBC+HS512",
            "A256GCM",
            "A192GCM",
            "A128GCM",
            "A128CBC-HS256",
            "A192CBC-HS384",
            "A256CBC-HS512",
            "A128CBC+HS256"
        ],
        "claims_parameter_supported": false,
        "id_token_encryption_alg_values_supported": [
            "RSA-OAEP",
            "RSA-OAEP-256",
            "RSA1_5"
        ],
        "code_challenge_methods_supported": [
            "plain",
            "S256"
        ],
        "token_endpoint_auth_signing_alg_values_supported": [
            "HS256",
            "HS384",
            "HS512",
            "RS256",
            "RS384",
            "RS512",
            "ES256",
            "ES384",
            "ES512",
            "PS256",
            "PS384",
            "PS512"
        ],
        "userinfo_endpoint": "https://login.elixir-czech.org/oidc/userinfo",
        "introspection_endpoint": "https://login.elixir-czech.org/oidc/introspect",
        "id_token_signing_alg_values_supported": [
            "HS256",
            "HS384",
            "HS512",
            "RS256",
            "RS384",
            "RS512",
            "ES256",
            "ES384",
            "ES512",
            "PS256",
            "PS384",
            "PS512",
            "none"
        ],
        "device_authorization_endpoint": "https://login.elixir-czech.org/oidc/devicecode",
        "op_tos_uri": "https://login.elixir-czech.org/oidc/about",
        "request_object_encryption_alg_values_supported": [
            "RSA-OAEP",
            "RSA-OAEP-256",
            "RSA1_5"
        ],
        "request_object_signing_alg_values_supported": [
            "HS256",
            "HS384",
            "HS512",
            "RS256",
            "RS384",
            "RS512",
            "ES256",
            "ES384",
            "ES512",
            "PS256",
            "PS384",
            "PS512"
        ],
        "response_types_supported": [
            "code",
            "token"
        ],
        "end_session_endpoint": "https://login.elixir-czech.org/oidc/endsession",
        "authorization_endpoint": "https://login.elixir-czech.org/oidc/authorize"
    }
    """


user_data = {
        'app_metadata': {},
        'clientID': 'dHnrsr87JWuA92kc8vV0VC5MCSfrTcUC',
        'created_at': '2017-08-29T06:31:41.567Z',
        'email': 'user1@example.com',
        'email_verified': False,
        'identities': [{'connection': 'Username-Password-Authentication',
                 'isSocial': False,
                 'provider': 'auth0',
                 'user_id': '59a50a4dfb030d7b2bf0cde7'}],
        'name': 'user1@example.com',
        'nickname': 'user1',
        'picture': 'https://s.gravatar.com/avatar/111d68d06e2d317b5a59c2c6c5bad808?s=480&r=pg&d=https%3A%2F%2Fcdn.auth0.com%2Favatars%2Fus.png',
        'sub': 'auth0|59a50a4dfb030d7b2bf0cde7',
        'updated_at': '2017-08-29T08:15:25.378Z',
        'user_id': 'auth0|59a50a4dfb030d7b2bf0cde7',
        'user_metadata': {}
    }

"""
Auth0 implementation based on:
https://auth0.com/docs/quickstart/webapp/django/01-login
"""
import json

from jose import jwt
from httpretty import HTTPretty

from social_core.tests.backends.oauth import OAuth2Test

JWK_KEY = {
    'kty': 'RSA',
    'd': 'ZmswNokEvBcxW_Kvcy8mWUQOQCBdGbnM0xR7nhvGHC-Q24z3XAQWlMWbsmGc_R1o' \
         '_F3zK7DBlc3BokdRaO1KJirNmnHCw5TlnBlJrXiWpFBtVglUg98-4sRRO0VWnGXK' \
         'JPOkBQ6b_DYRO3b0o8CSpWowpiV6HB71cjXTqKPZf-aXU9WjCCAtxVjfIxgQFu5I' \
         '-G1Qah8mZeY8HK_y99L4f0siZcbUoaIcfeWBhxi14ODyuSAHt0sNEkhiIVBZE7QZ' \
         'm-SEP1ryT9VAaljbwHHPmg7NC26vtLZhvaBGbTTJnEH0ZubbN2PMzsfeNyoCIHy4' \
         '4QDSpQDCHfgcGOlHY_t5gQ',
    'e': 'AQAB',
    'use': 'sig',
    'kid': 'foobar',
    'alg': 'RS256',
    'n': 'pUfcJ8WFrVue98Ygzb6KEQXHBzi8HavCu8VENB2As943--bHPcQ-nScXnrRFAUg8' \
         'H5ZltuOcHWvsGw_AQifSLmOCSWJAPkdNb0w0QzY7Re8NrPjCsP58Tytp5LicF0Ao' \
         'Ag28UK3JioY9hXHGvdZsWR1Rp3I-Z3nRBP6HyO18pEgcZ91c9aAzsqu80An9X4DA' \
         'b1lExtZorvcd5yTBzZgr-MUeytVRni2lDNEpa6OFuopHXmg27Hn3oWAaQlbymd4g' \
         'ifc01oahcwl3ze2tMK6gJxa_TdCf1y99Yq6oilmVvZJ8kwWWnbPE-oDmOVPVnEyT' \
         'vYVCvN4rBT1DQ-x0F1mo2Q'
}

JWK_PUBLIC_KEY = {key: value for key, value in JWK_KEY.items() if key != 'd'}

DOMAIN = 'foobar.auth0.com'


@pytest.mark.skip
class Auth0OAuth2Test(OAuth2Test):
    backend_path = 'social_core.backends.auth0.Auth0OAuth2'
    access_token_body = json.dumps({
        'access_token': 'foobar',
        'token_type': 'bearer',
        'expires_in': 86400,
        'id_token': jwt.encode({
            'nickname': 'foobar',
            'email': 'foobar@auth0.com',
            'name': 'John Doe',
            'picture': 'http://example.com/image.png',
            'sub': '123456',
            'iss': 'https://{}/'.format(DOMAIN),
        }, JWK_KEY, algorithm='RS256')
    })
    expected_username = 'foobar'
    jwks_url = 'https://foobar.auth0.com/.well-known/jwks.json'

    def extra_settings(self):
        settings = super(Auth0OAuth2Test, self).extra_settings()
        settings['SOCIAL_AUTH_' + self.name + '_DOMAIN'] = DOMAIN
        return settings

    def auth_handlers(self, start_url):
        HTTPretty.register_uri(HTTPretty.GET,
                               self.jwks_url,
                               body=json.dumps({'keys': [JWK_PUBLIC_KEY]}),
                               content_type='application/json')
        return super(Auth0OAuth2Test, self).auth_handlers(start_url)

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()


# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------


from django.contrib.auth.models import User
import json


from django.conf.urls import url
from django.http import HttpResponse
from django.test import TestCase
from rest_framework.views import APIView
from requests import Response, HTTPError, ConnectionError
# from oidc_auth.authentication import JSONWebTokenAuthentication, BearerTokenAuthentication
import sys
# from jwkest import long_to_base64
# from jwkest.jwk import RSAKey, KEYS
# from jwkest.jws import JWS
# if sys.version_info > (3,):
#     long = int

from unittest.mock import patch, Mock


# Refactored Code
from django.urls import include, path
from django_auth0_user.rest_framework.authentication import FastAuth0Authentication
from django_auth0_user.rest_framework.authentication import FullAuth0Authentication
from rest_framework.permissions import IsAuthenticated
# End Refactored Code


class MockView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def post(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})

    def put(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})


urlpatterns = [
    path(
        "rest_framework_auth_fast/",
        MockView.as_view(authentication_classes=[FastAuth0Authentication])
    ),
    path(
        "rest_framework_auth_full/",
        MockView.as_view(authentication_classes=[FullAuth0Authentication])
    ),
]


# key = RSAKey(kid="test",
#              kty="RSA",
#              e=long_to_base64(int(65537)),
#              n=long_to_base64(long(103144733181541730170695212353035735911272360475451101847332641719504193145911782103718552703497383385072400068398348471608551845979550140132066577502098324638900101678499876506366406838561711807168917151266210861310839976066381600661109647310812646802675105044570916072792610952531033569123889433857109695663)),
#              d=long_to_base64(long(87474011172773995802176478974956531454728135178991596207863469898989014679490621318105454312226445649668492543167679449044101982079487873850500638991205330610459744732712633893362912169260215247013564296846583369572335796121742404877695795618480142002129365141632060905382558309932032446524457731175746076993)))


def make_jwt(payload):
    jws = JWS(payload, alg='RS256')
    return jws.sign_compact([key])


def make_id_token(sub,
                  iss='http://example.com',
                  aud='you',
                  exp=999999999999,  # tests will start failing in September 33658
                  iat=999999999999,
                  **kwargs):
    return make_jwt(dict(
        iss=iss,
        aud=aud,
        exp=exp,
        iat=iat,
        sub=str(sub),
        **kwargs
    ))


class FakeRequests(object):
    def __init__(self):
        self.responses = {}

    def set_response(self, url, content, status_code=200):
        self.responses[url] = (status_code, json.dumps(content))

    def get(self, url, *args, **kwargs):
        wanted_response = self.responses.get(url)
        if not wanted_response:
            status_code, content = 404, ''
        else:
            status_code, content = wanted_response

        response = Response()
        response._content = content.encode('utf-8')
        response.status_code = status_code

        return response


@pytest.mark.skip
class AuthenticationTestCase(TestCase):
    urls = __name__

    def patch(self, thing_to_mock, **kwargs):
        patcher = patch(thing_to_mock, **kwargs)
        patched = patcher.start()
        self.addCleanup(patcher.stop)
        return patched

    def setUp(self):
        self.user = User.objects.create(username='henk')
        self.responder = FakeRequests()
        self.responder.set_response("http://example.com/.well-known/openid-configuration",
                                    {"jwks_uri": "http://example.com/jwks",
                                     "issuer": "http://example.com",
                                     "userinfo_endpoint": "http://example.com/userinfo"})
        self.mock_get = self.patch('requests.get')
        self.mock_get.side_effect = self.responder.get
        keys = KEYS()
        keys.add({'key': key, 'kty': 'RSA', 'kid': key.kid})
        self.patch('oidc_auth.authentication.request', return_value=Mock(status_code=200,
                                                                         text=keys.dump_jwks()))


@pytest.mark.skip
class TestBearerAuthentication(AuthenticationTestCase):
    def test_using_valid_bearer_token(self):
        self.responder.set_response('http://example.com/userinfo', {'sub': self.user.username})
        auth = 'Bearer abcdefg'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.content.decode(), 'a')
        self.assertEqual(resp.status_code, 200)
        self.mock_get.assert_called_with('http://example.com/userinfo', headers={'Authorization': auth})

    def test_cache_of_valid_bearer_token(self):
        self.responder.set_response('http://example.com/userinfo', {'sub': self.user.username})
        auth = 'Bearer egergerg'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 200)

        # Token expires, but validity is cached
        self.responder.set_response('http://example.com/userinfo', "", 401)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 200)

    def test_using_invalid_bearer_token(self):
        self.responder.set_response('http://example.com/userinfo', "", 401)
        auth = 'Bearer hjikasdf'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_cache_of_invalid_bearer_token(self):
        self.responder.set_response('http://example.com/userinfo', "", 401)
        auth = 'Bearer feegrgeregreg'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

        # Token becomes valid
        self.responder.set_response('http://example.com/userinfo', {'sub': self.user.username})
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 200)

    def test_using_malformed_bearer_token(self):
        auth = 'Bearer abc def'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_using_missing_bearer_token(self):
        auth = 'Bearer'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_using_inaccessible_userinfo_endpoint(self):
        self.mock_get.side_effect = ConnectionError
        auth = 'Bearer'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

@pytest.mark.skip
class TestJWTAuthentication(AuthenticationTestCase):
    def test_using_valid_jwt(self):
        auth = 'JWT ' + make_id_token(self.user.username)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.content.decode(), 'a')
        self.assertEqual(resp.status_code, 200)

    def test_without_jwt(self):
        resp = self.client.get('/test/')
        self.assertEqual(resp.status_code, 401)

    def test_with_invalid_jwt(self):
        auth = 'JWT bla'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_invalid_auth_header(self):
        auth = 'Bearer 12345'
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_expired_jwt(self):
        auth = 'JWT ' + make_id_token(self.user.username, exp=13151351)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_old_jwt(self):
        auth = 'JWT ' + make_id_token(self.user.username, iat=13151351)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_invalid_issuer(self):
        auth = 'JWT ' + make_id_token(self.user.username, iss='http://something.com')
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_invalid_audience(self):
        auth = 'JWT ' + make_id_token(self.user.username, aud='somebody')
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_too_new_jwt(self):
        auth = 'JWT ' + make_id_token(self.user.username, nbf=999999999999)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_unknown_subject(self):
        auth = 'JWT ' + make_id_token(self.user.username + 'x')
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_multiple_audiences(self):
        auth = 'JWT ' + make_id_token(self.user.username, aud=['you', 'me'])
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 401)

    def test_with_multiple_audiences_and_authorized_party(self):
        auth = 'JWT ' + make_id_token(self.user.username, aud=['you', 'me'], azp='you')
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth)
        self.assertEqual(resp.status_code, 200)

    def test_with_invalid_signature(self):
        auth = 'JWT ' + make_id_token(self.user.username)
        resp = self.client.get('/test/', HTTP_AUTHORIZATION=auth + 'x')
        self.assertEqual(resp.status_code, 401)
