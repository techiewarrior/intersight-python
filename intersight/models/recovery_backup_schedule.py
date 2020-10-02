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


class RecoveryBackupSchedule(object):
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
        'execution_time': 'datetime',
        'frequency_unit': 'str',
        'hours': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'execution_time': 'ExecutionTime',
        'frequency_unit': 'FrequencyUnit',
        'hours': 'Hours'
    }

    def __init__(self, object_type=None, execution_time=None, frequency_unit='Daily', hours=None):
        """
        RecoveryBackupSchedule - a model defined in Swagger
        """

        self._object_type = None
        self._execution_time = None
        self._frequency_unit = None
        self._hours = None

        if object_type is not None:
          self.object_type = object_type
        if execution_time is not None:
          self.execution_time = execution_time
        if frequency_unit is not None:
          self.frequency_unit = frequency_unit
        if hours is not None:
          self.hours = hours

    @property
    def object_type(self):
        """
        Gets the object_type of this RecoveryBackupSchedule.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this RecoveryBackupSchedule.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this RecoveryBackupSchedule.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this RecoveryBackupSchedule.
        :type: str
        """

        self._object_type = object_type

    @property
    def execution_time(self):
        """
        Gets the execution_time of this RecoveryBackupSchedule.
        The time at which the backup is to be run on a given day. This is used when the frequency unit is daily.

        :return: The execution_time of this RecoveryBackupSchedule.
        :rtype: datetime
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """
        Sets the execution_time of this RecoveryBackupSchedule.
        The time at which the backup is to be run on a given day. This is used when the frequency unit is daily.

        :param execution_time: The execution_time of this RecoveryBackupSchedule.
        :type: datetime
        """

        self._execution_time = execution_time

    @property
    def frequency_unit(self):
        """
        Gets the frequency_unit of this RecoveryBackupSchedule.
        The frequency at which the backup schedule must run.

        :return: The frequency_unit of this RecoveryBackupSchedule.
        :rtype: str
        """
        return self._frequency_unit

    @frequency_unit.setter
    def frequency_unit(self, frequency_unit):
        """
        Sets the frequency_unit of this RecoveryBackupSchedule.
        The frequency at which the backup schedule must run.

        :param frequency_unit: The frequency_unit of this RecoveryBackupSchedule.
        :type: str
        """
        allowed_values = ["Daily", "Periodic"]
        if frequency_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency_unit` ({0}), must be one of {1}"
                .format(frequency_unit, allowed_values)
            )

        self._frequency_unit = frequency_unit

    @property
    def hours(self):
        """
        Gets the hours of this RecoveryBackupSchedule.
        The frequency, in hours, at which the backup schedule runs.

        :return: The hours of this RecoveryBackupSchedule.
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, hours):
        """
        Sets the hours of this RecoveryBackupSchedule.
        The frequency, in hours, at which the backup schedule runs.

        :param hours: The hours of this RecoveryBackupSchedule.
        :type: int
        """

        self._hours = hours

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
        if not isinstance(other, RecoveryBackupSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other