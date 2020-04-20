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


class ApiClientResp(object):
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
        'max_role': 'FixedReferenceNoResourceType',
        'issuer': 'str',
        'public_key': 'str',
        'key_id': 'str',
        'enabled': 'bool',
        'access_token_ttl_in_ms': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'max_role': 'max_role',
        'issuer': 'issuer',
        'public_key': 'public_key',
        'key_id': 'key_id',
        'enabled': 'enabled',
        'access_token_ttl_in_ms': 'access_token_ttl_in_ms'
    }

    def __init__(self, id=None, name=None, max_role=None, issuer=None, public_key=None, key_id=None, enabled=None, access_token_ttl_in_ms=None):
        """
        ApiClientResp - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._max_role = None
        self._issuer = None
        self._public_key = None
        self._key_id = None
        self._enabled = None
        self._access_token_ttl_in_ms = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if max_role is not None:
          self.max_role = max_role
        if issuer is not None:
          self.issuer = issuer
        if public_key is not None:
          self.public_key = public_key
        if key_id is not None:
          self.key_id = key_id
        if enabled is not None:
          self.enabled = enabled
        if access_token_ttl_in_ms is not None:
          self.access_token_ttl_in_ms = access_token_ttl_in_ms

    @property
    def id(self):
        """
        Gets the id of this ApiClientResp.
        A non-modifiable, globally unique ID chosen by the system.

        :return: The id of this ApiClientResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApiClientResp.
        A non-modifiable, globally unique ID chosen by the system.

        :param id: The id of this ApiClientResp.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ApiClientResp.
        The name of the object (e.g., a file system or snapshot).

        :return: The name of this ApiClientResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiClientResp.
        The name of the object (e.g., a file system or snapshot).

        :param name: The name of this ApiClientResp.
        :type: str
        """

        self._name = name

    @property
    def max_role(self):
        """
        Gets the max_role of this ApiClientResp.
        The maximum role allowed for ID Tokens issued by this API client. The bearer of an access token will be authorized to perform actions within the intersection of this max_role and the role of the array user specified as the JWT sub (subject) claim. Valid max_role values are readonly, ops_admin, array_admin, and storage_admin. Users with the readonly (Read Only) role can perform operations that convey the state of the array. Read Only users cannot alter the state of the array. Users with the ops_admin (Ops Admin) role can perform the same operations as Read Only users plus enable and disable remote assistance sessions. Ops Admin users cannot alter the state of the array. Users with the storage_admin (Storage Admin) role can perform the same operations as Read Only users plus storage related operations, such as administering volumes, hosts, and host groups. Storage Admin users cannot perform operations that deal with global and system configurations. Users with the array_admin (Array Admin) role can perform the same operations as Storage Admin users plus array-wide changes dealing with global and system configurations. In other words, Array Admin users can perform all operations.

        :return: The max_role of this ApiClientResp.
        :rtype: FixedReferenceNoResourceType
        """
        return self._max_role

    @max_role.setter
    def max_role(self, max_role):
        """
        Sets the max_role of this ApiClientResp.
        The maximum role allowed for ID Tokens issued by this API client. The bearer of an access token will be authorized to perform actions within the intersection of this max_role and the role of the array user specified as the JWT sub (subject) claim. Valid max_role values are readonly, ops_admin, array_admin, and storage_admin. Users with the readonly (Read Only) role can perform operations that convey the state of the array. Read Only users cannot alter the state of the array. Users with the ops_admin (Ops Admin) role can perform the same operations as Read Only users plus enable and disable remote assistance sessions. Ops Admin users cannot alter the state of the array. Users with the storage_admin (Storage Admin) role can perform the same operations as Read Only users plus storage related operations, such as administering volumes, hosts, and host groups. Storage Admin users cannot perform operations that deal with global and system configurations. Users with the array_admin (Array Admin) role can perform the same operations as Storage Admin users plus array-wide changes dealing with global and system configurations. In other words, Array Admin users can perform all operations.

        :param max_role: The max_role of this ApiClientResp.
        :type: FixedReferenceNoResourceType
        """

        self._max_role = max_role

    @property
    def issuer(self):
        """
        Gets the issuer of this ApiClientResp.
        The name of the identity provider that will be issuing ID Tokens for this API client. This string represents the JWT iss (issuer) claim in ID Tokens issued for this API client.

        :return: The issuer of this ApiClientResp.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this ApiClientResp.
        The name of the identity provider that will be issuing ID Tokens for this API client. This string represents the JWT iss (issuer) claim in ID Tokens issued for this API client.

        :param issuer: The issuer of this ApiClientResp.
        :type: str
        """

        self._issuer = issuer

    @property
    def public_key(self):
        """
        Gets the public_key of this ApiClientResp.
        The API client's PEM formatted (Base64 encoded) RSA public key.

        :return: The public_key of this ApiClientResp.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this ApiClientResp.
        The API client's PEM formatted (Base64 encoded) RSA public key.

        :param public_key: The public_key of this ApiClientResp.
        :type: str
        """

        self._public_key = public_key

    @property
    def key_id(self):
        """
        Gets the key_id of this ApiClientResp.
        The unique identifier for the associated public key of this API client. This string must match the JWT kid (key ID) claim in ID Tokens issued for this API client.

        :return: The key_id of this ApiClientResp.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this ApiClientResp.
        The unique identifier for the associated public key of this API client. This string must match the JWT kid (key ID) claim in ID Tokens issued for this API client.

        :param key_id: The key_id of this ApiClientResp.
        :type: str
        """

        self._key_id = key_id

    @property
    def enabled(self):
        """
        Gets the enabled of this ApiClientResp.
        If true, the API client is permitted to exchange ID Tokens for access tokens. API clients are disabled by default.

        :return: The enabled of this ApiClientResp.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ApiClientResp.
        If true, the API client is permitted to exchange ID Tokens for access tokens. API clients are disabled by default.

        :param enabled: The enabled of this ApiClientResp.
        :type: bool
        """

        self._enabled = enabled

    @property
    def access_token_ttl_in_ms(self):
        """
        Gets the access_token_ttl_in_ms of this ApiClientResp.
        The requested TTL (Time To Live) length of time for the exchanged access token. Measured in milliseconds.

        :return: The access_token_ttl_in_ms of this ApiClientResp.
        :rtype: int
        """
        return self._access_token_ttl_in_ms

    @access_token_ttl_in_ms.setter
    def access_token_ttl_in_ms(self, access_token_ttl_in_ms):
        """
        Sets the access_token_ttl_in_ms of this ApiClientResp.
        The requested TTL (Time To Live) length of time for the exchanged access token. Measured in milliseconds.

        :param access_token_ttl_in_ms: The access_token_ttl_in_ms of this ApiClientResp.
        :type: int
        """

        self._access_token_ttl_in_ms = access_token_ttl_in_ms

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
        if not isinstance(other, ApiClientResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
