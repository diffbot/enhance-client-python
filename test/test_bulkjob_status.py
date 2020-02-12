# coding: utf-8

"""
    Diffbot Enhance Service

    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501

    The version of the OpenAPI document: v1.0.0
    Contact: support@diffbot.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import diffbot_enhance_client
from diffbot_enhance_client.models.bulkjob_status import BulkjobStatus  # noqa: E501
from diffbot_enhance_client.rest import ApiException

class TestBulkjobStatus(unittest.TestCase):
    """BulkjobStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BulkjobStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = diffbot_enhance_client.models.bulkjob_status.BulkjobStatus()  # noqa: E501
        if include_optional :
            return BulkjobStatus(
                job_id = '0', 
                message = '0', 
                jobs_total = 56, 
                jobs_completed = 56, 
                status = 'NOT_STARTED', 
                estimate_remaining_time = 56
            )
        else :
            return BulkjobStatus(
        )

    def testBulkjobStatus(self):
        """Test BulkjobStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
