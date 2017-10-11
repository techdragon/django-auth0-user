import math

from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
from django.conf import settings
from cached_property import threaded_cached_property_with_ttl
import logging


logger = logging.getLogger(__name__)


AUTH0_MANAGEMENT_API_TOKEN_DEFAULT_EXPIRY = 86400  # 24 hours = 86400 seconds

AUTH0_CACHED_TOKEN_TTL = 3600  # 1 hour = 3600 seconds

AUTH0_DOMAIN = getattr(settings, 'AUTH0_DOMAIN')

AUTH0_API_URL = 'https://' + AUTH0_DOMAIN + '/api/v2/'
# domain = AUTH0_DOMAIN

# Non Interactive API Client ID
AUTH0_MANAGEMENT_API_CLIENT_ID = getattr(settings, 'AUTH0_MANAGEMENT_API_CLIENT_ID')
# non_interactive_client_id = 'exampleid'

# Non Interactive API Client Secret
AUTH0_MANAGEMENT_API_CLIENT_SECRET = getattr(settings, 'AUTH0_MANAGEMENT_API_CLIENT_SECRET')
# non_interactive_client_secret = 'examplesecret'

# TODO: handle empty domain, client ID and client secret, in a user friendly fashion.

# get_token = GetToken(domain)
# token = get_token.client_credentials(non_interactive_client_id,
# non_interactive_client_secret, 'https://myaccount.auth0.com/api/v2/')
# mgmt_api_token = token['access_token']


class TokenCache(object):
    """
    Cache the Auth0 token with a TTL so that we get a new one regularly.

    Needed to prevent invalid token issues in production, since the production server needs to possibly live longer
    the token expiry, and we cannot just hammer the token API for a new token every time it makes a request.
    """

    @threaded_cached_property_with_ttl(ttl=AUTH0_CACHED_TOKEN_TTL)
    def auth0_management_api_token(self):
        # TODO: Convert this to a proper logging statement.
        logger.info('No cached Auth0 management API token was found...')
        get_token = GetToken(AUTH0_DOMAIN)
        token = get_token.client_credentials(
            AUTH0_MANAGEMENT_API_CLIENT_ID,
            AUTH0_MANAGEMENT_API_CLIENT_SECRET,
            AUTH0_API_URL
        )
        management_api_token = token['access_token']
        # TODO: Convert this to a proper logging statement.
        logger.info('Successfully generated a new Auth0 Management API Token, this will be cached.')
        return management_api_token


AUTH0_TOKEN_CACHE = TokenCache()


# TODO: Is this the best name for this function?
def get_auth0():
    return Auth0(AUTH0_DOMAIN, AUTH0_TOKEN_CACHE.auth0_management_api_token)


def get_all_auth0_users():
    """
    Update all the user objects...

    :return:
    """
    auth0 = get_auth0()

    auth0_users = []

    first_query = auth0.users.list()
    query_length = first_query['length']
    query_limit = first_query['limit']
    query_start = first_query['start']
    query_total = first_query['total']

    for auth0_user in first_query['users']:
        auth0_users.append(auth0_user)
    if query_length + query_start <= query_total:
        page_number = 0
        while query_length + query_start <= query_total:
            page_number += 1

            page_query = auth0.users.list(page=page_number)

            for auth0_user in page_query['users']:
                auth0_users.append(auth0_user)

            query_length = page_query['length']
            query_limit = page_query['limit']
            query_start = page_query['start']
            query_total = page_query['total']

    return auth0_users


def get_auth0_user(user_id, auth0=None):
    if auth0 is None:
        auth0 = get_auth0()
    # TODO: This does not appear to retrieve all user related data. So it may need to be improved.
    return auth0.users.get(user_id)


def get_users_from_auth0(auth0_conn: Auth0):
    """
    Get all users from Auth0

    :param auth0_conn: Authenticated Auth0 API client
    :param regex: Regex to filter users (re.match(user.email))
    """

    users_list = auth0_conn.users.list()

    total_users = users_list['total']
    page_size = users_list['length']

    # don't waste the first request
    for u in users_list['users']:
        yield u

    del users_list

    # iterate through subsequent pages
    if page_size > 0 and total_users > 0:
        for page in range(1, int(math.ceil(total_users / page_size))):
            for u in auth0_conn.users.list(page=page)['users']:
                yield u


# TODO: Add a function to get an Auth0 client's details from the Management API
# TODO: Add a function that returns true/false based on if the Auth0 client is configured to be OIDC conformant.
