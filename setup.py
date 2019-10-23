#!/usr/bin/env python
# coding=utf-8

import sys
from setuptools import setup
from setuptools import find_packages

if sys.version_info < (2, 6):
    sys.exit('Python 2.5 or greater is required.')

with open('README.rst') as fp:
    readme = fp.read()

setup(
    name='workflow-engine',
    version='0.1.1',
    description='Used for Batch Management System and Production Application',
    long_description=readme,

    url='',
    author='',
    author_email='',

    packages=find_packages(),
    include_package_data=True,
    platforms='linux',
    install_requires=[
        'paramiko',
        'PyYAML',
        'pymongo'
    ],
)
