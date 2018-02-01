#!/usr/bin/env python
"""
CloudGenix Python SDK - POST

**Author:** CloudGenix

**Copyright:** (c) 2017, 2018 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017, 2018 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017, 2018 CloudGenix, Inc

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

# Set logging to function name
api_logger = logging.getLogger(__name__)
"""logging.getlogger object to enable debug printing via `cloudgenix.API.set_debug`"""


class Post(object):
    """
    CloudGenix API - POST requests

    Object to handle making Post requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def access_elementusers(self, elementuser_id, data, tenant_id=None, api_version="v2.0"):
        """
        Grant Specific role to Element user on specific element

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/access".format(api_version,
                                                                                 tenant_id,
                                                                                 elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def aggregates_monitor(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Aggregates_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a custom application definition

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs".format(api_version,
                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs_query(self, data, tenant_id=None, api_version="v0.1"):
        """
        Queries db for limit number of app defs that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v0.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/query".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def base_permissions(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Base_Permissions API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/base_permissions".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def base_permissions_clients(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Base_Permissions_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/base_permissions".format(api_version,
                                                                                      tenant_id,
                                                                                      client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bulk_metrics_monitor(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Bulk_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/bulk_metrics".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def change_password(self, data, tenant_id=None, api_version="v2.0"):
        """
        Allows one to change password

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/accounts/password/change".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def coreroutepeers(self, site_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create new core route peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def corerouterpeers_operations(self, site_id, coreroutepeer_id, data, tenant_id=None, api_version="v2.1"):
        """
        POST Corerouterpeers_Operations API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **coreroutepeer_id**: Core Router peer ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers/{}/operations".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                coreroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dhcpservers(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Dhcpservers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def edgeroutepeers(self, site_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create new WAN edge route peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def edgerouterpeers_operations(self, site_id, edgeroutepeer_id, data, tenant_id=None, api_version="v2.1"):
        """
        POST Edgerouterpeers_Operations API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **edgeroutepeer_id**: Edge Router peer ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers/{}/operations".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                edgeroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_extensions(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create element level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions".format(api_version,
                                                                                          tenant_id,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementaccessconfigs(self, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        POST Elementaccessconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessconfigs".format(api_version,
                                                                                           tenant_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elements_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of elements that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/query".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementusers(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create Element User

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers".format(api_version,
                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def esp_tenant_permissions(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Esp_Tenant_Permissions API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/permissions".format(api_version,
                                                                                 tenant_id,
                                                                                 client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def events_query(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Events_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/events/query".format(api_version,
                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def flows_monitor(self, data, tenant_id=None, api_version="v3.1"):
        """
        POST Flows_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/flows".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def get_site_best_art(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Get_Site_Best_Art API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/get_site_best_art".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def get_site_best_bw_usage(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Get_Site_Best_Bw_Usage API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/get_site_best_bw_usage".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def globalprefixfilters(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new global prefix filter.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def hubclustermembers(self, site_id, hubcluster_id, data, tenant_id=None, api_version="v3.0"):
        """
        Creates a new hub cluster member.

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def hubclusters(self, site_id, data, tenant_id=None, api_version="v3.0"):
        """
        Creates a new hub cluster

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces(self, site_id, element_id, data, tenant_id=None, api_version="v4.1"):
        """
        Create an element sub-interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces".format(api_version,
                                                                                          tenant_id,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def lannetworks(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def lannetworks_query(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of LAN networks that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks/query".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def localprefixfilters(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new local prefix filter.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def login(self, data, api_version="v2.0"):
        """
        Login api

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/login".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def login_clients(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        Login api for esp client

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/login".format(api_version,
                                                                           tenant_id,
                                                                           client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def logout_clients(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Logout_Clients API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/logout".format(api_version,
                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def machines_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Machines_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/query".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def metrics_monitor(self, data, tenant_id=None, api_version="v2.1"):
        """
        POST Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/metrics".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkcontexts(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new LAN segment

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def object_stats_monitor(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Object_Stats_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/object_stats".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def otpaccess(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Verify Challenge phrase and generate response phrase 

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/otpaccess".format(api_version,
                                                                                tenant_id,
                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def pathgroups(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Path Group for a tenant.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups".format(api_version,
                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policyrules(self, policyset_id, data, tenant_id=None, api_version="v3.1"):
        """
        Create a new Policy

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules".format(api_version,
                                                                                    tenant_id,
                                                                                    policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policyrules_query(self, policyset_id, data, tenant_id=None, api_version="v3.1"):
        """
        Queries db for limit number of LAN networks that match query params.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules/query".format(api_version,
                                                                                          tenant_id,
                                                                                          policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policysets(self, data, tenant_id=None, api_version="v3.0"):
        """
        Create a new Policy Set

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets".format(api_version,
                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policysets_query(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Policysets_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/query".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prefixfilters(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and security prefix filter.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prefixfilters_query(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Query security prefix filter for NB API.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters/query".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_extensions_i(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Query_Extensions_I API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions/query".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def query_extensions_s(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Query_Extensions_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions/query".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def roles(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Roles API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/roles".format(api_version,
                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def roles_clients(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Roles_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/roles".format(api_version,
                                                                           tenant_id,
                                                                           client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyruleorder(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Securitypolicyruleorder API Function

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/firewallpolicyruleorder".format(api_version,
                                                                                                        tenant_id,
                                                                                                        securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyrules(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new tenant security policy rule.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules".format(api_version,
                                                                                                    tenant_id,
                                                                                                    securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyrules_query(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of LAN networks that match query params.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules/query".format(api_version,
                                                                                                          tenant_id,
                                                                                                          securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new tenant security policy set.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securityzones(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new security zone

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securityzones_query(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Query security zone for NB API.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones/query".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicebindingmaps(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new Service Binding Map

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def serviceendpoints(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new Service Endpoint

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicelabels(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new Service Label

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def signup(self, data, tenant_id=None, api_version="v2.0"):
        """
        Signup new operators

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/signup".format(api_version,
                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def signup_clients(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Signup_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/signup".format(api_version,
                                                                            tenant_id,
                                                                            client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_best_app_path(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Site_Best_App_Path API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/site_best_app_path".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_extensions(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create site level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions".format(api_version,
                                                                              tenant_id,
                                                                              site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sites(self, data, tenant_id=None, api_version="v4.1"):
        """
        Create a new site

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites".format(api_version,
                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sites_best_app_path(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Sites_Best_App_Path API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites_best_app_path".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sites_query(self, data, tenant_id=None, api_version="v4.1"):
        """
        Queries db for limit number of sites that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/query".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sitesecurityzones(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and security zone.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snmpagents(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create SNMP Agent

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmpagents".format(api_version,
                                                                                          tenant_id,
                                                                                          site_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snmptraps(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create SNMP Trap

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmptraps".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def staticroutes(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Staticroutes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sys_metrics_monitor(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Sys_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/sys_metrics".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_anynetlinks(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Tenant_Anynetlinks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/anynetlinks".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_element_operations(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Tenant_Element_Operations API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/operations".format(api_version,
                                                                                 tenant_id,
                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_forgot_password_login(self, data, tenant_id=None, api_version="v2.0"):
        """
        Forgot password API

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/login/password/forgot".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def tenant_machine_operations(self, machine_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Tenant_Machine_Operations API Function

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/operations".format(api_version,
                                                                                 tenant_id,
                                                                                 machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_permissions(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Tenant_Permissions API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/permissions".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topn_monitor(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Topn_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/topn".format(api_version,
                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topology(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Topology API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/topology".format(api_version,
                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def users(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Users API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/users".format(api_version,
                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vff_token_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Vff_Token_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/tokens/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vfflicense_tokens(self, vfflicense_id, data, tenant_id=None, api_version="v2.0"):
        """
        Generate Token for Model

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/tokens".format(api_version,
                                                                                tenant_id,
                                                                                vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vpnlinks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Vpnlinks_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/query".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces(self, site_id, data, tenant_id=None, api_version="v2.1"):
        """
        POST Waninterfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces_query(self, site_id, data, tenant_id=None, api_version="v2.1"):
        """
        POST Waninterfaces_Query API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/query".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wannetworks(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new WAN

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wannetworks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of sites that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks/query".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def wanoverlays(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new app/wan context

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlays".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    forgot_password_login_t = tenant_forgot_password_login
    """ Backwards-compatibility alias of `forgot_password_login_t` to `tenant_forgot_password_login`"""

    operations_e = tenant_element_operations
    """ Backwards-compatibility alias of `operations_e` to `tenant_element_operations`"""

    operations_t = tenant_machine_operations
    """ Backwards-compatibility alias of `operations_t` to `tenant_machine_operations`"""

    ops_coreroutepeers = corerouterpeers_operations
    """ Backwards-compatibility alias of `ops_coreroutepeers` to `corerouterpeers_operations`"""

    ops_edgeroutepeers = edgerouterpeers_operations
    """ Backwards-compatibility alias of `ops_edgeroutepeers` to `edgerouterpeers_operations`"""

    permissions_clients_t = esp_tenant_permissions
    """ Backwards-compatibility alias of `permissions_clients_t` to `esp_tenant_permissions`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    query_appdefs = appdefs_query
    """ Backwards-compatibility alias of `query_appdefs` to `appdefs_query`"""

    query_e = elements_query
    """ Backwards-compatibility alias of `query_e` to `elements_query`"""

    query_events = events_query
    """ Backwards-compatibility alias of `query_events` to `events_query`"""

    query_lannetworks = lannetworks_query
    """ Backwards-compatibility alias of `query_lannetworks` to `lannetworks_query`"""

    query_m = machines_query
    """ Backwards-compatibility alias of `query_m` to `machines_query`"""

    query_policyrules = policyrules_query
    """ Backwards-compatibility alias of `query_policyrules` to `policyrules_query`"""

    query_policysets = policysets_query
    """ Backwards-compatibility alias of `query_policysets` to `policysets_query`"""

    query_prefixfilters = prefixfilters_query
    """ Backwards-compatibility alias of `query_prefixfilters` to `prefixfilters_query`"""

    query_s = sites_query
    """ Backwards-compatibility alias of `query_s` to `sites_query`"""

    query_securitypolicyrules_securitypolicysets = securitypolicyrules_query
    """ Backwards-compatibility alias of `query_securitypolicyrules_securitypolicysets` to `securitypolicyrules_query`"""

    query_securityzones = securityzones_query
    """ Backwards-compatibility alias of `query_securityzones` to `securityzones_query`"""

    query_tokens_vfflicenses = vff_token_query
    """ Backwards-compatibility alias of `query_tokens_vfflicenses` to `vff_token_query`"""

    query_vpnlinks = vpnlinks_query
    """ Backwards-compatibility alias of `query_vpnlinks` to `vpnlinks_query`"""

    query_waninterfaces = waninterfaces_query
    """ Backwards-compatibility alias of `query_waninterfaces` to `waninterfaces_query`"""

    query_wannetworks = wannetworks_query
    """ Backwards-compatibility alias of `query_wannetworks` to `wannetworks_query`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

