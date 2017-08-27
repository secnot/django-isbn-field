from django.db import models
from isbn_field import ISBNField

class CleanISBNModel(models.Model):

    isbn = ISBNField() # clean_isbn=True (default)


class DirtyISBNModel(models.Model):
    
    isbn = ISBNField(clean_isbn=False)

