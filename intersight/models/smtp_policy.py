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


class SmtpPolicy(object):
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
        'enabled': 'bool',
        'min_severity': 'str',
        'sender_email': 'str',
        'smtp_port': 'int',
        'smtp_recipients': 'list[str]',
        'smtp_server': 'str',
        'organization': 'OrganizationOrganizationRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]'
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
        'enabled': 'Enabled',
        'min_severity': 'MinSeverity',
        'sender_email': 'SenderEmail',
        'smtp_port': 'SmtpPort',
        'smtp_recipients': 'SmtpRecipients',
        'smtp_server': 'SmtpServer',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, name=None, enabled=None, min_severity='critical', sender_email=None, smtp_port=None, smtp_recipients=None, smtp_server=None, organization=None, profiles=None):
        """
        SmtpPolicy - a model defined in Swagger
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
        self._enabled = None
        self._min_severity = None
        self._sender_email = None
        self._smtp_port = None
        self._smtp_recipients = None
        self._smtp_server = None
        self._organization = None
        self._profiles = None

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
        if enabled is not None:
          self.enabled = enabled
        if min_severity is not None:
          self.min_severity = min_severity
        if sender_email is not None:
          self.sender_email = sender_email
        if smtp_port is not None:
          self.smtp_port = smtp_port
        if smtp_recipients is not None:
          self.smtp_recipients = smtp_recipients
        if smtp_server is not None:
          self.smtp_server = smtp_server
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SmtpPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this SmtpPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SmtpPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SmtpPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this SmtpPolicy.
        The time when this managed object was created.  

        :return: The create_time of this SmtpPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SmtpPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this SmtpPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this SmtpPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this SmtpPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this SmtpPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this SmtpPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SmtpPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this SmtpPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SmtpPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SmtpPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SmtpPolicy.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this SmtpPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SmtpPolicy.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this SmtpPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SmtpPolicy.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this SmtpPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SmtpPolicy.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this SmtpPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SmtpPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this SmtpPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SmtpPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SmtpPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this SmtpPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this SmtpPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this SmtpPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this SmtpPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this SmtpPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this SmtpPolicy.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SmtpPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this SmtpPolicy.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this SmtpPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this SmtpPolicy.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this SmtpPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this SmtpPolicy.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SmtpPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SmtpPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SmtpPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SmtpPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this SmtpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SmtpPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SmtpPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SmtpPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this SmtpPolicy.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this SmtpPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this SmtpPolicy.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this SmtpPolicy.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this SmtpPolicy.
        Description of the policy.  

        :return: The description of this SmtpPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SmtpPolicy.
        Description of the policy.  

        :param description: The description of this SmtpPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this SmtpPolicy.
        Name of the concrete policy.   

        :return: The name of this SmtpPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SmtpPolicy.
        Name of the concrete policy.   

        :param name: The name of this SmtpPolicy.
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """
        Gets the enabled of this SmtpPolicy.
        If enabled, controls the state of the SMTP client service on the managed device.  

        :return: The enabled of this SmtpPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this SmtpPolicy.
        If enabled, controls the state of the SMTP client service on the managed device.  

        :param enabled: The enabled of this SmtpPolicy.
        :type: bool
        """

        self._enabled = enabled

    @property
    def min_severity(self):
        """
        Gets the min_severity of this SmtpPolicy.
        Minimum fault severity level to receive email notifications. Email notifications are sent for all faults whose severity is equal to or greater than the chosen level.  

        :return: The min_severity of this SmtpPolicy.
        :rtype: str
        """
        return self._min_severity

    @min_severity.setter
    def min_severity(self, min_severity):
        """
        Sets the min_severity of this SmtpPolicy.
        Minimum fault severity level to receive email notifications. Email notifications are sent for all faults whose severity is equal to or greater than the chosen level.  

        :param min_severity: The min_severity of this SmtpPolicy.
        :type: str
        """
        allowed_values = ["critical", "condition", "warning", "minor", "major"]
        if min_severity not in allowed_values:
            raise ValueError(
                "Invalid value for `min_severity` ({0}), must be one of {1}"
                .format(min_severity, allowed_values)
            )

        self._min_severity = min_severity

    @property
    def sender_email(self):
        """
        Gets the sender_email of this SmtpPolicy.
        The email address entered here will be displayed as the from address (mail received from address) of all the SMTP mail alerts that are received. If not configured, the hostname of the server is used in the from address field.  

        :return: The sender_email of this SmtpPolicy.
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """
        Sets the sender_email of this SmtpPolicy.
        The email address entered here will be displayed as the from address (mail received from address) of all the SMTP mail alerts that are received. If not configured, the hostname of the server is used in the from address field.  

        :param sender_email: The sender_email of this SmtpPolicy.
        :type: str
        """

        self._sender_email = sender_email

    @property
    def smtp_port(self):
        """
        Gets the smtp_port of this SmtpPolicy.
        Port number used by the SMTP server for outgoing SMTP communication.  

        :return: The smtp_port of this SmtpPolicy.
        :rtype: int
        """
        return self._smtp_port

    @smtp_port.setter
    def smtp_port(self, smtp_port):
        """
        Sets the smtp_port of this SmtpPolicy.
        Port number used by the SMTP server for outgoing SMTP communication.  

        :param smtp_port: The smtp_port of this SmtpPolicy.
        :type: int
        """

        self._smtp_port = smtp_port

    @property
    def smtp_recipients(self):
        """
        Gets the smtp_recipients of this SmtpPolicy.
        List of email addresses that will receive notifications for faults.  

        :return: The smtp_recipients of this SmtpPolicy.
        :rtype: list[str]
        """
        return self._smtp_recipients

    @smtp_recipients.setter
    def smtp_recipients(self, smtp_recipients):
        """
        Sets the smtp_recipients of this SmtpPolicy.
        List of email addresses that will receive notifications for faults.  

        :param smtp_recipients: The smtp_recipients of this SmtpPolicy.
        :type: list[str]
        """

        self._smtp_recipients = smtp_recipients

    @property
    def smtp_server(self):
        """
        Gets the smtp_server of this SmtpPolicy.
        IP address or hostname of the SMTP server. The SMTP server is used by the managed device to send email notifications.   

        :return: The smtp_server of this SmtpPolicy.
        :rtype: str
        """
        return self._smtp_server

    @smtp_server.setter
    def smtp_server(self, smtp_server):
        """
        Sets the smtp_server of this SmtpPolicy.
        IP address or hostname of the SMTP server. The SMTP server is used by the managed device to send email notifications.   

        :param smtp_server: The smtp_server of this SmtpPolicy.
        :type: str
        """

        self._smtp_server = smtp_server

    @property
    def organization(self):
        """
        Gets the organization of this SmtpPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this SmtpPolicy.
        :rtype: OrganizationOrganizationRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this SmtpPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this SmtpPolicy.
        :type: OrganizationOrganizationRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this SmtpPolicy.
        Relationship to the profile object. 

        :return: The profiles of this SmtpPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this SmtpPolicy.
        Relationship to the profile object. 

        :param profiles: The profiles of this SmtpPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

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
        if not isinstance(other, SmtpPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
