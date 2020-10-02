# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class EquipmentLocatorLedAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'color': 'str',
        'oper_state': 'str',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'registered_device': 'AssetDeviceRegistration',
        'storage_physical_disk': 'StoragePhysicalDisk'
    }

    attribute_map = {
        'color': 'Color',
        'oper_state': 'OperState',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'registered_device': 'RegisteredDevice',
        'storage_physical_disk': 'StoragePhysicalDisk'
    }

    def __init__(self,
                 color=None,
                 oper_state=None,
                 compute_blade=None,
                 compute_rack_unit=None,
                 registered_device=None,
                 storage_physical_disk=None,
                 local_vars_configuration=None):  # noqa: E501
        """EquipmentLocatorLedAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._color = None
        self._oper_state = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._registered_device = None
        self._storage_physical_disk = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if oper_state is not None:
            self.oper_state = oper_state
        if compute_blade is not None:
            self.compute_blade = compute_blade
        if compute_rack_unit is not None:
            self.compute_rack_unit = compute_rack_unit
        if registered_device is not None:
            self.registered_device = registered_device
        if storage_physical_disk is not None:
            self.storage_physical_disk = storage_physical_disk

    @property
    def color(self):
        """Gets the color of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The color of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this EquipmentLocatorLedAllOf.


        :param color: The color of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def oper_state(self):
        """Gets the oper_state of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The oper_state of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this EquipmentLocatorLedAllOf.


        :param oper_state: The oper_state of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def compute_blade(self):
        """Gets the compute_blade of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The compute_blade of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: ComputeBlade
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """Sets the compute_blade of this EquipmentLocatorLedAllOf.


        :param compute_blade: The compute_blade of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: ComputeBlade
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """Gets the compute_rack_unit of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The compute_rack_unit of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: ComputeRackUnit
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """Sets the compute_rack_unit of this EquipmentLocatorLedAllOf.


        :param compute_rack_unit: The compute_rack_unit of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: ComputeRackUnit
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def registered_device(self):
        """Gets the registered_device of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The registered_device of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this EquipmentLocatorLedAllOf.


        :param registered_device: The registered_device of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def storage_physical_disk(self):
        """Gets the storage_physical_disk of this EquipmentLocatorLedAllOf.  # noqa: E501


        :return: The storage_physical_disk of this EquipmentLocatorLedAllOf.  # noqa: E501
        :rtype: StoragePhysicalDisk
        """
        return self._storage_physical_disk

    @storage_physical_disk.setter
    def storage_physical_disk(self, storage_physical_disk):
        """Sets the storage_physical_disk of this EquipmentLocatorLedAllOf.


        :param storage_physical_disk: The storage_physical_disk of this EquipmentLocatorLedAllOf.  # noqa: E501
        :type: StoragePhysicalDisk
        """

        self._storage_physical_disk = storage_physical_disk

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EquipmentLocatorLedAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentLocatorLedAllOf):
            return True

        return self.to_dict() != other.to_dict()