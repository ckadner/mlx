# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.29-filter-categories
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiListDatasetsResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'datasets': 'list[ApiDataset]',
        'total_size': 'int',
        'next_page_token': 'str'
    }

    attribute_map = {
        'datasets': 'datasets',
        'total_size': 'total_size',
        'next_page_token': 'next_page_token'
    }

    def __init__(self, datasets=None, total_size=None, next_page_token=None):  # noqa: E501
        """ApiListDatasetsResponse - a model defined in Swagger"""  # noqa: E501

        self._datasets = None
        self._total_size = None
        self._next_page_token = None
        self.discriminator = None

        if datasets is not None:
            self.datasets = datasets
        if total_size is not None:
            self.total_size = total_size
        if next_page_token is not None:
            self.next_page_token = next_page_token

    @property
    def datasets(self):
        """Gets the datasets of this ApiListDatasetsResponse.  # noqa: E501


        :return: The datasets of this ApiListDatasetsResponse.  # noqa: E501
        :rtype: list[ApiDataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ApiListDatasetsResponse.


        :param datasets: The datasets of this ApiListDatasetsResponse.  # noqa: E501
        :type: list[ApiDataset]
        """

        self._datasets = datasets

    @property
    def total_size(self):
        """Gets the total_size of this ApiListDatasetsResponse.  # noqa: E501


        :return: The total_size of this ApiListDatasetsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this ApiListDatasetsResponse.


        :param total_size: The total_size of this ApiListDatasetsResponse.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def next_page_token(self):
        """Gets the next_page_token of this ApiListDatasetsResponse.  # noqa: E501


        :return: The next_page_token of this ApiListDatasetsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this ApiListDatasetsResponse.


        :param next_page_token: The next_page_token of this ApiListDatasetsResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiListDatasetsResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiListDatasetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
