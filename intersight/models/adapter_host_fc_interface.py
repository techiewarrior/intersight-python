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


class AdapterHostFcInterface(object):
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
        'admin_state': 'str',
        'ep_dn': 'str',
        'host_fc_interface_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'original_wwnn': 'str',
        'original_wwpn': 'str',
        'peer_dn': 'str',
        'wwnn': 'str',
        'wwpn': 'str',
        'adapter_unit': 'AdapterUnitRef',
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
        'admin_state': 'AdminState',
        'ep_dn': 'EpDn',
        'host_fc_interface_id': 'HostFcInterfaceId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'original_wwnn': 'OriginalWwnn',
        'original_wwpn': 'OriginalWwpn',
        'peer_dn': 'PeerDn',
        'wwnn': 'Wwnn',
        'wwpn': 'Wwpn',
        'adapter_unit': 'AdapterUnit',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, admin_state=None, ep_dn=None, host_fc_interface_id=None, name=None, oper_state=None, operability=None, original_wwnn=None, original_wwpn=None, peer_dn=None, wwnn=None, wwpn=None, adapter_unit=None, registered_device=None):
        """
        AdapterHostFcInterface - a model defined in Swagger
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
        self._admin_state = None
        self._ep_dn = None
        self._host_fc_interface_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._original_wwnn = None
        self._original_wwpn = None
        self._peer_dn = None
        self._wwnn = None
        self._wwpn = None
        self._adapter_unit = None
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
        if admin_state is not None:
          self.admin_state = admin_state
        if ep_dn is not None:
          self.ep_dn = ep_dn
        if host_fc_interface_id is not None:
          self.host_fc_interface_id = host_fc_interface_id
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if original_wwnn is not None:
          self.original_wwnn = original_wwnn
        if original_wwpn is not None:
          self.original_wwpn = original_wwpn
        if peer_dn is not None:
          self.peer_dn = peer_dn
        if wwnn is not None:
          self.wwnn = wwnn
        if wwpn is not None:
          self.wwpn = wwpn
        if adapter_unit is not None:
          self.adapter_unit = adapter_unit
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AdapterHostFcInterface.
        The Account ID for this managed object.

        :return: The account_moid of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AdapterHostFcInterface.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this AdapterHostFcInterface.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this AdapterHostFcInterface.
        The time when this managed object was created.

        :return: The create_time of this AdapterHostFcInterface.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AdapterHostFcInterface.
        The time when this managed object was created.

        :param create_time: The create_time of this AdapterHostFcInterface.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this AdapterHostFcInterface.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this AdapterHostFcInterface.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this AdapterHostFcInterface.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AdapterHostFcInterface.
        The time when this managed object was last modified.

        :return: The mod_time of this AdapterHostFcInterface.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AdapterHostFcInterface.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this AdapterHostFcInterface.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AdapterHostFcInterface.
        The unique identifier of this Managed Object instance.

        :return: The moid of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AdapterHostFcInterface.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this AdapterHostFcInterface.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterHostFcInterface.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterHostFcInterface.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this AdapterHostFcInterface.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AdapterHostFcInterface.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this AdapterHostFcInterface.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AdapterHostFcInterface.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this AdapterHostFcInterface.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this AdapterHostFcInterface.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this AdapterHostFcInterface.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this AdapterHostFcInterface.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this AdapterHostFcInterface.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this AdapterHostFcInterface.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AdapterHostFcInterface.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this AdapterHostFcInterface.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this AdapterHostFcInterface.
        The versioning info for this managed object.

        :return: The version_context of this AdapterHostFcInterface.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this AdapterHostFcInterface.
        The versioning info for this managed object.

        :param version_context: The version_context of this AdapterHostFcInterface.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AdapterHostFcInterface.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this AdapterHostFcInterface.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AdapterHostFcInterface.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this AdapterHostFcInterface.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this AdapterHostFcInterface.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this AdapterHostFcInterface.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AdapterHostFcInterface.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this AdapterHostFcInterface.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this AdapterHostFcInterface.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this AdapterHostFcInterface.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this AdapterHostFcInterface.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this AdapterHostFcInterface.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this AdapterHostFcInterface.

        :return: The device_mo_id of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this AdapterHostFcInterface.

        :param device_mo_id: The device_mo_id of this AdapterHostFcInterface.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this AdapterHostFcInterface.
        The Distinguished Name unambiguously identifies an object in the system.

        :return: The dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this AdapterHostFcInterface.
        The Distinguished Name unambiguously identifies an object in the system.

        :param dn: The dn of this AdapterHostFcInterface.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this AdapterHostFcInterface.
        The Relative Name uniquely identifies an object within a given context.

        :return: The rn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this AdapterHostFcInterface.
        The Relative Name uniquely identifies an object within a given context.

        :param rn: The rn of this AdapterHostFcInterface.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this AdapterHostFcInterface.
        This field identifies the model of the given component.

        :return: The model of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this AdapterHostFcInterface.
        This field identifies the model of the given component.

        :param model: The model of this AdapterHostFcInterface.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this AdapterHostFcInterface.

        :return: The revision of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AdapterHostFcInterface.

        :param revision: The revision of this AdapterHostFcInterface.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this AdapterHostFcInterface.
        This field identifies the serial of the given component.

        :return: The serial of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this AdapterHostFcInterface.
        This field identifies the serial of the given component.

        :param serial: The serial of this AdapterHostFcInterface.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this AdapterHostFcInterface.
        This field identifies the vendor of the given component.

        :return: The vendor of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this AdapterHostFcInterface.
        This field identifies the vendor of the given component.

        :param vendor: The vendor of this AdapterHostFcInterface.
        :type: str
        """

        self._vendor = vendor

    @property
    def admin_state(self):
        """
        Gets the admin_state of this AdapterHostFcInterface.

        :return: The admin_state of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this AdapterHostFcInterface.

        :param admin_state: The admin_state of this AdapterHostFcInterface.
        :type: str
        """

        self._admin_state = admin_state

    @property
    def ep_dn(self):
        """
        Gets the ep_dn of this AdapterHostFcInterface.

        :return: The ep_dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._ep_dn

    @ep_dn.setter
    def ep_dn(self, ep_dn):
        """
        Sets the ep_dn of this AdapterHostFcInterface.

        :param ep_dn: The ep_dn of this AdapterHostFcInterface.
        :type: str
        """

        self._ep_dn = ep_dn

    @property
    def host_fc_interface_id(self):
        """
        Gets the host_fc_interface_id of this AdapterHostFcInterface.

        :return: The host_fc_interface_id of this AdapterHostFcInterface.
        :rtype: int
        """
        return self._host_fc_interface_id

    @host_fc_interface_id.setter
    def host_fc_interface_id(self, host_fc_interface_id):
        """
        Sets the host_fc_interface_id of this AdapterHostFcInterface.

        :param host_fc_interface_id: The host_fc_interface_id of this AdapterHostFcInterface.
        :type: int
        """

        self._host_fc_interface_id = host_fc_interface_id

    @property
    def name(self):
        """
        Gets the name of this AdapterHostFcInterface.

        :return: The name of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AdapterHostFcInterface.

        :param name: The name of this AdapterHostFcInterface.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this AdapterHostFcInterface.

        :return: The oper_state of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this AdapterHostFcInterface.

        :param oper_state: The oper_state of this AdapterHostFcInterface.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this AdapterHostFcInterface.

        :return: The operability of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this AdapterHostFcInterface.

        :param operability: The operability of this AdapterHostFcInterface.
        :type: str
        """

        self._operability = operability

    @property
    def original_wwnn(self):
        """
        Gets the original_wwnn of this AdapterHostFcInterface.

        :return: The original_wwnn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._original_wwnn

    @original_wwnn.setter
    def original_wwnn(self, original_wwnn):
        """
        Sets the original_wwnn of this AdapterHostFcInterface.

        :param original_wwnn: The original_wwnn of this AdapterHostFcInterface.
        :type: str
        """

        self._original_wwnn = original_wwnn

    @property
    def original_wwpn(self):
        """
        Gets the original_wwpn of this AdapterHostFcInterface.

        :return: The original_wwpn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._original_wwpn

    @original_wwpn.setter
    def original_wwpn(self, original_wwpn):
        """
        Sets the original_wwpn of this AdapterHostFcInterface.

        :param original_wwpn: The original_wwpn of this AdapterHostFcInterface.
        :type: str
        """

        self._original_wwpn = original_wwpn

    @property
    def peer_dn(self):
        """
        Gets the peer_dn of this AdapterHostFcInterface.

        :return: The peer_dn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._peer_dn

    @peer_dn.setter
    def peer_dn(self, peer_dn):
        """
        Sets the peer_dn of this AdapterHostFcInterface.

        :param peer_dn: The peer_dn of this AdapterHostFcInterface.
        :type: str
        """

        self._peer_dn = peer_dn

    @property
    def wwnn(self):
        """
        Gets the wwnn of this AdapterHostFcInterface.

        :return: The wwnn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """
        Sets the wwnn of this AdapterHostFcInterface.

        :param wwnn: The wwnn of this AdapterHostFcInterface.
        :type: str
        """

        self._wwnn = wwnn

    @property
    def wwpn(self):
        """
        Gets the wwpn of this AdapterHostFcInterface.

        :return: The wwpn of this AdapterHostFcInterface.
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """
        Sets the wwpn of this AdapterHostFcInterface.

        :param wwpn: The wwpn of this AdapterHostFcInterface.
        :type: str
        """

        self._wwpn = wwpn

    @property
    def adapter_unit(self):
        """
        Gets the adapter_unit of this AdapterHostFcInterface.
        A collection of references to the [adapter.Unit](mo://adapter.Unit) Managed Object. When this managed object is deleted, the referenced [adapter.Unit](mo://adapter.Unit) MO unsets its reference to this deleted MO.

        :return: The adapter_unit of this AdapterHostFcInterface.
        :rtype: AdapterUnitRef
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """
        Sets the adapter_unit of this AdapterHostFcInterface.
        A collection of references to the [adapter.Unit](mo://adapter.Unit) Managed Object. When this managed object is deleted, the referenced [adapter.Unit](mo://adapter.Unit) MO unsets its reference to this deleted MO.

        :param adapter_unit: The adapter_unit of this AdapterHostFcInterface.
        :type: AdapterUnitRef
        """

        self._adapter_unit = adapter_unit

    @property
    def registered_device(self):
        """
        Gets the registered_device of this AdapterHostFcInterface.
        The Device to which this Managed Object is associated.

        :return: The registered_device of this AdapterHostFcInterface.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this AdapterHostFcInterface.
        The Device to which this Managed Object is associated.

        :param registered_device: The registered_device of this AdapterHostFcInterface.
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
        if not isinstance(other, AdapterHostFcInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
