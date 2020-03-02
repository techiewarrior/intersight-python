# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TamAction(object):
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
        'object_type': 'str',
        'affected_object_type': 'str',
        'alert_type': 'str',
        'identifiers': 'list[TamIdentifiers]',
        'name': 'str',
        'operation_type': 'str',
        'queries': 'list[TamQueryEntry]',
        'type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'affected_object_type': 'AffectedObjectType',
        'alert_type': 'AlertType',
        'identifiers': 'Identifiers',
        'name': 'Name',
        'operation_type': 'OperationType',
        'queries': 'Queries',
        'type': 'Type'
    }

    def __init__(self, object_type=None, affected_object_type=None, alert_type='psirt', identifiers=None, name=None, operation_type='create', queries=None, type='restApi'):
        """
        TamAction - a model defined in Swagger
        """

        self._object_type = None
        self._affected_object_type = None
        self._alert_type = None
        self._identifiers = None
        self._name = None
        self._operation_type = None
        self._queries = None
        self._type = None

        if object_type is not None:
          self.object_type = object_type
        if affected_object_type is not None:
          self.affected_object_type = affected_object_type
        if alert_type is not None:
          self.alert_type = alert_type
        if identifiers is not None:
          self.identifiers = identifiers
        if name is not None:
          self.name = name
        if operation_type is not None:
          self.operation_type = operation_type
        if queries is not None:
          self.queries = queries
        if type is not None:
          self.type = type

    @property
    def object_type(self):
        """
        Gets the object_type of this TamAction.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this TamAction.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TamAction.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this TamAction.
        :type: str
        """

        self._object_type = object_type

    @property
    def affected_object_type(self):
        """
        Gets the affected_object_type of this TamAction.
        Type of the managed object that should be marked with an instance of the Alert (when operation type is create) or that should have an alert instance removed (when operation type is remove).

        :return: The affected_object_type of this TamAction.
        :rtype: str
        """
        return self._affected_object_type

    @affected_object_type.setter
    def affected_object_type(self, affected_object_type):
        """
        Sets the affected_object_type of this TamAction.
        Type of the managed object that should be marked with an instance of the Alert (when operation type is create) or that should have an alert instance removed (when operation type is remove).

        :param affected_object_type: The affected_object_type of this TamAction.
        :type: str
        """

        self._affected_object_type = affected_object_type

    @property
    def alert_type(self):
        """
        Gets the alert_type of this TamAction.
        Alert type is used to denote the category of an Intersight alert (FieldNotice, equipment Fault etc.).

        :return: The alert_type of this TamAction.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this TamAction.
        Alert type is used to denote the category of an Intersight alert (FieldNotice, equipment Fault etc.).

        :param alert_type: The alert_type of this TamAction.
        :type: str
        """
        allowed_values = ["psirt", "fieldNotice"]
        if alert_type not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_type` ({0}), must be one of {1}"
                .format(alert_type, allowed_values)
            )

        self._alert_type = alert_type

    @property
    def identifiers(self):
        """
        Gets the identifiers of this TamAction.
        Identifiers represents the filter criteria (property names and values) used to identify an Intersight managed object of type specified in affectedObjectType property. An instance of an alert is then create on (or removed from) the identified managed object.

        :return: The identifiers of this TamAction.
        :rtype: list[TamIdentifiers]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """
        Sets the identifiers of this TamAction.
        Identifiers represents the filter criteria (property names and values) used to identify an Intersight managed object of type specified in affectedObjectType property. An instance of an alert is then create on (or removed from) the identified managed object.

        :param identifiers: The identifiers of this TamAction.
        :type: list[TamIdentifiers]
        """

        self._identifiers = identifiers

    @property
    def name(self):
        """
        Gets the name of this TamAction.
        Uniquely identifies a given action among the set of actions corresponding to an advisory. Primarily used to store and compare results of subsequent iterations corresponding to the action queries.

        :return: The name of this TamAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TamAction.
        Uniquely identifies a given action among the set of actions corresponding to an advisory. Primarily used to store and compare results of subsequent iterations corresponding to the action queries.

        :param name: The name of this TamAction.
        :type: str
        """

        self._name = name

    @property
    def operation_type(self):
        """
        Gets the operation_type of this TamAction.
        Operation type for the alert action. An action is used to carry out the process of \"reacting\" to an alert condition. For e.g.in case of a fieldNotice alert, the intention may be to create a new alert (if the condition matches and there is no existing alert) or to remove an existing alert when the alert condition has been remedied.

        :return: The operation_type of this TamAction.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this TamAction.
        Operation type for the alert action. An action is used to carry out the process of \"reacting\" to an alert condition. For e.g.in case of a fieldNotice alert, the intention may be to create a new alert (if the condition matches and there is no existing alert) or to remove an existing alert when the alert condition has been remedied.

        :param operation_type: The operation_type of this TamAction.
        :type: str
        """
        allowed_values = ["create", "remove"]
        if operation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_type` ({0}), must be one of {1}"
                .format(operation_type, allowed_values)
            )

        self._operation_type = operation_type

    @property
    def queries(self):
        """
        Gets the queries of this TamAction.
        Set of SparkSQL queries used determine if a given alert is applicable or not. Refer to https://spark.apache.org/sql/ for more details.

        :return: The queries of this TamAction.
        :rtype: list[TamQueryEntry]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """
        Sets the queries of this TamAction.
        Set of SparkSQL queries used determine if a given alert is applicable or not. Refer to https://spark.apache.org/sql/ for more details.

        :param queries: The queries of this TamAction.
        :type: list[TamQueryEntry]
        """

        self._queries = queries

    @property
    def type(self):
        """
        Gets the type of this TamAction.
        Type of Intersight alert. An alert in Intersight could be one of several kinds (FieldNotice, PSIRT etc.). Primarily used for filtering alerts based on the type.

        :return: The type of this TamAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TamAction.
        Type of Intersight alert. An alert in Intersight could be one of several kinds (FieldNotice, PSIRT etc.). Primarily used for filtering alerts based on the type.

        :param type: The type of this TamAction.
        :type: str
        """
        allowed_values = ["restApi"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, TamAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
