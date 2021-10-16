# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0
# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.api_settings_section import ApiSettingsSection  # noqa: F401,E501
from swagger_server import util


class ApiSettings(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sections: List[ApiSettingsSection]=None):  # noqa: E501
        """ApiSettings - a model defined in Swagger

        :param sections: The sections of this ApiSettings.  # noqa: E501
        :type sections: List[ApiSettingsSection]
        """
        self.swagger_types = {
            'sections': List[ApiSettingsSection]
        }

        self.attribute_map = {
            'sections': 'sections'
        }

        self._sections = sections

    @classmethod
    def from_dict(cls, dikt) -> 'ApiSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The apiSettings of this ApiSettings.  # noqa: E501
        :rtype: ApiSettings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sections(self) -> List[ApiSettingsSection]:
        """Gets the sections of this ApiSettings.

        List of configuration categories.  # noqa: E501

        :return: The sections of this ApiSettings.
        :rtype: List[ApiSettingsSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections: List[ApiSettingsSection]):
        """Sets the sections of this ApiSettings.

        List of configuration categories.  # noqa: E501

        :param sections: The sections of this ApiSettings.
        :type sections: List[ApiSettingsSection]
        """
        if sections is None:
            raise ValueError("Invalid value for `sections`, must not be `None`")  # noqa: E501

        self._sections = sections
