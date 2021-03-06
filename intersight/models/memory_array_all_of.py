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


class MemoryArrayAllOf(object):
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
        'array_id': 'int',
        'cpu_id': 'int',
        'current_capacity': 'str',
        'error_correction': 'str',
        'max_capacity': 'str',
        'max_devices': 'str',
        'oper_power_state': 'str',
        'presence': 'str',
        'compute_board': 'ComputeBoard',
        'persistent_memory_units': 'list[MemoryPersistentMemoryUnit]',
        'registered_device': 'AssetDeviceRegistration',
        'units': 'list[MemoryUnit]'
    }

    attribute_map = {
        'array_id': 'ArrayId',
        'cpu_id': 'CpuId',
        'current_capacity': 'CurrentCapacity',
        'error_correction': 'ErrorCorrection',
        'max_capacity': 'MaxCapacity',
        'max_devices': 'MaxDevices',
        'oper_power_state': 'OperPowerState',
        'presence': 'Presence',
        'compute_board': 'ComputeBoard',
        'persistent_memory_units': 'PersistentMemoryUnits',
        'registered_device': 'RegisteredDevice',
        'units': 'Units'
    }

    def __init__(self,
                 array_id=None,
                 cpu_id=None,
                 current_capacity=None,
                 error_correction=None,
                 max_capacity=None,
                 max_devices=None,
                 oper_power_state=None,
                 presence=None,
                 compute_board=None,
                 persistent_memory_units=None,
                 registered_device=None,
                 units=None,
                 local_vars_configuration=None):  # noqa: E501
        """MemoryArrayAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._array_id = None
        self._cpu_id = None
        self._current_capacity = None
        self._error_correction = None
        self._max_capacity = None
        self._max_devices = None
        self._oper_power_state = None
        self._presence = None
        self._compute_board = None
        self._persistent_memory_units = None
        self._registered_device = None
        self._units = None
        self.discriminator = None

        if array_id is not None:
            self.array_id = array_id
        if cpu_id is not None:
            self.cpu_id = cpu_id
        if current_capacity is not None:
            self.current_capacity = current_capacity
        if error_correction is not None:
            self.error_correction = error_correction
        if max_capacity is not None:
            self.max_capacity = max_capacity
        if max_devices is not None:
            self.max_devices = max_devices
        if oper_power_state is not None:
            self.oper_power_state = oper_power_state
        if presence is not None:
            self.presence = presence
        if compute_board is not None:
            self.compute_board = compute_board
        if persistent_memory_units is not None:
            self.persistent_memory_units = persistent_memory_units
        if registered_device is not None:
            self.registered_device = registered_device
        if units is not None:
            self.units = units

    @property
    def array_id(self):
        """Gets the array_id of this MemoryArrayAllOf.  # noqa: E501


        :return: The array_id of this MemoryArrayAllOf.  # noqa: E501
        :rtype: int
        """
        return self._array_id

    @array_id.setter
    def array_id(self, array_id):
        """Sets the array_id of this MemoryArrayAllOf.


        :param array_id: The array_id of this MemoryArrayAllOf.  # noqa: E501
        :type: int
        """

        self._array_id = array_id

    @property
    def cpu_id(self):
        """Gets the cpu_id of this MemoryArrayAllOf.  # noqa: E501


        :return: The cpu_id of this MemoryArrayAllOf.  # noqa: E501
        :rtype: int
        """
        return self._cpu_id

    @cpu_id.setter
    def cpu_id(self, cpu_id):
        """Sets the cpu_id of this MemoryArrayAllOf.


        :param cpu_id: The cpu_id of this MemoryArrayAllOf.  # noqa: E501
        :type: int
        """

        self._cpu_id = cpu_id

    @property
    def current_capacity(self):
        """Gets the current_capacity of this MemoryArrayAllOf.  # noqa: E501


        :return: The current_capacity of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._current_capacity

    @current_capacity.setter
    def current_capacity(self, current_capacity):
        """Sets the current_capacity of this MemoryArrayAllOf.


        :param current_capacity: The current_capacity of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._current_capacity = current_capacity

    @property
    def error_correction(self):
        """Gets the error_correction of this MemoryArrayAllOf.  # noqa: E501


        :return: The error_correction of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._error_correction

    @error_correction.setter
    def error_correction(self, error_correction):
        """Sets the error_correction of this MemoryArrayAllOf.


        :param error_correction: The error_correction of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._error_correction = error_correction

    @property
    def max_capacity(self):
        """Gets the max_capacity of this MemoryArrayAllOf.  # noqa: E501


        :return: The max_capacity of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this MemoryArrayAllOf.


        :param max_capacity: The max_capacity of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._max_capacity = max_capacity

    @property
    def max_devices(self):
        """Gets the max_devices of this MemoryArrayAllOf.  # noqa: E501


        :return: The max_devices of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._max_devices

    @max_devices.setter
    def max_devices(self, max_devices):
        """Sets the max_devices of this MemoryArrayAllOf.


        :param max_devices: The max_devices of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._max_devices = max_devices

    @property
    def oper_power_state(self):
        """Gets the oper_power_state of this MemoryArrayAllOf.  # noqa: E501


        :return: The oper_power_state of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_power_state

    @oper_power_state.setter
    def oper_power_state(self, oper_power_state):
        """Sets the oper_power_state of this MemoryArrayAllOf.


        :param oper_power_state: The oper_power_state of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._oper_power_state = oper_power_state

    @property
    def presence(self):
        """Gets the presence of this MemoryArrayAllOf.  # noqa: E501


        :return: The presence of this MemoryArrayAllOf.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this MemoryArrayAllOf.


        :param presence: The presence of this MemoryArrayAllOf.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def compute_board(self):
        """Gets the compute_board of this MemoryArrayAllOf.  # noqa: E501


        :return: The compute_board of this MemoryArrayAllOf.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """Sets the compute_board of this MemoryArrayAllOf.


        :param compute_board: The compute_board of this MemoryArrayAllOf.  # noqa: E501
        :type: ComputeBoard
        """

        self._compute_board = compute_board

    @property
    def persistent_memory_units(self):
        """Gets the persistent_memory_units of this MemoryArrayAllOf.  # noqa: E501

        A reference to a memoryPersistentMemoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the persistent memory modules found in a memory array of a server.   # noqa: E501

        :return: The persistent_memory_units of this MemoryArrayAllOf.  # noqa: E501
        :rtype: list[MemoryPersistentMemoryUnit]
        """
        return self._persistent_memory_units

    @persistent_memory_units.setter
    def persistent_memory_units(self, persistent_memory_units):
        """Sets the persistent_memory_units of this MemoryArrayAllOf.

        A reference to a memoryPersistentMemoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the persistent memory modules found in a memory array of a server.   # noqa: E501

        :param persistent_memory_units: The persistent_memory_units of this MemoryArrayAllOf.  # noqa: E501
        :type: list[MemoryPersistentMemoryUnit]
        """

        self._persistent_memory_units = persistent_memory_units

    @property
    def registered_device(self):
        """Gets the registered_device of this MemoryArrayAllOf.  # noqa: E501


        :return: The registered_device of this MemoryArrayAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this MemoryArrayAllOf.


        :param registered_device: The registered_device of this MemoryArrayAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def units(self):
        """Gets the units of this MemoryArrayAllOf.  # noqa: E501

        A reference to a memoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the DIMMs found in a memory array of a server. This includes both regular DIMMs and persistent memory modules.   # noqa: E501

        :return: The units of this MemoryArrayAllOf.  # noqa: E501
        :rtype: list[MemoryUnit]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this MemoryArrayAllOf.

        A reference to a memoryUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents all the DIMMs found in a memory array of a server. This includes both regular DIMMs and persistent memory modules.   # noqa: E501

        :param units: The units of this MemoryArrayAllOf.  # noqa: E501
        :type: list[MemoryUnit]
        """

        self._units = units

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
        if not isinstance(other, MemoryArrayAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemoryArrayAllOf):
            return True

        return self.to_dict() != other.to_dict()
