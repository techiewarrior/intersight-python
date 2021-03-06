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


class HyperflexClusterNetworkPolicyAllOf(object):
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
        'jumbo_frame': 'bool',
        'kvm_ip_range': 'HyperflexIpAddrRange',
        'mac_prefix_range': 'HyperflexMacAddrPrefixRange',
        'mgmt_vlan': 'HyperflexNamedVlan',
        'uplink_speed': 'str',
        'vm_migration_vlan': 'HyperflexNamedVlan',
        'vm_network_vlans': 'list[HyperflexNamedVlan]',
        'cluster_profiles': 'list[HyperflexClusterProfile]',
        'organization': 'OrganizationOrganization'
    }

    attribute_map = {
        'jumbo_frame': 'JumboFrame',
        'kvm_ip_range': 'KvmIpRange',
        'mac_prefix_range': 'MacPrefixRange',
        'mgmt_vlan': 'MgmtVlan',
        'uplink_speed': 'UplinkSpeed',
        'vm_migration_vlan': 'VmMigrationVlan',
        'vm_network_vlans': 'VmNetworkVlans',
        'cluster_profiles': 'ClusterProfiles',
        'organization': 'Organization'
    }

    def __init__(self,
                 jumbo_frame=None,
                 kvm_ip_range=None,
                 mac_prefix_range=None,
                 mgmt_vlan=None,
                 uplink_speed='default',
                 vm_migration_vlan=None,
                 vm_network_vlans=None,
                 cluster_profiles=None,
                 organization=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexClusterNetworkPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._jumbo_frame = None
        self._kvm_ip_range = None
        self._mac_prefix_range = None
        self._mgmt_vlan = None
        self._uplink_speed = None
        self._vm_migration_vlan = None
        self._vm_network_vlans = None
        self._cluster_profiles = None
        self._organization = None
        self.discriminator = None

        if jumbo_frame is not None:
            self.jumbo_frame = jumbo_frame
        if kvm_ip_range is not None:
            self.kvm_ip_range = kvm_ip_range
        if mac_prefix_range is not None:
            self.mac_prefix_range = mac_prefix_range
        if mgmt_vlan is not None:
            self.mgmt_vlan = mgmt_vlan
        if uplink_speed is not None:
            self.uplink_speed = uplink_speed
        if vm_migration_vlan is not None:
            self.vm_migration_vlan = vm_migration_vlan
        if vm_network_vlans is not None:
            self.vm_network_vlans = vm_network_vlans
        if cluster_profiles is not None:
            self.cluster_profiles = cluster_profiles
        if organization is not None:
            self.organization = organization

    @property
    def jumbo_frame(self):
        """Gets the jumbo_frame of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501

        Enable or disable jumbo frames.    # noqa: E501

        :return: The jumbo_frame of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._jumbo_frame

    @jumbo_frame.setter
    def jumbo_frame(self, jumbo_frame):
        """Sets the jumbo_frame of this HyperflexClusterNetworkPolicyAllOf.

        Enable or disable jumbo frames.    # noqa: E501

        :param jumbo_frame: The jumbo_frame of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._jumbo_frame = jumbo_frame

    @property
    def kvm_ip_range(self):
        """Gets the kvm_ip_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The kvm_ip_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: HyperflexIpAddrRange
        """
        return self._kvm_ip_range

    @kvm_ip_range.setter
    def kvm_ip_range(self, kvm_ip_range):
        """Sets the kvm_ip_range of this HyperflexClusterNetworkPolicyAllOf.


        :param kvm_ip_range: The kvm_ip_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: HyperflexIpAddrRange
        """

        self._kvm_ip_range = kvm_ip_range

    @property
    def mac_prefix_range(self):
        """Gets the mac_prefix_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The mac_prefix_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: HyperflexMacAddrPrefixRange
        """
        return self._mac_prefix_range

    @mac_prefix_range.setter
    def mac_prefix_range(self, mac_prefix_range):
        """Sets the mac_prefix_range of this HyperflexClusterNetworkPolicyAllOf.


        :param mac_prefix_range: The mac_prefix_range of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: HyperflexMacAddrPrefixRange
        """

        self._mac_prefix_range = mac_prefix_range

    @property
    def mgmt_vlan(self):
        """Gets the mgmt_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The mgmt_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: HyperflexNamedVlan
        """
        return self._mgmt_vlan

    @mgmt_vlan.setter
    def mgmt_vlan(self, mgmt_vlan):
        """Sets the mgmt_vlan of this HyperflexClusterNetworkPolicyAllOf.


        :param mgmt_vlan: The mgmt_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: HyperflexNamedVlan
        """

        self._mgmt_vlan = mgmt_vlan

    @property
    def uplink_speed(self):
        """Gets the uplink_speed of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501

        Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be '1G' or '10G'. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be 'default' only.    # noqa: E501

        :return: The uplink_speed of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uplink_speed

    @uplink_speed.setter
    def uplink_speed(self, uplink_speed):
        """Sets the uplink_speed of this HyperflexClusterNetworkPolicyAllOf.

        Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be '1G' or '10G'. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be 'default' only.    # noqa: E501

        :param uplink_speed: The uplink_speed of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["default", "1G", "10G"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and uplink_speed not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `uplink_speed` ({0}), must be one of {1}"  # noqa: E501
                .format(uplink_speed, allowed_values))

        self._uplink_speed = uplink_speed

    @property
    def vm_migration_vlan(self):
        """Gets the vm_migration_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The vm_migration_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: HyperflexNamedVlan
        """
        return self._vm_migration_vlan

    @vm_migration_vlan.setter
    def vm_migration_vlan(self, vm_migration_vlan):
        """Sets the vm_migration_vlan of this HyperflexClusterNetworkPolicyAllOf.


        :param vm_migration_vlan: The vm_migration_vlan of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: HyperflexNamedVlan
        """

        self._vm_migration_vlan = vm_migration_vlan

    @property
    def vm_network_vlans(self):
        """Gets the vm_network_vlans of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The vm_network_vlans of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: list[HyperflexNamedVlan]
        """
        return self._vm_network_vlans

    @vm_network_vlans.setter
    def vm_network_vlans(self, vm_network_vlans):
        """Sets the vm_network_vlans of this HyperflexClusterNetworkPolicyAllOf.


        :param vm_network_vlans: The vm_network_vlans of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: list[HyperflexNamedVlan]
        """

        self._vm_network_vlans = vm_network_vlans

    @property
    def cluster_profiles(self):
        """Gets the cluster_profiles of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :return: The cluster_profiles of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: list[HyperflexClusterProfile]
        """
        return self._cluster_profiles

    @cluster_profiles.setter
    def cluster_profiles(self, cluster_profiles):
        """Sets the cluster_profiles of this HyperflexClusterNetworkPolicyAllOf.

        A reference to a hyperflexClusterProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. List of cluster profiles using this policy.   # noqa: E501

        :param cluster_profiles: The cluster_profiles of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: list[HyperflexClusterProfile]
        """

        self._cluster_profiles = cluster_profiles

    @property
    def organization(self):
        """Gets the organization of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501


        :return: The organization of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this HyperflexClusterNetworkPolicyAllOf.


        :param organization: The organization of this HyperflexClusterNetworkPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

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
        if not isinstance(other, HyperflexClusterNetworkPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexClusterNetworkPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
