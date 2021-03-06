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


class AdapterUnit(object):
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
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'adapter_id': 'str',
        'base_mac_address': 'str',
        'integrated': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'part_number': 'str',
        'pci_slot': 'str',
        'power': 'str',
        'presence': 'str',
        'thermal': 'str',
        'vid': 'str',
        'compute_blade': 'ComputeBladeRef',
        'compute_rack_unit': 'ComputeRackUnitRef',
        'controller': 'ManagementControllerRef',
        'ext_eth_ifs': 'list[AdapterExtEthInterfaceRef]',
        'host_eth_ifs': 'list[AdapterHostEthInterfaceRef]',
        'host_fc_ifs': 'list[AdapterHostFcInterfaceRef]',
        'host_iscsi_ifs': 'list[AdapterHostIscsiInterfaceRef]',
        'registered_device': 'AssetDeviceRegistrationRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'adapter_id': 'AdapterId',
        'base_mac_address': 'BaseMacAddress',
        'integrated': 'Integrated',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'part_number': 'PartNumber',
        'pci_slot': 'PciSlot',
        'power': 'Power',
        'presence': 'Presence',
        'thermal': 'Thermal',
        'vid': 'Vid',
        'compute_blade': 'ComputeBlade',
        'compute_rack_unit': 'ComputeRackUnit',
        'controller': 'Controller',
        'ext_eth_ifs': 'ExtEthIfs',
        'host_eth_ifs': 'HostEthIfs',
        'host_fc_ifs': 'HostFcIfs',
        'host_iscsi_ifs': 'HostIscsiIfs',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, adapter_id=None, base_mac_address=None, integrated=None, oper_state=None, operability=None, part_number=None, pci_slot=None, power=None, presence=None, thermal=None, vid=None, compute_blade=None, compute_rack_unit=None, controller=None, ext_eth_ifs=None, host_eth_ifs=None, host_fc_ifs=None, host_iscsi_ifs=None, registered_device=None):
        """
        AdapterUnit - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._adapter_id = None
        self._base_mac_address = None
        self._integrated = None
        self._oper_state = None
        self._operability = None
        self._part_number = None
        self._pci_slot = None
        self._power = None
        self._presence = None
        self._thermal = None
        self._vid = None
        self._compute_blade = None
        self._compute_rack_unit = None
        self._controller = None
        self._ext_eth_ifs = None
        self._host_eth_ifs = None
        self._host_fc_ifs = None
        self._host_iscsi_ifs = None
        self._registered_device = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if adapter_id is not None:
          self.adapter_id = adapter_id
        if base_mac_address is not None:
          self.base_mac_address = base_mac_address
        if integrated is not None:
          self.integrated = integrated
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if part_number is not None:
          self.part_number = part_number
        if pci_slot is not None:
          self.pci_slot = pci_slot
        if power is not None:
          self.power = power
        if presence is not None:
          self.presence = presence
        if thermal is not None:
          self.thermal = thermal
        if vid is not None:
          self.vid = vid
        if compute_blade is not None:
          self.compute_blade = compute_blade
        if compute_rack_unit is not None:
          self.compute_rack_unit = compute_rack_unit
        if controller is not None:
          self.controller = controller
        if ext_eth_ifs is not None:
          self.ext_eth_ifs = ext_eth_ifs
        if host_eth_ifs is not None:
          self.host_eth_ifs = host_eth_ifs
        if host_fc_ifs is not None:
          self.host_fc_ifs = host_fc_ifs
        if host_iscsi_ifs is not None:
          self.host_iscsi_ifs = host_iscsi_ifs
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AdapterUnit.
        The Account ID for this managed object.

        :return: The account_moid of this AdapterUnit.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AdapterUnit.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this AdapterUnit.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this AdapterUnit.
        The time when this managed object was created.

        :return: The create_time of this AdapterUnit.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AdapterUnit.
        The time when this managed object was created.

        :param create_time: The create_time of this AdapterUnit.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this AdapterUnit.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this AdapterUnit.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this AdapterUnit.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this AdapterUnit.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AdapterUnit.
        The time when this managed object was last modified.

        :return: The mod_time of this AdapterUnit.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AdapterUnit.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this AdapterUnit.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AdapterUnit.
        The unique identifier of this Managed Object instance.

        :return: The moid of this AdapterUnit.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AdapterUnit.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this AdapterUnit.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterUnit.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this AdapterUnit.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterUnit.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this AdapterUnit.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AdapterUnit.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this AdapterUnit.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AdapterUnit.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this AdapterUnit.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this AdapterUnit.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this AdapterUnit.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this AdapterUnit.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this AdapterUnit.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this AdapterUnit.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this AdapterUnit.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AdapterUnit.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this AdapterUnit.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this AdapterUnit.
        The versioning info for this managed object.

        :return: The version_context of this AdapterUnit.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this AdapterUnit.
        The versioning info for this managed object.

        :param version_context: The version_context of this AdapterUnit.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AdapterUnit.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this AdapterUnit.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AdapterUnit.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this AdapterUnit.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this AdapterUnit.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this AdapterUnit.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AdapterUnit.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this AdapterUnit.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this AdapterUnit.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this AdapterUnit.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this AdapterUnit.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this AdapterUnit.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this AdapterUnit.

        :return: The device_mo_id of this AdapterUnit.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this AdapterUnit.

        :param device_mo_id: The device_mo_id of this AdapterUnit.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this AdapterUnit.
        The Distinguished Name unambiguously identifies an object in the system.

        :return: The dn of this AdapterUnit.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this AdapterUnit.
        The Distinguished Name unambiguously identifies an object in the system.

        :param dn: The dn of this AdapterUnit.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this AdapterUnit.
        The Relative Name uniquely identifies an object within a given context.

        :return: The rn of this AdapterUnit.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this AdapterUnit.
        The Relative Name uniquely identifies an object within a given context.

        :param rn: The rn of this AdapterUnit.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this AdapterUnit.
        This field identifies the model of the given component.

        :return: The model of this AdapterUnit.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this AdapterUnit.
        This field identifies the model of the given component.

        :param model: The model of this AdapterUnit.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this AdapterUnit.

        :return: The revision of this AdapterUnit.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AdapterUnit.

        :param revision: The revision of this AdapterUnit.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this AdapterUnit.
        This field identifies the serial of the given component.

        :return: The serial of this AdapterUnit.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this AdapterUnit.
        This field identifies the serial of the given component.

        :param serial: The serial of this AdapterUnit.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this AdapterUnit.
        This field identifies the vendor of the given component.

        :return: The vendor of this AdapterUnit.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this AdapterUnit.
        This field identifies the vendor of the given component.

        :param vendor: The vendor of this AdapterUnit.
        :type: str
        """

        self._vendor = vendor

    @property
    def adapter_id(self):
        """
        Gets the adapter_id of this AdapterUnit.
        Unique Identifier of an adapter Unit within a Rack Interface.

        :return: The adapter_id of this AdapterUnit.
        :rtype: str
        """
        return self._adapter_id

    @adapter_id.setter
    def adapter_id(self, adapter_id):
        """
        Sets the adapter_id of this AdapterUnit.
        Unique Identifier of an adapter Unit within a Rack Interface.

        :param adapter_id: The adapter_id of this AdapterUnit.
        :type: str
        """

        self._adapter_id = adapter_id

    @property
    def base_mac_address(self):
        """
        Gets the base_mac_address of this AdapterUnit.

        :return: The base_mac_address of this AdapterUnit.
        :rtype: str
        """
        return self._base_mac_address

    @base_mac_address.setter
    def base_mac_address(self, base_mac_address):
        """
        Sets the base_mac_address of this AdapterUnit.

        :param base_mac_address: The base_mac_address of this AdapterUnit.
        :type: str
        """

        self._base_mac_address = base_mac_address

    @property
    def integrated(self):
        """
        Gets the integrated of this AdapterUnit.

        :return: The integrated of this AdapterUnit.
        :rtype: str
        """
        return self._integrated

    @integrated.setter
    def integrated(self, integrated):
        """
        Sets the integrated of this AdapterUnit.

        :param integrated: The integrated of this AdapterUnit.
        :type: str
        """

        self._integrated = integrated

    @property
    def oper_state(self):
        """
        Gets the oper_state of this AdapterUnit.

        :return: The oper_state of this AdapterUnit.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this AdapterUnit.

        :param oper_state: The oper_state of this AdapterUnit.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this AdapterUnit.

        :return: The operability of this AdapterUnit.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this AdapterUnit.

        :param operability: The operability of this AdapterUnit.
        :type: str
        """

        self._operability = operability

    @property
    def part_number(self):
        """
        Gets the part_number of this AdapterUnit.

        :return: The part_number of this AdapterUnit.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this AdapterUnit.

        :param part_number: The part_number of this AdapterUnit.
        :type: str
        """

        self._part_number = part_number

    @property
    def pci_slot(self):
        """
        Gets the pci_slot of this AdapterUnit.

        :return: The pci_slot of this AdapterUnit.
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """
        Sets the pci_slot of this AdapterUnit.

        :param pci_slot: The pci_slot of this AdapterUnit.
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def power(self):
        """
        Gets the power of this AdapterUnit.

        :return: The power of this AdapterUnit.
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """
        Sets the power of this AdapterUnit.

        :param power: The power of this AdapterUnit.
        :type: str
        """

        self._power = power

    @property
    def presence(self):
        """
        Gets the presence of this AdapterUnit.

        :return: The presence of this AdapterUnit.
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """
        Sets the presence of this AdapterUnit.

        :param presence: The presence of this AdapterUnit.
        :type: str
        """

        self._presence = presence

    @property
    def thermal(self):
        """
        Gets the thermal of this AdapterUnit.

        :return: The thermal of this AdapterUnit.
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """
        Sets the thermal of this AdapterUnit.

        :param thermal: The thermal of this AdapterUnit.
        :type: str
        """

        self._thermal = thermal

    @property
    def vid(self):
        """
        Gets the vid of this AdapterUnit.

        :return: The vid of this AdapterUnit.
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """
        Sets the vid of this AdapterUnit.

        :param vid: The vid of this AdapterUnit.
        :type: str
        """

        self._vid = vid

    @property
    def compute_blade(self):
        """
        Gets the compute_blade of this AdapterUnit.
        A collection of references to the [compute.Blade](mo://compute.Blade) Managed Object. When this managed object is deleted, the referenced [compute.Blade](mo://compute.Blade) MO unsets its reference to this deleted MO.

        :return: The compute_blade of this AdapterUnit.
        :rtype: ComputeBladeRef
        """
        return self._compute_blade

    @compute_blade.setter
    def compute_blade(self, compute_blade):
        """
        Sets the compute_blade of this AdapterUnit.
        A collection of references to the [compute.Blade](mo://compute.Blade) Managed Object. When this managed object is deleted, the referenced [compute.Blade](mo://compute.Blade) MO unsets its reference to this deleted MO.

        :param compute_blade: The compute_blade of this AdapterUnit.
        :type: ComputeBladeRef
        """

        self._compute_blade = compute_blade

    @property
    def compute_rack_unit(self):
        """
        Gets the compute_rack_unit of this AdapterUnit.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object. When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO.

        :return: The compute_rack_unit of this AdapterUnit.
        :rtype: ComputeRackUnitRef
        """
        return self._compute_rack_unit

    @compute_rack_unit.setter
    def compute_rack_unit(self, compute_rack_unit):
        """
        Sets the compute_rack_unit of this AdapterUnit.
        A collection of references to the [compute.RackUnit](mo://compute.RackUnit) Managed Object. When this managed object is deleted, the referenced [compute.RackUnit](mo://compute.RackUnit) MO unsets its reference to this deleted MO.

        :param compute_rack_unit: The compute_rack_unit of this AdapterUnit.
        :type: ComputeRackUnitRef
        """

        self._compute_rack_unit = compute_rack_unit

    @property
    def controller(self):
        """
        Gets the controller of this AdapterUnit.

        :return: The controller of this AdapterUnit.
        :rtype: ManagementControllerRef
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """
        Sets the controller of this AdapterUnit.

        :param controller: The controller of this AdapterUnit.
        :type: ManagementControllerRef
        """

        self._controller = controller

    @property
    def ext_eth_ifs(self):
        """
        Gets the ext_eth_ifs of this AdapterUnit.

        :return: The ext_eth_ifs of this AdapterUnit.
        :rtype: list[AdapterExtEthInterfaceRef]
        """
        return self._ext_eth_ifs

    @ext_eth_ifs.setter
    def ext_eth_ifs(self, ext_eth_ifs):
        """
        Sets the ext_eth_ifs of this AdapterUnit.

        :param ext_eth_ifs: The ext_eth_ifs of this AdapterUnit.
        :type: list[AdapterExtEthInterfaceRef]
        """

        self._ext_eth_ifs = ext_eth_ifs

    @property
    def host_eth_ifs(self):
        """
        Gets the host_eth_ifs of this AdapterUnit.

        :return: The host_eth_ifs of this AdapterUnit.
        :rtype: list[AdapterHostEthInterfaceRef]
        """
        return self._host_eth_ifs

    @host_eth_ifs.setter
    def host_eth_ifs(self, host_eth_ifs):
        """
        Sets the host_eth_ifs of this AdapterUnit.

        :param host_eth_ifs: The host_eth_ifs of this AdapterUnit.
        :type: list[AdapterHostEthInterfaceRef]
        """

        self._host_eth_ifs = host_eth_ifs

    @property
    def host_fc_ifs(self):
        """
        Gets the host_fc_ifs of this AdapterUnit.

        :return: The host_fc_ifs of this AdapterUnit.
        :rtype: list[AdapterHostFcInterfaceRef]
        """
        return self._host_fc_ifs

    @host_fc_ifs.setter
    def host_fc_ifs(self, host_fc_ifs):
        """
        Sets the host_fc_ifs of this AdapterUnit.

        :param host_fc_ifs: The host_fc_ifs of this AdapterUnit.
        :type: list[AdapterHostFcInterfaceRef]
        """

        self._host_fc_ifs = host_fc_ifs

    @property
    def host_iscsi_ifs(self):
        """
        Gets the host_iscsi_ifs of this AdapterUnit.

        :return: The host_iscsi_ifs of this AdapterUnit.
        :rtype: list[AdapterHostIscsiInterfaceRef]
        """
        return self._host_iscsi_ifs

    @host_iscsi_ifs.setter
    def host_iscsi_ifs(self, host_iscsi_ifs):
        """
        Sets the host_iscsi_ifs of this AdapterUnit.

        :param host_iscsi_ifs: The host_iscsi_ifs of this AdapterUnit.
        :type: list[AdapterHostIscsiInterfaceRef]
        """

        self._host_iscsi_ifs = host_iscsi_ifs

    @property
    def registered_device(self):
        """
        Gets the registered_device of this AdapterUnit.
        The Device to which this Managed Object is associated.

        :return: The registered_device of this AdapterUnit.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this AdapterUnit.
        The Device to which this Managed Object is associated.

        :param registered_device: The registered_device of this AdapterUnit.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, AdapterUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
