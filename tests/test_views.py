from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from tests.utils.auth0 import delete_all_auth0_users_with_confirmation
from tests.utils.auth0 import create_auth0_user
from django.test.selenium import SeleniumTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

# from selenium import webdriver


class WebSiteAuthFlow(SeleniumTestCase):
    browser = 'firefox'
    # browsers = ['firefox']

    def setUp(self):
        delete_all_auth0_users_with_confirmation()
        create_auth0_user(overrides={'email': 'user1@example.com', 'password': 'known_password'})
        create_auth0_user(overrides={'email': 'user2@example.com', 'password': 'known_password'})

    def test_regular_user_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        # self.selenium.
