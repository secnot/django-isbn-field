# django-isbn-field [![Build Status](https://github.com/secnot/django-isbn-field/actions/workflows/django.yml/badge.svg)](https://github.com/secnot/django-isbn-field/actions)

Provides django model field to store and validate ISBN numbers.

## Requirements

It has been tested on

* Python >= 3.6
* Django 2.2, 3.3, 4.0

## Installation

From Pypi

```bash
$ pip install django-isbn-field
```

or from the repository

```bash
$ git clone https://github.com/secnot/django-isbn-field
$ python setup.py install
```

## Usage 

Add isbn_field to INSTALLED_APPS

```python
# settings.py
INSTALLED_APPS = (
	...
	'isbn_field',
)
```

Use the field in your model

```python
from django.db import models
from isbn_field import ISBNField

class Book(models.Model):
	isbn = ISBNField()
	...
```

It will raise a ValidationError when the number provided is invalid.

Further, by default any entered ISBN will be cleaned (dashes and spaces are removed) and stored in this canonical form. You can disable this and store the original form through the `clean_isbn` flag.

```python
from django.db import models
from isbn_field import ISBNField

class Book(models.Model):
	dirty_isbn = ISBNField(clean_isbn=False)
	...
```

In case you expect very chaotic input (e.g. more than one space or dash between digits), you might also want to increase the `max_length` of the field to allow for enough room for the string in the database.
