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


class FileSystemSnapshotsTransfer(object):
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
        'completed': 'int',
        'data_transferred': 'int',
        'direction': 'Direction',
        'progress': 'float',
        'remote': 'FixedReferenceWithId',
        'remote_snapshot': 'FixedReferenceWithId',
        'started': 'int',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'completed': 'completed',
        'data_transferred': 'data_transferred',
        'direction': 'direction',
        'progress': 'progress',
        'remote': 'remote',
        'remote_snapshot': 'remote_snapshot',
        'started': 'started',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, completed=None, data_transferred=None, direction=None, progress=None, remote=None, remote_snapshot=None, started=None, status=None):
        """
        FileSystemSnapshotsTransfer - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._completed = None
        self._data_transferred = None
        self._direction = None
        self._progress = None
        self._remote = None
        self._remote_snapshot = None
        self._started = None
        self._status = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if completed is not None:
          self.completed = completed
        if data_transferred is not None:
          self.data_transferred = data_transferred
        if direction is not None:
          self.direction = direction
        if progress is not None:
          self.progress = progress
        if remote is not None:
          self.remote = remote
        if remote_snapshot is not None:
          self.remote_snapshot = remote_snapshot
        if started is not None:
          self.started = started
        if status is not None:
          self.status = status

    @property
    def id(self):
        """
        Gets the id of this FileSystemSnapshotsTransfer.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this FileSystemSnapshotsTransfer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FileSystemSnapshotsTransfer.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this FileSystemSnapshotsTransfer.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this FileSystemSnapshotsTransfer.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this FileSystemSnapshotsTransfer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileSystemSnapshotsTransfer.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this FileSystemSnapshotsTransfer.
        :type: str
        """

        self._name = name

    @property
    def completed(self):
        """
        Gets the completed of this FileSystemSnapshotsTransfer.
        A timestamp at which the replication of the snapshot completed.

        :return: The completed of this FileSystemSnapshotsTransfer.
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """
        Sets the completed of this FileSystemSnapshotsTransfer.
        A timestamp at which the replication of the snapshot completed.

        :param completed: The completed of this FileSystemSnapshotsTransfer.
        :type: int
        """

        self._completed = completed

    @property
    def data_transferred(self):
        """
        Gets the data_transferred of this FileSystemSnapshotsTransfer.
        The amount of data transferred to the target, in bytes.

        :return: The data_transferred of this FileSystemSnapshotsTransfer.
        :rtype: int
        """
        return self._data_transferred

    @data_transferred.setter
    def data_transferred(self, data_transferred):
        """
        Sets the data_transferred of this FileSystemSnapshotsTransfer.
        The amount of data transferred to the target, in bytes.

        :param data_transferred: The data_transferred of this FileSystemSnapshotsTransfer.
        :type: int
        """

        self._data_transferred = data_transferred

    @property
    def direction(self):
        """
        Gets the direction of this FileSystemSnapshotsTransfer.

        :return: The direction of this FileSystemSnapshotsTransfer.
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this FileSystemSnapshotsTransfer.

        :param direction: The direction of this FileSystemSnapshotsTransfer.
        :type: Direction
        """

        self._direction = direction

    @property
    def progress(self):
        """
        Gets the progress of this FileSystemSnapshotsTransfer.
        A percentage that indicates how much progress has been made on the transfer.

        :return: The progress of this FileSystemSnapshotsTransfer.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this FileSystemSnapshotsTransfer.
        A percentage that indicates how much progress has been made on the transfer.

        :param progress: The progress of this FileSystemSnapshotsTransfer.
        :type: float
        """
        if progress is not None and progress > 1:
            raise ValueError("Invalid value for `progress`, must be a value less than or equal to `1`")
        if progress is not None and progress < 0:
            raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0`")

        self._progress = progress

    @property
    def remote(self):
        """
        Gets the remote of this FileSystemSnapshotsTransfer.
        The array where the remote file system snapshot is located.

        :return: The remote of this FileSystemSnapshotsTransfer.
        :rtype: FixedReferenceWithId
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """
        Sets the remote of this FileSystemSnapshotsTransfer.
        The array where the remote file system snapshot is located.

        :param remote: The remote of this FileSystemSnapshotsTransfer.
        :type: FixedReferenceWithId
        """

        self._remote = remote

    @property
    def remote_snapshot(self):
        """
        Gets the remote_snapshot of this FileSystemSnapshotsTransfer.
        A reference to the associated remote file system snapshot.

        :return: The remote_snapshot of this FileSystemSnapshotsTransfer.
        :rtype: FixedReferenceWithId
        """
        return self._remote_snapshot

    @remote_snapshot.setter
    def remote_snapshot(self, remote_snapshot):
        """
        Sets the remote_snapshot of this FileSystemSnapshotsTransfer.
        A reference to the associated remote file system snapshot.

        :param remote_snapshot: The remote_snapshot of this FileSystemSnapshotsTransfer.
        :type: FixedReferenceWithId
        """

        self._remote_snapshot = remote_snapshot

    @property
    def started(self):
        """
        Gets the started of this FileSystemSnapshotsTransfer.
        A timestamp at which the replication of the snapshot started.

        :return: The started of this FileSystemSnapshotsTransfer.
        :rtype: int
        """
        return self._started

    @started.setter
    def started(self, started):
        """
        Sets the started of this FileSystemSnapshotsTransfer.
        A timestamp at which the replication of the snapshot started.

        :param started: The started of this FileSystemSnapshotsTransfer.
        :type: int
        """

        self._started = started

    @property
    def status(self):
        """
        Gets the status of this FileSystemSnapshotsTransfer.
        The status of current replication. Valid values are `completed`, `in-progress`, and `queued`.

        :return: The status of this FileSystemSnapshotsTransfer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this FileSystemSnapshotsTransfer.
        The status of current replication. Valid values are `completed`, `in-progress`, and `queued`.

        :param status: The status of this FileSystemSnapshotsTransfer.
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
        if not isinstance(other, FileSystemSnapshotsTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
