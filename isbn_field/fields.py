from .validators import ISBNValidator
from django.db.models import CharField


class ISBNField(CharField):

    def __init__(self, *args, **kwargs):
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

    def __unicode__(self):
        return self.value
