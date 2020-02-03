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


class BootPxe(object):
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
        'enabled': 'bool',
        'name': 'str',
        'interface_name': 'str',
        'interface_source': 'str',
        'ip_type': 'str',
        'mac_address': 'str',
        'port': 'int',
        'slot': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'enabled': 'Enabled',
        'name': 'Name',
        'interface_name': 'InterfaceName',
        'interface_source': 'InterfaceSource',
        'ip_type': 'IpType',
        'mac_address': 'MacAddress',
        'port': 'Port',
        'slot': 'Slot'
    }

    def __init__(self, object_type=None, enabled=None, name=None, interface_name=None, interface_source='name', ip_type='None', mac_address=None, port=None, slot=None):
        """
        BootPxe - a model defined in Swagger
        """

        self._object_type = None
        self._enabled = None
        self._name = None
        self._interface_name = None
        self._interface_source = None
        self._ip_type = None
        self._mac_address = None
        self._port = None
        self._slot = None

        if object_type is not None:
          self.object_type = object_type
        if enabled is not None:
          self.enabled = enabled
        if name is not None:
          self.name = name
        if interface_name is not None:
          self.interface_name = interface_name
        if interface_source is not None:
          self.interface_source = interface_source
        if ip_type is not None:
          self.ip_type = ip_type
        if mac_address is not None:
          self.mac_address = mac_address
        if port is not None:
          self.port = port
        if slot is not None:
          self.slot = slot

    @property
    def object_type(self):
        """
        Gets the object_type of this BootPxe.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this BootPxe.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this BootPxe.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this BootPxe.
        :type: str
        """

        self._object_type = object_type

    @property
    def enabled(self):
        """
        Gets the enabled of this BootPxe.
        Specifies if the boot device is enabled or disabled.  

        :return: The enabled of this BootPxe.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BootPxe.
        Specifies if the boot device is enabled or disabled.  

        :param enabled: The enabled of this BootPxe.
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this BootPxe.
        A name that helps identify a boot device. It can be any string that adheres to the following constraints. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :return: The name of this BootPxe.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootPxe.
        A name that helps identify a boot device. It can be any string that adheres to the following constraints. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :param name: The name of this BootPxe.
        :type: str
        """

        self._name = name

    @property
    def interface_name(self):
        """
        Gets the interface_name of this BootPxe.
        The name of the underlying virtual ethernet interface used by the PXE boot device.  

        :return: The interface_name of this BootPxe.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this BootPxe.
        The name of the underlying virtual ethernet interface used by the PXE boot device.  

        :param interface_name: The interface_name of this BootPxe.
        :type: str
        """

        self._interface_name = interface_name

    @property
    def interface_source(self):
        """
        Gets the interface_source of this BootPxe.
        Lists the supported Interface Source for PXE device. Supported values are \"name\" and \"mac\".  

        :return: The interface_source of this BootPxe.
        :rtype: str
        """
        return self._interface_source

    @interface_source.setter
    def interface_source(self, interface_source):
        """
        Sets the interface_source of this BootPxe.
        Lists the supported Interface Source for PXE device. Supported values are \"name\" and \"mac\".  

        :param interface_source: The interface_source of this BootPxe.
        :type: str
        """
        allowed_values = ["name", "mac", "port"]
        if interface_source not in allowed_values:
            raise ValueError(
                "Invalid value for `interface_source` ({0}), must be one of {1}"
                .format(interface_source, allowed_values)
            )

        self._interface_source = interface_source

    @property
    def ip_type(self):
        """
        Gets the ip_type of this BootPxe.
        The IP Address family type to use during the PXE Boot process.  

        :return: The ip_type of this BootPxe.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """
        Sets the ip_type of this BootPxe.
        The IP Address family type to use during the PXE Boot process.  

        :param ip_type: The ip_type of this BootPxe.
        :type: str
        """
        allowed_values = ["None", "IPv4", "IPv6"]
        if ip_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_type` ({0}), must be one of {1}"
                .format(ip_type, allowed_values)
            )

        self._ip_type = ip_type

    @property
    def mac_address(self):
        """
        Gets the mac_address of this BootPxe.
        The MAC Address of the underlying virtual ethernet interface used by the PXE boot device.  

        :return: The mac_address of this BootPxe.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this BootPxe.
        The MAC Address of the underlying virtual ethernet interface used by the PXE boot device.  

        :param mac_address: The mac_address of this BootPxe.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def port(self):
        """
        Gets the port of this BootPxe.
        The logical port id of the ethernet interface used by the PXE device. Port is a deprecated property. Default value is changed to '-1' as this is invalid port. New or modified pxe device has the port value always set to '-1'.  

        :return: The port of this BootPxe.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this BootPxe.
        The logical port id of the ethernet interface used by the PXE device. Port is a deprecated property. Default value is changed to '-1' as this is invalid port. New or modified pxe device has the port value always set to '-1'.  

        :param port: The port of this BootPxe.
        :type: int
        """

        self._port = port

    @property
    def slot(self):
        """
        Gets the slot of this BootPxe.
        The slot ID of the adapter on which the underlying virtual ethernet interface is present. Supported values are ( 1 - 255, \"MLOM\", \"L\", \"L1\", \"L2\", \"OCP\").   

        :return: The slot of this BootPxe.
        :rtype: str
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """
        Sets the slot of this BootPxe.
        The slot ID of the adapter on which the underlying virtual ethernet interface is present. Supported values are ( 1 - 255, \"MLOM\", \"L\", \"L1\", \"L2\", \"OCP\").   

        :param slot: The slot of this BootPxe.
        :type: str
        """

        self._slot = slot

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
        if not isinstance(other, BootPxe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
