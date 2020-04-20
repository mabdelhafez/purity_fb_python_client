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


class DirectoryService(object):
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
        'base_dn': 'str',
        'bind_password': 'str',
        'bind_user': 'str',
        'ca_certificate': 'Reference',
        'ca_certificate_group': 'Reference',
        'enabled': 'bool',
        'management': 'DirectoryserviceManagement',
        'nfs': 'DirectoryserviceNfs',
        'services': 'list[str]',
        'smb': 'DirectoryserviceSmb',
        'uris': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'base_dn': 'base_dn',
        'bind_password': 'bind_password',
        'bind_user': 'bind_user',
        'ca_certificate': 'ca_certificate',
        'ca_certificate_group': 'ca_certificate_group',
        'enabled': 'enabled',
        'management': 'management',
        'nfs': 'nfs',
        'services': 'services',
        'smb': 'smb',
        'uris': 'uris'
    }

    def __init__(self, id=None, name=None, base_dn=None, bind_password=None, bind_user=None, ca_certificate=None, ca_certificate_group=None, enabled=None, management=None, nfs=None, services=None, smb=None, uris=None):
        """
        DirectoryService - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._base_dn = None
        self._bind_password = None
        self._bind_user = None
        self._ca_certificate = None
        self._ca_certificate_group = None
        self._enabled = None
        self._management = None
        self._nfs = None
        self._services = None
        self._smb = None
        self._uris = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if base_dn is not None:
          self.base_dn = base_dn
        if bind_password is not None:
          self.bind_password = bind_password
        if bind_user is not None:
          self.bind_user = bind_user
        if ca_certificate is not None:
          self.ca_certificate = ca_certificate
        if ca_certificate_group is not None:
          self.ca_certificate_group = ca_certificate_group
        if enabled is not None:
          self.enabled = enabled
        if management is not None:
          self.management = management
        if nfs is not None:
          self.nfs = nfs
        if services is not None:
          self.services = services
        if smb is not None:
          self.smb = smb
        if uris is not None:
          self.uris = uris

    @property
    def id(self):
        """
        Gets the id of this DirectoryService.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this DirectoryService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DirectoryService.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this DirectoryService.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DirectoryService.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this DirectoryService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DirectoryService.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this DirectoryService.
        :type: str
        """

        self._name = name

    @property
    def base_dn(self):
        """
        Gets the base_dn of this DirectoryService.
        Base of the Distinguished Name (DN) of the directory service groups.

        :return: The base_dn of this DirectoryService.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """
        Sets the base_dn of this DirectoryService.
        Base of the Distinguished Name (DN) of the directory service groups.

        :param base_dn: The base_dn of this DirectoryService.
        :type: str
        """

        self._base_dn = base_dn

    @property
    def bind_password(self):
        """
        Gets the bind_password of this DirectoryService.
        Obfuscated password used to query the directory.

        :return: The bind_password of this DirectoryService.
        :rtype: str
        """
        return self._bind_password

    @bind_password.setter
    def bind_password(self, bind_password):
        """
        Sets the bind_password of this DirectoryService.
        Obfuscated password used to query the directory.

        :param bind_password: The bind_password of this DirectoryService.
        :type: str
        """

        self._bind_password = bind_password

    @property
    def bind_user(self):
        """
        Gets the bind_user of this DirectoryService.
        Username used to query the directory.

        :return: The bind_user of this DirectoryService.
        :rtype: str
        """
        return self._bind_user

    @bind_user.setter
    def bind_user(self, bind_user):
        """
        Sets the bind_user of this DirectoryService.
        Username used to query the directory.

        :param bind_user: The bind_user of this DirectoryService.
        :type: str
        """

        self._bind_user = bind_user

    @property
    def ca_certificate(self):
        """
        Gets the ca_certificate of this DirectoryService.
        CA certificate used to validate the authenticity of the configured servers.

        :return: The ca_certificate of this DirectoryService.
        :rtype: Reference
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """
        Sets the ca_certificate of this DirectoryService.
        CA certificate used to validate the authenticity of the configured servers.

        :param ca_certificate: The ca_certificate of this DirectoryService.
        :type: Reference
        """

        self._ca_certificate = ca_certificate

    @property
    def ca_certificate_group(self):
        """
        Gets the ca_certificate_group of this DirectoryService.
        Certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.

        :return: The ca_certificate_group of this DirectoryService.
        :rtype: Reference
        """
        return self._ca_certificate_group

    @ca_certificate_group.setter
    def ca_certificate_group(self, ca_certificate_group):
        """
        Sets the ca_certificate_group of this DirectoryService.
        Certificate group containing CA certificates that can be used to validate the authenticity of the configured servers.

        :param ca_certificate_group: The ca_certificate_group of this DirectoryService.
        :type: Reference
        """

        self._ca_certificate_group = ca_certificate_group

    @property
    def enabled(self):
        """
        Gets the enabled of this DirectoryService.
        Is the directory service enabled or not?

        :return: The enabled of this DirectoryService.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this DirectoryService.
        Is the directory service enabled or not?

        :param enabled: The enabled of this DirectoryService.
        :type: bool
        """

        self._enabled = enabled

    @property
    def management(self):
        """
        Gets the management of this DirectoryService.

        :return: The management of this DirectoryService.
        :rtype: DirectoryserviceManagement
        """
        return self._management

    @management.setter
    def management(self, management):
        """
        Sets the management of this DirectoryService.

        :param management: The management of this DirectoryService.
        :type: DirectoryserviceManagement
        """

        self._management = management

    @property
    def nfs(self):
        """
        Gets the nfs of this DirectoryService.

        :return: The nfs of this DirectoryService.
        :rtype: DirectoryserviceNfs
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this DirectoryService.

        :param nfs: The nfs of this DirectoryService.
        :type: DirectoryserviceNfs
        """

        self._nfs = nfs

    @property
    def services(self):
        """
        Gets the services of this DirectoryService.
        Services that the directory service configuration is used for.

        :return: The services of this DirectoryService.
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this DirectoryService.
        Services that the directory service configuration is used for.

        :param services: The services of this DirectoryService.
        :type: list[str]
        """

        self._services = services

    @property
    def smb(self):
        """
        Gets the smb of this DirectoryService.

        :return: The smb of this DirectoryService.
        :rtype: DirectoryserviceSmb
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """
        Sets the smb of this DirectoryService.

        :param smb: The smb of this DirectoryService.
        :type: DirectoryserviceSmb
        """

        self._smb = smb

    @property
    def uris(self):
        """
        Gets the uris of this DirectoryService.
        List of URIs for the configured directory servers.

        :return: The uris of this DirectoryService.
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        """
        Sets the uris of this DirectoryService.
        List of URIs for the configured directory servers.

        :param uris: The uris of this DirectoryService.
        :type: list[str]
        """

        self._uris = uris

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
        if not isinstance(other, DirectoryService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
