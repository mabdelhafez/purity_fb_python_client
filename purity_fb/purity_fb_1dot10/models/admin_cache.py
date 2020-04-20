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


class AdminCache(object):
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
        'role': 'str',
        'time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'time': 'time'
    }

    def __init__(self, id=None, name=None, role=None, time=None):
        """
        AdminCache - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._role = None
        self._time = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if role is not None:
          self.role = role
        if time is not None:
          self.time = time

    @property
    def id(self):
        """
        Gets the id of this AdminCache.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this AdminCache.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AdminCache.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this AdminCache.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AdminCache.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this AdminCache.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AdminCache.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this AdminCache.
        :type: str
        """

        self._name = name

    @property
    def role(self):
        """
        Gets the role of this AdminCache.
        the role of the user

        :return: The role of this AdminCache.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AdminCache.
        the role of the user

        :param role: The role of this AdminCache.
        :type: str
        """

        self._role = role

    @property
    def time(self):
        """
        Gets the time of this AdminCache.
        Time the role was cached in milliseconds since UNIX epoch

        :return: The time of this AdminCache.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this AdminCache.
        Time the role was cached in milliseconds since UNIX epoch

        :param time: The time of this AdminCache.
        :type: int
        """

        self._time = time

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
        if not isinstance(other, AdminCache):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
