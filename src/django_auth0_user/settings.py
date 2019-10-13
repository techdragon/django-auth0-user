from django.conf import settings


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


# We need a namespace prefix provided by the user as there is not really a safe and unique default.
NAMESPACED_KEY_PREFIX = settings.AUTH0_NAMESPACED_KEY_PREFIX


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


AUTH0_RULE_CONFIGS = {
    'DJANGO_AUTH0_USER_OIDC_NAMESPACE_PREFIX': NAMESPACED_KEY_PREFIX
}


# Use the Auth0 Rule Configuration object to set the namespace prefix dynamically.
EXAMPLE_METADATA_RULE_FUNCTION = """function (user, context, callback) {
    const NAMESPACE_PREFIX = configuration.DJANGO_AUTH0_USER_OIDC_NAMESPACE_PREFIX;
    if (context.idToken && user.user_metadata) {
        context.idToken[NAMESPACE_PREFIX + 'user_metadata'] = user.user_metadata;
    }
    if (context.idToken && user.app_metadata) {
        context.idToken[NAMESPACE_PREFIX + 'app_metadata'] = user.app_metadata;
    }
    callback(null, user, context);
}
"""


AUTH0_RULES = {
    "Django-Auth0-User-ExampleMetadataRule": {
        "script": EXAMPLE_METADATA_RULE_FUNCTION,
        "stage": "login_success",
        "enabled": True,
        "order": 1,
    }
}
