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


class RecoveryBackupProfile(object):
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
        'description': 'str',
        'name': 'str',
        'type': 'str',
        'src_template': 'PolicyAbstractProfileRef',
        'action': 'str',
        'config_context': 'PolicyOptionalConfigContext',
        'enabled': 'bool',
        'backup_config': 'RecoveryBackupConfigPolicyRef',
        'config_result': 'RecoveryConfigResultRef',
        'device_id': 'AssetDeviceRegistrationRef',
        'organization': 'OrganizationOrganizationRef',
        'schedule_config': 'RecoveryScheduleConfigPolicyRef'
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
        'description': 'Description',
        'name': 'Name',
        'type': 'Type',
        'src_template': 'SrcTemplate',
        'action': 'Action',
        'config_context': 'ConfigContext',
        'enabled': 'Enabled',
        'backup_config': 'BackupConfig',
        'config_result': 'ConfigResult',
        'device_id': 'DeviceId',
        'organization': 'Organization',
        'schedule_config': 'ScheduleConfig'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, name=None, type='instance', src_template=None, action=None, config_context=None, enabled=None, backup_config=None, config_result=None, device_id=None, organization=None, schedule_config=None):
        """
        RecoveryBackupProfile - a model defined in Swagger
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
        self._description = None
        self._name = None
        self._type = None
        self._src_template = None
        self._action = None
        self._config_context = None
        self._enabled = None
        self._backup_config = None
        self._config_result = None
        self._device_id = None
        self._organization = None
        self._schedule_config = None

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
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if src_template is not None:
          self.src_template = src_template
        if action is not None:
          self.action = action
        if config_context is not None:
          self.config_context = config_context
        if enabled is not None:
          self.enabled = enabled
        if backup_config is not None:
          self.backup_config = backup_config
        if config_result is not None:
          self.config_result = config_result
        if device_id is not None:
          self.device_id = device_id
        if organization is not None:
          self.organization = organization
        if schedule_config is not None:
          self.schedule_config = schedule_config

    @property
    def account_moid(self):
        """
        Gets the account_moid of this RecoveryBackupProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this RecoveryBackupProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this RecoveryBackupProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this RecoveryBackupProfile.
        The time when this managed object was created.  

        :return: The create_time of this RecoveryBackupProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this RecoveryBackupProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this RecoveryBackupProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this RecoveryBackupProfile.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this RecoveryBackupProfile.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this RecoveryBackupProfile.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this RecoveryBackupProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this RecoveryBackupProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this RecoveryBackupProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this RecoveryBackupProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this RecoveryBackupProfile.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this RecoveryBackupProfile.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this RecoveryBackupProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this RecoveryBackupProfile.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this RecoveryBackupProfile.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this RecoveryBackupProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this RecoveryBackupProfile.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this RecoveryBackupProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this RecoveryBackupProfile.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this RecoveryBackupProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this RecoveryBackupProfile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this RecoveryBackupProfile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this RecoveryBackupProfile.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this RecoveryBackupProfile.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this RecoveryBackupProfile.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this RecoveryBackupProfile.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this RecoveryBackupProfile.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this RecoveryBackupProfile.
        The versioning info for this managed object.   

        :return: The version_context of this RecoveryBackupProfile.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this RecoveryBackupProfile.
        The versioning info for this managed object.   

        :param version_context: The version_context of this RecoveryBackupProfile.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this RecoveryBackupProfile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this RecoveryBackupProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this RecoveryBackupProfile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this RecoveryBackupProfile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this RecoveryBackupProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this RecoveryBackupProfile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this RecoveryBackupProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this RecoveryBackupProfile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this RecoveryBackupProfile.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this RecoveryBackupProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this RecoveryBackupProfile.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this RecoveryBackupProfile.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this RecoveryBackupProfile.
        Description of the profile.  

        :return: The description of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RecoveryBackupProfile.
        Description of the profile.  

        :param description: The description of this RecoveryBackupProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this RecoveryBackupProfile.
        Name of the concrete profile.  

        :return: The name of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecoveryBackupProfile.
        Name of the concrete profile.  

        :param name: The name of this RecoveryBackupProfile.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this RecoveryBackupProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RecoveryBackupProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this RecoveryBackupProfile.
        :type: str
        """
        allowed_values = ["instance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def src_template(self):
        """
        Gets the src_template of this RecoveryBackupProfile.
        The source profile template to apply to the profile instance. All configuration settings from the profile template will be applied to the profile instance. 

        :return: The src_template of this RecoveryBackupProfile.
        :rtype: PolicyAbstractProfileRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this RecoveryBackupProfile.
        The source profile template to apply to the profile instance. All configuration settings from the profile template will be applied to the profile instance. 

        :param src_template: The src_template of this RecoveryBackupProfile.
        :type: PolicyAbstractProfileRef
        """

        self._src_template = src_template

    @property
    def action(self):
        """
        Gets the action of this RecoveryBackupProfile.
        User initiated action. Each profile type has its own supported actions. For HyperFlex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign.  

        :return: The action of this RecoveryBackupProfile.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this RecoveryBackupProfile.
        User initiated action. Each profile type has its own supported actions. For HyperFlex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign.  

        :param action: The action of this RecoveryBackupProfile.
        :type: str
        """

        self._action = action

    @property
    def config_context(self):
        """
        Gets the config_context of this RecoveryBackupProfile.
        The configuration state and results of the last configuration operation.   

        :return: The config_context of this RecoveryBackupProfile.
        :rtype: PolicyOptionalConfigContext
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """
        Sets the config_context of this RecoveryBackupProfile.
        The configuration state and results of the last configuration operation.   

        :param config_context: The config_context of this RecoveryBackupProfile.
        :type: PolicyOptionalConfigContext
        """

        self._config_context = config_context

    @property
    def enabled(self):
        """
        Gets the enabled of this RecoveryBackupProfile.
        Enables/Disables the schedule on the endpoint.   

        :return: The enabled of this RecoveryBackupProfile.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this RecoveryBackupProfile.
        Enables/Disables the schedule on the endpoint.   

        :param enabled: The enabled of this RecoveryBackupProfile.
        :type: bool
        """

        self._enabled = enabled

    @property
    def backup_config(self):
        """
        Gets the backup_config of this RecoveryBackupProfile.
        A collection of references to the [recovery.BackupConfigPolicy](mo://recovery.BackupConfigPolicy) Managed Object.  When this managed object is deleted, the referenced [recovery.BackupConfigPolicy](mo://recovery.BackupConfigPolicy) MO unsets its reference to this deleted MO. 

        :return: The backup_config of this RecoveryBackupProfile.
        :rtype: RecoveryBackupConfigPolicyRef
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this RecoveryBackupProfile.
        A collection of references to the [recovery.BackupConfigPolicy](mo://recovery.BackupConfigPolicy) Managed Object.  When this managed object is deleted, the referenced [recovery.BackupConfigPolicy](mo://recovery.BackupConfigPolicy) MO unsets its reference to this deleted MO. 

        :param backup_config: The backup_config of this RecoveryBackupProfile.
        :type: RecoveryBackupConfigPolicyRef
        """

        self._backup_config = backup_config

    @property
    def config_result(self):
        """
        Gets the config_result of this RecoveryBackupProfile.
        The profile configuration (deploy, validation) results with the overall state and detailed result messages. 

        :return: The config_result of this RecoveryBackupProfile.
        :rtype: RecoveryConfigResultRef
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """
        Sets the config_result of this RecoveryBackupProfile.
        The profile configuration (deploy, validation) results with the overall state and detailed result messages. 

        :param config_result: The config_result of this RecoveryBackupProfile.
        :type: RecoveryConfigResultRef
        """

        self._config_result = config_result

    @property
    def device_id(self):
        """
        Gets the device_id of this RecoveryBackupProfile.
        Relationship to all the end devices associated to this backup profile. 

        :return: The device_id of this RecoveryBackupProfile.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this RecoveryBackupProfile.
        Relationship to all the end devices associated to this backup profile. 

        :param device_id: The device_id of this RecoveryBackupProfile.
        :type: AssetDeviceRegistrationRef
        """

        self._device_id = device_id

    @property
    def organization(self):
        """
        Gets the organization of this RecoveryBackupProfile.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this RecoveryBackupProfile.
        :rtype: OrganizationOrganizationRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this RecoveryBackupProfile.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this RecoveryBackupProfile.
        :type: OrganizationOrganizationRef
        """

        self._organization = organization

    @property
    def schedule_config(self):
        """
        Gets the schedule_config of this RecoveryBackupProfile.
        A collection of references to the [recovery.ScheduleConfigPolicy](mo://recovery.ScheduleConfigPolicy) Managed Object.  When this managed object is deleted, the referenced [recovery.ScheduleConfigPolicy](mo://recovery.ScheduleConfigPolicy) MO unsets its reference to this deleted MO. 

        :return: The schedule_config of this RecoveryBackupProfile.
        :rtype: RecoveryScheduleConfigPolicyRef
        """
        return self._schedule_config

    @schedule_config.setter
    def schedule_config(self, schedule_config):
        """
        Sets the schedule_config of this RecoveryBackupProfile.
        A collection of references to the [recovery.ScheduleConfigPolicy](mo://recovery.ScheduleConfigPolicy) Managed Object.  When this managed object is deleted, the referenced [recovery.ScheduleConfigPolicy](mo://recovery.ScheduleConfigPolicy) MO unsets its reference to this deleted MO. 

        :param schedule_config: The schedule_config of this RecoveryBackupProfile.
        :type: RecoveryScheduleConfigPolicyRef
        """

        self._schedule_config = schedule_config

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
        if not isinstance(other, RecoveryBackupProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
