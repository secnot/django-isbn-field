from django.core.exceptions import ValidationError
from django.test import TestCase

from isbn_field.validators import ISBNValidator
from .models import CleanISBNModel, DirtyISBNModel, BlankISBNModel, BlankNullISBNModel, UniqueCleanISBNModel


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

    def test_invalid_lower_case_x_ISBN(self):
        with self.assertRaises(ValidationError):
            ISBNValidator('832070801x')

    def test_dashes_as_valid_separators(self):
        assert(ISBNValidator('0-765-348-276'))
        assert(ISBNValidator('0-7-6-5-3-4-8-2-7-6'))

    def test_spaces_as_valid_separators(self):
        assert(ISBNValidator('0 765 348 276'))
        assert(ISBNValidator('0 7 6 5 3 4 8 2 7 6'))

    def test_space_and_dash_as_valid_separators(self):
        assert(ISBNValidator('0 765-348 276'))
        assert(ISBNValidator('0 7 6 5-3 4 8 2 7 6'))

    def test_valid_ISBNs(self):
        # Valid ISBN10
        assert(ISBNValidator('0765348276'))

        # Valid ISBN13
        assert(ISBNValidator('9780765348272'))

        # Valid ISBN10
        assert(ISBNValidator('832070801X'))

        # Valid ISBN13
        assert(ISBNValidator('9788320708011'))


class ISBNFieldTest(TestCase):

    def test_isbn_field_clean(self):
        
        isbns = [
            ('0765348276', '0-765-348-276'),
            ('0765348276', '0 765 348 276'),
            ('0765348276', '0-765 348-276'),
            ('076535618X', '0 765 35-61 8x'),
            ('9788320708011', '9788320708011')]
        
        for clean, original in isbns:
            m = CleanISBNModel.objects.create(isbn=original)
            self.assertEqual(m.isbn, clean)

            m = DirtyISBNModel.objects.create(isbn=original)
            self.assertEqual(m.isbn, original)

    def test_isbn_field_unique_clean(self):
        UniqueCleanISBNModel.objects.create(isbn='0-765-348-276')

        with self.assertRaises(ValidationError):
            instance = UniqueCleanISBNModel(isbn='0-765-348-276')
            instance.full_clean()
            # The previous line should throw the expected exception,
            # but if it does not, the line below throwing an IntegrityError
            # serves as a sanity check for this test.
            UniqueCleanISBNModel.objects.create(isbn='0-765-348-276')

    def test_isbn_field_blank(self):
        """Test empty values are accepted when blank=True"""
        m = BlankISBNModel.objects.create(isbn="")
        self.assertEqual(m.isbn, "")

    def test_isbn_field_null(self):
        """Test null values are accested when blank=True null=True"""
        m = BlankNullISBNModel.objects.create(isbn=None)
        self.assertEqual(m.isbn, None)

