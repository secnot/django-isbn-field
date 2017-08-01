from .validators import ISBNValidator
from django.db.models import CharField


class ISBNField(CharField):

    def __init__(self, *args, **kwargs):
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
