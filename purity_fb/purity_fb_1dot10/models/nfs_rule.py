# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.10 Python SDK

    Pure Storage FlashBlade REST 1.10 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.10
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NfsRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'rules': 'str',
        'v3_enabled': 'bool',
        'v4_1_enabled': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'rules': 'rules',
        'v3_enabled': 'v3_enabled',
        'v4_1_enabled': 'v4_1_enabled'
    }

    def __init__(self, enabled=None, rules=None, v3_enabled=None, v4_1_enabled=None):
        """
        NfsRule - a model defined in Swagger
        """

        self._enabled = None
        self._rules = None
        self._v3_enabled = None
        self._v4_1_enabled = None

        if enabled is not None:
          self.enabled = enabled
        if rules is not None:
          self.rules = rules
        if v3_enabled is not None:
          self.v3_enabled = v3_enabled
        if v4_1_enabled is not None:
          self.v4_1_enabled = v4_1_enabled

    @property
    def enabled(self):
        """
        Gets the enabled of this NfsRule.
        Is the NFSv3 protocol enabled? Default is false (deprecated).

        :return: The enabled of this NfsRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NfsRule.
        Is the NFSv3 protocol enabled? Default is false (deprecated).

        :param enabled: The enabled of this NfsRule.
        :type: bool
        """

        self._enabled = enabled

    @property
    def rules(self):
        """
        Gets the rules of this NfsRule.
        NFS rules.

        :return: The rules of this NfsRule.
        :rtype: str
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this NfsRule.
        NFS rules.

        :param rules: The rules of this NfsRule.
        :type: str
        """

        self._rules = rules

    @property
    def v3_enabled(self):
        """
        Gets the v3_enabled of this NfsRule.
        Is the NFSv3 protocol enabled? Default is false.

        :return: The v3_enabled of this NfsRule.
        :rtype: bool
        """
        return self._v3_enabled

    @v3_enabled.setter
    def v3_enabled(self, v3_enabled):
        """
        Sets the v3_enabled of this NfsRule.
        Is the NFSv3 protocol enabled? Default is false.

        :param v3_enabled: The v3_enabled of this NfsRule.
        :type: bool
        """

        self._v3_enabled = v3_enabled

    @property
    def v4_1_enabled(self):
        """
        Gets the v4_1_enabled of this NfsRule.
        Is the NFSv4.1 protocol enabled? Default is false.

        :return: The v4_1_enabled of this NfsRule.
        :rtype: bool
        """
        return self._v4_1_enabled

    @v4_1_enabled.setter
    def v4_1_enabled(self, v4_1_enabled):
        """
        Sets the v4_1_enabled of this NfsRule.
        Is the NFSv4.1 protocol enabled? Default is false.

        :param v4_1_enabled: The v4_1_enabled of this NfsRule.
        :type: bool
        """

        self._v4_1_enabled = v4_1_enabled

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, NfsRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
