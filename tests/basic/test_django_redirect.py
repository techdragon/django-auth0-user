from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
import pytest
# from tests.conftest import base_url, auth0_rules, auth0_user, auth0_user_with_metadata

from tests.xpaths import (
    AUTH0_LOCK_LOGIN_FORM,
    AUTH0_LOCK_EMAIL_INPUT,
    AUTH0_LOCK_PASSWORD_INPUT,
    AUTH0_LOCK_SUBMIT_BUTTON,
    AUTH0_AUTHORIZE_MODAL,
    AUTH0_AUTHORIZE_ALLOW_BUTTON,
    DJANGO_LOGGED_IN_USER_EMAIL,
    DJANGO_LOGGED_IN_USER_METADATA,
)


# LOGIN_FORM_LOCATOR = (By.XPATH, '//div[@class="auth0-lock-input-block auth0-lock-input-email"]')
# EMAIL_INPUT_LOCATOR = (By.XPATH, '//input[@class="auth0-lock-input" and @name="email"]')
# PASSWORD_INPUT_LOCATOR = (By.XPATH, '//input[@class="auth0-lock-input" and @name="password"]')
# AUTHORIZE_MODAL = (By.XPATH, '//div[@id="authorize-modal"]')
# AUTHORIZE_ALLOW_BUTTON = (By.XPATH, '//div[@id="authorize-modal"]/form/div/button[@id="allow"]')
# LOGGED_IN_USER_INFO = (By.XPATH, '//span[@id="user-email"]')


@pytest.mark.nondestructive
def test_regular_user_login(selenium, base_url, auth0_user, auth0_rules):
    user_email = auth0_user['email']
    user_password = auth0_user['password']

    selenium.get('%s%s' % (base_url, '/'))
    selenium.find_element_by_link_text('Login').click()
    wait = WebDriverWait(selenium, 60)

    wait.until(EC.visibility_of_element_located(AUTH0_LOCK_LOGIN_FORM))
    selenium.find_element(*AUTH0_LOCK_EMAIL_INPUT).send_keys(user_email)
    selenium.find_element(*AUTH0_LOCK_PASSWORD_INPUT).send_keys(user_password)
    selenium.find_element(*AUTH0_LOCK_SUBMIT_BUTTON).click()

    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTH0_AUTHORIZE_MODAL))
    selenium.find_element(*AUTH0_AUTHORIZE_ALLOW_BUTTON).click()

    wait.until(EC.visibility_of_element_located(DJANGO_LOGGED_IN_USER_EMAIL))
    email_on_page = selenium.find_element(*DJANGO_LOGGED_IN_USER_EMAIL).text

    assert email_on_page == user_email
    # TODO: Assert something about the username being the auth0 user_id.


@pytest.mark.nondestructive
def test_user_login_with_metadata(selenium, base_url, auth0_user_with_metadata, auth0_rules):
    user_email = auth0_user_with_metadata['email']
    user_password = auth0_user_with_metadata['password']

    selenium.get('%s%s' % (base_url, '/'))
    selenium.find_element_by_link_text('Login').click()
    wait = WebDriverWait(selenium, 60)

    wait.until(EC.visibility_of_element_located(AUTH0_LOCK_LOGIN_FORM))

    selenium.find_element(*AUTH0_LOCK_EMAIL_INPUT).send_keys(user_email)
    selenium.find_element(*AUTH0_LOCK_PASSWORD_INPUT).send_keys(user_password)
    selenium.find_element(*AUTH0_LOCK_SUBMIT_BUTTON).click()

    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTH0_AUTHORIZE_MODAL))
    selenium.find_element(*AUTH0_AUTHORIZE_ALLOW_BUTTON).click()

    wait.until(EC.visibility_of_element_located(DJANGO_LOGGED_IN_USER_EMAIL))
    user_email_on_page = selenium.find_element(*DJANGO_LOGGED_IN_USER_EMAIL).text

    wait.until(EC.visibility_of_element_located(DJANGO_LOGGED_IN_USER_METADATA))
    user_metadata_on_page = selenium.find_element(*DJANGO_LOGGED_IN_USER_METADATA).text

    assert user_email_on_page == user_email
    assert len(user_email_on_page) > 0
    # TODO: Assert something about the username being the auth0 user_id?
    # TODO: Assert something specific about the user metadata?

