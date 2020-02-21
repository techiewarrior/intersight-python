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


class EquipmentSystemIoController(object):
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
        'chassis_id': 'str',
        'connection_path': 'str',
        'connection_status': 'str',
        'description': 'str',
        'managing_instance': 'str',
        'oper_state': 'str',
        'part_number': 'str',
        'pid': 'str',
        'system_io_controller_id': 'int',
        'equipment_chassis': 'EquipmentChassisRef',
        'registered_device': 'AssetDeviceRegistrationRef',
        'shared_io_module': 'EquipmentSharedIoModuleRef'
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
        'chassis_id': 'ChassisId',
        'connection_path': 'ConnectionPath',
        'connection_status': 'ConnectionStatus',
        'description': 'Description',
        'managing_instance': 'ManagingInstance',
        'oper_state': 'OperState',
        'part_number': 'PartNumber',
        'pid': 'Pid',
        'system_io_controller_id': 'SystemIoControllerId',
        'equipment_chassis': 'EquipmentChassis',
        'registered_device': 'RegisteredDevice',
        'shared_io_module': 'SharedIoModule'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, chassis_id=None, connection_path=None, connection_status=None, description=None, managing_instance=None, oper_state=None, part_number=None, pid=None, system_io_controller_id=None, equipment_chassis=None, registered_device=None, shared_io_module=None):
        """
        EquipmentSystemIoController - a model defined in Swagger
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
        self._chassis_id = None
        self._connection_path = None
        self._connection_status = None
        self._description = None
        self._managing_instance = None
        self._oper_state = None
        self._part_number = None
        self._pid = None
        self._system_io_controller_id = None
        self._equipment_chassis = None
        self._registered_device = None
        self._shared_io_module = None

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
        if chassis_id is not None:
          self.chassis_id = chassis_id
        if connection_path is not None:
          self.connection_path = connection_path
        if connection_status is not None:
          self.connection_status = connection_status
        if description is not None:
          self.description = description
        if managing_instance is not None:
          self.managing_instance = managing_instance
        if oper_state is not None:
          self.oper_state = oper_state
        if part_number is not None:
          self.part_number = part_number
        if pid is not None:
          self.pid = pid
        if system_io_controller_id is not None:
          self.system_io_controller_id = system_io_controller_id
        if equipment_chassis is not None:
          self.equipment_chassis = equipment_chassis
        if registered_device is not None:
          self.registered_device = registered_device
        if shared_io_module is not None:
          self.shared_io_module = shared_io_module

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EquipmentSystemIoController.
        The Account ID for this managed object.  

        :return: The account_moid of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EquipmentSystemIoController.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EquipmentSystemIoController.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this EquipmentSystemIoController.
        The time when this managed object was created.  

        :return: The create_time of this EquipmentSystemIoController.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EquipmentSystemIoController.
        The time when this managed object was created.  

        :param create_time: The create_time of this EquipmentSystemIoController.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this EquipmentSystemIoController.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this EquipmentSystemIoController.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this EquipmentSystemIoController.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EquipmentSystemIoController.
        The time when this managed object was last modified.  

        :return: The mod_time of this EquipmentSystemIoController.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EquipmentSystemIoController.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EquipmentSystemIoController.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EquipmentSystemIoController.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EquipmentSystemIoController.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this EquipmentSystemIoController.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EquipmentSystemIoController.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EquipmentSystemIoController.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this EquipmentSystemIoController.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EquipmentSystemIoController.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this EquipmentSystemIoController.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EquipmentSystemIoController.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EquipmentSystemIoController.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this EquipmentSystemIoController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this EquipmentSystemIoController.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this EquipmentSystemIoController.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this EquipmentSystemIoController.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this EquipmentSystemIoController.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EquipmentSystemIoController.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this EquipmentSystemIoController.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EquipmentSystemIoController.
        The versioning info for this managed object.   

        :return: The version_context of this EquipmentSystemIoController.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EquipmentSystemIoController.
        The versioning info for this managed object.   

        :param version_context: The version_context of this EquipmentSystemIoController.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EquipmentSystemIoController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EquipmentSystemIoController.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EquipmentSystemIoController.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EquipmentSystemIoController.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this EquipmentSystemIoController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EquipmentSystemIoController.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EquipmentSystemIoController.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EquipmentSystemIoController.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this EquipmentSystemIoController.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this EquipmentSystemIoController.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this EquipmentSystemIoController.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this EquipmentSystemIoController.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EquipmentSystemIoController.

        :return: The device_mo_id of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EquipmentSystemIoController.

        :param device_mo_id: The device_mo_id of this EquipmentSystemIoController.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EquipmentSystemIoController.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EquipmentSystemIoController.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this EquipmentSystemIoController.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EquipmentSystemIoController.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EquipmentSystemIoController.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this EquipmentSystemIoController.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this EquipmentSystemIoController.
        This field identifies the model of the given component.  

        :return: The model of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this EquipmentSystemIoController.
        This field identifies the model of the given component.  

        :param model: The model of this EquipmentSystemIoController.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this EquipmentSystemIoController.

        :return: The revision of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this EquipmentSystemIoController.

        :param revision: The revision of this EquipmentSystemIoController.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this EquipmentSystemIoController.
        This field identifies the serial of the given component.  

        :return: The serial of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this EquipmentSystemIoController.
        This field identifies the serial of the given component.  

        :param serial: The serial of this EquipmentSystemIoController.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this EquipmentSystemIoController.
        This field identifies the vendor of the given component.   

        :return: The vendor of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this EquipmentSystemIoController.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this EquipmentSystemIoController.
        :type: str
        """

        self._vendor = vendor

    @property
    def chassis_id(self):
        """
        Gets the chassis_id of this EquipmentSystemIoController.
        The assigned identifier for a chassis.  

        :return: The chassis_id of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """
        Sets the chassis_id of this EquipmentSystemIoController.
        The assigned identifier for a chassis.  

        :param chassis_id: The chassis_id of this EquipmentSystemIoController.
        :type: str
        """

        self._chassis_id = chassis_id

    @property
    def connection_path(self):
        """
        Gets the connection_path of this EquipmentSystemIoController.
        Connection Path identifies the data path available between IOModule and FI.  

        :return: The connection_path of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._connection_path

    @connection_path.setter
    def connection_path(self, connection_path):
        """
        Sets the connection_path of this EquipmentSystemIoController.
        Connection Path identifies the data path available between IOModule and FI.  

        :param connection_path: The connection_path of this EquipmentSystemIoController.
        :type: str
        """

        self._connection_path = connection_path

    @property
    def connection_status(self):
        """
        Gets the connection_status of this EquipmentSystemIoController.
        Connection status identifies the status of data path.  

        :return: The connection_status of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this EquipmentSystemIoController.
        Connection status identifies the status of data path.  

        :param connection_status: The connection_status of this EquipmentSystemIoController.
        :type: str
        """

        self._connection_status = connection_status

    @property
    def description(self):
        """
        Gets the description of this EquipmentSystemIoController.
        This field gives a brief information on systemIOController.  

        :return: The description of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EquipmentSystemIoController.
        This field gives a brief information on systemIOController.  

        :param description: The description of this EquipmentSystemIoController.
        :type: str
        """

        self._description = description

    @property
    def managing_instance(self):
        """
        Gets the managing_instance of this EquipmentSystemIoController.
        This field identifies the CIMC that manages the controller.  

        :return: The managing_instance of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._managing_instance

    @managing_instance.setter
    def managing_instance(self, managing_instance):
        """
        Sets the managing_instance of this EquipmentSystemIoController.
        This field identifies the CIMC that manages the controller.  

        :param managing_instance: The managing_instance of this EquipmentSystemIoController.
        :type: str
        """

        self._managing_instance = managing_instance

    @property
    def oper_state(self):
        """
        Gets the oper_state of this EquipmentSystemIoController.
        This field identifies the SIOC operational state.  

        :return: The oper_state of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this EquipmentSystemIoController.
        This field identifies the SIOC operational state.  

        :param oper_state: The oper_state of this EquipmentSystemIoController.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def part_number(self):
        """
        Gets the part_number of this EquipmentSystemIoController.
        Part Number identifier for the IO module.  

        :return: The part_number of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this EquipmentSystemIoController.
        Part Number identifier for the IO module.  

        :param part_number: The part_number of this EquipmentSystemIoController.
        :type: str
        """

        self._part_number = part_number

    @property
    def pid(self):
        """
        Gets the pid of this EquipmentSystemIoController.
        This field identifies the Product ID for systemIOController.  

        :return: The pid of this EquipmentSystemIoController.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this EquipmentSystemIoController.
        This field identifies the Product ID for systemIOController.  

        :param pid: The pid of this EquipmentSystemIoController.
        :type: str
        """

        self._pid = pid

    @property
    def system_io_controller_id(self):
        """
        Gets the system_io_controller_id of this EquipmentSystemIoController.
        This represents system I/O Controller identifier.   

        :return: The system_io_controller_id of this EquipmentSystemIoController.
        :rtype: int
        """
        return self._system_io_controller_id

    @system_io_controller_id.setter
    def system_io_controller_id(self, system_io_controller_id):
        """
        Sets the system_io_controller_id of this EquipmentSystemIoController.
        This represents system I/O Controller identifier.   

        :param system_io_controller_id: The system_io_controller_id of this EquipmentSystemIoController.
        :type: int
        """

        self._system_io_controller_id = system_io_controller_id

    @property
    def equipment_chassis(self):
        """
        Gets the equipment_chassis of this EquipmentSystemIoController.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :return: The equipment_chassis of this EquipmentSystemIoController.
        :rtype: EquipmentChassisRef
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """
        Sets the equipment_chassis of this EquipmentSystemIoController.
        A collection of references to the [equipment.Chassis](mo://equipment.Chassis) Managed Object.  When this managed object is deleted, the referenced [equipment.Chassis](mo://equipment.Chassis) MO unsets its reference to this deleted MO. 

        :param equipment_chassis: The equipment_chassis of this EquipmentSystemIoController.
        :type: EquipmentChassisRef
        """

        self._equipment_chassis = equipment_chassis

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EquipmentSystemIoController.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this EquipmentSystemIoController.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EquipmentSystemIoController.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this EquipmentSystemIoController.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def shared_io_module(self):
        """
        Gets the shared_io_module of this EquipmentSystemIoController.
        This represents the adaptor housed in system I/O controller. 

        :return: The shared_io_module of this EquipmentSystemIoController.
        :rtype: EquipmentSharedIoModuleRef
        """
        return self._shared_io_module

    @shared_io_module.setter
    def shared_io_module(self, shared_io_module):
        """
        Sets the shared_io_module of this EquipmentSystemIoController.
        This represents the adaptor housed in system I/O controller. 

        :param shared_io_module: The shared_io_module of this EquipmentSystemIoController.
        :type: EquipmentSharedIoModuleRef
        """

        self._shared_io_module = shared_io_module

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
        if not isinstance(other, EquipmentSystemIoController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
