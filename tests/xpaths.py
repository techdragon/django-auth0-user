from selenium.webdriver.common.by import By


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Auth0 Component XPath Selectors ┃▓▓
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛▓▓
#   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
AUTH0_LOCK_LOGIN_FORM = (By.XPATH, '//div[@class="auth0-lock-input-block auth0-lock-input-email"]')
AUTH0_LOCK_EMAIL_INPUT = (By.XPATH, '//input[@class="auth0-lock-input" and @name="email"]')
AUTH0_LOCK_PASSWORD_INPUT = (By.XPATH, '//input[@class="auth0-lock-input" and @name="password"]')
AUTH0_LOCK_SUBMIT_BUTTON = (By.XPATH, '//button[@class="auth0-lock-submit"]')
# ----------------------------------------
AUTH0_AUTHORIZE_MODAL = (By.XPATH, '//div[@id="authorize-modal"]')
AUTH0_AUTHORIZE_ALLOW_BUTTON = (By.XPATH, '//div[@id="authorize-modal"]/form/div/button[@id="allow"]')


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Django Web App Redirect XPaths  ┃▓▓
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛▓▓
#   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
DJANGO_LOGGED_IN_USER_EMAIL = (By.XPATH, '//span[@id="user-email"]')
DJANGO_LOGGED_IN_USER_METADATA = (By.XPATH, '//pre[@id="user-metadata"]')

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ Single Page App XPath Selectors ┃▓▓
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛▓▓
#   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
LOGIN_BUTTON = (By.XPATH, '//button[@id="qsLoginBtn"]')
EXTERNAL_API_PAGE_LINK = (By.XPATH, '//a[@href="/external-api"]')
BUTTON_TO_TRIGGER_API_CALL_USING_TOKEN = (By.XPATH, '//a[@id="call-api"]')
EXTERNAL_API_CALL_RESULTS = (By.XPATH, '//code[@id="api-call-result"]')
