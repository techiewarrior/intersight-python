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


class WorkflowTaskDefinition(object):
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
        'default_version': 'bool',
        'description': 'str',
        'internal_properties': 'WorkflowInternalProperties',
        'label': 'str',
        'license_entitlement': 'str',
        'name': 'str',
        'properties': 'WorkflowProperties',
        'secure_prop_access': 'bool',
        'version': 'int',
        'catalog': 'WorkflowCatalogRef',
        'implemented_tasks': 'list[WorkflowTaskDefinitionRef]',
        'interface_task': 'WorkflowTaskDefinitionRef'
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
        'default_version': 'DefaultVersion',
        'description': 'Description',
        'internal_properties': 'InternalProperties',
        'label': 'Label',
        'license_entitlement': 'LicenseEntitlement',
        'name': 'Name',
        'properties': 'Properties',
        'secure_prop_access': 'SecurePropAccess',
        'version': 'Version',
        'catalog': 'Catalog',
        'implemented_tasks': 'ImplementedTasks',
        'interface_task': 'InterfaceTask'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, default_version=None, description=None, internal_properties=None, label=None, license_entitlement='Base', name=None, properties=None, secure_prop_access=None, version=None, catalog=None, implemented_tasks=None, interface_task=None):
        """
        WorkflowTaskDefinition - a model defined in Swagger
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
        self._default_version = None
        self._description = None
        self._internal_properties = None
        self._label = None
        self._license_entitlement = None
        self._name = None
        self._properties = None
        self._secure_prop_access = None
        self._version = None
        self._catalog = None
        self._implemented_tasks = None
        self._interface_task = None

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
        if default_version is not None:
          self.default_version = default_version
        if description is not None:
          self.description = description
        if internal_properties is not None:
          self.internal_properties = internal_properties
        if label is not None:
          self.label = label
        if license_entitlement is not None:
          self.license_entitlement = license_entitlement
        if name is not None:
          self.name = name
        if properties is not None:
          self.properties = properties
        if secure_prop_access is not None:
          self.secure_prop_access = secure_prop_access
        if version is not None:
          self.version = version
        if catalog is not None:
          self.catalog = catalog
        if implemented_tasks is not None:
          self.implemented_tasks = implemented_tasks
        if interface_task is not None:
          self.interface_task = interface_task

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowTaskDefinition.
        The Account ID for this managed object.

        :return: The account_moid of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowTaskDefinition.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this WorkflowTaskDefinition.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowTaskDefinition.
        The time when this managed object was created.

        :return: The create_time of this WorkflowTaskDefinition.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowTaskDefinition.
        The time when this managed object was created.

        :param create_time: The create_time of this WorkflowTaskDefinition.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this WorkflowTaskDefinition.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this WorkflowTaskDefinition.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this WorkflowTaskDefinition.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowTaskDefinition.
        The time when this managed object was last modified.

        :return: The mod_time of this WorkflowTaskDefinition.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowTaskDefinition.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this WorkflowTaskDefinition.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowTaskDefinition.
        The unique identifier of this Managed Object instance.

        :return: The moid of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowTaskDefinition.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this WorkflowTaskDefinition.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowTaskDefinition.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowTaskDefinition.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this WorkflowTaskDefinition.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowTaskDefinition.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this WorkflowTaskDefinition.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowTaskDefinition.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this WorkflowTaskDefinition.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this WorkflowTaskDefinition.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this WorkflowTaskDefinition.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this WorkflowTaskDefinition.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowTaskDefinition.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this WorkflowTaskDefinition.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowTaskDefinition.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this WorkflowTaskDefinition.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this WorkflowTaskDefinition.
        The versioning info for this managed object.

        :return: The version_context of this WorkflowTaskDefinition.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this WorkflowTaskDefinition.
        The versioning info for this managed object.

        :param version_context: The version_context of this WorkflowTaskDefinition.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowTaskDefinition.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this WorkflowTaskDefinition.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowTaskDefinition.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this WorkflowTaskDefinition.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowTaskDefinition.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this WorkflowTaskDefinition.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowTaskDefinition.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this WorkflowTaskDefinition.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this WorkflowTaskDefinition.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this WorkflowTaskDefinition.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this WorkflowTaskDefinition.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this WorkflowTaskDefinition.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def default_version(self):
        """
        Gets the default_version of this WorkflowTaskDefinition.
        When true this will be the task version that is used when a specific task definition version is not specified. The very first task definition created with a name will be set as the default version, after that user can explicitly set any version of the task definition as the default version.

        :return: The default_version of this WorkflowTaskDefinition.
        :rtype: bool
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        """
        Sets the default_version of this WorkflowTaskDefinition.
        When true this will be the task version that is used when a specific task definition version is not specified. The very first task definition created with a name will be set as the default version, after that user can explicitly set any version of the task definition as the default version.

        :param default_version: The default_version of this WorkflowTaskDefinition.
        :type: bool
        """

        self._default_version = default_version

    @property
    def description(self):
        """
        Gets the description of this WorkflowTaskDefinition.
        The task definition description to describe what this task will do when executed.

        :return: The description of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowTaskDefinition.
        The task definition description to describe what this task will do when executed.

        :param description: The description of this WorkflowTaskDefinition.
        :type: str
        """

        self._description = description

    @property
    def internal_properties(self):
        """
        Gets the internal_properties of this WorkflowTaskDefinition.
        Type to capture all the internal properties for the task definition.

        :return: The internal_properties of this WorkflowTaskDefinition.
        :rtype: WorkflowInternalProperties
        """
        return self._internal_properties

    @internal_properties.setter
    def internal_properties(self, internal_properties):
        """
        Sets the internal_properties of this WorkflowTaskDefinition.
        Type to capture all the internal properties for the task definition.

        :param internal_properties: The internal_properties of this WorkflowTaskDefinition.
        :type: WorkflowInternalProperties
        """

        self._internal_properties = internal_properties

    @property
    def label(self):
        """
        Gets the label of this WorkflowTaskDefinition.
        A user friendly short name to identify the task definition.

        :return: The label of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WorkflowTaskDefinition.
        A user friendly short name to identify the task definition.

        :param label: The label of this WorkflowTaskDefinition.
        :type: str
        """

        self._label = label

    @property
    def license_entitlement(self):
        """
        Gets the license_entitlement of this WorkflowTaskDefinition.
        License entitlement required to run this task. It is determined by license requirement of features.

        :return: The license_entitlement of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._license_entitlement

    @license_entitlement.setter
    def license_entitlement(self, license_entitlement):
        """
        Sets the license_entitlement of this WorkflowTaskDefinition.
        License entitlement required to run this task. It is determined by license requirement of features.

        :param license_entitlement: The license_entitlement of this WorkflowTaskDefinition.
        :type: str
        """
        allowed_values = ["Base", "Essential", "Standard", "Advantage", "Premier"]
        if license_entitlement not in allowed_values:
            raise ValueError(
                "Invalid value for `license_entitlement` ({0}), must be one of {1}"
                .format(license_entitlement, allowed_values)
            )

        self._license_entitlement = license_entitlement

    @property
    def name(self):
        """
        Gets the name of this WorkflowTaskDefinition.
        The name of the task definition. The name should follow this convention <Verb or Action><Category><Vendor><Product><Noun or object> Verb or Action is a required portion of the name and this must be part of the pre-approved verb list. Category is an optional field and this will refer to the broad category of the task referring to the type of resource or endpoint. If there is no specific category then use \"Generic\" if required. Vendor is an optional field and this will refer to the specific vendor this task applies to. If the task is generic and not tied to a vendor, then do not specify anything. Product is an optional field, this will contain the vendor product and model when desired. Noun or object is a required field and  this will contain the noun or object on which the action is being performed. Examples SendEmail  - This is a task in Generic category for sending email. NewStorageVolume - This is a vendor agnostic task under Storage device category for creating a new volume.

        :return: The name of this WorkflowTaskDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowTaskDefinition.
        The name of the task definition. The name should follow this convention <Verb or Action><Category><Vendor><Product><Noun or object> Verb or Action is a required portion of the name and this must be part of the pre-approved verb list. Category is an optional field and this will refer to the broad category of the task referring to the type of resource or endpoint. If there is no specific category then use \"Generic\" if required. Vendor is an optional field and this will refer to the specific vendor this task applies to. If the task is generic and not tied to a vendor, then do not specify anything. Product is an optional field, this will contain the vendor product and model when desired. Noun or object is a required field and  this will contain the noun or object on which the action is being performed. Examples SendEmail  - This is a task in Generic category for sending email. NewStorageVolume - This is a vendor agnostic task under Storage device category for creating a new volume.

        :param name: The name of this WorkflowTaskDefinition.
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """
        Gets the properties of this WorkflowTaskDefinition.
        Type to capture all the properties for the task definition.

        :return: The properties of this WorkflowTaskDefinition.
        :rtype: WorkflowProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this WorkflowTaskDefinition.
        Type to capture all the properties for the task definition.

        :param properties: The properties of this WorkflowTaskDefinition.
        :type: WorkflowProperties
        """

        self._properties = properties

    @property
    def secure_prop_access(self):
        """
        Gets the secure_prop_access of this WorkflowTaskDefinition.
        If set to true, the task requires access to secure properties and uses an encyption token associated with a workflow moid to encrypt or decrypt the secure properties.

        :return: The secure_prop_access of this WorkflowTaskDefinition.
        :rtype: bool
        """
        return self._secure_prop_access

    @secure_prop_access.setter
    def secure_prop_access(self, secure_prop_access):
        """
        Sets the secure_prop_access of this WorkflowTaskDefinition.
        If set to true, the task requires access to secure properties and uses an encyption token associated with a workflow moid to encrypt or decrypt the secure properties.

        :param secure_prop_access: The secure_prop_access of this WorkflowTaskDefinition.
        :type: bool
        """

        self._secure_prop_access = secure_prop_access

    @property
    def version(self):
        """
        Gets the version of this WorkflowTaskDefinition.
        The version of the task definition so we can support multiple versions of a task definition.

        :return: The version of this WorkflowTaskDefinition.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this WorkflowTaskDefinition.
        The version of the task definition so we can support multiple versions of a task definition.

        :param version: The version of this WorkflowTaskDefinition.
        :type: int
        """

        self._version = version

    @property
    def catalog(self):
        """
        Gets the catalog of this WorkflowTaskDefinition.
        The catalog under which the definition has been added.

        :return: The catalog of this WorkflowTaskDefinition.
        :rtype: WorkflowCatalogRef
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """
        Sets the catalog of this WorkflowTaskDefinition.
        The catalog under which the definition has been added.

        :param catalog: The catalog of this WorkflowTaskDefinition.
        :type: WorkflowCatalogRef
        """

        self._catalog = catalog

    @property
    def implemented_tasks(self):
        """
        Gets the implemented_tasks of this WorkflowTaskDefinition.
        List of all the implemented task for this TaskDefinition. When this list is populated it implies that this TaskDefinition has multiple implementations.

        :return: The implemented_tasks of this WorkflowTaskDefinition.
        :rtype: list[WorkflowTaskDefinitionRef]
        """
        return self._implemented_tasks

    @implemented_tasks.setter
    def implemented_tasks(self, implemented_tasks):
        """
        Sets the implemented_tasks of this WorkflowTaskDefinition.
        List of all the implemented task for this TaskDefinition. When this list is populated it implies that this TaskDefinition has multiple implementations.

        :param implemented_tasks: The implemented_tasks of this WorkflowTaskDefinition.
        :type: list[WorkflowTaskDefinitionRef]
        """

        self._implemented_tasks = implemented_tasks

    @property
    def interface_task(self):
        """
        Gets the interface_task of this WorkflowTaskDefinition.
        A collection of references to the [workflow.TaskDefinition](mo://workflow.TaskDefinition) Managed Object. When this managed object is deleted, the referenced [workflow.TaskDefinition](mo://workflow.TaskDefinition) MO unsets its reference to this deleted MO.

        :return: The interface_task of this WorkflowTaskDefinition.
        :rtype: WorkflowTaskDefinitionRef
        """
        return self._interface_task

    @interface_task.setter
    def interface_task(self, interface_task):
        """
        Sets the interface_task of this WorkflowTaskDefinition.
        A collection of references to the [workflow.TaskDefinition](mo://workflow.TaskDefinition) Managed Object. When this managed object is deleted, the referenced [workflow.TaskDefinition](mo://workflow.TaskDefinition) MO unsets its reference to this deleted MO.

        :param interface_task: The interface_task of this WorkflowTaskDefinition.
        :type: WorkflowTaskDefinitionRef
        """

        self._interface_task = interface_task

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
        if not isinstance(other, WorkflowTaskDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
