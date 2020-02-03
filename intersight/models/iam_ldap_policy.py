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


class IamLdapPolicy(object):
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
        'description': 'str',
        'name': 'str',
        'base_properties': 'IamLdapBaseProperties',
        'dns_parameters': 'IamLdapDnsParameters',
        'enable_dns': 'bool',
        'enabled': 'bool',
        'user_search_precedence': 'str',
        'appliance_account': 'IamAccountRef',
        'groups': 'list[IamLdapGroupRef]',
        'organization': 'OrganizationOrganizationRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]',
        'providers': 'list[IamLdapProviderRef]'
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
        'base_properties': 'BaseProperties',
        'dns_parameters': 'DnsParameters',
        'enable_dns': 'EnableDns',
        'enabled': 'Enabled',
        'user_search_precedence': 'UserSearchPrecedence',
        'appliance_account': 'ApplianceAccount',
        'groups': 'Groups',
        'organization': 'Organization',
        'profiles': 'Profiles',
        'providers': 'Providers'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, name=None, base_properties=None, dns_parameters=None, enable_dns=None, enabled=None, user_search_precedence='LocalUserDb', appliance_account=None, groups=None, organization=None, profiles=None, providers=None):
        """
        IamLdapPolicy - a model defined in Swagger
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
        self._base_properties = None
        self._dns_parameters = None
        self._enable_dns = None
        self._enabled = None
        self._user_search_precedence = None
        self._appliance_account = None
        self._groups = None
        self._organization = None
        self._profiles = None
        self._providers = None

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
        if base_properties is not None:
          self.base_properties = base_properties
        if dns_parameters is not None:
          self.dns_parameters = dns_parameters
        if enable_dns is not None:
          self.enable_dns = enable_dns
        if enabled is not None:
          self.enabled = enabled
        if user_search_precedence is not None:
          self.user_search_precedence = user_search_precedence
        if appliance_account is not None:
          self.appliance_account = appliance_account
        if groups is not None:
          self.groups = groups
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles
        if providers is not None:
          self.providers = providers

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamLdapPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this IamLdapPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamLdapPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamLdapPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this IamLdapPolicy.
        The time when this managed object was created.  

        :return: The create_time of this IamLdapPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamLdapPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamLdapPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this IamLdapPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this IamLdapPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this IamLdapPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this IamLdapPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamLdapPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamLdapPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamLdapPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamLdapPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamLdapPolicy.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this IamLdapPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamLdapPolicy.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this IamLdapPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamLdapPolicy.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this IamLdapPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamLdapPolicy.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this IamLdapPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamLdapPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this IamLdapPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamLdapPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamLdapPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this IamLdapPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this IamLdapPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this IamLdapPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this IamLdapPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this IamLdapPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IamLdapPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamLdapPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IamLdapPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this IamLdapPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this IamLdapPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this IamLdapPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this IamLdapPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamLdapPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamLdapPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamLdapPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamLdapPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this IamLdapPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamLdapPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamLdapPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamLdapPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this IamLdapPolicy.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this IamLdapPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this IamLdapPolicy.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this IamLdapPolicy.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this IamLdapPolicy.
        Description of the policy.  

        :return: The description of this IamLdapPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IamLdapPolicy.
        Description of the policy.  

        :param description: The description of this IamLdapPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this IamLdapPolicy.
        Name of the concrete policy.   

        :return: The name of this IamLdapPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamLdapPolicy.
        Name of the concrete policy.   

        :param name: The name of this IamLdapPolicy.
        :type: str
        """

        self._name = name

    @property
    def base_properties(self):
        """
        Gets the base_properties of this IamLdapPolicy.
        Base settings of LDAP required while configuring LDAP policy.  

        :return: The base_properties of this IamLdapPolicy.
        :rtype: IamLdapBaseProperties
        """
        return self._base_properties

    @base_properties.setter
    def base_properties(self, base_properties):
        """
        Sets the base_properties of this IamLdapPolicy.
        Base settings of LDAP required while configuring LDAP policy.  

        :param base_properties: The base_properties of this IamLdapPolicy.
        :type: IamLdapBaseProperties
        """

        self._base_properties = base_properties

    @property
    def dns_parameters(self):
        """
        Gets the dns_parameters of this IamLdapPolicy.
        Configuration settings to resolve LDAP servers, when DNS is enabled.  

        :return: The dns_parameters of this IamLdapPolicy.
        :rtype: IamLdapDnsParameters
        """
        return self._dns_parameters

    @dns_parameters.setter
    def dns_parameters(self, dns_parameters):
        """
        Sets the dns_parameters of this IamLdapPolicy.
        Configuration settings to resolve LDAP servers, when DNS is enabled.  

        :param dns_parameters: The dns_parameters of this IamLdapPolicy.
        :type: IamLdapDnsParameters
        """

        self._dns_parameters = dns_parameters

    @property
    def enable_dns(self):
        """
        Gets the enable_dns of this IamLdapPolicy.
        Enables DNS to access LDAP servers.  

        :return: The enable_dns of this IamLdapPolicy.
        :rtype: bool
        """
        return self._enable_dns

    @enable_dns.setter
    def enable_dns(self, enable_dns):
        """
        Sets the enable_dns of this IamLdapPolicy.
        Enables DNS to access LDAP servers.  

        :param enable_dns: The enable_dns of this IamLdapPolicy.
        :type: bool
        """

        self._enable_dns = enable_dns

    @property
    def enabled(self):
        """
        Gets the enabled of this IamLdapPolicy.
        LDAP server performs authentication.  

        :return: The enabled of this IamLdapPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this IamLdapPolicy.
        LDAP server performs authentication.  

        :param enabled: The enabled of this IamLdapPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def user_search_precedence(self):
        """
        Gets the user_search_precedence of this IamLdapPolicy.
        Search precedence between local user database and LDAP user database.   

        :return: The user_search_precedence of this IamLdapPolicy.
        :rtype: str
        """
        return self._user_search_precedence

    @user_search_precedence.setter
    def user_search_precedence(self, user_search_precedence):
        """
        Sets the user_search_precedence of this IamLdapPolicy.
        Search precedence between local user database and LDAP user database.   

        :param user_search_precedence: The user_search_precedence of this IamLdapPolicy.
        :type: str
        """
        allowed_values = ["LocalUserDb", "LDAPUserDb"]
        if user_search_precedence not in allowed_values:
            raise ValueError(
                "Invalid value for `user_search_precedence` ({0}), must be one of {1}"
                .format(user_search_precedence, allowed_values)
            )

        self._user_search_precedence = user_search_precedence

    @property
    def appliance_account(self):
        """
        Gets the appliance_account of this IamLdapPolicy.
        The appliance account to which the appliance LDAP policy belongs. 

        :return: The appliance_account of this IamLdapPolicy.
        :rtype: IamAccountRef
        """
        return self._appliance_account

    @appliance_account.setter
    def appliance_account(self, appliance_account):
        """
        Sets the appliance_account of this IamLdapPolicy.
        The appliance account to which the appliance LDAP policy belongs. 

        :param appliance_account: The appliance_account of this IamLdapPolicy.
        :type: IamAccountRef
        """

        self._appliance_account = appliance_account

    @property
    def groups(self):
        """
        Gets the groups of this IamLdapPolicy.
        Relationship to collection of LDAP Groups. 

        :return: The groups of this IamLdapPolicy.
        :rtype: list[IamLdapGroupRef]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this IamLdapPolicy.
        Relationship to collection of LDAP Groups. 

        :param groups: The groups of this IamLdapPolicy.
        :type: list[IamLdapGroupRef]
        """

        self._groups = groups

    @property
    def organization(self):
        """
        Gets the organization of this IamLdapPolicy.
        The organization to which the LDAP policy belongs. 

        :return: The organization of this IamLdapPolicy.
        :rtype: OrganizationOrganizationRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this IamLdapPolicy.
        The organization to which the LDAP policy belongs. 

        :param organization: The organization of this IamLdapPolicy.
        :type: OrganizationOrganizationRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this IamLdapPolicy.
        Relationship to the profile object. 

        :return: The profiles of this IamLdapPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this IamLdapPolicy.
        Relationship to the profile object. 

        :param profiles: The profiles of this IamLdapPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

    @property
    def providers(self):
        """
        Gets the providers of this IamLdapPolicy.
        Relationship to collection of LDAP Providers. 

        :return: The providers of this IamLdapPolicy.
        :rtype: list[IamLdapProviderRef]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """
        Sets the providers of this IamLdapPolicy.
        Relationship to collection of LDAP Providers. 

        :param providers: The providers of this IamLdapPolicy.
        :type: list[IamLdapProviderRef]
        """

        self._providers = providers

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
        if not isinstance(other, IamLdapPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
