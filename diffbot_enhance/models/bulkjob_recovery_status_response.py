# coding: utf-8

"""
    Diffbot Enhance Service

    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501

    The version of the OpenAPI document: v3.0.0
    Contact: support@diffbot.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from diffbot_enhance.configuration import Configuration


class BulkjobRecoveryStatusResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, status=None, message=None, local_vars_configuration=None):  # noqa: E501
        """BulkjobRecoveryStatusResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._message = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def status(self):
        """Gets the status of this BulkjobRecoveryStatusResponse.  # noqa: E501

        Bulkjob recovery status  # noqa: E501

        :return: The status of this BulkjobRecoveryStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BulkjobRecoveryStatusResponse.

        Bulkjob recovery status  # noqa: E501

        :param status: The status of this BulkjobRecoveryStatusResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_STARTED", "IN_PROCESS", "COMPLETE", "COMPLETE_WITH_FAILURES", "STOPPED", "ERROR_FINALIZING", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this BulkjobRecoveryStatusResponse.  # noqa: E501

        Bulkjob recovery status message  # noqa: E501

        :return: The message of this BulkjobRecoveryStatusResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BulkjobRecoveryStatusResponse.

        Bulkjob recovery status message  # noqa: E501

        :param message: The message of this BulkjobRecoveryStatusResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkjobRecoveryStatusResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkjobRecoveryStatusResponse):
            return True

        return self.to_dict() != other.to_dict()
