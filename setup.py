from setuptools import setup

setup(
	name='django-isbn-field',
	version='0.3',
	description='Provides a model field to manage and validate isbn numbers',

	url='https://github.com/secnot/django-isbn-field',
	author='secnot',
	
	license='LPGL, see LICENSE file.',
	
        keywords=['django', 'isbn', 'field'],

	classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'], 

	# Package
	packages = ['isbn_field'],
	install_requires = ['Django', 'python-stdnum>=1.5', 'six'],
	zip_safe = False, 
	include_package_data=True,
)
