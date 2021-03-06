# coding: utf-8

"""
    Diffbot Enhance Service

    Enhance is an API to find a person or organization in the Knowledge Graph using partial data  # noqa: E501

    The version of the OpenAPI document: v1.0.0
    Contact: support@diffbot.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from diffbot_enhance_client.configuration import Configuration


class EnhanceResponse(object):
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
        'score': 'object',
        'enhanced': 'object',
        'query': 'object',
        'warnings': 'object'
    }

    attribute_map = {
        'score': 'score',
        'enhanced': 'enhanced',
        'query': 'query',
        'warnings': 'warnings'
    }

    def __init__(self, score=None, enhanced=None, query=None, warnings=None, local_vars_configuration=None):  # noqa: E501
        """EnhanceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._score = None
        self._enhanced = None
        self._query = None
        self._warnings = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if enhanced is not None:
            self.enhanced = enhanced
        if query is not None:
            self.query = query
        if warnings is not None:
            self.warnings = warnings

    @property
    def score(self):
        """Gets the score of this EnhanceResponse.  # noqa: E501

        Enhance score  # noqa: E501

        :return: The score of this EnhanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this EnhanceResponse.

        Enhance score  # noqa: E501

        :param score: The score of this EnhanceResponse.  # noqa: E501
        :type: object
        """

        self._score = score

    @property
    def enhanced(self):
        """Gets the enhanced of this EnhanceResponse.  # noqa: E501

        Enhanced entity. Can be null if no entity was found.  # noqa: E501

        :return: The enhanced of this EnhanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._enhanced

    @enhanced.setter
    def enhanced(self, enhanced):
        """Sets the enhanced of this EnhanceResponse.

        Enhanced entity. Can be null if no entity was found.  # noqa: E501

        :param enhanced: The enhanced of this EnhanceResponse.  # noqa: E501
        :type: object
        """

        self._enhanced = enhanced

    @property
    def query(self):
        """Gets the query of this EnhanceResponse.  # noqa: E501

        Submitted Enhance query  # noqa: E501

        :return: The query of this EnhanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this EnhanceResponse.

        Submitted Enhance query  # noqa: E501

        :param query: The query of this EnhanceResponse.  # noqa: E501
        :type: object
        """

        self._query = query

    @property
    def warnings(self):
        """Gets the warnings of this EnhanceResponse.  # noqa: E501

        Any warnings while enhancing entity  # noqa: E501

        :return: The warnings of this EnhanceResponse.  # noqa: E501
        :rtype: object
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this EnhanceResponse.

        Any warnings while enhancing entity  # noqa: E501

        :param warnings: The warnings of this EnhanceResponse.  # noqa: E501
        :type: object
        """

        self._warnings = warnings

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
        if not isinstance(other, EnhanceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnhanceResponse):
            return True

        return self.to_dict() != other.to_dict()
