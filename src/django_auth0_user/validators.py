import re

from django.core import validators
from django.utils import six
from django.utils.deconstruct import deconstructible
from django.utils.translation import ugettext_lazy as _


@deconstructible
class Auth0UserIdValidator(validators.RegexValidator):
    regex = r'^[\w.@+-|]+$'
    message = _(
        'Enter a valid user_id. This value may contain only letters, '
        'numbers, and @/./+/-/_/| characters.'
    )
    flags = re.UNICODE if six.PY2 else 0
