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


class NiaapiNewReleaseDetail(object):
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
        'link': 'str',
        'release_note_link': 'str',
        'release_note_link_title': 'str',
        'software_download_link': 'str',
        'software_download_link_title': 'str',
        'title': 'str',
        'version': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'description': 'Description',
        'link': 'Link',
        'release_note_link': 'ReleaseNoteLink',
        'release_note_link_title': 'ReleaseNoteLinkTitle',
        'software_download_link': 'SoftwareDownloadLink',
        'software_download_link_title': 'SoftwareDownloadLinkTitle',
        'title': 'Title',
        'version': 'Version'
    }

    def __init__(self, object_type=None, description=None, link=None, release_note_link=None, release_note_link_title=None, software_download_link=None, software_download_link_title=None, title=None, version=None):
        """
        NiaapiNewReleaseDetail - a model defined in Swagger
        """

        self._object_type = None
        self._description = None
        self._link = None
        self._release_note_link = None
        self._release_note_link_title = None
        self._software_download_link = None
        self._software_download_link_title = None
        self._title = None
        self._version = None

        if object_type is not None:
          self.object_type = object_type
        if description is not None:
          self.description = description
        if link is not None:
          self.link = link
        if release_note_link is not None:
          self.release_note_link = release_note_link
        if release_note_link_title is not None:
          self.release_note_link_title = release_note_link_title
        if software_download_link is not None:
          self.software_download_link = software_download_link
        if software_download_link_title is not None:
          self.software_download_link_title = software_download_link_title
        if title is not None:
          self.title = title
        if version is not None:
          self.version = version

    @property
    def object_type(self):
        """
        Gets the object_type of this NiaapiNewReleaseDetail.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NiaapiNewReleaseDetail.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._object_type = object_type

    @property
    def description(self):
        """
        Gets the description of this NiaapiNewReleaseDetail.
        Description of this new verison release post.  

        :return: The description of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NiaapiNewReleaseDetail.
        Description of this new verison release post.  

        :param description: The description of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._description = description

    @property
    def link(self):
        """
        Gets the link of this NiaapiNewReleaseDetail.
        Link of downloading the release file.  

        :return: The link of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this NiaapiNewReleaseDetail.
        Link of downloading the release file.  

        :param link: The link of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._link = link

    @property
    def release_note_link(self):
        """
        Gets the release_note_link of this NiaapiNewReleaseDetail.
        The link used to provide a gateway for customer to review the release note.  

        :return: The release_note_link of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._release_note_link

    @release_note_link.setter
    def release_note_link(self, release_note_link):
        """
        Sets the release_note_link of this NiaapiNewReleaseDetail.
        The link used to provide a gateway for customer to review the release note.  

        :param release_note_link: The release_note_link of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._release_note_link = release_note_link

    @property
    def release_note_link_title(self):
        """
        Gets the release_note_link_title of this NiaapiNewReleaseDetail.
        The link title used to provide a gateway for customer to review the release note.  

        :return: The release_note_link_title of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._release_note_link_title

    @release_note_link_title.setter
    def release_note_link_title(self, release_note_link_title):
        """
        Sets the release_note_link_title of this NiaapiNewReleaseDetail.
        The link title used to provide a gateway for customer to review the release note.  

        :param release_note_link_title: The release_note_link_title of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._release_note_link_title = release_note_link_title

    @property
    def software_download_link(self):
        """
        Gets the software_download_link of this NiaapiNewReleaseDetail.
        The link used to provide a gateway for customer to download the release.  

        :return: The software_download_link of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._software_download_link

    @software_download_link.setter
    def software_download_link(self, software_download_link):
        """
        Sets the software_download_link of this NiaapiNewReleaseDetail.
        The link used to provide a gateway for customer to download the release.  

        :param software_download_link: The software_download_link of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._software_download_link = software_download_link

    @property
    def software_download_link_title(self):
        """
        Gets the software_download_link_title of this NiaapiNewReleaseDetail.
        The link title used to provide a gateway for customer to download the release.  

        :return: The software_download_link_title of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._software_download_link_title

    @software_download_link_title.setter
    def software_download_link_title(self, software_download_link_title):
        """
        Sets the software_download_link_title of this NiaapiNewReleaseDetail.
        The link title used to provide a gateway for customer to download the release.  

        :param software_download_link_title: The software_download_link_title of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._software_download_link_title = software_download_link_title

    @property
    def title(self):
        """
        Gets the title of this NiaapiNewReleaseDetail.
        Title of the new verison release post.  

        :return: The title of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this NiaapiNewReleaseDetail.
        Title of the new verison release post.  

        :param title: The title of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._title = title

    @property
    def version(self):
        """
        Gets the version of this NiaapiNewReleaseDetail.
        Version number Associate with this Post.   

        :return: The version of this NiaapiNewReleaseDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this NiaapiNewReleaseDetail.
        Version number Associate with this Post.   

        :param version: The version of this NiaapiNewReleaseDetail.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, NiaapiNewReleaseDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
