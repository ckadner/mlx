# Copyright 2021 The MLX Contributors
#
# SPDX-License-Identifier: Apache-2.0

from swagger_server.models.api_catalog_upload import ApiCatalogUpload  # noqa: E501
from swagger_server.models.api_catalog_upload_response import ApiCatalogUploadResponse  # noqa: E501
from swagger_server.models.api_list_catalog_items_response import ApiListCatalogItemsResponse  # noqa: E501
from swagger_server import util


def list_all_assets(page_token=None, page_size=None, sort_by=None, filter=None):  # noqa: E501
    """list_all_assets

     # noqa: E501

    :param page_token: 
    :type page_token: str
    :param page_size: 
    :type page_size: int
    :param sort_by: Can be format of \&quot;field_name\&quot;, \&quot;field_name asc\&quot; or \&quot;field_name desc\&quot; Ascending by default.
    :type sort_by: str
    :param filter: A string-serialized JSON dictionary with key-value pairs that correspond to the ApiComponent&#39;s attribute names and their respective values to be filtered for.
    :type filter: str

    :rtype: ApiListCatalogItemsResponse
    """
    return util.invoke_controller_impl()


def upload_multiple_assets(body):  # noqa: E501
    """upload_multiple_assets

     # noqa: E501

    :param body: 
    :type body: ApiCatalogUpload

    :rtype: ApiCatalogUploadResponse
    """
    return util.invoke_controller_impl()
