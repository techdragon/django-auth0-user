from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from jwt import decode as jwt_decode
from jwt import DecodeError

from django_auth0_user.validators import Auth0UserIdValidator
from django_auth0_user.settings import USER_ID_IS_DJANGO_USERNAME
from django_auth0_user.settings import NAMESPACED_USER_METADATA_KEY
from django_auth0_user.settings import NAMESPACED_APP_METADATA_KEY


# TODO: The default social_django model uses a foreign key from the social account model
#   to a django user model instance in order to allow multiple social logins for a single
#   django user, however since this is a function that Auth0 abstracts away for us,
#   we can bind the models more tightly and use a OneToOneField. Look into this option further.


class AbstractAuth0User(AbstractUser):
    """
    An abstract base user designed for easy use with Auth0
    """

    # In order to accept the "|" character in a Django Username we need to change the validator.
    if USER_ID_IS_DJANGO_USERNAME:
        username_validator = Auth0UserIdValidator()
        username_help_text = _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_/| only.')
    else:
        username_validator = UnicodeUsernameValidator()
        username_help_text = _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=username_help_text,
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    # ----------------
    # Helper Functions
    # ----------------

    @property
    def auth0_data(self):
        if self.social_auth.count() == 1:
            return self.social_auth.get().extra_data
        else:
            raise NotImplementedError(
                "More than one social auth model instance is associated with this django user model instance"
            )

    @property
    def id_token_payload(self):
        if self.auth0_data['id_token'] is not None:
            try:
                # TODO: Decide how I want to handle verifying the tokens.
                return jwt_decode(self.auth0_data['id_token'], verify=False)
            except DecodeError:
                return None
        else:
            return None

    @property
    def access_token_payload(self):
        if self.auth0_data['access_token'] is not None:
            try:
                # TODO: Decide how I want to handle verifying the tokens.
                return jwt_decode(self.auth0_data['access_token'], verify=False)
            except DecodeError:
                return None
        else:
            return None

    @property
    def refresh_token_payload(self):
        if self.auth0_data['refresh_token'] is not None:
            try:
                # TODO: Decide how I want to handle verifying the tokens.
                return jwt_decode(self.auth0_data['refresh_token'], verify=False)
            except DecodeError:
                return None
        else:
            return None

    # -------------------------------------
    # Convenience / Quick Access Properties
    # -------------------------------------
    # Accessing user data to make decisions should be quick and easy,
    # so our abstract class adds these properties to help make it easier
    # to leverage Auth0 functionality such as the user and app metadata.

    @property
    def user_metadata(self):
        # TODO: Only do this is we are dealing with an OIDC compliant endpoint.
        # TODO: Ensure any auto-created rule is based on the same metadata dict key so this doesnt break.

        if NAMESPACED_USER_METADATA_KEY is not None:
            if NAMESPACED_USER_METADATA_KEY in self.auth0_data['id_token_payload']:
                return self.auth0_data['id_token_payload'][NAMESPACED_USER_METADATA_KEY]

        if 'user_metadata' in self.auth0_data['id_token_payload']:
            return self.auth0_data['id_token_payload']['user_metadata']

        return None

    @property
    def app_metadata(self):
        # TODO: Only do this is we are dealing with an OIDC compliant endpoint.
        # TODO: Ensure any auto-created rule is based on the same metadata dict key so this doesnt break.

        if NAMESPACED_APP_METADATA_KEY is not None:
            if NAMESPACED_APP_METADATA_KEY in self.auth0_data['id_token_payload']:
                return self.auth0_data['id_token_payload'][NAMESPACED_APP_METADATA_KEY]

        if 'app_metadata' in self.auth0_data['id_token_payload']:
            return self.auth0_data['id_token_payload']['app_metadata']

        return None

    class Meta:
        abstract = True


# TODO: Move this into tests, or raise a warning when used?
# Users of this library should have their own custom user model!
