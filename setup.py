# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django_bootstrap',
    version='2.3.1',
    author=u'Charles Hathaway',
    author_email='chathaway@logrit.com',
    packages=['django_bootstrap'],
    url='https://github.com/chuck211991/django_boostrap',
    license='BSD licence, see LICENCE.txt',
    description='Very Django app that containts the static Bootstrap files in static/{css,js}',
    zip_safe=False,
    include_package_data=True,
)
