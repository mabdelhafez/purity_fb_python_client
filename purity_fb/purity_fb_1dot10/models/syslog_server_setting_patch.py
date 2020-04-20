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


class SyslogServerSettingPatch(object):
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
        'ca_certificate': 'Reference',
        'ca_certificate_group': 'Reference'
    }

    attribute_map = {
        'ca_certificate': 'ca_certificate',
        'ca_certificate_group': 'ca_certificate_group'
    }

    def __init__(self, ca_certificate=None, ca_certificate_group=None):
        """
        SyslogServerSettingPatch - a model defined in Swagger
        """

        self._ca_certificate = None
        self._ca_certificate_group = None

        if ca_certificate is not None:
          self.ca_certificate = ca_certificate
        if ca_certificate_group is not None:
          self.ca_certificate_group = ca_certificate_group

    @property
    def ca_certificate(self):
        """
        Gets the ca_certificate of this SyslogServerSettingPatch.
        CA certificate used to validate the authenticity of the configured servers.

        :return: The ca_certificate of this SyslogServerSettingPatch.
        :rtype: Reference
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this SyslogServerSettingPatch.
        CA certificate used to validate the authenticity of the configured servers.

        :param ca_certificate: The ca_certificate of this SyslogServerSettingPatch.
        :type: Reference
        """

        self._ca_certificate = ca_certificate

    @property
    def ca_certificate_group(self):
        """
        Gets the ca_certificate_group of this SyslogServerSettingPatch.
        A certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.

        :return: The ca_certificate_group of this SyslogServerSettingPatch.
        :rtype: Reference
        """
        return self._ca_certificate_group

    @ca_certificate_group.setter
    def ca_certificate_group(self, ca_certificate_group):
        """
        Sets the ca_certificate_group of this SyslogServerSettingPatch.
        A certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.

        :param ca_certificate_group: The ca_certificate_group of this SyslogServerSettingPatch.
        :type: Reference
        """

        self._ca_certificate_group = ca_certificate_group

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
        if not isinstance(other, SyslogServerSettingPatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
