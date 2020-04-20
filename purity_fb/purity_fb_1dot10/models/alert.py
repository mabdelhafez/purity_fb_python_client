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


class Alert(object):
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
        'index': 'int',
        'code': 'int',
        'severity': 'str',
        'component': 'str',
        'state': 'str',
        'flagged': 'bool',
        'updated': 'int',
        'notified': 'int',
        'subject': 'str',
        'description': 'str',
        'knowledge_base_url': 'str',
        'action': 'str',
        'variables': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'index': 'index',
        'code': 'code',
        'severity': 'severity',
        'component': 'component',
        'state': 'state',
        'flagged': 'flagged',
        'updated': 'updated',
        'notified': 'notified',
        'subject': 'subject',
        'description': 'description',
        'knowledge_base_url': 'knowledge_base_url',
        'action': 'action',
        'variables': 'variables'
    }

    def __init__(self, name=None, created=None, index=None, code=None, severity=None, component=None, state=None, flagged=None, updated=None, notified=None, subject=None, description=None, knowledge_base_url=None, action=None, variables=None):
        """
        Alert - a model defined in Swagger
        """

        self._name = None
        self._created = None
        self._index = None
        self._code = None
        self._severity = None
        self._component = None
        self._state = None
        self._flagged = None
        self._updated = None
        self._notified = None
        self._subject = None
        self._description = None
        self._knowledge_base_url = None
        self._action = None
        self._variables = None

        if name is not None:
          self.name = name
        if created is not None:
          self.created = created
        if index is not None:
          self.index = index
        if code is not None:
          self.code = code
        if severity is not None:
          self.severity = severity
        if component is not None:
          self.component = component
        if state is not None:
          self.state = state
        if flagged is not None:
          self.flagged = flagged
        if updated is not None:
          self.updated = updated
        if notified is not None:
          self.notified = notified
        if subject is not None:
          self.subject = subject
        if description is not None:
          self.description = description
        if knowledge_base_url is not None:
          self.knowledge_base_url = knowledge_base_url
        if action is not None:
          self.action = action
        if variables is not None:
          self.variables = variables

    @property
    def name(self):
        """
        Gets the name of this Alert.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this Alert.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Alert.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this Alert.
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """
        Gets the created of this Alert.
        creation timestamp of the object

        :return: The created of this Alert.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Alert.
        creation timestamp of the object

        :param created: The created of this Alert.
        :type: int
        """

        self._created = created

    @property
    def index(self):
        """
        Gets the index of this Alert.
        the unique index of the alert

        :return: The index of this Alert.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this Alert.
        the unique index of the alert

        :param index: The index of this Alert.
        :type: int
        """

        self._index = index

    @property
    def code(self):
        """
        Gets the code of this Alert.
        alert code

        :return: The code of this Alert.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Alert.
        alert code

        :param code: The code of this Alert.
        :type: int
        """

        self._code = code

    @property
    def severity(self):
        """
        Gets the severity of this Alert.
        Severity of the alert. Possible values are info, warning and critical.

        :return: The severity of this Alert.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this Alert.
        Severity of the alert. Possible values are info, warning and critical.

        :param severity: The severity of this Alert.
        :type: str
        """

        self._severity = severity

    @property
    def component(self):
        """
        Gets the component of this Alert.
        the component of the alert

        :return: The component of this Alert.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this Alert.
        the component of the alert

        :param component: The component of this Alert.
        :type: str
        """

        self._component = component

    @property
    def state(self):
        """
        Gets the state of this Alert.
        The current state of the alert. Possible values are open, closing, closed and waiting to downgrade.

        :return: The state of this Alert.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Alert.
        The current state of the alert. Possible values are open, closing, closed and waiting to downgrade.

        :param state: The state of this Alert.
        :type: str
        """

        self._state = state

    @property
    def flagged(self):
        """
        Gets the flagged of this Alert.
        whether the alert is flagged or not

        :return: The flagged of this Alert.
        :rtype: bool
        """
        return self._flagged

    @flagged.setter
    def flagged(self, flagged):
        """
        Sets the flagged of this Alert.
        whether the alert is flagged or not

        :param flagged: The flagged of this Alert.
        :type: bool
        """

        self._flagged = flagged

    @property
    def updated(self):
        """
        Gets the updated of this Alert.
        the last updated timestamp of the alert

        :return: The updated of this Alert.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this Alert.
        the last updated timestamp of the alert

        :param updated: The updated of this Alert.
        :type: int
        """

        self._updated = updated

    @property
    def notified(self):
        """
        Gets the notified of this Alert.
        the last notification timestamp of the alert

        :return: The notified of this Alert.
        :rtype: int
        """
        return self._notified

    @notified.setter
    def notified(self, notified):
        """
        Sets the notified of this Alert.
        the last notification timestamp of the alert

        :param notified: The notified of this Alert.
        :type: int
        """

        self._notified = notified

    @property
    def subject(self):
        """
        Gets the subject of this Alert.
        the subject of the alert

        :return: The subject of this Alert.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Alert.
        the subject of the alert

        :param subject: The subject of this Alert.
        :type: str
        """

        self._subject = subject

    @property
    def description(self):
        """
        Gets the description of this Alert.
        the description of the alert

        :return: The description of this Alert.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Alert.
        the description of the alert

        :param description: The description of this Alert.
        :type: str
        """

        self._description = description

    @property
    def knowledge_base_url(self):
        """
        Gets the knowledge_base_url of this Alert.
        the kb url of the alert

        :return: The knowledge_base_url of this Alert.
        :rtype: str
        """
        return self._knowledge_base_url

    @knowledge_base_url.setter
    def knowledge_base_url(self, knowledge_base_url):
        """
        Sets the knowledge_base_url of this Alert.
        the kb url of the alert

        :param knowledge_base_url: The knowledge_base_url of this Alert.
        :type: str
        """

        self._knowledge_base_url = knowledge_base_url

    @property
    def action(self):
        """
        Gets the action of this Alert.
        the action of the alert

        :return: The action of this Alert.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Alert.
        the action of the alert

        :param action: The action of this Alert.
        :type: str
        """

        self._action = action

    @property
    def variables(self):
        """
        Gets the variables of this Alert.
        key-value pairs of additional information of the alert

        :return: The variables of this Alert.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Alert.
        key-value pairs of additional information of the alert

        :param variables: The variables of this Alert.
        :type: dict(str, str)
        """

        self._variables = variables

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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
