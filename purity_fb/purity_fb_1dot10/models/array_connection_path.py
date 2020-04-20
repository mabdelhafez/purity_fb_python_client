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


class ArrayConnectionPath(object):
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
        'destination': 'str',
        'source': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destination': 'destination',
        'source': 'source',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, destination=None, source=None, status=None):
        """
        ArrayConnectionPath - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._destination = None
        self._source = None
        self._status = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if destination is not None:
          self.destination = destination
        if source is not None:
          self.source = source
        if status is not None:
          self.status = status

    @property
    def id(self):
        """
        Gets the id of this ArrayConnectionPath.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this ArrayConnectionPath.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ArrayConnectionPath.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this ArrayConnectionPath.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ArrayConnectionPath.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this ArrayConnectionPath.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ArrayConnectionPath.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this ArrayConnectionPath.
        :type: str
        """

        self._name = name

    @property
    def destination(self):
        """
        Gets the destination of this ArrayConnectionPath.
        IP address of the target array.

        :return: The destination of this ArrayConnectionPath.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this ArrayConnectionPath.
        IP address of the target array.

        :param destination: The destination of this ArrayConnectionPath.
        :type: str
        """

        self._destination = destination

    @property
    def source(self):
        """
        Gets the source of this ArrayConnectionPath.
        IP address of the source array.

        :return: The source of this ArrayConnectionPath.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this ArrayConnectionPath.
        IP address of the source array.

        :param source: The source of this ArrayConnectionPath.
        :type: str
        """

        self._source = source

    @property
    def status(self):
        """
        Gets the status of this ArrayConnectionPath.
        Status of the connection. Valid values are `connected` and `connecting`. `connected` - The connection is OK. `connecting` - No connection exists and the array is trying to reconnect.

        :return: The status of this ArrayConnectionPath.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ArrayConnectionPath.
        Status of the connection. Valid values are `connected` and `connecting`. `connected` - The connection is OK. `connecting` - No connection exists and the array is trying to reconnect.

        :param status: The status of this ArrayConnectionPath.
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
        if not isinstance(other, ArrayConnectionPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
