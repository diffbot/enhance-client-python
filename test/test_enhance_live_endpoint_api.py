# coding: utf-8

"""
    Diffbot Enhance Service

    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501

    The version of the OpenAPI document: v3.0.0
    Contact: support@diffbot.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import diffbot_enhance
from diffbot_enhance.api.enhance_live_endpoint_api import EnhanceLiveEndpointApi  # noqa: E501
from diffbot_enhance.rest import ApiException


class TestEnhanceLiveEndpointApi(unittest.TestCase):
    """EnhanceLiveEndpointApi unit test stubs"""

    def setUp(self):
        self.api = diffbot_enhance.api.enhance_live_endpoint_api.EnhanceLiveEndpointApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enhance(self):
        """Test case for enhance

        Live Enhance Endpoint  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
