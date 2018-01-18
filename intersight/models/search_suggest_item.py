# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchSuggestItem(object):
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
        'ancestors': 'list[MoMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoMoRef',
        'tags': 'list[MoTag]',
        'complete_mo': 'bool',
        'rawquery': 'str',
        'skip': 'int',
        'suggest_term': 'str',
        'top': 'int',
        'type': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'complete_mo': 'CompleteMo',
        'rawquery': 'Rawquery',
        'skip': 'Skip',
        'suggest_term': 'SuggestTerm',
        'top': 'Top',
        'type': 'Type'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, complete_mo=None, rawquery=None, skip=None, suggest_term=None, top=None, type=None):
        """
        SearchSuggestItem - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._complete_mo = None
        self._rawquery = None
        self._skip = None
        self._suggest_term = None
        self._top = None
        self._type = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if complete_mo is not None:
          self.complete_mo = complete_mo
        if rawquery is not None:
          self.rawquery = rawquery
        if skip is not None:
          self.skip = skip
        if suggest_term is not None:
          self.suggest_term = suggest_term
        if top is not None:
          self.top = top
        if type is not None:
          self.type = type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SearchSuggestItem.
        The Account ID for this managed object.  

        :return: The account_moid of this SearchSuggestItem.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SearchSuggestItem.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SearchSuggestItem.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SearchSuggestItem.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SearchSuggestItem.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SearchSuggestItem.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SearchSuggestItem.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SearchSuggestItem.
        The time when this managed object was created.  

        :return: The create_time of this SearchSuggestItem.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SearchSuggestItem.
        The time when this managed object was created.  

        :param create_time: The create_time of this SearchSuggestItem.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SearchSuggestItem.
        The time when this managed object was last modified.  

        :return: The mod_time of this SearchSuggestItem.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SearchSuggestItem.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SearchSuggestItem.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SearchSuggestItem.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this SearchSuggestItem.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SearchSuggestItem.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this SearchSuggestItem.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SearchSuggestItem.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SearchSuggestItem.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SearchSuggestItem.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SearchSuggestItem.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SearchSuggestItem.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this SearchSuggestItem.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SearchSuggestItem.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SearchSuggestItem.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SearchSuggestItem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SearchSuggestItem.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SearchSuggestItem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SearchSuggestItem.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this SearchSuggestItem.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this SearchSuggestItem.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SearchSuggestItem.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this SearchSuggestItem.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def complete_mo(self):
        """
        Gets the complete_mo of this SearchSuggestItem.
        Flag for returning complete objects that matched the global search criteria.  

        :return: The complete_mo of this SearchSuggestItem.
        :rtype: bool
        """
        return self._complete_mo

    @complete_mo.setter
    def complete_mo(self, complete_mo):
        """
        Sets the complete_mo of this SearchSuggestItem.
        Flag for returning complete objects that matched the global search criteria.  

        :param complete_mo: The complete_mo of this SearchSuggestItem.
        :type: bool
        """

        self._complete_mo = complete_mo

    @property
    def rawquery(self):
        """
        Gets the rawquery of this SearchSuggestItem.
        Additional filter parameters for global search. You can also specify odata select fields here.  

        :return: The rawquery of this SearchSuggestItem.
        :rtype: str
        """
        return self._rawquery

    @rawquery.setter
    def rawquery(self, rawquery):
        """
        Sets the rawquery of this SearchSuggestItem.
        Additional filter parameters for global search. You can also specify odata select fields here.  

        :param rawquery: The rawquery of this SearchSuggestItem.
        :type: str
        """

        self._rawquery = rawquery

    @property
    def skip(self):
        """
        Gets the skip of this SearchSuggestItem.
        Starting offset for the results to be returned from external search engine.  

        :return: The skip of this SearchSuggestItem.
        :rtype: int
        """
        return self._skip

    @skip.setter
    def skip(self, skip):
        """
        Sets the skip of this SearchSuggestItem.
        Starting offset for the results to be returned from external search engine.  

        :param skip: The skip of this SearchSuggestItem.
        :type: int
        """

        self._skip = skip

    @property
    def suggest_term(self):
        """
        Gets the suggest_term of this SearchSuggestItem.
        Main search term used for global search across all mos that has search enabled.  

        :return: The suggest_term of this SearchSuggestItem.
        :rtype: str
        """
        return self._suggest_term

    @suggest_term.setter
    def suggest_term(self, suggest_term):
        """
        Sets the suggest_term of this SearchSuggestItem.
        Main search term used for global search across all mos that has search enabled.  

        :param suggest_term: The suggest_term of this SearchSuggestItem.
        :type: str
        """

        self._suggest_term = suggest_term

    @property
    def top(self):
        """
        Gets the top of this SearchSuggestItem.
        Maximum number of results to be returned from external search engine.  

        :return: The top of this SearchSuggestItem.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        Sets the top of this SearchSuggestItem.
        Maximum number of results to be returned from external search engine.  

        :param top: The top of this SearchSuggestItem.
        :type: int
        """

        self._top = top

    @property
    def type(self):
        """
        Gets the type of this SearchSuggestItem.
        Mo object type filter. Search will be restricted only on the specified mo types.  Do not provide IndexMoTypes filter in the rawquery, if you specify values in this field. 

        :return: The type of this SearchSuggestItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchSuggestItem.
        Mo object type filter. Search will be restricted only on the specified mo types.  Do not provide IndexMoTypes filter in the rawquery, if you specify values in this field. 

        :param type: The type of this SearchSuggestItem.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, SearchSuggestItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other