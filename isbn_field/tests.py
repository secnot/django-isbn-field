from django.core.exceptions import ValidationError
from isbn_field.validators import ISBNValidator



class ISBNValidatorTest(SimpleTestCase):

    def test_calidation(self):
        # Short
        with self.assertRaises(ValidationError):
            ISBNValidator('111')

        # Long
        with self.assertRaises(ValidationError):
            ISBNValidator('12345678901234')

        # Valid ISBN10
        self.assertTrue(ISBNValidator('0765348276'))

        # Valid ISBN13
        self.assertTrue(ISBNValidator('9780765348272'))

