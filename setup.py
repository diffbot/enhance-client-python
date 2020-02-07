# coding: utf-8

"""
    Diffbot Enhance Service

    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501

    The version of the OpenAPI document: v3.0.0
    Contact: support@diffbot.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "diffbot_enhance_client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Diffbot Enhance Service",
    author="OpenAPI Generator community",
    author_email="support@diffbot.com",
    url="https://github.com/diffbot/enhance-client-python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Diffbot Enhance Service"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501
    """
)
