from .validators import ISBNValidator
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from django.core.validators import EMPTY_VALUES

class ISBNField(CharField):

    description = _("ISBN-10 or ISBN-13")

    def __init__(self, clean_isbn=True, *args, **kwargs):
        self.clean_isbn = clean_isbn
        kwargs['max_length'] = kwargs['max_length'] if 'max_length' in kwargs else 28
        kwargs['verbose_name'] = kwargs['verbose_name'] if 'verbose_name' in kwargs else u'ISBN'
        kwargs['validators'] = [ISBNValidator]
        super(ISBNField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'min_length': 10,
            'validators': [ISBNValidator],
        }
        defaults.update(kwargs)
        return super(ISBNField, self).formfield(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super(ISBNField, self).deconstruct()
        # Only include clean_isbn in kwarg if it's not the default value
        if not self.clean_isbn:
            kwargs['clean_isbn'] = self.clean_isbn
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        """Remove dashes, spaces, and convert isbn to uppercase before saving
        when clean_isbn is enabled"""
        value = getattr(model_instance, self.attname)
        if self.clean_isbn and value not in EMPTY_VALUES:
            cleaned_isbn = value.replace(' ', '').replace('-', '').upper()
            setattr(model_instance, self.attname, cleaned_isbn)
        return super(ISBNField, self).pre_save(model_instance, add)

    def __unicode__(self):
        return self.value
