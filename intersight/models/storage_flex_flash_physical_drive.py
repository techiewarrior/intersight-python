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


class StorageFlexFlashPhysicalDrive(object):
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
        'card_status': 'str',
        'card_type': 'str',
        'oem_id': 'str',
        'pd_status': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'storage_flex_flash_controller': 'StorageFlexFlashControllerRef'
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
        'card_status': 'CardStatus',
        'card_type': 'CardType',
        'oem_id': 'OemId',
        'pd_status': 'PdStatus',
        'registered_device': 'RegisteredDevice',
        'storage_flex_flash_controller': 'StorageFlexFlashController'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, card_status=None, card_type=None, oem_id=None, pd_status=None, registered_device=None, storage_flex_flash_controller=None):
        """
        StorageFlexFlashPhysicalDrive - a model defined in Swagger
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
        self._card_status = None
        self._card_type = None
        self._oem_id = None
        self._pd_status = None
        self._registered_device = None
        self._storage_flex_flash_controller = None

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
        if card_status is not None:
          self.card_status = card_status
        if card_type is not None:
          self.card_type = card_type
        if oem_id is not None:
          self.oem_id = oem_id
        if pd_status is not None:
          self.pd_status = pd_status
        if registered_device is not None:
          self.registered_device = registered_device
        if storage_flex_flash_controller is not None:
          self.storage_flex_flash_controller = storage_flex_flash_controller

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageFlexFlashPhysicalDrive.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageFlexFlashPhysicalDrive.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageFlexFlashPhysicalDrive.
        The time when this managed object was created.  

        :return: The create_time of this StorageFlexFlashPhysicalDrive.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageFlexFlashPhysicalDrive.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageFlexFlashPhysicalDrive.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageFlexFlashPhysicalDrive.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageFlexFlashPhysicalDrive.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageFlexFlashPhysicalDrive.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageFlexFlashPhysicalDrive.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageFlexFlashPhysicalDrive.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageFlexFlashPhysicalDrive.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageFlexFlashPhysicalDrive.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageFlexFlashPhysicalDrive.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageFlexFlashPhysicalDrive.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageFlexFlashPhysicalDrive.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageFlexFlashPhysicalDrive.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageFlexFlashPhysicalDrive.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageFlexFlashPhysicalDrive.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageFlexFlashPhysicalDrive.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageFlexFlashPhysicalDrive.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageFlexFlashPhysicalDrive.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageFlexFlashPhysicalDrive.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StorageFlexFlashPhysicalDrive.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageFlexFlashPhysicalDrive.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StorageFlexFlashPhysicalDrive.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageFlexFlashPhysicalDrive.
        The versioning info for this managed object.   

        :return: The version_context of this StorageFlexFlashPhysicalDrive.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageFlexFlashPhysicalDrive.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageFlexFlashPhysicalDrive.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageFlexFlashPhysicalDrive.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageFlexFlashPhysicalDrive.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageFlexFlashPhysicalDrive.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageFlexFlashPhysicalDrive.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StorageFlexFlashPhysicalDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageFlexFlashPhysicalDrive.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageFlexFlashPhysicalDrive.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageFlexFlashPhysicalDrive.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StorageFlexFlashPhysicalDrive.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this StorageFlexFlashPhysicalDrive.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StorageFlexFlashPhysicalDrive.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this StorageFlexFlashPhysicalDrive.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageFlexFlashPhysicalDrive.

        :return: The device_mo_id of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageFlexFlashPhysicalDrive.

        :param device_mo_id: The device_mo_id of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageFlexFlashPhysicalDrive.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageFlexFlashPhysicalDrive.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageFlexFlashPhysicalDrive.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageFlexFlashPhysicalDrive.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageFlexFlashPhysicalDrive.
        This field identifies the model of the given component.  

        :return: The model of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageFlexFlashPhysicalDrive.
        This field identifies the model of the given component.  

        :param model: The model of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageFlexFlashPhysicalDrive.

        :return: The revision of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageFlexFlashPhysicalDrive.

        :param revision: The revision of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageFlexFlashPhysicalDrive.
        This field identifies the serial of the given component.  

        :return: The serial of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageFlexFlashPhysicalDrive.
        This field identifies the serial of the given component.  

        :param serial: The serial of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageFlexFlashPhysicalDrive.
        This field identifies the vendor of the given component.   

        :return: The vendor of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageFlexFlashPhysicalDrive.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._vendor = vendor

    @property
    def card_status(self):
        """
        Gets the card_status of this StorageFlexFlashPhysicalDrive.

        :return: The card_status of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._card_status

    @card_status.setter
    def card_status(self, card_status):
        """
        Sets the card_status of this StorageFlexFlashPhysicalDrive.

        :param card_status: The card_status of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._card_status = card_status

    @property
    def card_type(self):
        """
        Gets the card_type of this StorageFlexFlashPhysicalDrive.

        :return: The card_type of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._card_type

    @card_type.setter
    def card_type(self, card_type):
        """
        Sets the card_type of this StorageFlexFlashPhysicalDrive.

        :param card_type: The card_type of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._card_type = card_type

    @property
    def oem_id(self):
        """
        Gets the oem_id of this StorageFlexFlashPhysicalDrive.

        :return: The oem_id of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._oem_id

    @oem_id.setter
    def oem_id(self, oem_id):
        """
        Sets the oem_id of this StorageFlexFlashPhysicalDrive.

        :param oem_id: The oem_id of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._oem_id = oem_id

    @property
    def pd_status(self):
        """
        Gets the pd_status of this StorageFlexFlashPhysicalDrive.

        :return: The pd_status of this StorageFlexFlashPhysicalDrive.
        :rtype: str
        """
        return self._pd_status

    @pd_status.setter
    def pd_status(self, pd_status):
        """
        Sets the pd_status of this StorageFlexFlashPhysicalDrive.

        :param pd_status: The pd_status of this StorageFlexFlashPhysicalDrive.
        :type: str
        """

        self._pd_status = pd_status

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StorageFlexFlashPhysicalDrive.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this StorageFlexFlashPhysicalDrive.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StorageFlexFlashPhysicalDrive.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this StorageFlexFlashPhysicalDrive.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def storage_flex_flash_controller(self):
        """
        Gets the storage_flex_flash_controller of this StorageFlexFlashPhysicalDrive.
        A collection of references to the [storage.FlexFlashController](mo://storage.FlexFlashController) Managed Object.  When this managed object is deleted, the referenced [storage.FlexFlashController](mo://storage.FlexFlashController) MO unsets its reference to this deleted MO. 

        :return: The storage_flex_flash_controller of this StorageFlexFlashPhysicalDrive.
        :rtype: StorageFlexFlashControllerRef
        """
        return self._storage_flex_flash_controller

    @storage_flex_flash_controller.setter
    def storage_flex_flash_controller(self, storage_flex_flash_controller):
        """
        Sets the storage_flex_flash_controller of this StorageFlexFlashPhysicalDrive.
        A collection of references to the [storage.FlexFlashController](mo://storage.FlexFlashController) Managed Object.  When this managed object is deleted, the referenced [storage.FlexFlashController](mo://storage.FlexFlashController) MO unsets its reference to this deleted MO. 

        :param storage_flex_flash_controller: The storage_flex_flash_controller of this StorageFlexFlashPhysicalDrive.
        :type: StorageFlexFlashControllerRef
        """

        self._storage_flex_flash_controller = storage_flex_flash_controller

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
        if not isinstance(other, StorageFlexFlashPhysicalDrive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
