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


class FixedReferenceWithRemote(object):
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
        'id': 'str',
        'name': 'str',
        'resource_type': 'ResourceType',
        'remote': 'FixedReferenceNoResourceType'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resource_type': 'resource_type',
        'remote': 'remote'
    }

    def __init__(self, id=None, name=None, resource_type=None, remote=None):
        """
        FixedReferenceWithRemote - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._resource_type = None
        self._remote = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if resource_type is not None:
          self.resource_type = resource_type
        if remote is not None:
          self.remote = remote

    @property
    def id(self):
        """
        Gets the id of this FixedReferenceWithRemote.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this FixedReferenceWithRemote.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FixedReferenceWithRemote.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this FixedReferenceWithRemote.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FixedReferenceWithRemote.

        :return: The name of this FixedReferenceWithRemote.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FixedReferenceWithRemote.

        :param name: The name of this FixedReferenceWithRemote.
        :type: str
        """

        self._name = name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this FixedReferenceWithRemote.

        :return: The resource_type of this FixedReferenceWithRemote.
        :rtype: ResourceType
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this FixedReferenceWithRemote.

        :param resource_type: The resource_type of this FixedReferenceWithRemote.
        :type: ResourceType
        """

        self._resource_type = resource_type

    @property
    def remote(self):
        """
        Gets the remote of this FixedReferenceWithRemote.
        The remote field of the corresponding array connection.

        :return: The remote of this FixedReferenceWithRemote.
        :rtype: FixedReferenceNoResourceType
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """
        Sets the remote of this FixedReferenceWithRemote.
        The remote field of the corresponding array connection.

        :param remote: The remote of this FixedReferenceWithRemote.
        :type: FixedReferenceNoResourceType
        """

        self._remote = remote

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
        if not isinstance(other, FixedReferenceWithRemote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
