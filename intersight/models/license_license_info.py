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


class LicenseLicenseInfo(object):
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
        'active_admin': 'bool',
        'days_left': 'int',
        'end_time': 'datetime',
        'enforce_mode': 'str',
        'error_desc': 'str',
        'evaluation_period': 'int',
        'extra_evaluation': 'int',
        'license_count': 'int',
        'license_state': 'str',
        'license_type': 'str',
        'start_time': 'datetime',
        'trial_admin': 'bool',
        'account_license_data': 'LicenseAccountLicenseDataRef'
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
        'active_admin': 'ActiveAdmin',
        'days_left': 'DaysLeft',
        'end_time': 'EndTime',
        'enforce_mode': 'EnforceMode',
        'error_desc': 'ErrorDesc',
        'evaluation_period': 'EvaluationPeriod',
        'extra_evaluation': 'ExtraEvaluation',
        'license_count': 'LicenseCount',
        'license_state': 'LicenseState',
        'license_type': 'LicenseType',
        'start_time': 'StartTime',
        'trial_admin': 'TrialAdmin',
        'account_license_data': 'AccountLicenseData'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, active_admin=None, days_left=None, end_time=None, enforce_mode=None, error_desc=None, evaluation_period=None, extra_evaluation=None, license_count=None, license_state='NotLicensed', license_type='Base', start_time=None, trial_admin=None, account_license_data=None):
        """
        LicenseLicenseInfo - a model defined in Swagger
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
        self._active_admin = None
        self._days_left = None
        self._end_time = None
        self._enforce_mode = None
        self._error_desc = None
        self._evaluation_period = None
        self._extra_evaluation = None
        self._license_count = None
        self._license_state = None
        self._license_type = None
        self._start_time = None
        self._trial_admin = None
        self._account_license_data = None

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
        if active_admin is not None:
          self.active_admin = active_admin
        if days_left is not None:
          self.days_left = days_left
        if end_time is not None:
          self.end_time = end_time
        if enforce_mode is not None:
          self.enforce_mode = enforce_mode
        if error_desc is not None:
          self.error_desc = error_desc
        if evaluation_period is not None:
          self.evaluation_period = evaluation_period
        if extra_evaluation is not None:
          self.extra_evaluation = extra_evaluation
        if license_count is not None:
          self.license_count = license_count
        if license_state is not None:
          self.license_state = license_state
        if license_type is not None:
          self.license_type = license_type
        if start_time is not None:
          self.start_time = start_time
        if trial_admin is not None:
          self.trial_admin = trial_admin
        if account_license_data is not None:
          self.account_license_data = account_license_data

    @property
    def account_moid(self):
        """
        Gets the account_moid of this LicenseLicenseInfo.
        The Account ID for this managed object.  

        :return: The account_moid of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this LicenseLicenseInfo.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this LicenseLicenseInfo.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this LicenseLicenseInfo.
        The time when this managed object was created.  

        :return: The create_time of this LicenseLicenseInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this LicenseLicenseInfo.
        The time when this managed object was created.  

        :param create_time: The create_time of this LicenseLicenseInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this LicenseLicenseInfo.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this LicenseLicenseInfo.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this LicenseLicenseInfo.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this LicenseLicenseInfo.
        The time when this managed object was last modified.  

        :return: The mod_time of this LicenseLicenseInfo.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this LicenseLicenseInfo.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this LicenseLicenseInfo.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this LicenseLicenseInfo.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this LicenseLicenseInfo.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this LicenseLicenseInfo.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this LicenseLicenseInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this LicenseLicenseInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this LicenseLicenseInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this LicenseLicenseInfo.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this LicenseLicenseInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this LicenseLicenseInfo.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this LicenseLicenseInfo.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this LicenseLicenseInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this LicenseLicenseInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this LicenseLicenseInfo.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this LicenseLicenseInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this LicenseLicenseInfo.
        :rtype: list[MoOptionalTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this LicenseLicenseInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this LicenseLicenseInfo.
        :type: list[MoOptionalTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this LicenseLicenseInfo.
        The versioning info for this managed object.   

        :return: The version_context of this LicenseLicenseInfo.
        :rtype: MoOptionalVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this LicenseLicenseInfo.
        The versioning info for this managed object.   

        :param version_context: The version_context of this LicenseLicenseInfo.
        :type: MoOptionalVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this LicenseLicenseInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this LicenseLicenseInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this LicenseLicenseInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this LicenseLicenseInfo.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this LicenseLicenseInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this LicenseLicenseInfo.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this LicenseLicenseInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this LicenseLicenseInfo.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this LicenseLicenseInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this LicenseLicenseInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this LicenseLicenseInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this LicenseLicenseInfo.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def active_admin(self):
        """
        Gets the active_admin of this LicenseLicenseInfo.
        The license administrative state.  Set this property to 'true' to activate the license entitlements.   

        :return: The active_admin of this LicenseLicenseInfo.
        :rtype: bool
        """
        return self._active_admin

    @active_admin.setter
    def active_admin(self, active_admin):
        """
        Sets the active_admin of this LicenseLicenseInfo.
        The license administrative state.  Set this property to 'true' to activate the license entitlements.   

        :param active_admin: The active_admin of this LicenseLicenseInfo.
        :type: bool
        """

        self._active_admin = active_admin

    @property
    def days_left(self):
        """
        Gets the days_left of this LicenseLicenseInfo.
        The number of days left for licenseState to stay in TrialPeriod or OutOfCompliance state.  

        :return: The days_left of this LicenseLicenseInfo.
        :rtype: int
        """
        return self._days_left

    @days_left.setter
    def days_left(self, days_left):
        """
        Sets the days_left of this LicenseLicenseInfo.
        The number of days left for licenseState to stay in TrialPeriod or OutOfCompliance state.  

        :param days_left: The days_left of this LicenseLicenseInfo.
        :type: int
        """

        self._days_left = days_left

    @property
    def end_time(self):
        """
        Gets the end_time of this LicenseLicenseInfo.
        The date and time when the trial period expires.  The value of the 'endTime' property is set when the account enters the TrialPeriod or OutOfCompliance state.   

        :return: The end_time of this LicenseLicenseInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this LicenseLicenseInfo.
        The date and time when the trial period expires.  The value of the 'endTime' property is set when the account enters the TrialPeriod or OutOfCompliance state.   

        :param end_time: The end_time of this LicenseLicenseInfo.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def enforce_mode(self):
        """
        Gets the enforce_mode of this LicenseLicenseInfo.
        The entitlement mode reported by Cisco Smart Software Manager.  

        :return: The enforce_mode of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._enforce_mode

    @enforce_mode.setter
    def enforce_mode(self, enforce_mode):
        """
        Sets the enforce_mode of this LicenseLicenseInfo.
        The entitlement mode reported by Cisco Smart Software Manager.  

        :param enforce_mode: The enforce_mode of this LicenseLicenseInfo.
        :type: str
        """

        self._enforce_mode = enforce_mode

    @property
    def error_desc(self):
        """
        Gets the error_desc of this LicenseLicenseInfo.
        The detailed error message when there is any error related to this licensing entitlement.  

        :return: The error_desc of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._error_desc

    @error_desc.setter
    def error_desc(self, error_desc):
        """
        Sets the error_desc of this LicenseLicenseInfo.
        The detailed error message when there is any error related to this licensing entitlement.  

        :param error_desc: The error_desc of this LicenseLicenseInfo.
        :type: str
        """

        self._error_desc = error_desc

    @property
    def evaluation_period(self):
        """
        Gets the evaluation_period of this LicenseLicenseInfo.
        The default Trial or Grace period customer is entitled to.  

        :return: The evaluation_period of this LicenseLicenseInfo.
        :rtype: int
        """
        return self._evaluation_period

    @evaluation_period.setter
    def evaluation_period(self, evaluation_period):
        """
        Sets the evaluation_period of this LicenseLicenseInfo.
        The default Trial or Grace period customer is entitled to.  

        :param evaluation_period: The evaluation_period of this LicenseLicenseInfo.
        :type: int
        """

        self._evaluation_period = evaluation_period

    @property
    def extra_evaluation(self):
        """
        Gets the extra_evaluation of this LicenseLicenseInfo.
        The number of days the trial Trial or Grace period is extended.  The trial or grace period can be extended once.   

        :return: The extra_evaluation of this LicenseLicenseInfo.
        :rtype: int
        """
        return self._extra_evaluation

    @extra_evaluation.setter
    def extra_evaluation(self, extra_evaluation):
        """
        Sets the extra_evaluation of this LicenseLicenseInfo.
        The number of days the trial Trial or Grace period is extended.  The trial or grace period can be extended once.   

        :param extra_evaluation: The extra_evaluation of this LicenseLicenseInfo.
        :type: int
        """

        self._extra_evaluation = extra_evaluation

    @property
    def license_count(self):
        """
        Gets the license_count of this LicenseLicenseInfo.
        The total number of devices claimed in the Intersight account.  

        :return: The license_count of this LicenseLicenseInfo.
        :rtype: int
        """
        return self._license_count

    @license_count.setter
    def license_count(self, license_count):
        """
        Sets the license_count of this LicenseLicenseInfo.
        The total number of devices claimed in the Intersight account.  

        :param license_count: The license_count of this LicenseLicenseInfo.
        :type: int
        """

        self._license_count = license_count

    @property
    def license_state(self):
        """
        Gets the license_state of this LicenseLicenseInfo.
        The license state defined by Intersight.  The value may be one of NotLicensed, TrialPeriod, OutOfCompliance, Compliance, GraceExpired, or TrialExpired.   

        :return: The license_state of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._license_state

    @license_state.setter
    def license_state(self, license_state):
        """
        Sets the license_state of this LicenseLicenseInfo.
        The license state defined by Intersight.  The value may be one of NotLicensed, TrialPeriod, OutOfCompliance, Compliance, GraceExpired, or TrialExpired.   

        :param license_state: The license_state of this LicenseLicenseInfo.
        :type: str
        """
        allowed_values = ["NotLicensed", "GraceExpired", "TrialPeriod", "OutOfCompliance", "Compliance", "TrialExpired"]
        if license_state not in allowed_values:
            raise ValueError(
                "Invalid value for `license_state` ({0}), must be one of {1}"
                .format(license_state, allowed_values)
            )

        self._license_state = license_state

    @property
    def license_type(self):
        """
        Gets the license_type of this LicenseLicenseInfo.
        The name of the Intersight license entitlement. For example, this property may be set to 'Essential'.   

        :return: The license_type of this LicenseLicenseInfo.
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """
        Sets the license_type of this LicenseLicenseInfo.
        The name of the Intersight license entitlement. For example, this property may be set to 'Essential'.   

        :param license_type: The license_type of this LicenseLicenseInfo.
        :type: str
        """
        allowed_values = ["Base", "Essential", "Standard", "Advantage", "Premier"]
        if license_type not in allowed_values:
            raise ValueError(
                "Invalid value for `license_type` ({0}), must be one of {1}"
                .format(license_type, allowed_values)
            )

        self._license_type = license_type

    @property
    def start_time(self):
        """
        Gets the start_time of this LicenseLicenseInfo.
        The date and time when the licenseState entered the TrialPeriod or OutOfCompliance state.  

        :return: The start_time of this LicenseLicenseInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this LicenseLicenseInfo.
        The date and time when the licenseState entered the TrialPeriod or OutOfCompliance state.  

        :param start_time: The start_time of this LicenseLicenseInfo.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def trial_admin(self):
        """
        Gets the trial_admin of this LicenseLicenseInfo.
        The administrative state of the trial license.  When the LicenseState is set to 'NotLicensed', 'trialAdmin' can be set to true to start the trial period, i.e. licenseState is set to be TrialPeriod.    

        :return: The trial_admin of this LicenseLicenseInfo.
        :rtype: bool
        """
        return self._trial_admin

    @trial_admin.setter
    def trial_admin(self, trial_admin):
        """
        Sets the trial_admin of this LicenseLicenseInfo.
        The administrative state of the trial license.  When the LicenseState is set to 'NotLicensed', 'trialAdmin' can be set to true to start the trial period, i.e. licenseState is set to be TrialPeriod.    

        :param trial_admin: The trial_admin of this LicenseLicenseInfo.
        :type: bool
        """

        self._trial_admin = trial_admin

    @property
    def account_license_data(self):
        """
        Gets the account_license_data of this LicenseLicenseInfo.
        A collection of references to the [license.AccountLicenseData](mo://license.AccountLicenseData) Managed Object.  When this managed object is deleted, the referenced [license.AccountLicenseData](mo://license.AccountLicenseData) MO unsets its reference to this deleted MO. 

        :return: The account_license_data of this LicenseLicenseInfo.
        :rtype: LicenseAccountLicenseDataRef
        """
        return self._account_license_data

    @account_license_data.setter
    def account_license_data(self, account_license_data):
        """
        Sets the account_license_data of this LicenseLicenseInfo.
        A collection of references to the [license.AccountLicenseData](mo://license.AccountLicenseData) Managed Object.  When this managed object is deleted, the referenced [license.AccountLicenseData](mo://license.AccountLicenseData) MO unsets its reference to this deleted MO. 

        :param account_license_data: The account_license_data of this LicenseLicenseInfo.
        :type: LicenseAccountLicenseDataRef
        """

        self._account_license_data = account_license_data

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
        if not isinstance(other, LicenseLicenseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
