# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TamApiDataSource(object):
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
        'name': 'str',
        'type': 'str',
        'mo_type': 'str',
        'queries': 'list[TamQueryEntry]'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'name': 'Name',
        'type': 'Type',
        'mo_type': 'MoType',
        'queries': 'Queries'
    }

    def __init__(self, object_type=None, name=None, type='nxos', mo_type=None, queries=None):
        """
        TamApiDataSource - a model defined in Swagger
        """

        self._object_type = None
        self._name = None
        self._type = None
        self._mo_type = None
        self._queries = None

        if object_type is not None:
          self.object_type = object_type
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if mo_type is not None:
          self.mo_type = mo_type
        if queries is not None:
          self.queries = queries

    @property
    def object_type(self):
        """
        Gets the object_type of this TamApiDataSource.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this TamApiDataSource.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TamApiDataSource.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this TamApiDataSource.
        :type: str
        """

        self._object_type = object_type

    @property
    def name(self):
        """
        Gets the name of this TamApiDataSource.
        Name is used to unique identify and refer a given data source in an alert definition.  

        :return: The name of this TamApiDataSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TamApiDataSource.
        Name is used to unique identify and refer a given data source in an alert definition.  

        :param name: The name of this TamApiDataSource.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this TamApiDataSource.
        Type of data source (for e.g. TextFsmTempalate based, Intersight API based etc.).   

        :return: The type of this TamApiDataSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TamApiDataSource.
        Type of data source (for e.g. TextFsmTempalate based, Intersight API based etc.).   

        :param type: The type of this TamApiDataSource.
        :type: str
        """
        allowed_values = ["nxos", "intersightApi"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def mo_type(self):
        """
        Gets the mo_type of this TamApiDataSource.
        Type of Intersight managed object used as data source.  

        :return: The mo_type of this TamApiDataSource.
        :rtype: str
        """
        return self._mo_type

    @mo_type.setter
    def mo_type(self, mo_type):
        """
        Sets the mo_type of this TamApiDataSource.
        Type of Intersight managed object used as data source.  

        :param mo_type: The mo_type of this TamApiDataSource.
        :type: str
        """

        self._mo_type = mo_type

    @property
    def queries(self):
        """
        Gets the queries of this TamApiDataSource.
        Optional set of Queries to filter the output for Api datasource. the queries are executed in the order specified.   

        :return: The queries of this TamApiDataSource.
        :rtype: list[TamQueryEntry]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """
        Sets the queries of this TamApiDataSource.
        Optional set of Queries to filter the output for Api datasource. the queries are executed in the order specified.   

        :param queries: The queries of this TamApiDataSource.
        :type: list[TamQueryEntry]
        """

        self._queries = queries

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
        if not isinstance(other, TamApiDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
