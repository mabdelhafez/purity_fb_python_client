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


class BucketReplicaLink(object):
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
        'local_bucket': 'FixedReferenceWithId',
        'paused': 'bool',
        'recovery_point': 'int',
        'remote_bucket': 'Reference',
        'remote_credentials': 'Reference',
        'status': 'str'
    }

    attribute_map = {
        'direction': 'direction',
        'id': 'id',
        'lag': 'lag',
        'remote': 'remote',
        'status_details': 'status_details',
        'local_bucket': 'local_bucket',
        'paused': 'paused',
        'recovery_point': 'recovery_point',
        'remote_bucket': 'remote_bucket',
        'remote_credentials': 'remote_credentials',
        'status': 'status'
    }

    def __init__(self, direction=None, id=None, lag=None, remote=None, status_details=None, local_bucket=None, paused=None, recovery_point=None, remote_bucket=None, remote_credentials=None, status=None):
        """
        BucketReplicaLink - a model defined in Swagger
        """

        self._direction = None
        self._id = None
        self._lag = None
        self._remote = None
        self._status_details = None
        self._local_bucket = None
        self._paused = None
        self._recovery_point = None
        self._remote_bucket = None
        self._remote_credentials = None
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
        if local_bucket is not None:
          self.local_bucket = local_bucket
        if paused is not None:
          self.paused = paused
        if recovery_point is not None:
          self.recovery_point = recovery_point
        if remote_bucket is not None:
          self.remote_bucket = remote_bucket
        if remote_credentials is not None:
          self.remote_credentials = remote_credentials
        if status is not None:
          self.status = status

    @property
    def direction(self):
        """
        Gets the direction of this BucketReplicaLink.

        :return: The direction of this BucketReplicaLink.
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this BucketReplicaLink.

        :param direction: The direction of this BucketReplicaLink.
        :type: Direction
        """

        self._direction = direction

    @property
    def id(self):
        """
        Gets the id of this BucketReplicaLink.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this BucketReplicaLink.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BucketReplicaLink.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this BucketReplicaLink.
        :type: str
        """

        self._id = id

    @property
    def lag(self):
        """
        Gets the lag of this BucketReplicaLink.
        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.

        :return: The lag of this BucketReplicaLink.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """
        Sets the lag of this BucketReplicaLink.
        Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.

        :param lag: The lag of this BucketReplicaLink.
        :type: int
        """

        self._lag = lag

    @property
    def remote(self):
        """
        Gets the remote of this BucketReplicaLink.
        Reference to a remote target.

        :return: The remote of this BucketReplicaLink.
        :rtype: FixedReferenceWithId
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """
        Sets the remote of this BucketReplicaLink.
        Reference to a remote target.

        :param remote: The remote of this BucketReplicaLink.
        :type: FixedReferenceWithId
        """

        self._remote = remote

    @property
    def status_details(self):
        """
        Gets the status_details of this BucketReplicaLink.
        Detailed information about the status of the replica link.

        :return: The status_details of this BucketReplicaLink.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this BucketReplicaLink.
        Detailed information about the status of the replica link.

        :param status_details: The status_details of this BucketReplicaLink.
        :type: str
        """

        self._status_details = status_details

    @property
    def local_bucket(self):
        """
        Gets the local_bucket of this BucketReplicaLink.
        Reference to a local bucket.

        :return: The local_bucket of this BucketReplicaLink.
        :rtype: FixedReferenceWithId
        """
        return self._local_bucket

    @local_bucket.setter
    def local_bucket(self, local_bucket):
        """
        Sets the local_bucket of this BucketReplicaLink.
        Reference to a local bucket.

        :param local_bucket: The local_bucket of this BucketReplicaLink.
        :type: FixedReferenceWithId
        """

        self._local_bucket = local_bucket

    @property
    def paused(self):
        """
        Gets the paused of this BucketReplicaLink.
        Is the replica link paused?

        :return: The paused of this BucketReplicaLink.
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """
        Sets the paused of this BucketReplicaLink.
        Is the replica link paused?

        :param paused: The paused of this BucketReplicaLink.
        :type: bool
        """

        self._paused = paused

    @property
    def recovery_point(self):
        """
        Gets the recovery_point of this BucketReplicaLink.
        Time, in milliseconds since UNIX epoch, where all object changes before this time are guaranteed to have been replicated. Changes after this time may have been replicated.

        :return: The recovery_point of this BucketReplicaLink.
        :rtype: int
        """
        return self._recovery_point

    @recovery_point.setter
    def recovery_point(self, recovery_point):
        """
        Sets the recovery_point of this BucketReplicaLink.
        Time, in milliseconds since UNIX epoch, where all object changes before this time are guaranteed to have been replicated. Changes after this time may have been replicated.

        :param recovery_point: The recovery_point of this BucketReplicaLink.
        :type: int
        """

        self._recovery_point = recovery_point

    @property
    def remote_bucket(self):
        """
        Gets the remote_bucket of this BucketReplicaLink.
        Reference to a remote bucket.

        :return: The remote_bucket of this BucketReplicaLink.
        :rtype: Reference
        """
        return self._remote_bucket

    @remote_bucket.setter
    def remote_bucket(self, remote_bucket):
        """
        Sets the remote_bucket of this BucketReplicaLink.
        Reference to a remote bucket.

        :param remote_bucket: The remote_bucket of this BucketReplicaLink.
        :type: Reference
        """

        self._remote_bucket = remote_bucket

    @property
    def remote_credentials(self):
        """
        Gets the remote_credentials of this BucketReplicaLink.
        Reference to a remote-credentials object to access the remote bucket.

        :return: The remote_credentials of this BucketReplicaLink.
        :rtype: Reference
        """
        return self._remote_credentials

    @remote_credentials.setter
    def remote_credentials(self, remote_credentials):
        """
        Sets the remote_credentials of this BucketReplicaLink.
        Reference to a remote-credentials object to access the remote bucket.

        :param remote_credentials: The remote_credentials of this BucketReplicaLink.
        :type: Reference
        """

        self._remote_credentials = remote_credentials

    @property
    def status(self):
        """
        Gets the status of this BucketReplicaLink.
        Status of the replica link. Values include replicating, paused, and unhealthy.

        :return: The status of this BucketReplicaLink.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BucketReplicaLink.
        Status of the replica link. Values include replicating, paused, and unhealthy.

        :param status: The status of this BucketReplicaLink.
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
        if not isinstance(other, BucketReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
