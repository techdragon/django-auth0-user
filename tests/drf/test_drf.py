from selenium.webdriver.support.ui import WebDriverWait
# noinspection PyPep8Naming
from selenium.webdriver.support import expected_conditions as EC
# noinspection PyUnresolvedReferences,PyPackageRequirements
import pytest
# from tests.conftest import base_url, single_page_app_test_server, javascript_frontend_config, auth0_user, \
#     auth0_user_with_metadata

from tests.xpaths import (
    LOGIN_BUTTON,
    AUTH0_LOCK_LOGIN_FORM,
    AUTH0_LOCK_EMAIL_INPUT,
    AUTH0_LOCK_PASSWORD_INPUT,
    AUTH0_LOCK_SUBMIT_BUTTON,
    AUTH0_AUTHORIZE_MODAL,
    AUTH0_AUTHORIZE_ALLOW_BUTTON,
    EXTERNAL_API_PAGE_LINK,
    BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN,
    EXTERNAL_API_CALL_RESULTS
)


@pytest.mark.nondestructive
def test_single_page_app_login(selenium, base_url, auth0_user, javascript_frontend_config, single_page_app_test_server):
    user_email = auth0_user['email']
    user_password = auth0_user['password']
    web_url = single_page_app_test_server.uri

    selenium.get('%s%s' % (web_url, '/'))
    wait = WebDriverWait(selenium, 60)

    # Click Login Button
    wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
    selenium.find_element(*LOGIN_BUTTON).click()

    # Login Using Auth0
    wait.until(EC.visibility_of_element_located(AUTH0_LOCK_LOGIN_FORM))
    selenium.find_element(*AUTH0_LOCK_EMAIL_INPUT).send_keys(user_email)
    selenium.find_element(*AUTH0_LOCK_PASSWORD_INPUT).send_keys(user_password)
    selenium.find_element(*AUTH0_LOCK_SUBMIT_BUTTON).click()
    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTH0_AUTHORIZE_MODAL))
    selenium.find_element(*AUTH0_AUTHORIZE_ALLOW_BUTTON).click()

    # Wait for page to load after returning to the single page app.
    wait.until(EC.visibility_of_element_located(EXTERNAL_API_PAGE_LINK))
    selenium.find_element(*EXTERNAL_API_PAGE_LINK).click()

    # Wait for the button to appear after clicking on the external api page button.
    wait.until(EC.visibility_of_element_located(BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN))
    selenium.find_element(*BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN).click()

    # Check the returned data.
    wait.until(EC.visibility_of_element_located(EXTERNAL_API_CALL_RESULTS))
    api_result = selenium.find_element(*EXTERNAL_API_CALL_RESULTS)
    api_result_text = api_result.text

    assert '"provider": "auth0"' in str(api_result_text)


@pytest.mark.nondestructive
def test_single_page_app_login_with_metadata(
    selenium, base_url, auth0_user_with_metadata, javascript_frontend_config, single_page_app_test_server
):
    user_email = auth0_user_with_metadata['email']
    user_password = auth0_user_with_metadata['password']
    web_url = single_page_app_test_server.uri

    selenium.get('%s%s' % (web_url, '/'))
    wait = WebDriverWait(selenium, 60)

    # Click Login Button
    wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))
    selenium.find_element(*LOGIN_BUTTON).click()

    # Login Using Auth0
    wait.until(EC.visibility_of_element_located(AUTH0_LOCK_LOGIN_FORM))
    selenium.find_element(*AUTH0_LOCK_EMAIL_INPUT).send_keys(user_email)
    selenium.find_element(*AUTH0_LOCK_PASSWORD_INPUT).send_keys(user_password)
    selenium.find_element(*AUTH0_LOCK_SUBMIT_BUTTON).click()
    # TODO: This really should be using some conditional logic!
    wait.until(EC.visibility_of_element_located(AUTH0_AUTHORIZE_MODAL))
    selenium.find_element(*AUTH0_AUTHORIZE_ALLOW_BUTTON).click()

    # Wait for page to load after returning to the single page app.
    wait.until(EC.visibility_of_element_located(EXTERNAL_API_PAGE_LINK))
    selenium.find_element(*EXTERNAL_API_PAGE_LINK).click()

    # Wait for the button to appear after clicking on the external api page button.
    wait.until(EC.visibility_of_element_located(BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN))
    selenium.find_element(*BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN).click()

    # Check the returned data.
    wait.until(EC.visibility_of_element_located(EXTERNAL_API_CALL_RESULTS))
    api_result = selenium.find_element(*EXTERNAL_API_CALL_RESULTS)
    api_result_text = api_result.text

    assert '"provider": "auth0"' in api_result_text
    assert 'user_metadata' in api_result_text

