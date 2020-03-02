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


class WorkflowSubWorkflowTask(object):
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
        'object_type': 'str',
        'description': 'str',
        'label': 'str',
        'name': 'str',
        'input_parameters': 'object',
        'on_failure': 'str',
        'on_success': 'str',
        'catalog_moid': 'str',
        'version': 'int',
        'workflow_definition_id': 'str',
        'workflow_definition_name': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'description': 'Description',
        'label': 'Label',
        'name': 'Name',
        'input_parameters': 'InputParameters',
        'on_failure': 'OnFailure',
        'on_success': 'OnSuccess',
        'catalog_moid': 'CatalogMoid',
        'version': 'Version',
        'workflow_definition_id': 'WorkflowDefinitionId',
        'workflow_definition_name': 'WorkflowDefinitionName'
    }

    def __init__(self, object_type=None, description=None, label=None, name=None, input_parameters=None, on_failure=None, on_success=None, catalog_moid=None, version=None, workflow_definition_id=None, workflow_definition_name=None):
        """
        WorkflowSubWorkflowTask - a model defined in Swagger
        """

        self._object_type = None
        self._description = None
        self._label = None
        self._name = None
        self._input_parameters = None
        self._on_failure = None
        self._on_success = None
        self._catalog_moid = None
        self._version = None
        self._workflow_definition_id = None
        self._workflow_definition_name = None

        if object_type is not None:
          self.object_type = object_type
        if description is not None:
          self.description = description
        if label is not None:
          self.label = label
        if name is not None:
          self.name = name
        if input_parameters is not None:
          self.input_parameters = input_parameters
        if on_failure is not None:
          self.on_failure = on_failure
        if on_success is not None:
          self.on_success = on_success
        if catalog_moid is not None:
          self.catalog_moid = catalog_moid
        if version is not None:
          self.version = version
        if workflow_definition_id is not None:
          self.workflow_definition_id = workflow_definition_id
        if workflow_definition_name is not None:
          self.workflow_definition_name = workflow_definition_name

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowSubWorkflowTask.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowSubWorkflowTask.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._object_type = object_type

    @property
    def description(self):
        """
        Gets the description of this WorkflowSubWorkflowTask.
        The description of this task instance in the workflow.

        :return: The description of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowSubWorkflowTask.
        The description of this task instance in the workflow.

        :param description: The description of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """
        Gets the label of this WorkflowSubWorkflowTask.
        A user defined label identifier of the workflow task used for UI display.

        :return: The label of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WorkflowSubWorkflowTask.
        A user defined label identifier of the workflow task used for UI display.

        :param label: The label of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this WorkflowSubWorkflowTask.
        The name of the task within the workflow and it must be unique among all WorkflowTasks within a workflow definition. This name serves as the internal unique identifier for the task and is used to pick input and output parameters to feed into other tasks.

        :return: The name of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowSubWorkflowTask.
        The name of the task within the workflow and it must be unique among all WorkflowTasks within a workflow definition. This name serves as the internal unique identifier for the task and is used to pick input and output parameters to feed into other tasks.

        :param name: The name of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._name = name

    @property
    def input_parameters(self):
        """
        Gets the input_parameters of this WorkflowSubWorkflowTask.
        JSON formatted map that defines the input given to the task. JSONPath is used for chaining output from previous tasks as inputs into the current task. The format to specify the mapping is '${Source.input/output.JsonPath}'. 'Source' can be either workflow or the name of the task within the workflow. You can map the task input to either a workflow input or a task output. Following this is JSON path expression to extract JSON fragment from source's input/output.

        :return: The input_parameters of this WorkflowSubWorkflowTask.
        :rtype: object
        """
        return self._input_parameters

    @input_parameters.setter
    def input_parameters(self, input_parameters):
        """
        Sets the input_parameters of this WorkflowSubWorkflowTask.
        JSON formatted map that defines the input given to the task. JSONPath is used for chaining output from previous tasks as inputs into the current task. The format to specify the mapping is '${Source.input/output.JsonPath}'. 'Source' can be either workflow or the name of the task within the workflow. You can map the task input to either a workflow input or a task output. Following this is JSON path expression to extract JSON fragment from source's input/output.

        :param input_parameters: The input_parameters of this WorkflowSubWorkflowTask.
        :type: object
        """

        self._input_parameters = input_parameters

    @property
    def on_failure(self):
        """
        Gets the on_failure of this WorkflowSubWorkflowTask.
        This specifies the name of the next task to run if Task fails.  This is the unique name given to the task instance within the workflow. In a graph model, denotes an edge to another Task Node.

        :return: The on_failure of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._on_failure

    @on_failure.setter
    def on_failure(self, on_failure):
        """
        Sets the on_failure of this WorkflowSubWorkflowTask.
        This specifies the name of the next task to run if Task fails.  This is the unique name given to the task instance within the workflow. In a graph model, denotes an edge to another Task Node.

        :param on_failure: The on_failure of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._on_failure = on_failure

    @property
    def on_success(self):
        """
        Gets the on_success of this WorkflowSubWorkflowTask.
        This specifies the name of the next task to run if Task succeeds.  This is the unique name given to the task instance within the workflow. In a graph model, denotes an edge to another Task Node.

        :return: The on_success of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._on_success

    @on_success.setter
    def on_success(self, on_success):
        """
        Sets the on_success of this WorkflowSubWorkflowTask.
        This specifies the name of the next task to run if Task succeeds.  This is the unique name given to the task instance within the workflow. In a graph model, denotes an edge to another Task Node.

        :param on_success: The on_success of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._on_success = on_success

    @property
    def catalog_moid(self):
        """
        Gets the catalog_moid of this WorkflowSubWorkflowTask.
        Specify the catalog moid that this task belongs.

        :return: The catalog_moid of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._catalog_moid

    @catalog_moid.setter
    def catalog_moid(self, catalog_moid):
        """
        Sets the catalog_moid of this WorkflowSubWorkflowTask.
        Specify the catalog moid that this task belongs.

        :param catalog_moid: The catalog_moid of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._catalog_moid = catalog_moid

    @property
    def version(self):
        """
        Gets the version of this WorkflowSubWorkflowTask.
        The workflow definition version to use as subworkflow. When no version is specified then the default version of the workflow at the time of creating or updating this workflow is used.

        :return: The version of this WorkflowSubWorkflowTask.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this WorkflowSubWorkflowTask.
        The workflow definition version to use as subworkflow. When no version is specified then the default version of the workflow at the time of creating or updating this workflow is used.

        :param version: The version of this WorkflowSubWorkflowTask.
        :type: int
        """

        self._version = version

    @property
    def workflow_definition_id(self):
        """
        Gets the workflow_definition_id of this WorkflowSubWorkflowTask.
        The resolved referenced workflow definition managed object.

        :return: The workflow_definition_id of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._workflow_definition_id

    @workflow_definition_id.setter
    def workflow_definition_id(self, workflow_definition_id):
        """
        Sets the workflow_definition_id of this WorkflowSubWorkflowTask.
        The resolved referenced workflow definition managed object.

        :param workflow_definition_id: The workflow_definition_id of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._workflow_definition_id = workflow_definition_id

    @property
    def workflow_definition_name(self):
        """
        Gets the workflow_definition_name of this WorkflowSubWorkflowTask.
        The qualified name of workflow that should be executed as a task.

        :return: The workflow_definition_name of this WorkflowSubWorkflowTask.
        :rtype: str
        """
        return self._workflow_definition_name

    @workflow_definition_name.setter
    def workflow_definition_name(self, workflow_definition_name):
        """
        Sets the workflow_definition_name of this WorkflowSubWorkflowTask.
        The qualified name of workflow that should be executed as a task.

        :param workflow_definition_name: The workflow_definition_name of this WorkflowSubWorkflowTask.
        :type: str
        """

        self._workflow_definition_name = workflow_definition_name

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
        if not isinstance(other, WorkflowSubWorkflowTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
