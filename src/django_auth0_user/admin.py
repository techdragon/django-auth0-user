from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.contrib.admin import AdminSite
from django.utils.http import is_safe_url
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import resolve_url
from django_auth0_user.util import monkeypatch_method

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


class AdminSiteAuth0LoginMixin(object):
    """
    Mixin that uses Auth0 for login and Auth0 user data for permissions.
    """

    def login(self, request, extra_context=None):
        """
        Redirects to the site login page for the given HttpRequest.

        :param request:
        :param extra_context:
        :return:
        """
        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))

        if not redirect_to or not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        return redirect_to_login(redirect_to)


class AdminSiteWithAuth0Authentication(AdminSiteAuth0LoginMixin, AdminSite):
    """
    AdminSite using Auth0 for authentication and Auth0 user data for permission checking.
    """
    pass


# Should I be using wrapt?
def patch_admin():
    @monkeypatch_method(AdminSite)
    def login(self, request, extra_context=None):
        """
        Redirects to the site login page for the given HttpRequest.

        :param self:
        :param request:
        :param extra_context:
        :return:
        """
        redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))

        if not redirect_to or not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        return redirect_to_login(redirect_to)

        # return redirect('%s?%s' % (
        #     settings.LOGIN_URL,
        #     urlencode({REDIRECT_FIELD_NAME: request.get_full_path()})
        # ))


def unpatch_admin():
    setattr(AdminSite, 'login', original_login)


original_login = AdminSite.login
if getattr(settings, 'AUTH0_PATCH_ADMIN', True):
    patch_admin()
