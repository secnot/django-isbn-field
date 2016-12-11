from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from six import string_types
from stdnum import isbn


def ISBNValidator(value):
    """ Check string is a valid ISBN number"""
    
    if not isinstance(value, string_types):
        raise ValidationError(_(u'Invalid ISBN: Not a string'))

    if len(value) != 10 and len(value) != 13:
        raise ValidationError(_(u'Invalid ISBN: Wrong length'))
    
    if not value.isdigit():
        raise ValidationError(_(u'Invalid ISBN: Only numbers are allowed'))

    if not isbn.is_valid(value):
        raise ValidationError(_(u'Invalid ISBN: Failed checksum'))
