from django.core.exceptions import ValidationError
from isbn_field.validators import ISBNValidator
from django.test import SimpleTestCase


class ISBNValidatorTest(SimpleTestCase):

    def test_calidation(self):
        # Short
        with self.assertRaises(ValidationError):
            ISBNValidator('111')

        # Long
        with self.assertRaises(ValidationError):
            ISBNValidator('12345678901234')

        # ISBN w Error
        with self.assertRaises(ValidationError):
            ISBNValidator('0765348275')

        # Valid ISBN10
        ISBNValidator('0765348276')

        # Valid ISBN13
        ISBNValidator('9780765348272')

