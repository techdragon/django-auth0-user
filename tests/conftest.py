import json
import os
from pathlib import Path

import pytest
from django.conf import settings
from pytest_server_fixtures.http import SimpleHTTPTestServer

from django_auth0_user.util.auth0_api import set_auth0_rule_config_values, setup_auth0_rules, tear_down_auth0_rules, \
    remove_auth0_rule_config_values
from tests.utils.auth0 import create_auth0_users_and_confirm


@pytest.fixture(scope='session')
def base_url(live_server):
    return live_server.url


class SinglePageAppHTTPTestServer(SimpleHTTPTestServer):
    """
    Just a subclass of SimpleHTTPTestServer, but customized so
    it hosts the directory we want without creating a subdirectory, and
    it doesnt delete our working directory / workspace when we are done.
    """
    def __init__(self, *args, **kwargs):
        # TODO: Should I set delete=false as hardcoded here?
        kwargs['delete'] = False
        super(SinglePageAppHTTPTestServer, self).__init__(*args, **kwargs)

    @property
    def document_root(self):
        """This is the folder of files served up by this SinglePageAppHTTPTestServer"""
        file_dir = str(self.workspace)
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        return file_dir


@pytest.yield_fixture
def single_page_app_test_server():
    """ Function-scoped py.test fixture to serve up a directory via HTTP.
    """
    with SinglePageAppHTTPTestServer(
        # hostname='localhost'
        port=5000,
        uri='http://localhost:5000',
        workspace='test_sample_apps/javascript/02-Calling-an-API/',
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
            "apiUrl": f"{live_server.url}/api/v1/user_data/current_user_details/"
        }
        auth_config_file.write(json.dumps(auth_config_data))
    yield
    # TODO: Delete the config file when done. Keeping this during test development.
    # os.remove(auth_config_file_path)


@pytest.fixture(scope='session')
def auth0_rules():
    set_auth0_rule_config_values()
    setup_auth0_rules(dry_run=False)
    yield
    tear_down_auth0_rules(dry_run=False)
    remove_auth0_rule_config_values()


@pytest.fixture
def auth0_user():
    users = create_auth0_users_and_confirm(1)
    return users[0]


@pytest.fixture
def auth0_user_with_metadata():
    users = create_auth0_users_and_confirm(1, user_metadata={'favourite_colour': 'purple'})
    return users[0]
