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


class SnmpManager(object):
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
        'id': 'str',
        'host': 'str',
        'notification': 'str',
        'version': 'str',
        'v2c': 'SnmpV2c',
        'v3': 'SnmpV3'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'host': 'host',
        'notification': 'notification',
        'version': 'version',
        'v2c': 'v2c',
        'v3': 'v3'
    }

    def __init__(self, name=None, id=None, host=None, notification=None, version=None, v2c=None, v3=None):
        """
        SnmpManager - a model defined in Swagger
        """

        self._name = None
        self._id = None
        self._host = None
        self._notification = None
        self._version = None
        self._v2c = None
        self._v3 = None

        if name is not None:
          self.name = name
        if id is not None:
          self.id = id
        if host is not None:
          self.host = host
        if notification is not None:
          self.notification = notification
        if version is not None:
          self.version = version
        if v2c is not None:
          self.v2c = v2c
        if v3 is not None:
          self.v3 = v3

    @property
    def name(self):
        """
        Gets the name of this SnmpManager.
        name of the object

        :return: The name of this SnmpManager.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnmpManager.
        name of the object

        :param name: The name of this SnmpManager.
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this SnmpManager.
        A unique ID chosen by the system. Cannot change.

        :return: The id of this SnmpManager.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SnmpManager.
        A unique ID chosen by the system. Cannot change.

        :param id: The id of this SnmpManager.
        :type: str
        """

        self._id = id

    @property
    def host(self):
        """
        Gets the host of this SnmpManager.
        DNS hostname or IP address of a computer that hosts an SNMP manager to which Purity is to send trap messages when it generates alerts.

        :return: The host of this SnmpManager.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this SnmpManager.
        DNS hostname or IP address of a computer that hosts an SNMP manager to which Purity is to send trap messages when it generates alerts.

        :param host: The host of this SnmpManager.
        :type: str
        """

        self._host = host

    @property
    def notification(self):
        """
        Gets the notification of this SnmpManager.
        The type of notification the agent will send. Valid values are `inform` and `trap`.

        :return: The notification of this SnmpManager.
        :rtype: str
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this SnmpManager.
        The type of notification the agent will send. Valid values are `inform` and `trap`.

        :param notification: The notification of this SnmpManager.
        :type: str
        """

        self._notification = notification

    @property
    def version(self):
        """
        Gets the version of this SnmpManager.
        Version of the SNMP protocol to be used by Purity in communications with the specified manager. Valid values are `v2c` and `v3`.

        :return: The version of this SnmpManager.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SnmpManager.
        Version of the SNMP protocol to be used by Purity in communications with the specified manager. Valid values are `v2c` and `v3`.

        :param version: The version of this SnmpManager.
        :type: str
        """

        self._version = version

    @property
    def v2c(self):
        """
        Gets the v2c of this SnmpManager.

        :return: The v2c of this SnmpManager.
        :rtype: SnmpV2c
        """
        return self._v2c

    @v2c.setter
    def v2c(self, v2c):
        """
        Sets the v2c of this SnmpManager.

        :param v2c: The v2c of this SnmpManager.
        :type: SnmpV2c
        """

        self._v2c = v2c

    @property
    def v3(self):
        """
        Gets the v3 of this SnmpManager.

        :return: The v3 of this SnmpManager.
        :rtype: SnmpV3
        """
        return self._v3

    @v3.setter
    def v3(self, v3):
        """
        Sets the v3 of this SnmpManager.

        :param v3: The v3 of this SnmpManager.
        :type: SnmpV3
        """

        self._v3 = v3

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
        if not isinstance(other, SnmpManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
