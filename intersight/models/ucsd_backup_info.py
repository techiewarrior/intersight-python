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


class UcsdBackupInfo(object):
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
        'registered_device': 'AssetDeviceRegistrationRef',
        'backup_file_name': 'str',
        'backup_location': 'str',
        'backup_server_ip': 'str',
        'backup_size': 'int',
        'connectors': 'list[UcsdConnectorPack]',
        'duration': 'int',
        'encryption_key': 'str',
        'failure_reason': 'str',
        'is_purged': 'bool',
        'last_modified': 'datetime',
        'percentage_completion': 'int',
        'product_version': 'str',
        'protocol': 'str',
        'stage_completion': 'str',
        'start_time': 'datetime',
        'status': 'str'
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
        'registered_device': 'RegisteredDevice',
        'backup_file_name': 'BackupFileName',
        'backup_location': 'BackupLocation',
        'backup_server_ip': 'BackupServerIp',
        'backup_size': 'BackupSize',
        'connectors': 'Connectors',
        'duration': 'Duration',
        'encryption_key': 'EncryptionKey',
        'failure_reason': 'FailureReason',
        'is_purged': 'IsPurged',
        'last_modified': 'LastModified',
        'percentage_completion': 'PercentageCompletion',
        'product_version': 'ProductVersion',
        'protocol': 'Protocol',
        'stage_completion': 'StageCompletion',
        'start_time': 'StartTime',
        'status': 'Status'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, registered_device=None, backup_file_name=None, backup_location=None, backup_server_ip=None, backup_size=None, connectors=None, duration=None, encryption_key=None, failure_reason=None, is_purged=None, last_modified=None, percentage_completion=None, product_version=None, protocol=None, stage_completion=None, start_time=None, status=None):
        """
        UcsdBackupInfo - a model defined in Swagger
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
        self._registered_device = None
        self._backup_file_name = None
        self._backup_location = None
        self._backup_server_ip = None
        self._backup_size = None
        self._connectors = None
        self._duration = None
        self._encryption_key = None
        self._failure_reason = None
        self._is_purged = None
        self._last_modified = None
        self._percentage_completion = None
        self._product_version = None
        self._protocol = None
        self._stage_completion = None
        self._start_time = None
        self._status = None

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
        if registered_device is not None:
          self.registered_device = registered_device
        if backup_file_name is not None:
          self.backup_file_name = backup_file_name
        if backup_location is not None:
          self.backup_location = backup_location
        if backup_server_ip is not None:
          self.backup_server_ip = backup_server_ip
        if backup_size is not None:
          self.backup_size = backup_size
        if connectors is not None:
          self.connectors = connectors
        if duration is not None:
          self.duration = duration
        if encryption_key is not None:
          self.encryption_key = encryption_key
        if failure_reason is not None:
          self.failure_reason = failure_reason
        if is_purged is not None:
          self.is_purged = is_purged
        if last_modified is not None:
          self.last_modified = last_modified
        if percentage_completion is not None:
          self.percentage_completion = percentage_completion
        if product_version is not None:
          self.product_version = product_version
        if protocol is not None:
          self.protocol = protocol
        if stage_completion is not None:
          self.stage_completion = stage_completion
        if start_time is not None:
          self.start_time = start_time
        if status is not None:
          self.status = status

    @property
    def account_moid(self):
        """
        Gets the account_moid of this UcsdBackupInfo.
        The Account ID for this managed object.

        :return: The account_moid of this UcsdBackupInfo.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this UcsdBackupInfo.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this UcsdBackupInfo.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this UcsdBackupInfo.
        The time when this managed object was created.

        :return: The create_time of this UcsdBackupInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this UcsdBackupInfo.
        The time when this managed object was created.

        :param create_time: The create_time of this UcsdBackupInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this UcsdBackupInfo.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this UcsdBackupInfo.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this UcsdBackupInfo.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this UcsdBackupInfo.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this UcsdBackupInfo.
        The time when this managed object was last modified.

        :return: The mod_time of this UcsdBackupInfo.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this UcsdBackupInfo.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this UcsdBackupInfo.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this UcsdBackupInfo.
        The unique identifier of this Managed Object instance.

        :return: The moid of this UcsdBackupInfo.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this UcsdBackupInfo.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this UcsdBackupInfo.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this UcsdBackupInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this UcsdBackupInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this UcsdBackupInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this UcsdBackupInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this UcsdBackupInfo.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this UcsdBackupInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this UcsdBackupInfo.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this UcsdBackupInfo.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this UcsdBackupInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this UcsdBackupInfo.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this UcsdBackupInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this UcsdBackupInfo.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this UcsdBackupInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this UcsdBackupInfo.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UcsdBackupInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this UcsdBackupInfo.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this UcsdBackupInfo.
        The versioning info for this managed object.

        :return: The version_context of this UcsdBackupInfo.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this UcsdBackupInfo.
        The versioning info for this managed object.

        :param version_context: The version_context of this UcsdBackupInfo.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this UcsdBackupInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this UcsdBackupInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this UcsdBackupInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this UcsdBackupInfo.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this UcsdBackupInfo.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this UcsdBackupInfo.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this UcsdBackupInfo.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this UcsdBackupInfo.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this UcsdBackupInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this UcsdBackupInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this UcsdBackupInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this UcsdBackupInfo.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def registered_device(self):
        """
        Gets the registered_device of this UcsdBackupInfo.
        The device for which backup has been created.

        :return: The registered_device of this UcsdBackupInfo.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this UcsdBackupInfo.
        The device for which backup has been created.

        :param registered_device: The registered_device of this UcsdBackupInfo.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def backup_file_name(self):
        """
        Gets the backup_file_name of this UcsdBackupInfo.
        Auto generated backup File Name with combination of file prefix given an user input and the timestamp.

        :return: The backup_file_name of this UcsdBackupInfo.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """
        Sets the backup_file_name of this UcsdBackupInfo.
        Auto generated backup File Name with combination of file prefix given an user input and the timestamp.

        :param backup_file_name: The backup_file_name of this UcsdBackupInfo.
        :type: str
        """

        self._backup_file_name = backup_file_name

    @property
    def backup_location(self):
        """
        Gets the backup_location of this UcsdBackupInfo.
        Backup location that contains the backup images for end device which can be used for restore operation.

        :return: The backup_location of this UcsdBackupInfo.
        :rtype: str
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """
        Sets the backup_location of this UcsdBackupInfo.
        Backup location that contains the backup images for end device which can be used for restore operation.

        :param backup_location: The backup_location of this UcsdBackupInfo.
        :type: str
        """

        self._backup_location = backup_location

    @property
    def backup_server_ip(self):
        """
        Gets the backup_server_ip of this UcsdBackupInfo.
        Backup server where backup images are maintained.

        :return: The backup_server_ip of this UcsdBackupInfo.
        :rtype: str
        """
        return self._backup_server_ip

    @backup_server_ip.setter
    def backup_server_ip(self, backup_server_ip):
        """
        Sets the backup_server_ip of this UcsdBackupInfo.
        Backup server where backup images are maintained.

        :param backup_server_ip: The backup_server_ip of this UcsdBackupInfo.
        :type: str
        """

        self._backup_server_ip = backup_server_ip

    @property
    def backup_size(self):
        """
        Gets the backup_size of this UcsdBackupInfo.
        Size of the backup image in bytes.

        :return: The backup_size of this UcsdBackupInfo.
        :rtype: int
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """
        Sets the backup_size of this UcsdBackupInfo.
        Size of the backup image in bytes.

        :param backup_size: The backup_size of this UcsdBackupInfo.
        :type: int
        """

        self._backup_size = backup_size

    @property
    def connectors(self):
        """
        Gets the connectors of this UcsdBackupInfo.
        Connector pack versions that are active on the UCS Director when this backup image was taken.

        :return: The connectors of this UcsdBackupInfo.
        :rtype: list[UcsdConnectorPack]
        """
        return self._connectors

    @connectors.setter
    def connectors(self, connectors):
        """
        Sets the connectors of this UcsdBackupInfo.
        Connector pack versions that are active on the UCS Director when this backup image was taken.

        :param connectors: The connectors of this UcsdBackupInfo.
        :type: list[UcsdConnectorPack]
        """

        self._connectors = connectors

    @property
    def duration(self):
        """
        Gets the duration of this UcsdBackupInfo.
        Time taken for the backup to be completed.

        :return: The duration of this UcsdBackupInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this UcsdBackupInfo.
        Time taken for the backup to be completed.

        :param duration: The duration of this UcsdBackupInfo.
        :type: int
        """

        self._duration = duration

    @property
    def encryption_key(self):
        """
        Gets the encryption_key of this UcsdBackupInfo.
        The key used for encrypting the backup file.

        :return: The encryption_key of this UcsdBackupInfo.
        :rtype: str
        """
        return self._encryption_key

    @encryption_key.setter
    def encryption_key(self, encryption_key):
        """
        Sets the encryption_key of this UcsdBackupInfo.
        The key used for encrypting the backup file.

        :param encryption_key: The encryption_key of this UcsdBackupInfo.
        :type: str
        """

        self._encryption_key = encryption_key

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this UcsdBackupInfo.
        Reason for backup failure.

        :return: The failure_reason of this UcsdBackupInfo.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this UcsdBackupInfo.
        Reason for backup failure.

        :param failure_reason: The failure_reason of this UcsdBackupInfo.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def is_purged(self):
        """
        Gets the is_purged of this UcsdBackupInfo.
        Backup image got purged or not. The backup images get purged based on the retention count set by the user in the backup config policy.

        :return: The is_purged of this UcsdBackupInfo.
        :rtype: bool
        """
        return self._is_purged

    @is_purged.setter
    def is_purged(self, is_purged):
        """
        Sets the is_purged of this UcsdBackupInfo.
        Backup image got purged or not. The backup images get purged based on the retention count set by the user in the backup config policy.

        :param is_purged: The is_purged of this UcsdBackupInfo.
        :type: bool
        """

        self._is_purged = is_purged

    @property
    def last_modified(self):
        """
        Gets the last_modified of this UcsdBackupInfo.
        Last modified time when this backup record got updated.

        :return: The last_modified of this UcsdBackupInfo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this UcsdBackupInfo.
        Last modified time when this backup record got updated.

        :param last_modified: The last_modified of this UcsdBackupInfo.
        :type: datetime
        """

        self._last_modified = last_modified

    @property
    def percentage_completion(self):
        """
        Gets the percentage_completion of this UcsdBackupInfo.
        Backup current precentage completion status information.

        :return: The percentage_completion of this UcsdBackupInfo.
        :rtype: int
        """
        return self._percentage_completion

    @percentage_completion.setter
    def percentage_completion(self, percentage_completion):
        """
        Sets the percentage_completion of this UcsdBackupInfo.
        Backup current precentage completion status information.

        :param percentage_completion: The percentage_completion of this UcsdBackupInfo.
        :type: int
        """

        self._percentage_completion = percentage_completion

    @property
    def product_version(self):
        """
        Gets the product_version of this UcsdBackupInfo.
        The end device product version when the backup image was taken.

        :return: The product_version of this UcsdBackupInfo.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this UcsdBackupInfo.
        The end device product version when the backup image was taken.

        :param product_version: The product_version of this UcsdBackupInfo.
        :type: str
        """

        self._product_version = product_version

    @property
    def protocol(self):
        """
        Gets the protocol of this UcsdBackupInfo.
        Protocol used for the remote backup. possible values are FTP, SCP and SFTP. Not applicable for the localhost (127.0.0.1).

        :return: The protocol of this UcsdBackupInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UcsdBackupInfo.
        Protocol used for the remote backup. possible values are FTP, SCP and SFTP. Not applicable for the localhost (127.0.0.1).

        :param protocol: The protocol of this UcsdBackupInfo.
        :type: str
        """

        self._protocol = protocol

    @property
    def stage_completion(self):
        """
        Gets the stage_completion of this UcsdBackupInfo.
        Backup current status stage information.

        :return: The stage_completion of this UcsdBackupInfo.
        :rtype: str
        """
        return self._stage_completion

    @stage_completion.setter
    def stage_completion(self, stage_completion):
        """
        Sets the stage_completion of this UcsdBackupInfo.
        Backup current status stage information.

        :param stage_completion: The stage_completion of this UcsdBackupInfo.
        :type: str
        """

        self._stage_completion = stage_completion

    @property
    def start_time(self):
        """
        Gets the start_time of this UcsdBackupInfo.
        Start time of backup when it got initiated.

        :return: The start_time of this UcsdBackupInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this UcsdBackupInfo.
        Start time of backup when it got initiated.

        :param start_time: The start_time of this UcsdBackupInfo.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """
        Gets the status of this UcsdBackupInfo.
        Current status of Backup current.

        :return: The status of this UcsdBackupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UcsdBackupInfo.
        Current status of Backup current.

        :param status: The status of this UcsdBackupInfo.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, UcsdBackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
