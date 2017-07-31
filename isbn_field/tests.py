from django.core.exceptions import ValidationError
from isbn_field.validators import ISBNValidator

from django.test import TestCase
from django.test.utils import override_settings

class ISBNValidatorTest(TestCase):

    def test_ISBN_too_short(self):
        with self.assertRaises(ValidationError):
            ISBNValidator('111')

        with self.assertRaises(ValidationError):
            ISBNValidator('')

    def test_ISBN_too_long(self):
        with self.assertRaises(ValidationError):
            ISBNValidator('12345678901234')

    def test_ISBN_with_illegal_structure(self):
        with self.assertRaises(ValidationError):
            ISBNValidator('0765348275')

    def test_dashes_as_valid_separators(self):
        assert(ISBNValidator('0-765-348-276'))
        assert(ISBNValidator('0-7-6-5-3-4-8-2-7-6'))

    def test_spaces_as_valid_separators(self):
        assert (ISBNValidator('0 765 348 276'))
        assert (ISBNValidator('0 7 6 5 3 4 8 2 7 6'))

    def test_space_and_dash_as_valid_separators(self):
        assert (ISBNValidator('0 765-348 276'))
        assert (ISBNValidator('0 7 6 5-3 4 8 2 7 6'))

    def test_valid_ISBNs(self):
        # Valid ISBN10
        assert(ISBNValidator('0765348276'))

        # Valid ISBN13
        assert(ISBNValidator('9780765348272'))

        # Valid ISBN10
        assert(ISBNValidator('832070801X'))

        # Valid ISBN13
        assert(ISBNValidator('9788320708011'))
