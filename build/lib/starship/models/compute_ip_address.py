# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ComputeIpAddress(object):
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
        'address': 'str',
        'category': 'str',
        'default_gateway': 'str',
        'dn': 'str',
        'name': 'str',
        'subnet': 'str',
        'type': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'category': 'Category',
        'default_gateway': 'DefaultGateway',
        'dn': 'Dn',
        'name': 'Name',
        'subnet': 'Subnet',
        'type': 'Type'
    }

    def __init__(self, address=None, category='Equipment', default_gateway=None, dn=None, name='Outband', subnet=None, type='VnicIpV4StaticAddr'):
        """
        ComputeIpAddress - a model defined in Swagger
        """

        self._address = None
        self._category = None
        self._default_gateway = None
        self._dn = None
        self._name = None
        self._subnet = None
        self._type = None

        if address is not None:
          self.address = address
        if category is not None:
          self.category = category
        if default_gateway is not None:
          self.default_gateway = default_gateway
        if dn is not None:
          self.dn = dn
        if name is not None:
          self.name = name
        if subnet is not None:
          self.subnet = subnet
        if type is not None:
          self.type = type

    @property
    def address(self):
        """
        Gets the address of this ComputeIpAddress.

        :return: The address of this ComputeIpAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ComputeIpAddress.

        :param address: The address of this ComputeIpAddress.
        :type: str
        """

        self._address = address

    @property
    def category(self):
        """
        Gets the category of this ComputeIpAddress.

        :return: The category of this ComputeIpAddress.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ComputeIpAddress.

        :param category: The category of this ComputeIpAddress.
        :type: str
        """
        allowed_values = ["Equipment", "ServiceProfile"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def default_gateway(self):
        """
        Gets the default_gateway of this ComputeIpAddress.

        :return: The default_gateway of this ComputeIpAddress.
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """
        Sets the default_gateway of this ComputeIpAddress.

        :param default_gateway: The default_gateway of this ComputeIpAddress.
        :type: str
        """

        self._default_gateway = default_gateway

    @property
    def dn(self):
        """
        Gets the dn of this ComputeIpAddress.

        :return: The dn of this ComputeIpAddress.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this ComputeIpAddress.

        :param dn: The dn of this ComputeIpAddress.
        :type: str
        """

        self._dn = dn

    @property
    def name(self):
        """
        Gets the name of this ComputeIpAddress.

        :return: The name of this ComputeIpAddress.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ComputeIpAddress.

        :param name: The name of this ComputeIpAddress.
        :type: str
        """
        allowed_values = ["Outband", "Inband"]
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def subnet(self):
        """
        Gets the subnet of this ComputeIpAddress.

        :return: The subnet of this ComputeIpAddress.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """
        Sets the subnet of this ComputeIpAddress.

        :param subnet: The subnet of this ComputeIpAddress.
        :type: str
        """

        self._subnet = subnet

    @property
    def type(self):
        """
        Gets the type of this ComputeIpAddress.

        :return: The type of this ComputeIpAddress.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ComputeIpAddress.

        :param type: The type of this ComputeIpAddress.
        :type: str
        """
        allowed_values = ["VnicIpV4StaticAddr", "VnicIpV4PooledAddr", "VnicIpV4MgmtPooledAddr", "VnicIpV6StaticAddr", "VnicIpV6MgmtPooledAddr", "VnicIpV4ProfDerivedAddr"]
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
        if not isinstance(other, ComputeIpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other