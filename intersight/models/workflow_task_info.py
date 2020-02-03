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


class WorkflowTaskInfo(object):
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
        'end_time': 'datetime',
        'failure_reason': 'str',
        'input': 'object',
        'inst_id': 'str',
        'internal': 'bool',
        'label': 'str',
        'message': 'list[WorkflowMessage]',
        'name': 'str',
        'output': 'object',
        'ref_name': 'str',
        'retry_count': 'int',
        'start_time': 'datetime',
        'status': 'str',
        'task_inst_id_list': 'list[WorkflowTaskRetryInfo]',
        'sub_workflow_info': 'WorkflowWorkflowInfoRef',
        'task_definition': 'WorkflowTaskDefinitionRef',
        'workflow_info': 'WorkflowWorkflowInfoRef'
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
        'end_time': 'EndTime',
        'failure_reason': 'FailureReason',
        'input': 'Input',
        'inst_id': 'InstId',
        'internal': 'Internal',
        'label': 'Label',
        'message': 'Message',
        'name': 'Name',
        'output': 'Output',
        'ref_name': 'RefName',
        'retry_count': 'RetryCount',
        'start_time': 'StartTime',
        'status': 'Status',
        'task_inst_id_list': 'TaskInstIdList',
        'sub_workflow_info': 'SubWorkflowInfo',
        'task_definition': 'TaskDefinition',
        'workflow_info': 'WorkflowInfo'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, end_time=None, failure_reason=None, input=None, inst_id=None, internal=None, label=None, message=None, name=None, output=None, ref_name=None, retry_count=None, start_time=None, status=None, task_inst_id_list=None, sub_workflow_info=None, task_definition=None, workflow_info=None):
        """
        WorkflowTaskInfo - a model defined in Swagger
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
        self._end_time = None
        self._failure_reason = None
        self._input = None
        self._inst_id = None
        self._internal = None
        self._label = None
        self._message = None
        self._name = None
        self._output = None
        self._ref_name = None
        self._retry_count = None
        self._start_time = None
        self._status = None
        self._task_inst_id_list = None
        self._sub_workflow_info = None
        self._task_definition = None
        self._workflow_info = None

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
        if end_time is not None:
          self.end_time = end_time
        if failure_reason is not None:
          self.failure_reason = failure_reason
        if input is not None:
          self.input = input
        if inst_id is not None:
          self.inst_id = inst_id
        if internal is not None:
          self.internal = internal
        if label is not None:
          self.label = label
        if message is not None:
          self.message = message
        if name is not None:
          self.name = name
        if output is not None:
          self.output = output
        if ref_name is not None:
          self.ref_name = ref_name
        if retry_count is not None:
          self.retry_count = retry_count
        if start_time is not None:
          self.start_time = start_time
        if status is not None:
          self.status = status
        if task_inst_id_list is not None:
          self.task_inst_id_list = task_inst_id_list
        if sub_workflow_info is not None:
          self.sub_workflow_info = sub_workflow_info
        if task_definition is not None:
          self.task_definition = task_definition
        if workflow_info is not None:
          self.workflow_info = workflow_info

    @property
    def account_moid(self):
        """
        Gets the account_moid of this WorkflowTaskInfo.
        The Account ID for this managed object.  

        :return: The account_moid of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this WorkflowTaskInfo.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this WorkflowTaskInfo.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this WorkflowTaskInfo.
        The time when this managed object was created.  

        :return: The create_time of this WorkflowTaskInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this WorkflowTaskInfo.
        The time when this managed object was created.  

        :param create_time: The create_time of this WorkflowTaskInfo.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this WorkflowTaskInfo.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this WorkflowTaskInfo.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this WorkflowTaskInfo.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this WorkflowTaskInfo.
        The time when this managed object was last modified.  

        :return: The mod_time of this WorkflowTaskInfo.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this WorkflowTaskInfo.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this WorkflowTaskInfo.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this WorkflowTaskInfo.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this WorkflowTaskInfo.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this WorkflowTaskInfo.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowTaskInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowTaskInfo.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this WorkflowTaskInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this WorkflowTaskInfo.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this WorkflowTaskInfo.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WorkflowTaskInfo.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this WorkflowTaskInfo.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this WorkflowTaskInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this WorkflowTaskInfo.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this WorkflowTaskInfo.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this WorkflowTaskInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this WorkflowTaskInfo.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this WorkflowTaskInfo.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this WorkflowTaskInfo.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this WorkflowTaskInfo.
        The versioning info for this managed object.   

        :return: The version_context of this WorkflowTaskInfo.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this WorkflowTaskInfo.
        The versioning info for this managed object.   

        :param version_context: The version_context of this WorkflowTaskInfo.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this WorkflowTaskInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this WorkflowTaskInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this WorkflowTaskInfo.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this WorkflowTaskInfo.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this WorkflowTaskInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this WorkflowTaskInfo.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this WorkflowTaskInfo.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this WorkflowTaskInfo.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this WorkflowTaskInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this WorkflowTaskInfo.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this WorkflowTaskInfo.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this WorkflowTaskInfo.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this WorkflowTaskInfo.
        The task description and this is the description that was added when the task was included into the workflow.  

        :return: The description of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowTaskInfo.
        The task description and this is the description that was added when the task was included into the workflow.  

        :param description: The description of this WorkflowTaskInfo.
        :type: str
        """

        self._description = description

    @property
    def end_time(self):
        """
        Gets the end_time of this WorkflowTaskInfo.
        The time stamp when the task reached a final state.  

        :return: The end_time of this WorkflowTaskInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this WorkflowTaskInfo.
        The time stamp when the task reached a final state.  

        :param end_time: The end_time of this WorkflowTaskInfo.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def failure_reason(self):
        """
        Gets the failure_reason of this WorkflowTaskInfo.
        Description of the reason why the task failed.  

        :return: The failure_reason of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """
        Sets the failure_reason of this WorkflowTaskInfo.
        Description of the reason why the task failed.  

        :param failure_reason: The failure_reason of this WorkflowTaskInfo.
        :type: str
        """

        self._failure_reason = failure_reason

    @property
    def input(self):
        """
        Gets the input of this WorkflowTaskInfo.
        The input data that was sent to the task at the start of execution.  

        :return: The input of this WorkflowTaskInfo.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """
        Sets the input of this WorkflowTaskInfo.
        The input data that was sent to the task at the start of execution.  

        :param input: The input of this WorkflowTaskInfo.
        :type: object
        """

        self._input = input

    @property
    def inst_id(self):
        """
        Gets the inst_id of this WorkflowTaskInfo.
        The current running task instance Id.  

        :return: The inst_id of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._inst_id

    @inst_id.setter
    def inst_id(self, inst_id):
        """
        Sets the inst_id of this WorkflowTaskInfo.
        The current running task instance Id.  

        :param inst_id: The inst_id of this WorkflowTaskInfo.
        :type: str
        """

        self._inst_id = inst_id

    @property
    def internal(self):
        """
        Gets the internal of this WorkflowTaskInfo.
        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.  

        :return: The internal of this WorkflowTaskInfo.
        :rtype: bool
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """
        Sets the internal of this WorkflowTaskInfo.
        Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow.  

        :param internal: The internal of this WorkflowTaskInfo.
        :type: bool
        """

        self._internal = internal

    @property
    def label(self):
        """
        Gets the label of this WorkflowTaskInfo.
        User friendly short label to describe this task instance in the workflow.  

        :return: The label of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WorkflowTaskInfo.
        User friendly short label to describe this task instance in the workflow.  

        :param label: The label of this WorkflowTaskInfo.
        :type: str
        """

        self._label = label

    @property
    def message(self):
        """
        Gets the message of this WorkflowTaskInfo.
        Collection of Task execution messages with severity.  

        :return: The message of this WorkflowTaskInfo.
        :rtype: list[WorkflowMessage]
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkflowTaskInfo.
        Collection of Task execution messages with severity.  

        :param message: The message of this WorkflowTaskInfo.
        :type: list[WorkflowMessage]
        """

        self._message = message

    @property
    def name(self):
        """
        Gets the name of this WorkflowTaskInfo.
        Task definition name which specifies the task type.  

        :return: The name of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowTaskInfo.
        Task definition name which specifies the task type.  

        :param name: The name of this WorkflowTaskInfo.
        :type: str
        """

        self._name = name

    @property
    def output(self):
        """
        Gets the output of this WorkflowTaskInfo.
        The output data that was generated by this task.  

        :return: The output of this WorkflowTaskInfo.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """
        Sets the output of this WorkflowTaskInfo.
        The output data that was generated by this task.  

        :param output: The output of this WorkflowTaskInfo.
        :type: object
        """

        self._output = output

    @property
    def ref_name(self):
        """
        Gets the ref_name of this WorkflowTaskInfo.
        The task reference name to ensure its unique inside a workflow.  

        :return: The ref_name of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """
        Sets the ref_name of this WorkflowTaskInfo.
        The task reference name to ensure its unique inside a workflow.  

        :param ref_name: The ref_name of this WorkflowTaskInfo.
        :type: str
        """

        self._ref_name = ref_name

    @property
    def retry_count(self):
        """
        Gets the retry_count of this WorkflowTaskInfo.
        A counter for number of retries.  

        :return: The retry_count of this WorkflowTaskInfo.
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """
        Sets the retry_count of this WorkflowTaskInfo.
        A counter for number of retries.  

        :param retry_count: The retry_count of this WorkflowTaskInfo.
        :type: int
        """

        self._retry_count = retry_count

    @property
    def start_time(self):
        """
        Gets the start_time of this WorkflowTaskInfo.
        The time stamp when the task started execution.  

        :return: The start_time of this WorkflowTaskInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this WorkflowTaskInfo.
        The time stamp when the task started execution.  

        :param start_time: The start_time of this WorkflowTaskInfo.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def status(self):
        """
        Gets the status of this WorkflowTaskInfo.
        The status of the task and this will specify if the task is running or has reached a final state.  

        :return: The status of this WorkflowTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkflowTaskInfo.
        The status of the task and this will specify if the task is running or has reached a final state.  

        :param status: The status of this WorkflowTaskInfo.
        :type: str
        """

        self._status = status

    @property
    def task_inst_id_list(self):
        """
        Gets the task_inst_id_list of this WorkflowTaskInfo.
        The list keeps a list of retried task instances.   

        :return: The task_inst_id_list of this WorkflowTaskInfo.
        :rtype: list[WorkflowTaskRetryInfo]
        """
        return self._task_inst_id_list

    @task_inst_id_list.setter
    def task_inst_id_list(self, task_inst_id_list):
        """
        Sets the task_inst_id_list of this WorkflowTaskInfo.
        The list keeps a list of retried task instances.   

        :param task_inst_id_list: The task_inst_id_list of this WorkflowTaskInfo.
        :type: list[WorkflowTaskRetryInfo]
        """

        self._task_inst_id_list = task_inst_id_list

    @property
    def sub_workflow_info(self):
        """
        Gets the sub_workflow_info of this WorkflowTaskInfo.
        A collection of references to the [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) Managed Object.  When this managed object is deleted, the referenced [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) MO unsets its reference to this deleted MO. 

        :return: The sub_workflow_info of this WorkflowTaskInfo.
        :rtype: WorkflowWorkflowInfoRef
        """
        return self._sub_workflow_info

    @sub_workflow_info.setter
    def sub_workflow_info(self, sub_workflow_info):
        """
        Sets the sub_workflow_info of this WorkflowTaskInfo.
        A collection of references to the [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) Managed Object.  When this managed object is deleted, the referenced [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) MO unsets its reference to this deleted MO. 

        :param sub_workflow_info: The sub_workflow_info of this WorkflowTaskInfo.
        :type: WorkflowWorkflowInfoRef
        """

        self._sub_workflow_info = sub_workflow_info

    @property
    def task_definition(self):
        """
        Gets the task_definition of this WorkflowTaskInfo.
        The task definition that was used to launch this task execution instance. 

        :return: The task_definition of this WorkflowTaskInfo.
        :rtype: WorkflowTaskDefinitionRef
        """
        return self._task_definition

    @task_definition.setter
    def task_definition(self, task_definition):
        """
        Sets the task_definition of this WorkflowTaskInfo.
        The task definition that was used to launch this task execution instance. 

        :param task_definition: The task_definition of this WorkflowTaskInfo.
        :type: WorkflowTaskDefinitionRef
        """

        self._task_definition = task_definition

    @property
    def workflow_info(self):
        """
        Gets the workflow_info of this WorkflowTaskInfo.
        A collection of references to the [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) Managed Object.  When this managed object is deleted, the referenced [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) MO unsets its reference to this deleted MO. 

        :return: The workflow_info of this WorkflowTaskInfo.
        :rtype: WorkflowWorkflowInfoRef
        """
        return self._workflow_info

    @workflow_info.setter
    def workflow_info(self, workflow_info):
        """
        Sets the workflow_info of this WorkflowTaskInfo.
        A collection of references to the [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) Managed Object.  When this managed object is deleted, the referenced [workflow.WorkflowInfo](mo://workflow.WorkflowInfo) MO unsets its reference to this deleted MO. 

        :param workflow_info: The workflow_info of this WorkflowTaskInfo.
        :type: WorkflowWorkflowInfoRef
        """

        self._workflow_info = workflow_info

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
        if not isinstance(other, WorkflowTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
