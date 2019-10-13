from django.test.selenium import SeleniumTestCase
from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
# noinspection PyUnresolvedReferences,PyPackageRequirements
from tests.utils.fixtures import one_auth0_user
from tests.utils.fixtures import create_auth0_users_and_confirm
from tests.utils.fixtures import auth0_rules
import pytest


# @pytest.fixture
# def chrome_options(chrome_options):
#     # chrome_options.add_argument('headless')
#     # chrome_options.headless = True
#     return chrome_options


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

LOGIN_FORM_LOCATOR = (By.XPATH, '//div[@class="auth0-lock-input-block auth0-lock-input-email"]')
EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@class="auth0-lock-input" and @name="email"]')
PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[@class="auth0-lock-input" and @name="password"]')
AUTHORIZE_MODAL = (By.XPATH, '//div[@id="authorize-modal"]')
AUTHORIZE_ALLOW_BUTTON = (By.XPATH, '//div[@id="authorize-modal"]/form/div/button[@id="allow"]')
LOGGED_IN_USER_INFO = (By.XPATH, '//span[@id="user-email"]')

_email_locator = (By.ID, '1-email')
_enter_email_button_locator = (By.ID, 'enter-initial')
_send_email_locator = (By.CSS_SELECTOR, '#non-ldap button[data-handler=send-passwordless-link]')
_password_locator = (By.ID, 'field-password')
_enter_button_locator = (By.ID, 'authorise-ldap-credentials')
_passcode_field_locator = (By.CSS_SELECTOR, '.passcode-label input[name="passcode"]')
_ldap_error_message = (By.CSS_SELECTOR, '#error-password span')
_passwordless_login_confirmation_message = (By.CSS_SELECTOR, '#error-message-passwordless span')
_loading_spinner_locator = (By.CSS_SELECTOR, 'form[lock-state="loading"]')
_spinner_locator = (By.CSS_SELECTOR, '.loading__spinner')
_autologin_message_locator = (By.ID, 'loading__status')
_login_form_locator = (By.ID, 'login-form')


def test_regular_user_login(selenium, base_url, auth0_user, auth0_rules):
    user_email = auth0_user['email']
    user_password = auth0_user['password']

    selenium.get('%s%s' % (base_url, '/'))
    selenium.find_element_by_link_text('Login').click()
    wait = WebDriverWait(selenium, 60)

    wait.until(EC.visibility_of_element_located(LOGIN_FORM_LOCATOR))

    selenium.find_element(*EMAIL_INPUT_LOCATOR).send_keys(user_email)
    selenium.find_element(*PASSWORD_INPUT_LOCATOR).send_keys(user_password)

    selenium.find_element_by_xpath('//button[@class="auth0-lock-submit"]').click()

    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTHORIZE_MODAL))
    selenium.find_element(*AUTHORIZE_ALLOW_BUTTON).click()

    wait.until(EC.visibility_of_element_located(LOGGED_IN_USER_INFO))
    email_on_page = selenium.find_element_by_xpath('//span[@id="user-email"]').text

    assert email_on_page == user_email
    # TODO: Assert something about the username being the auth0 user_id.


def test_user_login_with_metadata(selenium, base_url, auth0_user_with_metadata, auth0_rules):
    user_email = auth0_user['email']
    user_password = auth0_user['password']

    selenium.get('%s%s' % (base_url, '/'))
    selenium.find_element_by_link_text('Login').click()
    wait = WebDriverWait(selenium, 60)

    wait.until(EC.visibility_of_element_located(LOGIN_FORM_LOCATOR))

    selenium.find_element(*EMAIL_INPUT_LOCATOR).send_keys(user_email)
    selenium.find_element(*PASSWORD_INPUT_LOCATOR).send_keys(user_password)

    selenium.find_element_by_xpath('//button[@class="auth0-lock-submit"]').click()

    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTHORIZE_MODAL))
    selenium.find_element(*AUTHORIZE_ALLOW_BUTTON).click()

    wait.until(EC.visibility_of_element_located(LOGGED_IN_USER_INFO))
    email_on_page = selenium.find_element_by_xpath('//span[@id="user-email"]').text

    wait.until(EC.visibility_of_element_located(LOGGED_IN_USER_INFO))
    email_on_page = selenium.find_element_by_xpath('//span[@id="user-email"]').text



    assert email_on_page == user_email
    # TODO: Assert something about the username being the auth0 user_id.

