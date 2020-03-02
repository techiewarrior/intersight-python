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


class HyperflexAlarm(object):
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
        'acknowledged': 'bool',
        'acknowledged_by': 'str',
        'acknowledged_time': 'int',
        'acknowledged_time_as_utc': 'str',
        'description': 'str',
        'entity_data': 'str',
        'entity_name': 'str',
        'entity_type': 'str',
        'entity_uu_id': 'str',
        'message': 'str',
        'name': 'str',
        'status': 'str',
        'triggered_time': 'int',
        'triggered_time_as_utc': 'str',
        'uuid': 'str',
        'cluster': 'HyperflexClusterRef'
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
        'acknowledged': 'Acknowledged',
        'acknowledged_by': 'AcknowledgedBy',
        'acknowledged_time': 'AcknowledgedTime',
        'acknowledged_time_as_utc': 'AcknowledgedTimeAsUtc',
        'description': 'Description',
        'entity_data': 'EntityData',
        'entity_name': 'EntityName',
        'entity_type': 'EntityType',
        'entity_uu_id': 'EntityUuId',
        'message': 'Message',
        'name': 'Name',
        'status': 'Status',
        'triggered_time': 'TriggeredTime',
        'triggered_time_as_utc': 'TriggeredTimeAsUtc',
        'uuid': 'Uuid',
        'cluster': 'Cluster'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, acknowledged=None, acknowledged_by=None, acknowledged_time=None, acknowledged_time_as_utc=None, description=None, entity_data=None, entity_name=None, entity_type='UNKNOWN', entity_uu_id=None, message=None, name=None, status='UNKNOWN', triggered_time=None, triggered_time_as_utc=None, uuid=None, cluster=None):
        """
        HyperflexAlarm - a model defined in Swagger
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
        self._acknowledged = None
        self._acknowledged_by = None
        self._acknowledged_time = None
        self._acknowledged_time_as_utc = None
        self._description = None
        self._entity_data = None
        self._entity_name = None
        self._entity_type = None
        self._entity_uu_id = None
        self._message = None
        self._name = None
        self._status = None
        self._triggered_time = None
        self._triggered_time_as_utc = None
        self._uuid = None
        self._cluster = None

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
        if acknowledged is not None:
          self.acknowledged = acknowledged
        if acknowledged_by is not None:
          self.acknowledged_by = acknowledged_by
        if acknowledged_time is not None:
          self.acknowledged_time = acknowledged_time
        if acknowledged_time_as_utc is not None:
          self.acknowledged_time_as_utc = acknowledged_time_as_utc
        if description is not None:
          self.description = description
        if entity_data is not None:
          self.entity_data = entity_data
        if entity_name is not None:
          self.entity_name = entity_name
        if entity_type is not None:
          self.entity_type = entity_type
        if entity_uu_id is not None:
          self.entity_uu_id = entity_uu_id
        if message is not None:
          self.message = message
        if name is not None:
          self.name = name
        if status is not None:
          self.status = status
        if triggered_time is not None:
          self.triggered_time = triggered_time
        if triggered_time_as_utc is not None:
          self.triggered_time_as_utc = triggered_time_as_utc
        if uuid is not None:
          self.uuid = uuid
        if cluster is not None:
          self.cluster = cluster

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexAlarm.
        The Account ID for this managed object.

        :return: The account_moid of this HyperflexAlarm.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexAlarm.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this HyperflexAlarm.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexAlarm.
        The time when this managed object was created.

        :return: The create_time of this HyperflexAlarm.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexAlarm.
        The time when this managed object was created.

        :param create_time: The create_time of this HyperflexAlarm.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this HyperflexAlarm.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this HyperflexAlarm.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this HyperflexAlarm.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this HyperflexAlarm.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexAlarm.
        The time when this managed object was last modified.

        :return: The mod_time of this HyperflexAlarm.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexAlarm.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this HyperflexAlarm.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexAlarm.
        The unique identifier of this Managed Object instance.

        :return: The moid of this HyperflexAlarm.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexAlarm.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this HyperflexAlarm.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexAlarm.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this HyperflexAlarm.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexAlarm.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this HyperflexAlarm.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexAlarm.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this HyperflexAlarm.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexAlarm.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this HyperflexAlarm.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this HyperflexAlarm.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this HyperflexAlarm.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this HyperflexAlarm.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this HyperflexAlarm.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexAlarm.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this HyperflexAlarm.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexAlarm.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this HyperflexAlarm.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexAlarm.
        The versioning info for this managed object.

        :return: The version_context of this HyperflexAlarm.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexAlarm.
        The versioning info for this managed object.

        :param version_context: The version_context of this HyperflexAlarm.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexAlarm.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this HyperflexAlarm.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexAlarm.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this HyperflexAlarm.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexAlarm.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this HyperflexAlarm.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexAlarm.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this HyperflexAlarm.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this HyperflexAlarm.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this HyperflexAlarm.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this HyperflexAlarm.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this HyperflexAlarm.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def acknowledged(self):
        """
        Gets the acknowledged of this HyperflexAlarm.

        :return: The acknowledged of this HyperflexAlarm.
        :rtype: bool
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """
        Sets the acknowledged of this HyperflexAlarm.

        :param acknowledged: The acknowledged of this HyperflexAlarm.
        :type: bool
        """

        self._acknowledged = acknowledged

    @property
    def acknowledged_by(self):
        """
        Gets the acknowledged_by of this HyperflexAlarm.

        :return: The acknowledged_by of this HyperflexAlarm.
        :rtype: str
        """
        return self._acknowledged_by

    @acknowledged_by.setter
    def acknowledged_by(self, acknowledged_by):
        """
        Sets the acknowledged_by of this HyperflexAlarm.

        :param acknowledged_by: The acknowledged_by of this HyperflexAlarm.
        :type: str
        """

        self._acknowledged_by = acknowledged_by

    @property
    def acknowledged_time(self):
        """
        Gets the acknowledged_time of this HyperflexAlarm.

        :return: The acknowledged_time of this HyperflexAlarm.
        :rtype: int
        """
        return self._acknowledged_time

    @acknowledged_time.setter
    def acknowledged_time(self, acknowledged_time):
        """
        Sets the acknowledged_time of this HyperflexAlarm.

        :param acknowledged_time: The acknowledged_time of this HyperflexAlarm.
        :type: int
        """

        self._acknowledged_time = acknowledged_time

    @property
    def acknowledged_time_as_utc(self):
        """
        Gets the acknowledged_time_as_utc of this HyperflexAlarm.

        :return: The acknowledged_time_as_utc of this HyperflexAlarm.
        :rtype: str
        """
        return self._acknowledged_time_as_utc

    @acknowledged_time_as_utc.setter
    def acknowledged_time_as_utc(self, acknowledged_time_as_utc):
        """
        Sets the acknowledged_time_as_utc of this HyperflexAlarm.

        :param acknowledged_time_as_utc: The acknowledged_time_as_utc of this HyperflexAlarm.
        :type: str
        """

        self._acknowledged_time_as_utc = acknowledged_time_as_utc

    @property
    def description(self):
        """
        Gets the description of this HyperflexAlarm.

        :return: The description of this HyperflexAlarm.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexAlarm.

        :param description: The description of this HyperflexAlarm.
        :type: str
        """

        self._description = description

    @property
    def entity_data(self):
        """
        Gets the entity_data of this HyperflexAlarm.

        :return: The entity_data of this HyperflexAlarm.
        :rtype: str
        """
        return self._entity_data

    @entity_data.setter
    def entity_data(self, entity_data):
        """
        Sets the entity_data of this HyperflexAlarm.

        :param entity_data: The entity_data of this HyperflexAlarm.
        :type: str
        """

        self._entity_data = entity_data

    @property
    def entity_name(self):
        """
        Gets the entity_name of this HyperflexAlarm.

        :return: The entity_name of this HyperflexAlarm.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this HyperflexAlarm.

        :param entity_name: The entity_name of this HyperflexAlarm.
        :type: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HyperflexAlarm.

        :return: The entity_type of this HyperflexAlarm.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HyperflexAlarm.

        :param entity_type: The entity_type of this HyperflexAlarm.
        :type: str
        """
        allowed_values = ["UNKNOWN", "DISK", "NODE", "CLUSTER", "DATASTORE", "ZONE", "VIRTUALMACHINE"]
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def entity_uu_id(self):
        """
        Gets the entity_uu_id of this HyperflexAlarm.

        :return: The entity_uu_id of this HyperflexAlarm.
        :rtype: str
        """
        return self._entity_uu_id

    @entity_uu_id.setter
    def entity_uu_id(self, entity_uu_id):
        """
        Sets the entity_uu_id of this HyperflexAlarm.

        :param entity_uu_id: The entity_uu_id of this HyperflexAlarm.
        :type: str
        """

        self._entity_uu_id = entity_uu_id

    @property
    def message(self):
        """
        Gets the message of this HyperflexAlarm.

        :return: The message of this HyperflexAlarm.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this HyperflexAlarm.

        :param message: The message of this HyperflexAlarm.
        :type: str
        """

        self._message = message

    @property
    def name(self):
        """
        Gets the name of this HyperflexAlarm.

        :return: The name of this HyperflexAlarm.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexAlarm.

        :param name: The name of this HyperflexAlarm.
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """
        Gets the status of this HyperflexAlarm.

        :return: The status of this HyperflexAlarm.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HyperflexAlarm.

        :param status: The status of this HyperflexAlarm.
        :type: str
        """
        allowed_values = ["UNKNOWN", "CLEARED", "INFO", "WARNING", "CRITICAL"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def triggered_time(self):
        """
        Gets the triggered_time of this HyperflexAlarm.

        :return: The triggered_time of this HyperflexAlarm.
        :rtype: int
        """
        return self._triggered_time

    @triggered_time.setter
    def triggered_time(self, triggered_time):
        """
        Sets the triggered_time of this HyperflexAlarm.

        :param triggered_time: The triggered_time of this HyperflexAlarm.
        :type: int
        """

        self._triggered_time = triggered_time

    @property
    def triggered_time_as_utc(self):
        """
        Gets the triggered_time_as_utc of this HyperflexAlarm.

        :return: The triggered_time_as_utc of this HyperflexAlarm.
        :rtype: str
        """
        return self._triggered_time_as_utc

    @triggered_time_as_utc.setter
    def triggered_time_as_utc(self, triggered_time_as_utc):
        """
        Sets the triggered_time_as_utc of this HyperflexAlarm.

        :param triggered_time_as_utc: The triggered_time_as_utc of this HyperflexAlarm.
        :type: str
        """

        self._triggered_time_as_utc = triggered_time_as_utc

    @property
    def uuid(self):
        """
        Gets the uuid of this HyperflexAlarm.

        :return: The uuid of this HyperflexAlarm.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this HyperflexAlarm.

        :param uuid: The uuid of this HyperflexAlarm.
        :type: str
        """

        self._uuid = uuid

    @property
    def cluster(self):
        """
        Gets the cluster of this HyperflexAlarm.
        A collection of references to the [hyperflex.Cluster](mo://hyperflex.Cluster) Managed Object. When this managed object is deleted, the referenced [hyperflex.Cluster](mo://hyperflex.Cluster) MO unsets its reference to this deleted MO.

        :return: The cluster of this HyperflexAlarm.
        :rtype: HyperflexClusterRef
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """
        Sets the cluster of this HyperflexAlarm.
        A collection of references to the [hyperflex.Cluster](mo://hyperflex.Cluster) Managed Object. When this managed object is deleted, the referenced [hyperflex.Cluster](mo://hyperflex.Cluster) MO unsets its reference to this deleted MO.

        :param cluster: The cluster of this HyperflexAlarm.
        :type: HyperflexClusterRef
        """

        self._cluster = cluster

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
        if not isinstance(other, HyperflexAlarm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
