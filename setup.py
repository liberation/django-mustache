"""Setup script for django-mustache"""
from setuptools import setup
from setuptools import find_packages

import django_mustache


setup(
    name='django-mustache',
    version=django_mustache.__version__,
    packages=find_packages(),
    include_package_data=True,
    license=django_mustache.__license__,
    description='Mustache templates server side rendering in Django',
    long_description=open('README.md').read(),
    author='Djaz Team',
    author_email='devweb@liberation.fr',
    url='http://www.liberation.fr/',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ])
