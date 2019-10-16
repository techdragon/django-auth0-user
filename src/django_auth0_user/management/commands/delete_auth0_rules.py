from django.core.management.base import BaseCommand, CommandError
from django_auth0_user.util.auth0_api import tear_down_auth0_rules


# TODO: It should also be possible to set the Auth0 Management API Credentials
#  here instead of requiring them in settings.
class Command(BaseCommand):
    help = 'Remove the values specified in AUTH0_RULES from the Rules in Auth0 using the Auth0 Management API'

    def handle(self, *args, **options):
        tear_down_auth0_rules(dry_run=False)
