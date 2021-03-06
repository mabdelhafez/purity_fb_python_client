# coding: utf-8

"""
    Pure Storage FlashBlade REST 1.8.1 Python SDK

    Pure Storage FlashBlade REST 1.8.1 Python SDK, developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.8.1
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileSystem(object):
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
        'created': 'int',
        'id': 'str',
        'default_user_quota': 'int',
        'default_group_quota': 'int',
        'destroyed': 'bool',
        'fast_remove_directory_enabled': 'bool',
        'hard_limit_enabled': 'bool',
        'http': 'ProtocolRule',
        'nfs': 'NfsRule',
        'provisioned': 'int',
        'snapshot_directory_enabled': 'bool',
        'smb': 'SmbRule',
        'space': 'Space',
        'time_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'id': 'id',
        'default_user_quota': 'default_user_quota',
        'default_group_quota': 'default_group_quota',
        'destroyed': 'destroyed',
        'fast_remove_directory_enabled': 'fast_remove_directory_enabled',
        'hard_limit_enabled': 'hard_limit_enabled',
        'http': 'http',
        'nfs': 'nfs',
        'provisioned': 'provisioned',
        'snapshot_directory_enabled': 'snapshot_directory_enabled',
        'smb': 'smb',
        'space': 'space',
        'time_remaining': 'time_remaining'
    }

    def __init__(self, name=None, created=None, id=None, default_user_quota=None, default_group_quota=None, destroyed=None, fast_remove_directory_enabled=None, hard_limit_enabled=None, http=None, nfs=None, provisioned=None, snapshot_directory_enabled=None, smb=None, space=None, time_remaining=None):
        """
        FileSystem - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._id = None
        self._default_user_quota = None
        self._default_group_quota = None
        self._destroyed = None
        self._fast_remove_directory_enabled = None
        self._hard_limit_enabled = None
        self._http = None
        self._nfs = None
        self._provisioned = None
        self._snapshot_directory_enabled = None
        self._smb = None
        self._space = None
        self._time_remaining = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if id is not None:
          self.id = id
        if default_user_quota is not None:
          self.default_user_quota = default_user_quota
        if default_group_quota is not None:
          self.default_group_quota = default_group_quota
        if destroyed is not None:
          self.destroyed = destroyed
        if fast_remove_directory_enabled is not None:
          self.fast_remove_directory_enabled = fast_remove_directory_enabled
        if hard_limit_enabled is not None:
          self.hard_limit_enabled = hard_limit_enabled
        if http is not None:
          self.http = http
        if nfs is not None:
          self.nfs = nfs
        if provisioned is not None:
          self.provisioned = provisioned
        if snapshot_directory_enabled is not None:
          self.snapshot_directory_enabled = snapshot_directory_enabled
        if smb is not None:
          self.smb = smb
        if space is not None:
          self.space = space
        if time_remaining is not None:
          self.time_remaining = time_remaining

    @property
    def name(self):
        """
        Gets the name of this FileSystem.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this FileSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileSystem.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this FileSystem.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this FileSystem.
        creation timestamp of the object

        :return: The created of this FileSystem.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this FileSystem.
        creation timestamp of the object

        :param created: The created of this FileSystem.
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """
        Gets the id of this FileSystem.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this FileSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FileSystem.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this FileSystem.
        :type: str
        """

        self._id = id

    @property
    def default_user_quota(self):
        """
        Gets the default_user_quota of this FileSystem.
        Default quota for a user under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system.

        :return: The default_user_quota of this FileSystem.
        :rtype: int
        """
        return self._default_user_quota

    @default_user_quota.setter
    def default_user_quota(self, default_user_quota):
        """
        Sets the default_user_quota of this FileSystem.
        Default quota for a user under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system.

        :param default_user_quota: The default_user_quota of this FileSystem.
        :type: int
        """

        self._default_user_quota = default_user_quota

    @property
    def default_group_quota(self):
        """
        Gets the default_group_quota of this FileSystem.
        Default quota for a group under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system.

        :return: The default_group_quota of this FileSystem.
        :rtype: int
        """
        return self._default_group_quota

    @default_group_quota.setter
    def default_group_quota(self, default_group_quota):
        """
        Sets the default_group_quota of this FileSystem.
        Default quota for a group under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system.

        :param default_group_quota: The default_group_quota of this FileSystem.
        :type: int
        """

        self._default_group_quota = default_group_quota

    @property
    def destroyed(self):
        """
        Gets the destroyed of this FileSystem.
        Is the file system destroyed? False by default. Modifiable.

        :return: The destroyed of this FileSystem.
        :rtype: bool
        """
        return self._destroyed

    @destroyed.setter
    def destroyed(self, destroyed):
        """
        Sets the destroyed of this FileSystem.
        Is the file system destroyed? False by default. Modifiable.

        :param destroyed: The destroyed of this FileSystem.
        :type: bool
        """

        self._destroyed = destroyed

    @property
    def fast_remove_directory_enabled(self):
        """
        Gets the fast_remove_directory_enabled of this FileSystem.
        Is fast remove directory enabled? Modifiable. Default false when creating a new file-system.

        :return: The fast_remove_directory_enabled of this FileSystem.
        :rtype: bool
        """
        return self._fast_remove_directory_enabled

    @fast_remove_directory_enabled.setter
    def fast_remove_directory_enabled(self, fast_remove_directory_enabled):
        """
        Sets the fast_remove_directory_enabled of this FileSystem.
        Is fast remove directory enabled? Modifiable. Default false when creating a new file-system.

        :param fast_remove_directory_enabled: The fast_remove_directory_enabled of this FileSystem.
        :type: bool
        """

        self._fast_remove_directory_enabled = fast_remove_directory_enabled

    @property
    def hard_limit_enabled(self):
        """
        Gets the hard_limit_enabled of this FileSystem.
        Is the file system's size a hard limit quota. Modifiable. Default is false.

        :return: The hard_limit_enabled of this FileSystem.
        :rtype: bool
        """
        return self._hard_limit_enabled

    @hard_limit_enabled.setter
    def hard_limit_enabled(self, hard_limit_enabled):
        """
        Sets the hard_limit_enabled of this FileSystem.
        Is the file system's size a hard limit quota. Modifiable. Default is false.

        :param hard_limit_enabled: The hard_limit_enabled of this FileSystem.
        :type: bool
        """

        self._hard_limit_enabled = hard_limit_enabled

    @property
    def http(self):
        """
        Gets the http of this FileSystem.
        HTTP configuration. Modifiable.

        :return: The http of this FileSystem.
        :rtype: ProtocolRule
        """
        return self._http

    @http.setter
    def http(self, http):
        """
        Sets the http of this FileSystem.
        HTTP configuration. Modifiable.

        :param http: The http of this FileSystem.
        :type: ProtocolRule
        """

        self._http = http

    @property
    def nfs(self):
        """
        Gets the nfs of this FileSystem.
        NFS configuration. Modifiable.

        :return: The nfs of this FileSystem.
        :rtype: NfsRule
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this FileSystem.
        NFS configuration. Modifiable.

        :param nfs: The nfs of this FileSystem.
        :type: NfsRule
        """

        self._nfs = nfs

    @property
    def provisioned(self):
        """
        Gets the provisioned of this FileSystem.
        The provisioned size of the file system in bytes. Modifiable. Default is 0 when creating a new file-system.

        :return: The provisioned of this FileSystem.
        :rtype: int
        """
        return self._provisioned

    @provisioned.setter
    def provisioned(self, provisioned):
        """
        Sets the provisioned of this FileSystem.
        The provisioned size of the file system in bytes. Modifiable. Default is 0 when creating a new file-system.

        :param provisioned: The provisioned of this FileSystem.
        :type: int
        """

        self._provisioned = provisioned

    @property
    def snapshot_directory_enabled(self):
        """
        Gets the snapshot_directory_enabled of this FileSystem.
        Is snapshot directory enabled? Modifiable. Default false when creating a new file-system.

        :return: The snapshot_directory_enabled of this FileSystem.
        :rtype: bool
        """
        return self._snapshot_directory_enabled

    @snapshot_directory_enabled.setter
    def snapshot_directory_enabled(self, snapshot_directory_enabled):
        """
        Sets the snapshot_directory_enabled of this FileSystem.
        Is snapshot directory enabled? Modifiable. Default false when creating a new file-system.

        :param snapshot_directory_enabled: The snapshot_directory_enabled of this FileSystem.
        :type: bool
        """

        self._snapshot_directory_enabled = snapshot_directory_enabled

    @property
    def smb(self):
        """
        Gets the smb of this FileSystem.
        SMB configuration. Modifiable.

        :return: The smb of this FileSystem.
        :rtype: SmbRule
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """
        Sets the smb of this FileSystem.
        SMB configuration. Modifiable.

        :param smb: The smb of this FileSystem.
        :type: SmbRule
        """

        self._smb = smb

    @property
    def space(self):
        """
        Gets the space of this FileSystem.
        the space specification of the file system

        :return: The space of this FileSystem.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """
        Sets the space of this FileSystem.
        the space specification of the file system

        :param space: The space of this FileSystem.
        :type: Space
        """

        self._space = space

    @property
    def time_remaining(self):
        """
        Gets the time_remaining of this FileSystem.
        Time in milliseconds before the file system is eradicated. Null if not destroyed.

        :return: The time_remaining of this FileSystem.
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """
        Sets the time_remaining of this FileSystem.
        Time in milliseconds before the file system is eradicated. Null if not destroyed.

        :param time_remaining: The time_remaining of this FileSystem.
        :type: int
        """

        self._time_remaining = time_remaining

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
        if not isinstance(other, FileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
