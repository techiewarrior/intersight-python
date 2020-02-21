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


class FirmwareHttpServer(object):
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
        'location_link': 'str',
        'mount_options': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'location_link': 'LocationLink',
        'mount_options': 'MountOptions'
    }

    def __init__(self, object_type=None, location_link=None, mount_options=None):
        """
        FirmwareHttpServer - a model defined in Swagger
        """

        self._object_type = None
        self._location_link = None
        self._mount_options = None

        if object_type is not None:
          self.object_type = object_type
        if location_link is not None:
          self.location_link = location_link
        if mount_options is not None:
          self.mount_options = mount_options

    @property
    def object_type(self):
        """
        Gets the object_type of this FirmwareHttpServer.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this FirmwareHttpServer.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this FirmwareHttpServer.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this FirmwareHttpServer.
        :type: str
        """

        self._object_type = object_type

    @property
    def location_link(self):
        """
        Gets the location_link of this FirmwareHttpServer.
        HTTP/HTTPS link to the image. Accepted formats HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image.  

        :return: The location_link of this FirmwareHttpServer.
        :rtype: str
        """
        return self._location_link

    @location_link.setter
    def location_link(self, location_link):
        """
        Sets the location_link of this FirmwareHttpServer.
        HTTP/HTTPS link to the image. Accepted formats HTTP[s]://server-hostname/share/image or HTTP[s]://serverip/share/image.  

        :param location_link: The location_link of this FirmwareHttpServer.
        :type: str
        """

        self._location_link = location_link

    @property
    def mount_options(self):
        """
        Gets the mount_options of this FirmwareHttpServer.
        Mount option as configured on the HTTP server. Empty if nothing is configured.   

        :return: The mount_options of this FirmwareHttpServer.
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this FirmwareHttpServer.
        Mount option as configured on the HTTP server. Empty if nothing is configured.   

        :param mount_options: The mount_options of this FirmwareHttpServer.
        :type: str
        """

        self._mount_options = mount_options

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
        if not isinstance(other, FirmwareHttpServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
