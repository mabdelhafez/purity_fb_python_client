# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.11 Python SDK

    Pure Storage FlashBlade REST 1.11 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.11
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class QuotasSetting(object):
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
        'name': 'str',
        'contact': 'str',
        'direct_notifications_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'contact': 'contact',
        'direct_notifications_enabled': 'direct_notifications_enabled'
    }

    def __init__(self, name=None, contact=None, direct_notifications_enabled=None):
        """
        QuotasSetting - a model defined in Swagger
        """

        self._name = None
        self._contact = None
        self._direct_notifications_enabled = None

        if name is not None:
          self.name = name
        if contact is not None:
          self.contact = contact
        if direct_notifications_enabled is not None:
          self.direct_notifications_enabled = direct_notifications_enabled

    @property
    def name(self):
        """
        Gets the name of this QuotasSetting.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this QuotasSetting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QuotasSetting.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this QuotasSetting.
        :type: str
        """

        self._name = name

    @property
    def contact(self):
        """
        Gets the contact of this QuotasSetting.
        The contact information that will be provided in any notifications sent directly to users and groups. This can be an email, a phone number, a name, or some other form of contact information.

        :return: The contact of this QuotasSetting.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this QuotasSetting.
        The contact information that will be provided in any notifications sent directly to users and groups. This can be an email, a phone number, a name, or some other form of contact information.

        :param contact: The contact of this QuotasSetting.
        :type: str
        """

        self._contact = contact

    @property
    def direct_notifications_enabled(self):
        """
        Gets the direct_notifications_enabled of this QuotasSetting.
        Are notifications regarding space usage and quotas being sent directly to user and group emails?

        :return: The direct_notifications_enabled of this QuotasSetting.
        :rtype: bool
        """
        return self._direct_notifications_enabled

    @direct_notifications_enabled.setter
    def direct_notifications_enabled(self, direct_notifications_enabled):
        """
        Sets the direct_notifications_enabled of this QuotasSetting.
        Are notifications regarding space usage and quotas being sent directly to user and group emails?

        :param direct_notifications_enabled: The direct_notifications_enabled of this QuotasSetting.
        :type: bool
        """

        self._direct_notifications_enabled = direct_notifications_enabled

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
        if not isinstance(other, QuotasSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
