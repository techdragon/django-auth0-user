import importlib
from django.conf import settings


def auth0_user_is_superuser(auth0_user):
    """
    Check if an Auth0User has been marked as having superuser status.

    :param django_db_auth0_user.models.Auth0User auth0_user: The Auth0User to check for supervisor status.
    :return:
    """
    if auth0_user.auth0_app_metadata:
        return auth0_user.auth0_app_metadata.get('is_superuser', False)
    else:
        return False


def auth0_user_is_staff(auth0_user):
    """
    Check if an Auth0User has been marked as having staff status.

    :param django_db_auth0_user.models.Auth0User auth0_user: The Auth0User to check for staff status.
    :return:
    """
    if auth0_user.auth0_app_metadata:
        if auth0_user.is_superuser:
            return True
        return auth0_user.auth0_app_metadata.get('is_staff', False)
    else:
        return False


def auth0_user_is_active(auth0_user):
    """
    Check if an Auth0User has been marked as having active status.

    The built in default is True, since the majority of sites will want to set new users as active.

    :param django_db_auth0_user.models.Auth0User auth0_user: The Auth0User to check for active status.
    :return:
    """
    default_active_value = getattr(settings, 'AUTH0_USER_DEFAULT_IS_ACTIVE_VALUE', True)
    if auth0_user.auth0_app_metadata:
        return auth0_user.auth0_app_metadata.get('is_active', default_active_value)
    else:
        return default_active_value


# Just a reminder how this import magic works.
# function_string = 'mypackage.mymodule.myfunc'
# mod_name, func_name = function_string.rsplit('.',1)
# mod = importlib.import_module(mod_name)
# func = getattr(mod, func_name)
# result = func()


AUTH0_USER_IS_SUPERUSER_CHECK_FUNCTION = getattr(settings, 'AUTH0_USER_IS_SUPERUSER_CHECK_FUNCTION',
                                                 'django_auth0_user.permission_checks.auth0_user_is_superuser')
superuser_module_name, supervisor_func_name = AUTH0_USER_IS_SUPERUSER_CHECK_FUNCTION.rsplit('.', 1)
superuser_module = importlib.import_module(superuser_module_name)
IS_SUPERUSER = getattr(superuser_module, supervisor_func_name)


AUTH0_USER_IS_STAFF_CHECK_FUNCTION = getattr(settings, 'AUTH0_USER_IS_STAFF_CHECK_FUNCTION',
                                             'django_auth0_user.permission_checks.auth0_user_is_staff')
staff_module_name, staff_func_name = AUTH0_USER_IS_STAFF_CHECK_FUNCTION.rsplit('.', 1)
staff_module = importlib.import_module(staff_module_name)
IS_STAFF = getattr(staff_module, staff_func_name)


AUTH0_USER_IS_ACTIVE_CHECK_FUNCTION = getattr(settings, 'AUTH0_USER_IS_ACTIVE_CHECK_FUNCTION',
                                              'django_auth0_user.permission_checks.auth0_user_is_active')
active_module_name, active_func_name = AUTH0_USER_IS_ACTIVE_CHECK_FUNCTION.rsplit('.', 1)
active_module = importlib.import_module(active_module_name)
IS_ACTIVE = getattr(active_module, active_func_name)








