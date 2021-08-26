# -*- encoding: utf-8 -*-
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rest-structure',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'djangorestframework>=3.12.4',
        'django>=3.0.0',

    ],
    python_requires=">=3.8",
    description='Structure for django rest framework.',
    long_description=README,
    url='https://github.com/ArefMousakhani/django_rest_structure',
    author='Aref Mousakhani',
    author_email='aref.mousakhani@gmail.com',
    classifiers=[
        "Framework :: Django :: 3",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)