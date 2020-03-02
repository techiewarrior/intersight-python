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


class IaasLicenseKeysInfo(object):
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
        'count': 'int',
        'expiration_date': 'str',
        'license_id': 'str',
        'pid': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'count': 'Count',
        'expiration_date': 'ExpirationDate',
        'license_id': 'LicenseId',
        'pid': 'Pid'
    }

    def __init__(self, object_type=None, count=None, expiration_date=None, license_id=None, pid=None):
        """
        IaasLicenseKeysInfo - a model defined in Swagger
        """

        self._object_type = None
        self._count = None
        self._expiration_date = None
        self._license_id = None
        self._pid = None

        if object_type is not None:
          self.object_type = object_type
        if count is not None:
          self.count = count
        if expiration_date is not None:
          self.expiration_date = expiration_date
        if license_id is not None:
          self.license_id = license_id
        if pid is not None:
          self.pid = pid

    @property
    def object_type(self):
        """
        Gets the object_type of this IaasLicenseKeysInfo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this IaasLicenseKeysInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IaasLicenseKeysInfo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this IaasLicenseKeysInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def count(self):
        """
        Gets the count of this IaasLicenseKeysInfo.
        Number of licenses available for the UCSD PID (Product ID).

        :return: The count of this IaasLicenseKeysInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this IaasLicenseKeysInfo.
        Number of licenses available for the UCSD PID (Product ID).

        :param count: The count of this IaasLicenseKeysInfo.
        :type: int
        """

        self._count = count

    @property
    def expiration_date(self):
        """
        Gets the expiration_date of this IaasLicenseKeysInfo.
        Expiration date for the license.

        :return: The expiration_date of this IaasLicenseKeysInfo.
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """
        Sets the expiration_date of this IaasLicenseKeysInfo.
        Expiration date for the license.

        :param expiration_date: The expiration_date of this IaasLicenseKeysInfo.
        :type: str
        """

        self._expiration_date = expiration_date

    @property
    def license_id(self):
        """
        Gets the license_id of this IaasLicenseKeysInfo.
        UCS Director Unique license ID.

        :return: The license_id of this IaasLicenseKeysInfo.
        :rtype: str
        """
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        """
        Sets the license_id of this IaasLicenseKeysInfo.
        UCS Director Unique license ID.

        :param license_id: The license_id of this IaasLicenseKeysInfo.
        :type: str
        """

        self._license_id = license_id

    @property
    def pid(self):
        """
        Gets the pid of this IaasLicenseKeysInfo.
        PID (Product ID) for UCSD License.

        :return: The pid of this IaasLicenseKeysInfo.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this IaasLicenseKeysInfo.
        PID (Product ID) for UCSD License.

        :param pid: The pid of this IaasLicenseKeysInfo.
        :type: str
        """

        self._pid = pid

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
        if not isinstance(other, IaasLicenseKeysInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
