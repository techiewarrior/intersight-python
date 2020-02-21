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


class NetworkElement(object):
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
        'tags': 'list[MoOptionalTag]',
        'version_context': 'MoOptionalVersionContext',
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
        'admin_inband_interface_state': 'str',
        'fault_summary': 'int',
        'inband_ip_address': 'str',
        'inband_ip_gateway': 'str',
        'inband_ip_mask': 'str',
        'inband_vlan': 'int',
        'out_of_band_ip_address': 'str',
        'out_of_band_ip_gateway': 'str',
        'out_of_band_ip_mask': 'str',
        'out_of_band_mac': 'str',
        'switch_id': 'str',
        'cards': 'list[EquipmentSwitchCardRef]',
        'fanmodules': 'list[EquipmentFanModuleRef]',
        'management_contoller': 'ManagementControllerRef',
        'management_entity': 'ManagementEntityRef',
        'psus': 'list[EquipmentPsuRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'top_system': 'TopSystemRef',
        'ucsm_running_firmware': 'FirmwareRunningFirmwareRef'
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
        'admin_inband_interface_state': 'AdminInbandInterfaceState',
        'fault_summary': 'FaultSummary',
        'inband_ip_address': 'InbandIpAddress',
        'inband_ip_gateway': 'InbandIpGateway',
        'inband_ip_mask': 'InbandIpMask',
        'inband_vlan': 'InbandVlan',
        'out_of_band_ip_address': 'OutOfBandIpAddress',
        'out_of_band_ip_gateway': 'OutOfBandIpGateway',
        'out_of_band_ip_mask': 'OutOfBandIpMask',
        'out_of_band_mac': 'OutOfBandMac',
        'switch_id': 'SwitchId',
        'cards': 'Cards',
        'fanmodules': 'Fanmodules',
        'management_contoller': 'ManagementContoller',
        'management_entity': 'ManagementEntity',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'top_system': 'TopSystem',
        'ucsm_running_firmware': 'UcsmRunningFirmware'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, admin_inband_interface_state=None, fault_summary=None, inband_ip_address=None, inband_ip_gateway=None, inband_ip_mask=None, inband_vlan=None, out_of_band_ip_address=None, out_of_band_ip_gateway=None, out_of_band_ip_mask=None, out_of_band_mac=None, switch_id=None, cards=None, fanmodules=None, management_contoller=None, management_entity=None, psus=None, registered_device=None, top_system=None, ucsm_running_firmware=None):
        """
        NetworkElement - a model defined in Swagger
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
        self._admin_inband_interface_state = None
        self._fault_summary = None
        self._inband_ip_address = None
        self._inband_ip_gateway = None
        self._inband_ip_mask = None
        self._inband_vlan = None
        self._out_of_band_ip_address = None
        self._out_of_band_ip_gateway = None
        self._out_of_band_ip_mask = None
        self._out_of_band_mac = None
        self._switch_id = None
        self._cards = None
        self._fanmodules = None
        self._management_contoller = None
        self._management_entity = None
        self._psus = None
        self._registered_device = None
        self._top_system = None
        self._ucsm_running_firmware = None

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
        if admin_inband_interface_state is not None:
          self.admin_inband_interface_state = admin_inband_interface_state
        if fault_summary is not None:
          self.fault_summary = fault_summary
        if inband_ip_address is not None:
          self.inband_ip_address = inband_ip_address
        if inband_ip_gateway is not None:
          self.inband_ip_gateway = inband_ip_gateway
        if inband_ip_mask is not None:
          self.inband_ip_mask = inband_ip_mask
        if inband_vlan is not None:
          self.inband_vlan = inband_vlan
        if out_of_band_ip_address is not None:
          self.out_of_band_ip_address = out_of_band_ip_address
        if out_of_band_ip_gateway is not None:
          self.out_of_band_ip_gateway = out_of_band_ip_gateway
        if out_of_band_ip_mask is not None:
          self.out_of_band_ip_mask = out_of_band_ip_mask
        if out_of_band_mac is not None:
          self.out_of_band_mac = out_of_band_mac
        if switch_id is not None:
          self.switch_id = switch_id
        if cards is not None:
          self.cards = cards
        if fanmodules is not None:
          self.fanmodules = fanmodules
        if management_contoller is not None:
          self.management_contoller = management_contoller
        if management_entity is not None:
          self.management_entity = management_entity
        if psus is not None:
          self.psus = psus
        if registered_device is not None:
          self.registered_device = registered_device
        if top_system is not None:
          self.top_system = top_system
        if ucsm_running_firmware is not None:
          self.ucsm_running_firmware = ucsm_running_firmware

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NetworkElement.
        The Account ID for this managed object.  

        :return: The account_moid of this NetworkElement.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NetworkElement.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NetworkElement.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this NetworkElement.
        The time when this managed object was created.  

        :return: The create_time of this NetworkElement.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NetworkElement.
        The time when this managed object was created.  

        :param create_time: The create_time of this NetworkElement.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NetworkElement.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NetworkElement.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NetworkElement.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NetworkElement.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NetworkElement.
        The time when this managed object was last modified.  

        :return: The mod_time of this NetworkElement.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NetworkElement.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NetworkElement.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NetworkElement.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this NetworkElement.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NetworkElement.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this NetworkElement.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NetworkElement.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this NetworkElement.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NetworkElement.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this NetworkElement.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NetworkElement.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NetworkElement.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NetworkElement.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NetworkElement.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NetworkElement.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NetworkElement.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NetworkElement.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NetworkElement.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NetworkElement.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this NetworkElement.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NetworkElement.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this NetworkElement.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NetworkElement.
        The versioning info for this managed object.   

        :return: The version_context of this NetworkElement.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NetworkElement.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NetworkElement.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NetworkElement.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NetworkElement.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NetworkElement.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NetworkElement.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this NetworkElement.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NetworkElement.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NetworkElement.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NetworkElement.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this NetworkElement.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this NetworkElement.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this NetworkElement.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this NetworkElement.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this NetworkElement.

        :return: The device_mo_id of this NetworkElement.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this NetworkElement.

        :param device_mo_id: The device_mo_id of this NetworkElement.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this NetworkElement.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this NetworkElement.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this NetworkElement.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this NetworkElement.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this NetworkElement.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this NetworkElement.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this NetworkElement.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this NetworkElement.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this NetworkElement.
        This field identifies the model of the given component.  

        :return: The model of this NetworkElement.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this NetworkElement.
        This field identifies the model of the given component.  

        :param model: The model of this NetworkElement.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this NetworkElement.

        :return: The revision of this NetworkElement.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this NetworkElement.

        :param revision: The revision of this NetworkElement.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this NetworkElement.
        This field identifies the serial of the given component.  

        :return: The serial of this NetworkElement.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this NetworkElement.
        This field identifies the serial of the given component.  

        :param serial: The serial of this NetworkElement.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this NetworkElement.
        This field identifies the vendor of the given component.   

        :return: The vendor of this NetworkElement.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this NetworkElement.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this NetworkElement.
        :type: str
        """

        self._vendor = vendor

    @property
    def admin_inband_interface_state(self):
        """
        Gets the admin_inband_interface_state of this NetworkElement.
        The administrative state of the network Element inband management interface.  

        :return: The admin_inband_interface_state of this NetworkElement.
        :rtype: str
        """
        return self._admin_inband_interface_state

    @admin_inband_interface_state.setter
    def admin_inband_interface_state(self, admin_inband_interface_state):
        """
        Sets the admin_inband_interface_state of this NetworkElement.
        The administrative state of the network Element inband management interface.  

        :param admin_inband_interface_state: The admin_inband_interface_state of this NetworkElement.
        :type: str
        """

        self._admin_inband_interface_state = admin_inband_interface_state

    @property
    def fault_summary(self):
        """
        Gets the fault_summary of this NetworkElement.

        :return: The fault_summary of this NetworkElement.
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """
        Sets the fault_summary of this NetworkElement.

        :param fault_summary: The fault_summary of this NetworkElement.
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def inband_ip_address(self):
        """
        Gets the inband_ip_address of this NetworkElement.
        The IP address of the network Element inband management interface.  

        :return: The inband_ip_address of this NetworkElement.
        :rtype: str
        """
        return self._inband_ip_address

    @inband_ip_address.setter
    def inband_ip_address(self, inband_ip_address):
        """
        Sets the inband_ip_address of this NetworkElement.
        The IP address of the network Element inband management interface.  

        :param inband_ip_address: The inband_ip_address of this NetworkElement.
        :type: str
        """

        self._inband_ip_address = inband_ip_address

    @property
    def inband_ip_gateway(self):
        """
        Gets the inband_ip_gateway of this NetworkElement.
        The default gateway of the network Element inband management interface.  

        :return: The inband_ip_gateway of this NetworkElement.
        :rtype: str
        """
        return self._inband_ip_gateway

    @inband_ip_gateway.setter
    def inband_ip_gateway(self, inband_ip_gateway):
        """
        Sets the inband_ip_gateway of this NetworkElement.
        The default gateway of the network Element inband management interface.  

        :param inband_ip_gateway: The inband_ip_gateway of this NetworkElement.
        :type: str
        """

        self._inband_ip_gateway = inband_ip_gateway

    @property
    def inband_ip_mask(self):
        """
        Gets the inband_ip_mask of this NetworkElement.
        The network mask of the network Element inband management interface.  

        :return: The inband_ip_mask of this NetworkElement.
        :rtype: str
        """
        return self._inband_ip_mask

    @inband_ip_mask.setter
    def inband_ip_mask(self, inband_ip_mask):
        """
        Sets the inband_ip_mask of this NetworkElement.
        The network mask of the network Element inband management interface.  

        :param inband_ip_mask: The inband_ip_mask of this NetworkElement.
        :type: str
        """

        self._inband_ip_mask = inband_ip_mask

    @property
    def inband_vlan(self):
        """
        Gets the inband_vlan of this NetworkElement.
        The VLAN ID of the network Element inband management interface.  

        :return: The inband_vlan of this NetworkElement.
        :rtype: int
        """
        return self._inband_vlan

    @inband_vlan.setter
    def inband_vlan(self, inband_vlan):
        """
        Sets the inband_vlan of this NetworkElement.
        The VLAN ID of the network Element inband management interface.  

        :param inband_vlan: The inband_vlan of this NetworkElement.
        :type: int
        """

        self._inband_vlan = inband_vlan

    @property
    def out_of_band_ip_address(self):
        """
        Gets the out_of_band_ip_address of this NetworkElement.
        The IP address of the network Element out-of-band management interface.  

        :return: The out_of_band_ip_address of this NetworkElement.
        :rtype: str
        """
        return self._out_of_band_ip_address

    @out_of_band_ip_address.setter
    def out_of_band_ip_address(self, out_of_band_ip_address):
        """
        Sets the out_of_band_ip_address of this NetworkElement.
        The IP address of the network Element out-of-band management interface.  

        :param out_of_band_ip_address: The out_of_band_ip_address of this NetworkElement.
        :type: str
        """

        self._out_of_band_ip_address = out_of_band_ip_address

    @property
    def out_of_band_ip_gateway(self):
        """
        Gets the out_of_band_ip_gateway of this NetworkElement.
        The default gateway of the network Element out-of-band management interface.  

        :return: The out_of_band_ip_gateway of this NetworkElement.
        :rtype: str
        """
        return self._out_of_band_ip_gateway

    @out_of_band_ip_gateway.setter
    def out_of_band_ip_gateway(self, out_of_band_ip_gateway):
        """
        Sets the out_of_band_ip_gateway of this NetworkElement.
        The default gateway of the network Element out-of-band management interface.  

        :param out_of_band_ip_gateway: The out_of_band_ip_gateway of this NetworkElement.
        :type: str
        """

        self._out_of_band_ip_gateway = out_of_band_ip_gateway

    @property
    def out_of_band_ip_mask(self):
        """
        Gets the out_of_band_ip_mask of this NetworkElement.
        The network mask of the network Element out-of-band management interface.  

        :return: The out_of_band_ip_mask of this NetworkElement.
        :rtype: str
        """
        return self._out_of_band_ip_mask

    @out_of_band_ip_mask.setter
    def out_of_band_ip_mask(self, out_of_band_ip_mask):
        """
        Sets the out_of_band_ip_mask of this NetworkElement.
        The network mask of the network Element out-of-band management interface.  

        :param out_of_band_ip_mask: The out_of_band_ip_mask of this NetworkElement.
        :type: str
        """

        self._out_of_band_ip_mask = out_of_band_ip_mask

    @property
    def out_of_band_mac(self):
        """
        Gets the out_of_band_mac of this NetworkElement.
        The MAC address of the network Element out-of-band management interface.  

        :return: The out_of_band_mac of this NetworkElement.
        :rtype: str
        """
        return self._out_of_band_mac

    @out_of_band_mac.setter
    def out_of_band_mac(self, out_of_band_mac):
        """
        Sets the out_of_band_mac of this NetworkElement.
        The MAC address of the network Element out-of-band management interface.  

        :param out_of_band_mac: The out_of_band_mac of this NetworkElement.
        :type: str
        """

        self._out_of_band_mac = out_of_band_mac

    @property
    def switch_id(self):
        """
        Gets the switch_id of this NetworkElement.
        The Switch Id of the network Element.   

        :return: The switch_id of this NetworkElement.
        :rtype: str
        """
        return self._switch_id

    @switch_id.setter
    def switch_id(self, switch_id):
        """
        Sets the switch_id of this NetworkElement.
        The Switch Id of the network Element.   

        :param switch_id: The switch_id of this NetworkElement.
        :type: str
        """

        self._switch_id = switch_id

    @property
    def cards(self):
        """
        Gets the cards of this NetworkElement.

        :return: The cards of this NetworkElement.
        :rtype: list[EquipmentSwitchCardRef]
        """
        return self._cards

    @cards.setter
    def cards(self, cards):
        """
        Sets the cards of this NetworkElement.

        :param cards: The cards of this NetworkElement.
        :type: list[EquipmentSwitchCardRef]
        """

        self._cards = cards

    @property
    def fanmodules(self):
        """
        Gets the fanmodules of this NetworkElement.

        :return: The fanmodules of this NetworkElement.
        :rtype: list[EquipmentFanModuleRef]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """
        Sets the fanmodules of this NetworkElement.

        :param fanmodules: The fanmodules of this NetworkElement.
        :type: list[EquipmentFanModuleRef]
        """

        self._fanmodules = fanmodules

    @property
    def management_contoller(self):
        """
        Gets the management_contoller of this NetworkElement.

        :return: The management_contoller of this NetworkElement.
        :rtype: ManagementControllerRef
        """
        return self._management_contoller

    @management_contoller.setter
    def management_contoller(self, management_contoller):
        """
        Sets the management_contoller of this NetworkElement.

        :param management_contoller: The management_contoller of this NetworkElement.
        :type: ManagementControllerRef
        """

        self._management_contoller = management_contoller

    @property
    def management_entity(self):
        """
        Gets the management_entity of this NetworkElement.

        :return: The management_entity of this NetworkElement.
        :rtype: ManagementEntityRef
        """
        return self._management_entity

    @management_entity.setter
    def management_entity(self, management_entity):
        """
        Sets the management_entity of this NetworkElement.

        :param management_entity: The management_entity of this NetworkElement.
        :type: ManagementEntityRef
        """

        self._management_entity = management_entity

    @property
    def psus(self):
        """
        Gets the psus of this NetworkElement.

        :return: The psus of this NetworkElement.
        :rtype: list[EquipmentPsuRef]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """
        Sets the psus of this NetworkElement.

        :param psus: The psus of this NetworkElement.
        :type: list[EquipmentPsuRef]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """
        Gets the registered_device of this NetworkElement.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this NetworkElement.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this NetworkElement.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this NetworkElement.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def top_system(self):
        """
        Gets the top_system of this NetworkElement.
        A collection of references to the [top.System](mo://top.System) Managed Object.  When this managed object is deleted, the referenced [top.System](mo://top.System) MO unsets its reference to this deleted MO. 

        :return: The top_system of this NetworkElement.
        :rtype: TopSystemRef
        """
        return self._top_system

    @top_system.setter
    def top_system(self, top_system):
        """
        Sets the top_system of this NetworkElement.
        A collection of references to the [top.System](mo://top.System) Managed Object.  When this managed object is deleted, the referenced [top.System](mo://top.System) MO unsets its reference to this deleted MO. 

        :param top_system: The top_system of this NetworkElement.
        :type: TopSystemRef
        """

        self._top_system = top_system

    @property
    def ucsm_running_firmware(self):
        """
        Gets the ucsm_running_firmware of this NetworkElement.
        A collection of references to the [firmware.RunningFirmware](mo://firmware.RunningFirmware) Managed Object.  When this managed object is deleted, the referenced [firmware.RunningFirmware](mo://firmware.RunningFirmware) MO unsets its reference to this deleted MO. 

        :return: The ucsm_running_firmware of this NetworkElement.
        :rtype: FirmwareRunningFirmwareRef
        """
        return self._ucsm_running_firmware

    @ucsm_running_firmware.setter
    def ucsm_running_firmware(self, ucsm_running_firmware):
        """
        Sets the ucsm_running_firmware of this NetworkElement.
        A collection of references to the [firmware.RunningFirmware](mo://firmware.RunningFirmware) Managed Object.  When this managed object is deleted, the referenced [firmware.RunningFirmware](mo://firmware.RunningFirmware) MO unsets its reference to this deleted MO. 

        :param ucsm_running_firmware: The ucsm_running_firmware of this NetworkElement.
        :type: FirmwareRunningFirmwareRef
        """

        self._ucsm_running_firmware = ucsm_running_firmware

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
        if not isinstance(other, NetworkElement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
