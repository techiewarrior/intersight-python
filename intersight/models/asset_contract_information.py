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


class AssetContractInformation(object):
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
        'bill_to': 'AssetAddressInformation',
        'bill_to_global_ultimate': 'AssetGlobalUltimate',
        'contract_number': 'str',
        'line_status': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'bill_to': 'BillTo',
        'bill_to_global_ultimate': 'BillToGlobalUltimate',
        'contract_number': 'ContractNumber',
        'line_status': 'LineStatus'
    }

    def __init__(self, object_type=None, bill_to=None, bill_to_global_ultimate=None, contract_number=None, line_status=None):
        """
        AssetContractInformation - a model defined in Swagger
        """

        self._object_type = None
        self._bill_to = None
        self._bill_to_global_ultimate = None
        self._contract_number = None
        self._line_status = None

        if object_type is not None:
          self.object_type = object_type
        if bill_to is not None:
          self.bill_to = bill_to
        if bill_to_global_ultimate is not None:
          self.bill_to_global_ultimate = bill_to_global_ultimate
        if contract_number is not None:
          self.contract_number = contract_number
        if line_status is not None:
          self.line_status = line_status

    @property
    def object_type(self):
        """
        Gets the object_type of this AssetContractInformation.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this AssetContractInformation.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AssetContractInformation.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this AssetContractInformation.
        :type: str
        """

        self._object_type = object_type

    @property
    def bill_to(self):
        """
        Gets the bill_to of this AssetContractInformation.
        BillTo address of listed for the contract.  

        :return: The bill_to of this AssetContractInformation.
        :rtype: AssetAddressInformation
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this AssetContractInformation.
        BillTo address of listed for the contract.  

        :param bill_to: The bill_to of this AssetContractInformation.
        :type: AssetAddressInformation
        """

        self._bill_to = bill_to

    @property
    def bill_to_global_ultimate(self):
        """
        Gets the bill_to_global_ultimate of this AssetContractInformation.
        BillToGlobalUltimate information listed in the contract.  

        :return: The bill_to_global_ultimate of this AssetContractInformation.
        :rtype: AssetGlobalUltimate
        """
        return self._bill_to_global_ultimate

    @bill_to_global_ultimate.setter
    def bill_to_global_ultimate(self, bill_to_global_ultimate):
        """
        Sets the bill_to_global_ultimate of this AssetContractInformation.
        BillToGlobalUltimate information listed in the contract.  

        :param bill_to_global_ultimate: The bill_to_global_ultimate of this AssetContractInformation.
        :type: AssetGlobalUltimate
        """

        self._bill_to_global_ultimate = bill_to_global_ultimate

    @property
    def contract_number(self):
        """
        Gets the contract_number of this AssetContractInformation.
        Contract number for the Cisco support contract purchased for the Cisco device.  

        :return: The contract_number of this AssetContractInformation.
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """
        Sets the contract_number of this AssetContractInformation.
        Contract number for the Cisco support contract purchased for the Cisco device.  

        :param contract_number: The contract_number of this AssetContractInformation.
        :type: str
        """

        self._contract_number = contract_number

    @property
    def line_status(self):
        """
        Gets the line_status of this AssetContractInformation.
        Contract status as per the Cisco Contract APIx.   

        :return: The line_status of this AssetContractInformation.
        :rtype: str
        """
        return self._line_status

    @line_status.setter
    def line_status(self, line_status):
        """
        Sets the line_status of this AssetContractInformation.
        Contract status as per the Cisco Contract APIx.   

        :param line_status: The line_status of this AssetContractInformation.
        :type: str
        """

        self._line_status = line_status

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
        if not isinstance(other, AssetContractInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
