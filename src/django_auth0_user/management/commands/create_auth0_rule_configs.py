from django.core.management.base import BaseCommand, CommandError
from django_auth0_user.util.auth0_api import set_auth0_rule_config_values


# TODO: It should also be possible to set the Auth0 Management API Credentials
#  here instead of requiring them in settings.
class Command(BaseCommand):
    help = 'Add the values specified in AUTH0_RULE_CONFIGS to the Auth0 Rule Configs using the Auth0 Management API'

    def handle(self, *args, **options):
        set_auth0_rule_config_values()
