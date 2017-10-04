from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .validators import Auth0UserIdValidator
from .permission_checks import IS_STAFF
from .permission_checks import IS_ACTIVE
from .permission_checks import IS_SUPERUSER
from decorator import decorate
from decorator import decorator


# This app comes with its own custom user model so that going forward
# we can enhance the model with deeper integration with Auth0, such as:
#  permissions based on user_data.
class AbstractAuth0User(AbstractUser):
    """
    """
    username_validator = Auth0UserIdValidator
    use_auth0_username = True

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_/| only.'),
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

    # -------------------------------------
    # Convenience / Quick Access Properties
    # -------------------------------------
    # Accessing user data to make decisions should be quick and easy,
    # so our abstract class adds these properties to help make it easier
    # to leverage Auth0 functionality such as the user and app metadata.

    @property
    def user_metadata(self):
        return self.auth0_data['id_token_payload']['user_metadata']

    @property
    def app_metadata(self):
        return self.auth0_data['id_token_payload']['app_metadata']

    class Meta:
        abstract = True


class Auth0User(AbstractAuth0User):
    """
    """
    pass
