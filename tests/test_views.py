from django.test.selenium import SeleniumTestCase
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
# noinspection PyUnresolvedReferences,PyPackageRequirements
from tests.utils.fixtures import one_auth0_user


# TODO: Convert this into a non-class based test so we can drive it more flexibly via PyTest.
@pytest.mark.usefixtures('one_auth0_user')
class WebSiteAuthFlow(SeleniumTestCase):
    """
    Integration test of Auth0 web authentication process.

    The PyTest fixture generates a new random user on Auth0 and
    """
    browser = 'firefox'
    port = 63180
    # browser = 'phantomjs'
    # browsers = ['firefox']

    # def setUp(self):
    #     delete_all_auth0_users_with_confirmation()
    #     create_auth0_user(overrides={'email': 'user1@example.com', 'password': 'known_password'})
    #     create_auth0_user(overrides={'email': 'user2@example.com', 'password': 'known_password'})

    def test_regular_user_login(self):
        # """Self.user is
        user_email = self.user['email']
        user_password = self.user['password']

        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        self.selenium.find_element_by_link_text('Login').click()
        wait = WebDriverWait(self.selenium, 60)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@class="auth0-lock-input-block auth0-lock-input-email"]/div/input')))
        self.selenium.find_element_by_xpath(
            '//div[@class="auth0-lock-input-block auth0-lock-input-email"]/div/input').send_keys(user_email)
        self.selenium.find_element_by_xpath(
            '//div[@class="auth0-lock-input-block auth0-lock-input-password"]/div/input').send_keys(user_password)
        self.selenium.find_element_by_xpath('//button[@class="auth0-lock-submit"]').click()
        email_on_page = self.selenium.find_element_by_xpath('//span[@id="user-email"]').text
        assert email_on_page == user_email
        # TODO: Assert something about the username being the auth0 user_id.
