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


class FileSystemReplicaLink(object):
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
        'direction': 'Direction',
        'id': 'str',
        'lag': 'int',
        'remote': 'FixedReferenceWithId',
        'status_details': 'str',
        'local_file_system': 'FixedReferenceWithId',
        'policies': 'list[LocationReference]',
        'recovery_point': 'int',
        'remote_file_system': 'FixedReferenceNoResourceType',
        'status': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'id': 'id',
        'lag': 'lag',
        'remote': 'remote',
        'status_details': 'status_details',
        'local_file_system': 'local_file_system',
        'policies': 'policies',
        'recovery_point': 'recovery_point',
        'remote_file_system': 'remote_file_system',
        'status': 'status'
    }

    def __init__(self, direction=None, id=None, lag=None, remote=None, status_details=None, local_file_system=None, policies=None, recovery_point=None, remote_file_system=None, status=None):
        """
        FileSystemReplicaLink - a model defined in Swagger
        """

        self._direction = None
        self._id = None
        self._lag = None
        self._remote = None
        self._status_details = None
        self._local_file_system = None
        self._policies = None
        self._recovery_point = None
        self._remote_file_system = None
        self._status = None

        if direction is not None:
          self.direction = direction
        if id is not None:
          self.id = id
        if lag is not None:
          self.lag = lag
        if remote is not None:
          self.remote = remote
        if status_details is not None:
          self.status_details = status_details
        if local_file_system is not None:
          self.local_file_system = local_file_system
        if policies is not None:
          self.policies = policies
        if recovery_point is not None:
          self.recovery_point = recovery_point
        if remote_file_system is not None:
          self.remote_file_system = remote_file_system
        if status is not None:
          self.status = status

    @property
    def direction(self):
        """
        Gets the direction of this FileSystemReplicaLink.

        :return: The direction of this FileSystemReplicaLink.
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this FileSystemReplicaLink.

        :param direction: The direction of this FileSystemReplicaLink.
        :type: Direction
        """

        self._direction = direction

    @property
    def id(self):
        """
        Gets the id of this FileSystemReplicaLink.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this FileSystemReplicaLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FileSystemReplicaLink.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this FileSystemReplicaLink.
        :type: str
        """

        self._id = id

    @property
    def lag(self):
        """
        Gets the lag of this FileSystemReplicaLink.
        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.

        :return: The lag of this FileSystemReplicaLink.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """
        Sets the lag of this FileSystemReplicaLink.
        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.

        :param lag: The lag of this FileSystemReplicaLink.
        :type: int
        """

        self._lag = lag

    @property
    def remote(self):
        """
        Gets the remote of this FileSystemReplicaLink.
        Reference to a remote target.

        :return: The remote of this FileSystemReplicaLink.
        :rtype: FixedReferenceWithId
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """
        Sets the remote of this FileSystemReplicaLink.
        Reference to a remote target.

        :param remote: The remote of this FileSystemReplicaLink.
        :type: FixedReferenceWithId
        """

        self._remote = remote

    @property
    def status_details(self):
        """
        Gets the status_details of this FileSystemReplicaLink.
        Detailed information about the status of the replica link.

        :return: The status_details of this FileSystemReplicaLink.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this FileSystemReplicaLink.
        Detailed information about the status of the replica link.

        :param status_details: The status_details of this FileSystemReplicaLink.
        :type: str
        """

        self._status_details = status_details

    @property
    def local_file_system(self):
        """
        Gets the local_file_system of this FileSystemReplicaLink.
        Reference to a local file system.

        :return: The local_file_system of this FileSystemReplicaLink.
        :rtype: FixedReferenceWithId
        """
        return self._local_file_system

    @local_file_system.setter
    def local_file_system(self, local_file_system):
        """
        Sets the local_file_system of this FileSystemReplicaLink.
        Reference to a local file system.

        :param local_file_system: The local_file_system of this FileSystemReplicaLink.
        :type: FixedReferenceWithId
        """

        self._local_file_system = local_file_system

    @property
    def policies(self):
        """
        Gets the policies of this FileSystemReplicaLink.

        :return: The policies of this FileSystemReplicaLink.
        :rtype: list[LocationReference]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this FileSystemReplicaLink.

        :param policies: The policies of this FileSystemReplicaLink.
        :type: list[LocationReference]
        """

        self._policies = policies

    @property
    def recovery_point(self):
        """
        Gets the recovery_point of this FileSystemReplicaLink.
        Time when the last replicated snapshot was created, in milliseconds since UNIX epoch. I.e. the recovery point if the file system is promoted.

        :return: The recovery_point of this FileSystemReplicaLink.
        :rtype: int
        """
        return self._recovery_point

    @recovery_point.setter
    def recovery_point(self, recovery_point):
        """
        Sets the recovery_point of this FileSystemReplicaLink.
        Time when the last replicated snapshot was created, in milliseconds since UNIX epoch. I.e. the recovery point if the file system is promoted.

        :param recovery_point: The recovery_point of this FileSystemReplicaLink.
        :type: int
        """

        self._recovery_point = recovery_point

    @property
    def remote_file_system(self):
        """
        Gets the remote_file_system of this FileSystemReplicaLink.
        Reference to a remote file system.

        :return: The remote_file_system of this FileSystemReplicaLink.
        :rtype: FixedReferenceNoResourceType
        """
        return self._remote_file_system

    @remote_file_system.setter
    def remote_file_system(self, remote_file_system):
        """
        Sets the remote_file_system of this FileSystemReplicaLink.
        Reference to a remote file system.

        :param remote_file_system: The remote_file_system of this FileSystemReplicaLink.
        :type: FixedReferenceNoResourceType
        """

        self._remote_file_system = remote_file_system

    @property
    def status(self):
        """
        Gets the status of this FileSystemReplicaLink.
        Status of the replica link. Values include replicating, idle, and unhealthy.

        :return: The status of this FileSystemReplicaLink.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FileSystemReplicaLink.
        Status of the replica link. Values include replicating, idle, and unhealthy.

        :param status: The status of this FileSystemReplicaLink.
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
        if not isinstance(other, FileSystemReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
