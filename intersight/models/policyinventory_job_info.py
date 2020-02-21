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


class PolicyinventoryJobInfo(object):
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
        'execution_status': 'str',
        'last_scheduled_time': 'datetime',
        'policy_id': 'str',
        'policy_name': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'execution_status': 'ExecutionStatus',
        'last_scheduled_time': 'LastScheduledTime',
        'policy_id': 'PolicyId',
        'policy_name': 'PolicyName'
    }

    def __init__(self, object_type=None, execution_status='Scheduled', last_scheduled_time=None, policy_id=None, policy_name=None):
        """
        PolicyinventoryJobInfo - a model defined in Swagger
        """

        self._object_type = None
        self._execution_status = None
        self._last_scheduled_time = None
        self._policy_id = None
        self._policy_name = None

        if object_type is not None:
          self.object_type = object_type
        if execution_status is not None:
          self.execution_status = execution_status
        if last_scheduled_time is not None:
          self.last_scheduled_time = last_scheduled_time
        if policy_id is not None:
          self.policy_id = policy_id
        if policy_name is not None:
          self.policy_name = policy_name

    @property
    def object_type(self):
        """
        Gets the object_type of this PolicyinventoryJobInfo.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this PolicyinventoryJobInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this PolicyinventoryJobInfo.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this PolicyinventoryJobInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def execution_status(self):
        """
        Gets the execution_status of this PolicyinventoryJobInfo.
        Execution status of the inventory job.  

        :return: The execution_status of this PolicyinventoryJobInfo.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """
        Sets the execution_status of this PolicyinventoryJobInfo.
        Execution status of the inventory job.  

        :param execution_status: The execution_status of this PolicyinventoryJobInfo.
        :type: str
        """
        allowed_values = ["Scheduled", "Completed", "Error"]
        if execution_status not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_status` ({0}), must be one of {1}"
                .format(execution_status, allowed_values)
            )

        self._execution_status = execution_status

    @property
    def last_scheduled_time(self):
        """
        Gets the last_scheduled_time of this PolicyinventoryJobInfo.
        Last scheduled time of the inventory job.  

        :return: The last_scheduled_time of this PolicyinventoryJobInfo.
        :rtype: datetime
        """
        return self._last_scheduled_time

    @last_scheduled_time.setter
    def last_scheduled_time(self, last_scheduled_time):
        """
        Sets the last_scheduled_time of this PolicyinventoryJobInfo.
        Last scheduled time of the inventory job.  

        :param last_scheduled_time: The last_scheduled_time of this PolicyinventoryJobInfo.
        :type: datetime
        """

        self._last_scheduled_time = last_scheduled_time

    @property
    def policy_id(self):
        """
        Gets the policy_id of this PolicyinventoryJobInfo.
        Policy ID for the inventory job.  

        :return: The policy_id of this PolicyinventoryJobInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this PolicyinventoryJobInfo.
        Policy ID for the inventory job.  

        :param policy_id: The policy_id of this PolicyinventoryJobInfo.
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """
        Gets the policy_name of this PolicyinventoryJobInfo.
        Policy name for the inventory job.   

        :return: The policy_name of this PolicyinventoryJobInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this PolicyinventoryJobInfo.
        Policy name for the inventory job.   

        :param policy_name: The policy_name of this PolicyinventoryJobInfo.
        :type: str
        """

        self._policy_name = policy_name

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
        if not isinstance(other, PolicyinventoryJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
