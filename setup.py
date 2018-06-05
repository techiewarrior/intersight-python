# coding: utf-8

"""
    Intersight API

    This is the Intersight REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "intersight"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six", "certifi", "python-dateutil", "pycrypto >= 2.6.1", "requests"]

setup(
    name=NAME,
    version=VERSION,
    description="Intersight API",
    author_email="",
    url="",
    keywords=["Swagger", "Intersight API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the Intersight REST API
    """
)
