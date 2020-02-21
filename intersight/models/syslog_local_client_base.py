# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1415
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SyslogLocalClientBase(object):
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
        'min_severity': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'min_severity': 'MinSeverity'
    }

    def __init__(self, object_type=None, min_severity='warning'):
        """
        SyslogLocalClientBase - a model defined in Swagger
        """

        self._object_type = None
        self._min_severity = None

        if object_type is not None:
          self.object_type = object_type
        if min_severity is not None:
          self.min_severity = min_severity

    @property
    def object_type(self):
        """
        Gets the object_type of this SyslogLocalClientBase.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this SyslogLocalClientBase.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SyslogLocalClientBase.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this SyslogLocalClientBase.
        :type: str
        """

        self._object_type = object_type

    @property
    def min_severity(self):
        """
        Gets the min_severity of this SyslogLocalClientBase.
        Lowest level of messages to be included in the local log.   

        :return: The min_severity of this SyslogLocalClientBase.
        :rtype: str
        """
        return self._min_severity

    @min_severity.setter
    def min_severity(self, min_severity):
        """
        Sets the min_severity of this SyslogLocalClientBase.
        Lowest level of messages to be included in the local log.   

        :param min_severity: The min_severity of this SyslogLocalClientBase.
        :type: str
        """
        allowed_values = ["warning", "emergency", "alert", "critical", "error", "notice", "informational", "debug"]
        if min_severity not in allowed_values:
            raise ValueError(
                "Invalid value for `min_severity` ({0}), must be one of {1}"
                .format(min_severity, allowed_values)
            )

        self._min_severity = min_severity

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
        if not isinstance(other, SyslogLocalClientBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
