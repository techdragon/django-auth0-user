import six
import unicodedata
import re


# This slugify version was borrowed from django revision a61dbd6
def slugify(value):
    """Converts to lowercase, removes non-word characters (alphanumerics
    and underscores) and converts spaces to hyphens. Also strips leading
    and trailing whitespace."""
    value = unicodedata.normalize('NFKD', six.text_type(value)).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^[\w.@+-|]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)
