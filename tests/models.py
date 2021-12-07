from django.db import models
from isbn_field import ISBNField

class CleanISBNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = ISBNField() # clean_isbn=True (default)


class DirtyISBNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = ISBNField(clean_isbn=False)


class BlankISBNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = ISBNField(clean_isbn=True, blank=True)

class BlankNullISBNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn = ISBNField(clean_isbn=True, blank=True, null=True)
