# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.9 Python SDK

    Pure Storage FlashBlade REST 1.9 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.9
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HardwareConnector(object):
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
        'connector_type': 'str',
        'lane_speed': 'int',
        'port_count': 'int',
        'transceiver_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'connector_type': 'connector_type',
        'lane_speed': 'lane_speed',
        'port_count': 'port_count',
        'transceiver_type': 'transceiver_type'
    }

    def __init__(self, name=None, connector_type=None, lane_speed=None, port_count=None, transceiver_type=None):
        """
        HardwareConnector - a model defined in Swagger
        """

        self._name = None
        self._connector_type = None
        self._lane_speed = None
        self._port_count = None
        self._transceiver_type = None

        if name is not None:
          self.name = name
        if connector_type is not None:
          self.connector_type = connector_type
        if lane_speed is not None:
          self.lane_speed = lane_speed
        if port_count is not None:
          self.port_count = port_count
        if transceiver_type is not None:
          self.transceiver_type = transceiver_type

    @property
    def name(self):
        """
        Gets the name of this HardwareConnector.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this HardwareConnector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HardwareConnector.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this HardwareConnector.
        :type: str
        """

        self._name = name

    @property
    def connector_type(self):
        """
        Gets the connector_type of this HardwareConnector.
        Form-factor of the interface. Possible values are QSFP, RJ-45 and SFP.

        :return: The connector_type of this HardwareConnector.
        :rtype: str
        """
        return self._connector_type

    @connector_type.setter
    def connector_type(self, connector_type):
        """
        Sets the connector_type of this HardwareConnector.
        Form-factor of the interface. Possible values are QSFP, RJ-45 and SFP.

        :param connector_type: The connector_type of this HardwareConnector.
        :type: str
        """

        self._connector_type = connector_type

    @property
    def lane_speed(self):
        """
        Gets the lane_speed of this HardwareConnector.
        Configured speed of each lane in the connector in bits-per-second

        :return: The lane_speed of this HardwareConnector.
        :rtype: int
        """
        return self._lane_speed

    @lane_speed.setter
    def lane_speed(self, lane_speed):
        """
        Sets the lane_speed of this HardwareConnector.
        Configured speed of each lane in the connector in bits-per-second

        :param lane_speed: The lane_speed of this HardwareConnector.
        :type: int
        """

        self._lane_speed = lane_speed

    @property
    def port_count(self):
        """
        Gets the port_count of this HardwareConnector.
        Configured number of ports in the connector. (1/2/4 for QSFP)

        :return: The port_count of this HardwareConnector.
        :rtype: int
        """
        return self._port_count

    @port_count.setter
    def port_count(self, port_count):
        """
        Sets the port_count of this HardwareConnector.
        Configured number of ports in the connector. (1/2/4 for QSFP)

        :param port_count: The port_count of this HardwareConnector.
        :type: int
        """

        self._port_count = port_count

    @property
    def transceiver_type(self):
        """
        Gets the transceiver_type of this HardwareConnector.
        Details about the transceiver which is plugged into the connector port. Transceiver type will be read-only for Pureuser. If nothing is plugged into QSFP port, value will be “Unused”. If a transceiver is plugged in, and type cannot be auto-detected,  and internal user has not specified a type - value will be “Unknown”. If transceiver is plugged in, and type is auto-detected, and/or type has been explicitly set by internal user - that value will be shown. Transceiver type is not applicable for RJ-45 connectors.

        :return: The transceiver_type of this HardwareConnector.
        :rtype: str
        """
        return self._transceiver_type

    @transceiver_type.setter
    def transceiver_type(self, transceiver_type):
        """
        Sets the transceiver_type of this HardwareConnector.
        Details about the transceiver which is plugged into the connector port. Transceiver type will be read-only for Pureuser. If nothing is plugged into QSFP port, value will be “Unused”. If a transceiver is plugged in, and type cannot be auto-detected,  and internal user has not specified a type - value will be “Unknown”. If transceiver is plugged in, and type is auto-detected, and/or type has been explicitly set by internal user - that value will be shown. Transceiver type is not applicable for RJ-45 connectors.

        :param transceiver_type: The transceiver_type of this HardwareConnector.
        :type: str
        """

        self._transceiver_type = transceiver_type

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
        if not isinstance(other, HardwareConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
