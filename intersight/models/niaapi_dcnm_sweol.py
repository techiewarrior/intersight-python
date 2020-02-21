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


class NiaapiDcnmSweol(object):
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
        'affected_versions': 'str',
        'announcement_date': 'datetime',
        'announcement_date_epoch': 'int',
        'bulletin_no': 'str',
        'description': 'str',
        'endof_new_service_attachment_date': 'datetime',
        'endof_new_service_attachment_date_epoch': 'int',
        'endof_service_contract_renewal_date': 'datetime',
        'endof_service_contract_renewal_date_epoch': 'int',
        'endof_sw_maintenance_date': 'datetime',
        'endof_sw_maintenance_date_epoch': 'int',
        'headline': 'str',
        'last_dateof_support': 'datetime',
        'last_dateof_support_epoch': 'int',
        'last_ship_date': 'datetime',
        'last_ship_date_epoch': 'int',
        'migration_url': 'str',
        'software_eol_url': 'str'
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
        'affected_versions': 'AffectedVersions',
        'announcement_date': 'AnnouncementDate',
        'announcement_date_epoch': 'AnnouncementDateEpoch',
        'bulletin_no': 'BulletinNo',
        'description': 'Description',
        'endof_new_service_attachment_date': 'EndofNewServiceAttachmentDate',
        'endof_new_service_attachment_date_epoch': 'EndofNewServiceAttachmentDateEpoch',
        'endof_service_contract_renewal_date': 'EndofServiceContractRenewalDate',
        'endof_service_contract_renewal_date_epoch': 'EndofServiceContractRenewalDateEpoch',
        'endof_sw_maintenance_date': 'EndofSwMaintenanceDate',
        'endof_sw_maintenance_date_epoch': 'EndofSwMaintenanceDateEpoch',
        'headline': 'Headline',
        'last_dateof_support': 'LastDateofSupport',
        'last_dateof_support_epoch': 'LastDateofSupportEpoch',
        'last_ship_date': 'LastShipDate',
        'last_ship_date_epoch': 'LastShipDateEpoch',
        'migration_url': 'MigrationUrl',
        'software_eol_url': 'SoftwareEolUrl'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, affected_versions=None, announcement_date=None, announcement_date_epoch=None, bulletin_no=None, description=None, endof_new_service_attachment_date=None, endof_new_service_attachment_date_epoch=None, endof_service_contract_renewal_date=None, endof_service_contract_renewal_date_epoch=None, endof_sw_maintenance_date=None, endof_sw_maintenance_date_epoch=None, headline=None, last_dateof_support=None, last_dateof_support_epoch=None, last_ship_date=None, last_ship_date_epoch=None, migration_url=None, software_eol_url=None):
        """
        NiaapiDcnmSweol - a model defined in Swagger
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
        self._affected_versions = None
        self._announcement_date = None
        self._announcement_date_epoch = None
        self._bulletin_no = None
        self._description = None
        self._endof_new_service_attachment_date = None
        self._endof_new_service_attachment_date_epoch = None
        self._endof_service_contract_renewal_date = None
        self._endof_service_contract_renewal_date_epoch = None
        self._endof_sw_maintenance_date = None
        self._endof_sw_maintenance_date_epoch = None
        self._headline = None
        self._last_dateof_support = None
        self._last_dateof_support_epoch = None
        self._last_ship_date = None
        self._last_ship_date_epoch = None
        self._migration_url = None
        self._software_eol_url = None

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
        if affected_versions is not None:
          self.affected_versions = affected_versions
        if announcement_date is not None:
          self.announcement_date = announcement_date
        if announcement_date_epoch is not None:
          self.announcement_date_epoch = announcement_date_epoch
        if bulletin_no is not None:
          self.bulletin_no = bulletin_no
        if description is not None:
          self.description = description
        if endof_new_service_attachment_date is not None:
          self.endof_new_service_attachment_date = endof_new_service_attachment_date
        if endof_new_service_attachment_date_epoch is not None:
          self.endof_new_service_attachment_date_epoch = endof_new_service_attachment_date_epoch
        if endof_service_contract_renewal_date is not None:
          self.endof_service_contract_renewal_date = endof_service_contract_renewal_date
        if endof_service_contract_renewal_date_epoch is not None:
          self.endof_service_contract_renewal_date_epoch = endof_service_contract_renewal_date_epoch
        if endof_sw_maintenance_date is not None:
          self.endof_sw_maintenance_date = endof_sw_maintenance_date
        if endof_sw_maintenance_date_epoch is not None:
          self.endof_sw_maintenance_date_epoch = endof_sw_maintenance_date_epoch
        if headline is not None:
          self.headline = headline
        if last_dateof_support is not None:
          self.last_dateof_support = last_dateof_support
        if last_dateof_support_epoch is not None:
          self.last_dateof_support_epoch = last_dateof_support_epoch
        if last_ship_date is not None:
          self.last_ship_date = last_ship_date
        if last_ship_date_epoch is not None:
          self.last_ship_date_epoch = last_ship_date_epoch
        if migration_url is not None:
          self.migration_url = migration_url
        if software_eol_url is not None:
          self.software_eol_url = software_eol_url

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NiaapiDcnmSweol.
        The Account ID for this managed object.  

        :return: The account_moid of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NiaapiDcnmSweol.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NiaapiDcnmSweol.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this NiaapiDcnmSweol.
        The time when this managed object was created.  

        :return: The create_time of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NiaapiDcnmSweol.
        The time when this managed object was created.  

        :param create_time: The create_time of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this NiaapiDcnmSweol.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this NiaapiDcnmSweol.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this NiaapiDcnmSweol.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NiaapiDcnmSweol.
        The time when this managed object was last modified.  

        :return: The mod_time of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NiaapiDcnmSweol.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NiaapiDcnmSweol.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NiaapiDcnmSweol.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this NiaapiDcnmSweol.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NiaapiDcnmSweol.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NiaapiDcnmSweol.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this NiaapiDcnmSweol.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NiaapiDcnmSweol.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this NiaapiDcnmSweol.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NiaapiDcnmSweol.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NiaapiDcnmSweol.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this NiaapiDcnmSweol.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this NiaapiDcnmSweol.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this NiaapiDcnmSweol.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this NiaapiDcnmSweol.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this NiaapiDcnmSweol.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NiaapiDcnmSweol.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this NiaapiDcnmSweol.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this NiaapiDcnmSweol.
        The versioning info for this managed object.   

        :return: The version_context of this NiaapiDcnmSweol.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this NiaapiDcnmSweol.
        The versioning info for this managed object.   

        :param version_context: The version_context of this NiaapiDcnmSweol.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NiaapiDcnmSweol.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NiaapiDcnmSweol.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NiaapiDcnmSweol.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NiaapiDcnmSweol.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this NiaapiDcnmSweol.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NiaapiDcnmSweol.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NiaapiDcnmSweol.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NiaapiDcnmSweol.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this NiaapiDcnmSweol.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this NiaapiDcnmSweol.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this NiaapiDcnmSweol.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this NiaapiDcnmSweol.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def affected_versions(self):
        """
        Gets the affected_versions of this NiaapiDcnmSweol.
        String contains the Release versions affected by this notice, seperated by comma.  

        :return: The affected_versions of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._affected_versions

    @affected_versions.setter
    def affected_versions(self, affected_versions):
        """
        Sets the affected_versions of this NiaapiDcnmSweol.
        String contains the Release versions affected by this notice, seperated by comma.  

        :param affected_versions: The affected_versions of this NiaapiDcnmSweol.
        :type: str
        """

        self._affected_versions = affected_versions

    @property
    def announcement_date(self):
        """
        Gets the announcement_date of this NiaapiDcnmSweol.
        Date time of this notice Announced.  

        :return: The announcement_date of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._announcement_date

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """
        Sets the announcement_date of this NiaapiDcnmSweol.
        Date time of this notice Announced.  

        :param announcement_date: The announcement_date of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._announcement_date = announcement_date

    @property
    def announcement_date_epoch(self):
        """
        Gets the announcement_date_epoch of this NiaapiDcnmSweol.
        Epoch time of this notice Announced.  

        :return: The announcement_date_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._announcement_date_epoch

    @announcement_date_epoch.setter
    def announcement_date_epoch(self, announcement_date_epoch):
        """
        Sets the announcement_date_epoch of this NiaapiDcnmSweol.
        Epoch time of this notice Announced.  

        :param announcement_date_epoch: The announcement_date_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._announcement_date_epoch = announcement_date_epoch

    @property
    def bulletin_no(self):
        """
        Gets the bulletin_no of this NiaapiDcnmSweol.
        The bulletinno of this software release end of life notice.  

        :return: The bulletin_no of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._bulletin_no

    @bulletin_no.setter
    def bulletin_no(self, bulletin_no):
        """
        Sets the bulletin_no of this NiaapiDcnmSweol.
        The bulletinno of this software release end of life notice.  

        :param bulletin_no: The bulletin_no of this NiaapiDcnmSweol.
        :type: str
        """

        self._bulletin_no = bulletin_no

    @property
    def description(self):
        """
        Gets the description of this NiaapiDcnmSweol.
        The description of this software release end of life notice.  

        :return: The description of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NiaapiDcnmSweol.
        The description of this software release end of life notice.  

        :param description: The description of this NiaapiDcnmSweol.
        :type: str
        """

        self._description = description

    @property
    def endof_new_service_attachment_date(self):
        """
        Gets the endof_new_service_attachment_date of this NiaapiDcnmSweol.
        Date time of End of New service attachment .  

        :return: The endof_new_service_attachment_date of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._endof_new_service_attachment_date

    @endof_new_service_attachment_date.setter
    def endof_new_service_attachment_date(self, endof_new_service_attachment_date):
        """
        Sets the endof_new_service_attachment_date of this NiaapiDcnmSweol.
        Date time of End of New service attachment .  

        :param endof_new_service_attachment_date: The endof_new_service_attachment_date of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._endof_new_service_attachment_date = endof_new_service_attachment_date

    @property
    def endof_new_service_attachment_date_epoch(self):
        """
        Gets the endof_new_service_attachment_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of New service attachment .  

        :return: The endof_new_service_attachment_date_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._endof_new_service_attachment_date_epoch

    @endof_new_service_attachment_date_epoch.setter
    def endof_new_service_attachment_date_epoch(self, endof_new_service_attachment_date_epoch):
        """
        Sets the endof_new_service_attachment_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of New service attachment .  

        :param endof_new_service_attachment_date_epoch: The endof_new_service_attachment_date_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._endof_new_service_attachment_date_epoch = endof_new_service_attachment_date_epoch

    @property
    def endof_service_contract_renewal_date(self):
        """
        Gets the endof_service_contract_renewal_date of this NiaapiDcnmSweol.
        Date time of End of Renewal of service contract .  

        :return: The endof_service_contract_renewal_date of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._endof_service_contract_renewal_date

    @endof_service_contract_renewal_date.setter
    def endof_service_contract_renewal_date(self, endof_service_contract_renewal_date):
        """
        Sets the endof_service_contract_renewal_date of this NiaapiDcnmSweol.
        Date time of End of Renewal of service contract .  

        :param endof_service_contract_renewal_date: The endof_service_contract_renewal_date of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._endof_service_contract_renewal_date = endof_service_contract_renewal_date

    @property
    def endof_service_contract_renewal_date_epoch(self):
        """
        Gets the endof_service_contract_renewal_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of Renewal of service contract .  

        :return: The endof_service_contract_renewal_date_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._endof_service_contract_renewal_date_epoch

    @endof_service_contract_renewal_date_epoch.setter
    def endof_service_contract_renewal_date_epoch(self, endof_service_contract_renewal_date_epoch):
        """
        Sets the endof_service_contract_renewal_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of Renewal of service contract .  

        :param endof_service_contract_renewal_date_epoch: The endof_service_contract_renewal_date_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._endof_service_contract_renewal_date_epoch = endof_service_contract_renewal_date_epoch

    @property
    def endof_sw_maintenance_date(self):
        """
        Gets the endof_sw_maintenance_date of this NiaapiDcnmSweol.
        Date time of End of Maintenance.  

        :return: The endof_sw_maintenance_date of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._endof_sw_maintenance_date

    @endof_sw_maintenance_date.setter
    def endof_sw_maintenance_date(self, endof_sw_maintenance_date):
        """
        Sets the endof_sw_maintenance_date of this NiaapiDcnmSweol.
        Date time of End of Maintenance.  

        :param endof_sw_maintenance_date: The endof_sw_maintenance_date of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._endof_sw_maintenance_date = endof_sw_maintenance_date

    @property
    def endof_sw_maintenance_date_epoch(self):
        """
        Gets the endof_sw_maintenance_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of Maintenance.  

        :return: The endof_sw_maintenance_date_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._endof_sw_maintenance_date_epoch

    @endof_sw_maintenance_date_epoch.setter
    def endof_sw_maintenance_date_epoch(self, endof_sw_maintenance_date_epoch):
        """
        Sets the endof_sw_maintenance_date_epoch of this NiaapiDcnmSweol.
        Epoch time of End of Maintenance.  

        :param endof_sw_maintenance_date_epoch: The endof_sw_maintenance_date_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._endof_sw_maintenance_date_epoch = endof_sw_maintenance_date_epoch

    @property
    def headline(self):
        """
        Gets the headline of this NiaapiDcnmSweol.
        The title of this software release end of life notice.  

        :return: The headline of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this NiaapiDcnmSweol.
        The title of this software release end of life notice.  

        :param headline: The headline of this NiaapiDcnmSweol.
        :type: str
        """

        self._headline = headline

    @property
    def last_dateof_support(self):
        """
        Gets the last_dateof_support of this NiaapiDcnmSweol.
        Date time of Last day of Support .  

        :return: The last_dateof_support of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._last_dateof_support

    @last_dateof_support.setter
    def last_dateof_support(self, last_dateof_support):
        """
        Sets the last_dateof_support of this NiaapiDcnmSweol.
        Date time of Last day of Support .  

        :param last_dateof_support: The last_dateof_support of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._last_dateof_support = last_dateof_support

    @property
    def last_dateof_support_epoch(self):
        """
        Gets the last_dateof_support_epoch of this NiaapiDcnmSweol.
        Epoch time of Last day of Support .  

        :return: The last_dateof_support_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._last_dateof_support_epoch

    @last_dateof_support_epoch.setter
    def last_dateof_support_epoch(self, last_dateof_support_epoch):
        """
        Sets the last_dateof_support_epoch of this NiaapiDcnmSweol.
        Epoch time of Last day of Support .  

        :param last_dateof_support_epoch: The last_dateof_support_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._last_dateof_support_epoch = last_dateof_support_epoch

    @property
    def last_ship_date(self):
        """
        Gets the last_ship_date of this NiaapiDcnmSweol.
        Date time of Lastship Date.  

        :return: The last_ship_date of this NiaapiDcnmSweol.
        :rtype: datetime
        """
        return self._last_ship_date

    @last_ship_date.setter
    def last_ship_date(self, last_ship_date):
        """
        Sets the last_ship_date of this NiaapiDcnmSweol.
        Date time of Lastship Date.  

        :param last_ship_date: The last_ship_date of this NiaapiDcnmSweol.
        :type: datetime
        """

        self._last_ship_date = last_ship_date

    @property
    def last_ship_date_epoch(self):
        """
        Gets the last_ship_date_epoch of this NiaapiDcnmSweol.
        Epoch time of Lastship Date.  

        :return: The last_ship_date_epoch of this NiaapiDcnmSweol.
        :rtype: int
        """
        return self._last_ship_date_epoch

    @last_ship_date_epoch.setter
    def last_ship_date_epoch(self, last_ship_date_epoch):
        """
        Sets the last_ship_date_epoch of this NiaapiDcnmSweol.
        Epoch time of Lastship Date.  

        :param last_ship_date_epoch: The last_ship_date_epoch of this NiaapiDcnmSweol.
        :type: int
        """

        self._last_ship_date_epoch = last_ship_date_epoch

    @property
    def migration_url(self):
        """
        Gets the migration_url of this NiaapiDcnmSweol.
        The URL of this migration notice.  

        :return: The migration_url of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._migration_url

    @migration_url.setter
    def migration_url(self, migration_url):
        """
        Sets the migration_url of this NiaapiDcnmSweol.
        The URL of this migration notice.  

        :param migration_url: The migration_url of this NiaapiDcnmSweol.
        :type: str
        """

        self._migration_url = migration_url

    @property
    def software_eol_url(self):
        """
        Gets the software_eol_url of this NiaapiDcnmSweol.
        Software end of life notice URL link to the notice webpage.   

        :return: The software_eol_url of this NiaapiDcnmSweol.
        :rtype: str
        """
        return self._software_eol_url

    @software_eol_url.setter
    def software_eol_url(self, software_eol_url):
        """
        Sets the software_eol_url of this NiaapiDcnmSweol.
        Software end of life notice URL link to the notice webpage.   

        :param software_eol_url: The software_eol_url of this NiaapiDcnmSweol.
        :type: str
        """

        self._software_eol_url = software_eol_url

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
        if not isinstance(other, NiaapiDcnmSweol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
