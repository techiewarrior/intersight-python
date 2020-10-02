# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class AssetParentConnectionSignatureAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'device_id': 'str',
        'node_id': 'str',
        'signature': 'str',
        'time_stamp': 'datetime'
    }

    attribute_map = {
        'device_id': 'DeviceId',
        'node_id': 'NodeId',
        'signature': 'Signature',
        'time_stamp': 'TimeStamp'
    }

    def __init__(self,
                 device_id=None,
                 node_id=None,
                 signature=None,
                 time_stamp=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetParentConnectionSignatureAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._node_id = None
        self._signature = None
        self._time_stamp = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if node_id is not None:
            self.node_id = node_id
        if signature is not None:
            self.signature = signature
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def device_id(self):
        """Gets the device_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501

        The moid of the parent device registration.    # noqa: E501

        :return: The device_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this AssetParentConnectionSignatureAllOf.

        The moid of the parent device registration.    # noqa: E501

        :param device_id: The device_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def node_id(self):
        """Gets the node_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501

        The node identity of the parent device, corresponds to the parents ClusterMember.memberIdentity. Used on connect to establish through which device in a cluster the child is connected through.    # noqa: E501

        :return: The node_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AssetParentConnectionSignatureAllOf.

        The node identity of the parent device, corresponds to the parents ClusterMember.memberIdentity. Used on connect to establish through which device in a cluster the child is connected through.    # noqa: E501

        :param node_id: The node_id of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def signature(self):
        """Gets the signature of this AssetParentConnectionSignatureAllOf.  # noqa: E501

        The result of signing the deviceId appended with the timeStamp fields with the devices private key.    # noqa: E501

        :return: The signature of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this AssetParentConnectionSignatureAllOf.

        The result of signing the deviceId appended with the timeStamp fields with the devices private key.    # noqa: E501

        :param signature: The signature of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def time_stamp(self):
        """Gets the time_stamp of this AssetParentConnectionSignatureAllOf.  # noqa: E501

        The time at which the signature was generated. Date is accurate to Intersights clock. Used to expire the signature.     # noqa: E501

        :return: The time_stamp of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this AssetParentConnectionSignatureAllOf.

        The time at which the signature was generated. Date is accurate to Intersights clock. Used to expire the signature.     # noqa: E501

        :param time_stamp: The time_stamp of this AssetParentConnectionSignatureAllOf.  # noqa: E501
        :type: datetime
        """

        self._time_stamp = time_stamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetParentConnectionSignatureAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetParentConnectionSignatureAllOf):
            return True

        return self.to_dict() != other.to_dict()