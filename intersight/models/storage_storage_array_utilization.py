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


class StorageStorageArrayUtilization(object):
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
        'available': 'int',
        'free': 'int',
        'total': 'int',
        'used': 'int',
        'data_reduction': 'float',
        'parity': 'float',
        'provisioned': 'int',
        'shared': 'int',
        'snapshot': 'int',
        'system': 'int',
        'thin_provisioned': 'float',
        'total_reduction': 'float',
        'volume': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'available': 'Available',
        'free': 'Free',
        'total': 'Total',
        'used': 'Used',
        'data_reduction': 'DataReduction',
        'parity': 'Parity',
        'provisioned': 'Provisioned',
        'shared': 'Shared',
        'snapshot': 'Snapshot',
        'system': 'System',
        'thin_provisioned': 'ThinProvisioned',
        'total_reduction': 'TotalReduction',
        'volume': 'Volume'
    }

    def __init__(self, object_type=None, available=None, free=None, total=None, used=None, data_reduction=None, parity=None, provisioned=None, shared=None, snapshot=None, system=None, thin_provisioned=None, total_reduction=None, volume=None):
        """
        StorageStorageArrayUtilization - a model defined in Swagger
        """

        self._object_type = None
        self._available = None
        self._free = None
        self._total = None
        self._used = None
        self._data_reduction = None
        self._parity = None
        self._provisioned = None
        self._shared = None
        self._snapshot = None
        self._system = None
        self._thin_provisioned = None
        self._total_reduction = None
        self._volume = None

        if object_type is not None:
          self.object_type = object_type
        if available is not None:
          self.available = available
        if free is not None:
          self.free = free
        if total is not None:
          self.total = total
        if used is not None:
          self.used = used
        if data_reduction is not None:
          self.data_reduction = data_reduction
        if parity is not None:
          self.parity = parity
        if provisioned is not None:
          self.provisioned = provisioned
        if shared is not None:
          self.shared = shared
        if snapshot is not None:
          self.snapshot = snapshot
        if system is not None:
          self.system = system
        if thin_provisioned is not None:
          self.thin_provisioned = thin_provisioned
        if total_reduction is not None:
          self.total_reduction = total_reduction
        if volume is not None:
          self.volume = volume

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageStorageArrayUtilization.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this StorageStorageArrayUtilization.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageStorageArrayUtilization.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this StorageStorageArrayUtilization.
        :type: str
        """

        self._object_type = object_type

    @property
    def available(self):
        """
        Gets the available of this StorageStorageArrayUtilization.
        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.  

        :return: The available of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """
        Sets the available of this StorageStorageArrayUtilization.
        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.  

        :param available: The available of this StorageStorageArrayUtilization.
        :type: int
        """

        self._available = available

    @property
    def free(self):
        """
        Gets the free of this StorageStorageArrayUtilization.
        Unused space available for user to consume, represented in bytes.  

        :return: The free of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """
        Sets the free of this StorageStorageArrayUtilization.
        Unused space available for user to consume, represented in bytes.  

        :param free: The free of this StorageStorageArrayUtilization.
        :type: int
        """

        self._free = free

    @property
    def total(self):
        """
        Gets the total of this StorageStorageArrayUtilization.
        Total storage capacity, represented in bytes. It is set by the component manufacture.  

        :return: The total of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this StorageStorageArrayUtilization.
        Total storage capacity, represented in bytes. It is set by the component manufacture.  

        :param total: The total of this StorageStorageArrayUtilization.
        :type: int
        """

        self._total = total

    @property
    def used(self):
        """
        Gets the used of this StorageStorageArrayUtilization.
        Used or consumed storage capacity, represented in bytes.   

        :return: The used of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this StorageStorageArrayUtilization.
        Used or consumed storage capacity, represented in bytes.   

        :param used: The used of this StorageStorageArrayUtilization.
        :type: int
        """

        self._used = used

    @property
    def data_reduction(self):
        """
        Gets the data_reduction of this StorageStorageArrayUtilization.
        Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.  

        :return: The data_reduction of this StorageStorageArrayUtilization.
        :rtype: float
        """
        return self._data_reduction

    @data_reduction.setter
    def data_reduction(self, data_reduction):
        """
        Sets the data_reduction of this StorageStorageArrayUtilization.
        Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.  

        :param data_reduction: The data_reduction of this StorageStorageArrayUtilization.
        :type: float
        """

        self._data_reduction = data_reduction

    @property
    def parity(self):
        """
        Gets the parity of this StorageStorageArrayUtilization.
        Percentage of data that is fully protected. The percentage value will drop below 100% if the data is not fully protected.  

        :return: The parity of this StorageStorageArrayUtilization.
        :rtype: float
        """
        return self._parity

    @parity.setter
    def parity(self, parity):
        """
        Sets the parity of this StorageStorageArrayUtilization.
        Percentage of data that is fully protected. The percentage value will drop below 100% if the data is not fully protected.  

        :param parity: The parity of this StorageStorageArrayUtilization.
        :type: float
        """

        self._parity = parity

    @property
    def provisioned(self):
        """
        Gets the provisioned of this StorageStorageArrayUtilization.
        Total provisioned storage capacity in Pure FlashArray, represented in bytes.  

        :return: The provisioned of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._provisioned

    @provisioned.setter
    def provisioned(self, provisioned):
        """
        Sets the provisioned of this StorageStorageArrayUtilization.
        Total provisioned storage capacity in Pure FlashArray, represented in bytes.  

        :param provisioned: The provisioned of this StorageStorageArrayUtilization.
        :type: int
        """

        self._provisioned = provisioned

    @property
    def shared(self):
        """
        Gets the shared of this StorageStorageArrayUtilization.
        Physical space occupied by deduplicated data, represented in bytes. The space is shared with other volumes and snapshots as a result of data deduplication.  

        :return: The shared of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this StorageStorageArrayUtilization.
        Physical space occupied by deduplicated data, represented in bytes. The space is shared with other volumes and snapshots as a result of data deduplication.  

        :param shared: The shared of this StorageStorageArrayUtilization.
        :type: int
        """

        self._shared = shared

    @property
    def snapshot(self):
        """
        Gets the snapshot of this StorageStorageArrayUtilization.
        Physical space occupied by the snapshots, represented in bytes.  

        :return: The snapshot of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """
        Sets the snapshot of this StorageStorageArrayUtilization.
        Physical space occupied by the snapshots, represented in bytes.  

        :param snapshot: The snapshot of this StorageStorageArrayUtilization.
        :type: int
        """

        self._snapshot = snapshot

    @property
    def system(self):
        """
        Gets the system of this StorageStorageArrayUtilization.
        Physical space occupied by internal array metadata, represented in bytes.  

        :return: The system of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this StorageStorageArrayUtilization.
        Physical space occupied by internal array metadata, represented in bytes.  

        :param system: The system of this StorageStorageArrayUtilization.
        :type: int
        """

        self._system = system

    @property
    def thin_provisioned(self):
        """
        Gets the thin_provisioned of this StorageStorageArrayUtilization.
        Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.  

        :return: The thin_provisioned of this StorageStorageArrayUtilization.
        :rtype: float
        """
        return self._thin_provisioned

    @thin_provisioned.setter
    def thin_provisioned(self, thin_provisioned):
        """
        Sets the thin_provisioned of this StorageStorageArrayUtilization.
        Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.  

        :param thin_provisioned: The thin_provisioned of this StorageStorageArrayUtilization.
        :type: float
        """

        self._thin_provisioned = thin_provisioned

    @property
    def total_reduction(self):
        """
        Gets the total_reduction of this StorageStorageArrayUtilization.
        Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.  

        :return: The total_reduction of this StorageStorageArrayUtilization.
        :rtype: float
        """
        return self._total_reduction

    @total_reduction.setter
    def total_reduction(self, total_reduction):
        """
        Sets the total_reduction of this StorageStorageArrayUtilization.
        Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.  

        :param total_reduction: The total_reduction of this StorageStorageArrayUtilization.
        :type: float
        """

        self._total_reduction = total_reduction

    @property
    def volume(self):
        """
        Gets the volume of this StorageStorageArrayUtilization.
        Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size is represented in bytes.   

        :return: The volume of this StorageStorageArrayUtilization.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this StorageStorageArrayUtilization.
        Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size is represented in bytes.   

        :param volume: The volume of this StorageStorageArrayUtilization.
        :type: int
        """

        self._volume = volume

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
        if not isinstance(other, StorageStorageArrayUtilization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
