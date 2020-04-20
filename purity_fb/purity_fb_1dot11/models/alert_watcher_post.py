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


class AlertWatcherPost(object):
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
        'minimum_notification_severity': 'str'
    }

    attribute_map = {
        'minimum_notification_severity': 'minimum_notification_severity'
    }

    def __init__(self, minimum_notification_severity=None):
        """
        AlertWatcherPost - a model defined in Swagger
        """

        self._minimum_notification_severity = None

        if minimum_notification_severity is not None:
          self.minimum_notification_severity = minimum_notification_severity

    @property
    def minimum_notification_severity(self):
        """
        Gets the minimum_notification_severity of this AlertWatcherPost.
        The minimum severity that an alert must have in order for emails to be sent to the array's alert watchers. Possible values include 'info', 'warning', and 'critical'. Defaults to 'info' if not specified.

        :return: The minimum_notification_severity of this AlertWatcherPost.
        :rtype: str
        """
        return self._minimum_notification_severity

    @minimum_notification_severity.setter
    def minimum_notification_severity(self, minimum_notification_severity):
        """
        Sets the minimum_notification_severity of this AlertWatcherPost.
        The minimum severity that an alert must have in order for emails to be sent to the array's alert watchers. Possible values include 'info', 'warning', and 'critical'. Defaults to 'info' if not specified.

        :param minimum_notification_severity: The minimum_notification_severity of this AlertWatcherPost.
        :type: str
        """

        self._minimum_notification_severity = minimum_notification_severity

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
        if not isinstance(other, AlertWatcherPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
