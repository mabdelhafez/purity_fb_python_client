# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.4 Python SDK

    Pure Storage FlashBlade REST 1.4 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.4
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SmbRule(object):
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
        'acl_mode': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'acl_mode': 'acl_mode'
    }

    def __init__(self, enabled=None, acl_mode=None):
        """
        SmbRule - a model defined in Swagger
        """

        self._enabled = None
        self._acl_mode = None

        if enabled is not None:
          self.enabled = enabled
        if acl_mode is not None:
          self.acl_mode = acl_mode

    @property
    def enabled(self):
        """
        Gets the enabled of this SmbRule.
        is the protocol enabled? Default false when creating a new rule

        :return: The enabled of this SmbRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SmbRule.
        is the protocol enabled? Default false when creating a new rule

        :param enabled: The enabled of this SmbRule.
        :type: bool
        """

        self._enabled = enabled

    @property
    def acl_mode(self):
        """
        Gets the acl_mode of this SmbRule.
        SMB ACL mode. Default shared when creating a new file system. Possible values are shared and native.

        :return: The acl_mode of this SmbRule.
        :rtype: str
        """
        return self._acl_mode

    @acl_mode.setter
    def acl_mode(self, acl_mode):
        """
        Sets the acl_mode of this SmbRule.
        SMB ACL mode. Default shared when creating a new file system. Possible values are shared and native.

        :param acl_mode: The acl_mode of this SmbRule.
        :type: str
        """

        self._acl_mode = acl_mode

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
        if not isinstance(other, SmbRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
