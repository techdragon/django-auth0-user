from django.conf import settings


if getattr(settings, 'AUTH0_DOMAIN', None) is not None:
    AUTH0_DOMAIN = settings.AUTH0_DOMAIN
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_DOMAIN', None) is not None:
    AUTH0_DOMAIN = settings.SOCIAL_AUTH_AUTH0_DOMAIN
else:
    AUTH0_DOMAIN = None

AUTH0_API_URL = 'https://' + AUTH0_DOMAIN + '/api/v2/'

if getattr(settings, 'AUTH0_OIDC_ENDPOINT', None) is not None:
    AUTH0_OIDC_ENDPOINT = settings.AUTH0_OIDC_ENDPOINT
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_OIDC_ENDPOINT', None) is not None:
    AUTH0_OIDC_ENDPOINT = settings.SOCIAL_AUTH_AUTH0_OIDC_ENDPOINT
else:
    AUTH0_OIDC_ENDPOINT = None

if getattr(settings, 'AUTH0_USER_ID_IS_DJANGO_USERNAME', None) is not None:
    USER_ID_IS_DJANGO_USERNAME = settings.AUTH0_USER_ID_IS_DJANGO_USERNAME
if getattr(settings, 'SOCIAL_AUTH_AUTH0_USER_ID_IS_DJANGO_USERNAME', None) is not None:
    USER_ID_IS_DJANGO_USERNAME = settings.SOCIAL_AUTH_AUTH0_USER_ID_IS_DJANGO_USERNAME
else:
    USER_ID_IS_DJANGO_USERNAME = True


#


# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃  Auth0 Management API Settings  ┃▓▓
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛▓▓
#   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
if getattr(settings, 'AUTH0_MANAGEMENT_API_CLIENT_ID', None) is not None:
    AUTH0_MANAGEMENT_API_CLIENT_ID = settings.AUTH0_MANAGEMENT_API_CLIENT_ID
if getattr(settings, 'SOCIAL_AUTH_AUTH0_MANAGEMENT_API_CLIENT_ID', None) is not None:
    AUTH0_MANAGEMENT_API_CLIENT_ID = settings.SOCIAL_AUTH_AUTH0_MANAGEMENT_API_CLIENT_ID
else:
    AUTH0_MANAGEMENT_API_CLIENT_ID = None
if getattr(settings, 'AUTH0_MANAGEMENT_API_CLIENT_SECRET', None) is not None:
    AUTH0_MANAGEMENT_API_CLIENT_SECRET = settings.AUTH0_MANAGEMENT_API_CLIENT_SECRET
if getattr(settings, 'SOCIAL_AUTH_AUTH0_MANAGEMENT_API_CLIENT_SECRET', None) is not None:
    AUTH0_MANAGEMENT_API_CLIENT_SECRET = settings.SOCIAL_AUTH_AUTH0_MANAGEMENT_API_CLIENT_SECRET
else:
    AUTH0_MANAGEMENT_API_CLIENT_SECRET = None


#


# We need a namespace prefix provided by the user as there is not really a safe and unique default.
if getattr(settings, 'AUTH0_NAMESPACED_KEY_PREFIX', None) is not None:
    NAMESPACED_KEY_PREFIX = settings.AUTH0_NAMESPACED_KEY_PREFIX
else:
    NAMESPACED_KEY_PREFIX = ''


if getattr(settings, 'AUTH0_NAMESPACED_USER_METADATA_KEY', None) is not None:
    NAMESPACED_USER_METADATA_KEY = settings.AUTH0_NAMESPACED_USER_METADATA_KEY
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_NAMESPACED_USER_METADATA_KEY', None) is not None:
    NAMESPACED_USER_METADATA_KEY = settings.SOCIAL_AUTH_AUTH0_NAMESPACED_USER_METADATA_KEY
else:
    NAMESPACED_USER_METADATA_KEY = NAMESPACED_KEY_PREFIX + '/user_metadata'

if getattr(settings, 'AUTH0_NAMESPACED_APP_METADATA_KEY', None) is not None:
    NAMESPACED_APP_METADATA_KEY = settings.AUTH0_NAMESPACED_APP_METADATA_KEY
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_NAMESPACED_APP_METADATA_KEY', None) is not None:
    NAMESPACED_APP_METADATA_KEY = settings.SOCIAL_AUTH_AUTH0_NAMESPACED_APP_METADATA_KEY
else:
    NAMESPACED_APP_METADATA_KEY = NAMESPACED_KEY_PREFIX + '/app_metadata'


DEFAULT_AUTH0_RULE_CONFIGS = {
        'DJANGO_AUTH0_USER_OIDC_NAMESPACE_PREFIX': NAMESPACED_KEY_PREFIX,
        'DJANGO_AUTH0_USER_NAMESPACED_USER_METADATA_KEY': NAMESPACED_USER_METADATA_KEY,
        'DJANGO_AUTH0_USER_NAMESPACED_APP_METADATA_KEY': NAMESPACED_APP_METADATA_KEY,
    }
if getattr(settings, 'AUTH0_RULE_CONFIGS', None) is not None:
    AUTH0_RULE_CONFIGS = settings.AUTH0_RULE_CONFIGS
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_RULE_CONFIGS', None) is not None:
    AUTH0_RULE_CONFIGS = settings.SOCIAL_AUTH_AUTH0_RULE_CONFIGS
else:
    AUTH0_RULE_CONFIGS = DEFAULT_AUTH0_RULE_CONFIGS


# TODO: Decide if this should keep living here or belongs in test settings...
# Use the Auth0 Rule Configuration object to set the namespace prefix dynamically.
EXAMPLE_METADATA_RULE_FUNCTION = """function (user, context, callback) {
    const NAMESPACE_PREFIX = configuration.DJANGO_AUTH0_USER_OIDC_NAMESPACE_PREFIX;
    const NAMESPACED_USER_METADATA_KEY = configuration.DJANGO_AUTH0_USER_NAMESPACED_USER_METADATA_KEY;
    const NAMESPACED_APP_METADATA_KEY = configuration.DJANGO_AUTH0_USER_NAMESPACED_APP_METADATA_KEY;
    if (context.idToken && user.user_metadata) {
        context.idToken[NAMESPACED_USER_METADATA_KEY] = user.user_metadata;
    }
    if (context.idToken && user.app_metadata) {
        context.idToken[NAMESPACED_APP_METADATA_KEY] = user.app_metadata;
    }
    if (context.accessToken && user.user_metadata) {
        context.accessToken[NAMESPACED_USER_METADATA_KEY] = user.user_metadata;
    }
    if (context.accessToken && user.app_metadata) {
        context.accessToken[NAMESPACED_APP_METADATA_KEY] = user.app_metadata;
    }
    callback(null, user, context);
}
"""


DEFAULT_AUTH0_RULES = {
        "Django-Auth0-User-ExampleMetadataRule": {
            "script": EXAMPLE_METADATA_RULE_FUNCTION,
            "stage": "login_success",
            "enabled": True,
            "order": 1,
        }
    }
if getattr(settings, 'AUTH0_RULES', None) is not None:
    AUTH0_RULES = settings.AUTH0_RULES
elif getattr(settings, 'SOCIAL_AUTH_AUTH0_RULES', None) is not None:
    AUTH0_RULES = settings.SOCIAL_AUTH_AUTH0_RULES
else:
    AUTH0_RULES = DEFAULT_AUTH0_RULES
