import json
import pytest
from pathlib import Path
import os
from django.conf import settings
from tests.utils.auth0 import create_auth0_users_and_confirm
from pytest_server_fixtures.http import SimpleHTTPTestServer
from contextlib import contextmanager

@pytest.fixture(scope='session')
def base_url(live_server):
    return live_server.url


@pytest.fixture
def auth0_user():
    users = create_auth0_users_and_confirm(1)
    return users[0]


@pytest.fixture
def auth0_user_with_metadata():
    users = create_auth0_users_and_confirm(1, user_metadata={'favourite_colour': 'purple'})
    return users[0]


@pytest.yield_fixture
def single_page_app_test_server():
    """ Function-scoped py.test fixture to serve up a directory via HTTP.
    """
    with SimpleHTTPTestServer(
        uri='http://localhost:5000',
        workspace='test_sample_apps/javascript'
    ) as s:
        s.start()
        yield s


@pytest.yield_fixture
def javascript_frontend_config(live_server):
    auth_config_file_path = Path('test_sample_apps/javascript/02-Calling-an-API/auth_config.json')
    with open(auth_config_file_path, 'w') as auth_config_file:
        auth_config_data = {
            "domain": f"{settings.AUTH0_DOMAIN}",
            "clientId": f"{settings.AUTH0_JAVASCRIPT_TEST_CLIENT_CLIENT_ID}",
            "audience": f"{settings.AUTH0_JAVASCRIPT_TEST_CLIENT_API_AUDIENCE}",
            # TODO: Pass this in from the django live server url.
            "apiUrl": f"{live_server.url}/api/v1/drf-api-lives-here"
        }
        auth_config_file.write(json.dumps(auth_config_data))
    yield
    # os.remove(auth_config_file_path)


