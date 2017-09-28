from __future__ import unicode_literals
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .validators import Auth0UserIdValidator


# This app comes with its own custom user model so that going forward
# we can enhance the model with deeper integration with Auth0, such as:
#  permissions based on user_data.
class Auth0User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username, password and email are required. Other fields are optional.
    """
    username_validator = Auth0UserIdValidator

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

    # Because First and Last names just don't cut it.
    name = models.CharField(_('name'), max_length=255, blank=True)

    class Meta(AbstractUser.Meta):
        # This is swappable because I'm not arrogant.
        swappable = 'DJANGO_AUTH0_AUTH_USER_MODEL'
