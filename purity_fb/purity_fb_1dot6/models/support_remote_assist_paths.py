# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0 - 1.6), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.6
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SupportRemoteAssistPaths(object):
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
        'component_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'component_name': 'component_name',
        'status': 'status'
    }

    def __init__(self, component_name=None, status=None):
        """
        SupportRemoteAssistPaths - a model defined in Swagger
        """

        self._component_name = None
        self._status = None

        if component_name is not None:
          self.component_name = component_name
        if status is not None:
          self.status = status

    @property
    def component_name(self):
        """
        Gets the component_name of this SupportRemoteAssistPaths.
        The name of the component.

        :return: The component_name of this SupportRemoteAssistPaths.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this SupportRemoteAssistPaths.
        The name of the component.

        :param component_name: The component_name of this SupportRemoteAssistPaths.
        :type: str
        """

        self._component_name = component_name

    @property
    def status(self):
        """
        Gets the status of this SupportRemoteAssistPaths.
        The status of the remote-assist session on the local FM. Possible values are reconnecting, connected, disconnected, and unknown.

        :return: The status of this SupportRemoteAssistPaths.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SupportRemoteAssistPaths.
        The status of the remote-assist session on the local FM. Possible values are reconnecting, connected, disconnected, and unknown.

        :param status: The status of this SupportRemoteAssistPaths.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, SupportRemoteAssistPaths):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
