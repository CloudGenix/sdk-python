#!/usr/bin/env python
"""
CloudGenix Python SDK - GET

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


class Get(object):
    """
    CloudGenix API - GET requests

    Object to handle making Get requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def access_elementusers(self, elementuser_id, access_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all accesses for a particular user

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: (optional) Access ID
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

        if not access_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/access".format(api_version,
                                                                                     tenant_id,
                                                                                     elementuser_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/access/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        elementuser_id,
                                                                                        access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def aggregates_monitor(self, tenant_id=None, api_version="v3.0"):
        """
        GET Aggregates_Monitor API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def anynetlinks_s(self, site_id, anynetlink_id, tenant_id=None, api_version="v2.0"):
        """
        GET Anynetlinks_S API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/anynetlinks/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs(self, appdef_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all application definitions

          **Parameters:**:

          - **appdef_id**: (optional) Application Definition ID
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

        if not appdef_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs".format(api_version,
                                                                      tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}".format(api_version,
                                                                         tenant_id,
                                                                         appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs_version(self, appdefs_version_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get application version for a tenant

          **Parameters:**:

          - **appdefs_version_id**: (optional)
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

        if not appdefs_version_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs_version".format(api_version,
                                                                              tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs_version/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 appdefs_version_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def authtokens(self, operator_id, authtoken_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Authtokens API Function

          **Parameters:**:

          - **operator_id**: Operator ID
          - **authtoken_id**: (optional)
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

        if not authtoken_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/authtokens".format(api_version,
                                                                                      tenant_id,
                                                                                      operator_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/authtokens/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         operator_id,
                                                                                         authtoken_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def base_permissions(self, tenant_id=None, api_version="v2.0"):
        """
        Get a list of tenant base permissions

          **Parameters:**:

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
        return self._parent_class.rest_call(url, "get")

    def base_roles(self, tenant_id=None, api_version="v2.0"):
        """
        Get a list of tenant base roles

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/base_roles".format(api_version,
                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def base_roles_clients(self, client_id, tenant_id=None, api_version="v2.0"):
        """
        Get a list of client base roles

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/base_roles".format(api_version,
                                                                                tenant_id,
                                                                                client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bulk_metrics_monitor(self, bulk_metric_id, tenant_id=None, api_version="v2.0"):
        """
        GET Bulk_Metrics_Monitor API Function

          **Parameters:**:

          - **bulk_metric_id**:
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/bulk_metrics/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  bulk_metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def coreroutepeers(self, site_id, coreroutepeer_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get config for core route peer config for a site

          **Parameters:**:

          - **site_id**: Site ID
          - **coreroutepeer_id**: (optional) Core Router peer ID
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

        if not coreroutepeer_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         coreroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def corerouterpeers_status(self, site_id, tenant_id=None, api_version="v2.1"):
        """
        GET Corerouterpeers_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers/status".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def corerouterpeers_status_single(self, site_id, coreroutepeer_id, tenant_id=None, api_version="v2.1"):
        """
        GET Corerouterpeers_Status_Single API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **coreroutepeer_id**: Core Router peer ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers/{}/status".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            coreroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dhcpservers(self, site_id, dhcpserver_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Dhcpservers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: (optional) DHCP Server ID
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

        if not dhcpserver_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers".format(api_version,
                                                                                   tenant_id,
                                                                                   site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id,
                                                                                      dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def edgeroutepeers(self, site_id, edgeroutepeer_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get config for wan edge routers for a site

          **Parameters:**:

          - **site_id**: Site ID
          - **edgeroutepeer_id**: (optional) Edge Router peer ID
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

        if not edgeroutepeer_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         edgeroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def edgerouterpeers_status(self, site_id, tenant_id=None, api_version="v2.1"):
        """
        GET Edgerouterpeers_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers/status".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def edgerouterpeers_status_single(self, site_id, edgeroutepeer_id, tenant_id=None, api_version="v2.1"):
        """
        GET Edgerouterpeers_Status_Single API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **edgeroutepeer_id**: Edge Router peer ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers/{}/status".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            edgeroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_extensions(self, site_id, element_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element level extensions from NB

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: (optional) Extension ID
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

        if not extension_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_images(self, element_image_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Element_Images API Function

          **Parameters:**:

          - **element_image_id**: (optional)
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

        if not element_image_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/element_images".format(api_version,
                                                                             tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/element_images/{}".format(api_version,
                                                                                tenant_id,
                                                                                element_image_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_passages(self, element_id, passage_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Element_Passages API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **passage_id**: (optional) Passage Configuration ID
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

        if not passage_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/passages".format(api_version,
                                                                                   tenant_id,
                                                                                   element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/passages/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      element_id,
                                                                                      passage_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementaccessconfigs(self, element_id, elementaccessconfig_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get specific element's ElementAccess Config

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: (optional) Element Access Config ID
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

        if not elementaccessconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessconfigs".format(api_version,
                                                                                               tenant_id,
                                                                                               element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessconfigs/{}".format(api_version,
                                                                                                  tenant_id,
                                                                                                  element_id,
                                                                                                  elementaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementaccessstates(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get specific element's Access State

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessstates".format(api_version,
                                                                                          tenant_id,
                                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementpassageconfigs(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        GET Elementpassageconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementpassageconfigs".format(api_version,
                                                                                            tenant_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elements(self, element_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Elements of a tenant

          **Parameters:**:

          - **element_id**: (optional) Element (Device) ID
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

        if not element_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}".format(api_version,
                                                                          tenant_id,
                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementusers(self, elementuser_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element User

          **Parameters:**:

          - **elementuser_id**: (optional) Element User ID
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

        if not elementuser_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers".format(api_version,
                                                                           tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}".format(api_version,
                                                                              tenant_id,
                                                                              elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def enterpriseprefixset(self, tenant_id=None, api_version="v2.0"):
        """
        GET Enterpriseprefixset API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/enterpriseprefixset".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp(self, tenant_id=None, api_version="v2.0"):
        """
        Get esp tenant details for tenant id

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/esp".format(api_version,
                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp_operator_permissions(self, operator_id, tenant_id=None, api_version="v2.0"):
        """
        Get esp operator permissions assigned under all clients

          **Parameters:**:

          - **operator_id**: Operator ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/clients/permissions".format(api_version,
                                                                                           tenant_id,
                                                                                           operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp_operator_permissions_client(self, operator_id, client_id, tenant_id=None, api_version="v2.0"):
        """
        Get esp operator permissions assigned under a client

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/clients/{}/permissions".format(api_version,
                                                                                              tenant_id,
                                                                                              operator_id,
                                                                                              client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def events(self, event_id, tenant_id=None, api_version="v2.0"):
        """
        GET Events API Function

          **Parameters:**:

          - **event_id**: Event ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/events/{}".format(api_version,
                                                                    tenant_id,
                                                                    event_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def globalprefixfilters(self, globalprefixfilter_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get global prefix filters.

          **Parameters:**:

          - **globalprefixfilter_id**: (optional) Global Prefix Filter ID
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

        if not globalprefixfilter_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters".format(api_version,
                                                                                  tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hardwarebypass(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get Elements of a tenant

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/hardwarebypass".format(api_version,
                                                                                     tenant_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubcluster_status(self, site_id, hubcluster_id, tenant_id=None, api_version="v3.0"):
        """
        Get specific hub cluster state

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/status".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubclustermember_status(self, site_id, hubcluster_id, hubclustermember_id, tenant_id=None, api_version="v3.0"):
        """
        Get specific hub cluster member state.

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers/{}/status".format(api_version,
                                                                                                              tenant_id,
                                                                                                              site_id,
                                                                                                              hubcluster_id,
                                                                                                              hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id=None, tenant_id=None, api_version="v3.0"):
        """
        Get all hub cluster members

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: (optional) Hub Cluster Member ID
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

        if not hubclustermember_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers".format(api_version,
                                                                                                        tenant_id,
                                                                                                        site_id,
                                                                                                        hubcluster_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                           tenant_id,
                                                                                                           site_id,
                                                                                                           hubcluster_id,
                                                                                                           hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def hubclusters(self, site_id, hubcluster_id=None, tenant_id=None, api_version="v3.0"):
        """
        Get all hub clusters

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: (optional) Hub (DC) Cluster ID
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

        if not hubcluster_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters".format(api_version,
                                                                                   tenant_id,
                                                                                   site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id,
                                                                                      hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def idps(self, idp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all idps

          **Parameters:**:

          - **idp_id**: (optional) SAML IDentity provider configuration ID
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

        if not idp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/idps".format(api_version,
                                                                   tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/idps/{}".format(api_version,
                                                                      tenant_id,
                                                                      idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces(self, site_id, element_id, interface_id=None, tenant_id=None, api_version="v4.2"):
        """
        Get element interface ids

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: (optional) Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.2)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not interface_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces_status(self, site_id, element_id, interface_id, tenant_id=None, api_version="v2.1"):
        """
        GET Interfaces_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/status".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def lannetworks(self, site_id, lannetwork_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get LAN Networks

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: (optional) LAN Network ID
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

        if not lannetwork_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks".format(api_version,
                                                                                   tenant_id,
                                                                                   site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id,
                                                                                      lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def localprefixfilters(self, localprefixfilter_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get local prefix filters.

          **Parameters:**:

          - **localprefixfilter_id**: (optional) Local Prefix Filter ID
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

        if not localprefixfilter_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def logout(self, api_version="v2.0"):
        """
        Logout current session

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/logout".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machines(self, machine_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all machines of tenant

          **Parameters:**:

          - **machine_id**: (optional) Machine ID
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

        if not machine_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}".format(api_version,
                                                                          tenant_id,
                                                                          machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def metrics_monitor(self, metric_id, tenant_id=None, api_version="v2.1"):
        """
        GET Metrics_Monitor API Function

          **Parameters:**:

          - **metric_id**: Metric ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/metrics/{}".format(api_version,
                                                                             tenant_id,
                                                                             metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkcontexts(self, networkcontext_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get LAN segments

          **Parameters:**:

          - **networkcontext_id**: (optional) Network Context ID
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

        if not networkcontext_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts".format(api_version,
                                                                              tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def object_stats_monitor(self, tenant_id=None, api_version="v2.0"):
        """
        GET Object_Stats_Monitor API Function

          **Parameters:**:

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
        return self._parent_class.rest_call(url, "get")

    def operator_sessions(self, operator_id, session_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all sessions for operator id belonging to a tenant id

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: (optional)
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

        if not session_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/sessions".format(api_version,
                                                                                    tenant_id,
                                                                                    operator_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/sessions/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       operator_id,
                                                                                       session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def otpaccessconfigs(self, tenant_id=None, api_version="v2.0"):
        """
        Get specific element's Access Config

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/otpaccessconfigs".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def password_elementusers(self, elementuser_id, tenant_id=None, api_version="v2.0"):
        """
        GET Password_Elementusers API Function

          **Parameters:**:

          - **elementuser_id**: Element User ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/password".format(api_version,
                                                                                   tenant_id,
                                                                                   elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def pathgroups(self, pathgroup_id=None, tenant_id=None, api_version="v2.0"):
        """
        get all Path Groups for a tenant.

          **Parameters:**:

          - **pathgroup_id**: (optional) Path Group ID (for network service/DC routing)
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

        if not pathgroup_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups".format(api_version,
                                                                         tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups/{}".format(api_version,
                                                                            tenant_id,
                                                                            pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def permissions(self, api_version="v2.0"):
        """
        Get list of permitted APIs that the current operator can invoke

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/permissions".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def policyrules(self, policyset_id, policyrule_id=None, tenant_id=None, api_version="v3.1"):
        """
        Get policy rules of tenant

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: (optional) Policy Rule ID
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

        if not policyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules".format(api_version,
                                                                                        tenant_id,
                                                                                        policyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules/{}".format(api_version,
                                                                                           tenant_id,
                                                                                           policyset_id,
                                                                                           policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def policysets(self, policyset_id=None, tenant_id=None, api_version="v3.0"):
        """
        Get all policy sets of tenant.

          **Parameters:**:

          - **policyset_id**: (optional) Policy Set ID
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

        if not policyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets".format(api_version,
                                                                         tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}".format(api_version,
                                                                            tenant_id,
                                                                            policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def policysets_status(self, policyset_id, tenant_id=None, api_version="v3.0"):
        """
        Get a specific policy set status of tenant.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/status".format(api_version,
                                                                               tenant_id,
                                                                               policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prefixfilters(self, site_id, prefixfilter_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site security filters

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: (optional) Prefix Filter ID
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

        if not prefixfilter_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def profile(self, api_version="v2.0"):
        """
        Get current user profile

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/profile".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def request_get_site_best_art(self, request_id, tenant_id=None, api_version="v2.0"):
        """
        GET Request_Get_Site_Best_Art API Function

          **Parameters:**:

          - **request_id**: Request ID to be queried for status.
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/get_site_best_art/request/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       request_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def request_get_site_best_bw_usage(self, request_id, tenant_id=None, api_version="v2.0"):
        """
        GET Request_Get_Site_Best_Bw_Usage API Function

          **Parameters:**:

          - **request_id**: Request ID to be queried for status.
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/get_site_best_bw_usage/request/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            request_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def request_site_best_app_path(self, request_id, tenant_id=None, api_version="v2.0"):
        """
        GET Request_Site_Best_App_Path API Function

          **Parameters:**:

          - **request_id**: Request ID to be queried for status.
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/site_best_app_path/request/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        request_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def request_sites_best_app_path(self, request_id, tenant_id=None, api_version="v2.0"):
        """
        GET Request_Sites_Best_App_Path API Function

          **Parameters:**:

          - **request_id**: Request ID to be queried for status.
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites_best_app_path/request/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         request_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def roles(self, role_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get a list of custom roles

          **Parameters:**:

          - **role_id**: (optional) Role ID
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

        if not role_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/roles".format(api_version,
                                                                    tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/roles/{}".format(api_version,
                                                                       tenant_id,
                                                                       role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def roles_clients(self, client_id, role_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get a list of client custom roles

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **role_id**: (optional) Role ID
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

        if not role_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/roles".format(api_version,
                                                                               tenant_id,
                                                                               client_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/roles/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  client_id,
                                                                                  role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get tenant security policy rules.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: (optional) Security Policy Rule ID
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

        if not securitypolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules".format(api_version,
                                                                                                        tenant_id,
                                                                                                        securitypolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                           tenant_id,
                                                                                                           securitypolicyset_id,
                                                                                                           securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securitypolicysets(self, securitypolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get tenant security policy sets.

          **Parameters:**:

          - **securitypolicyset_id**: (optional) Security Policy Set ID
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

        if not securitypolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def securityzones(self, securityzone_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get security zones

          **Parameters:**:

          - **securityzone_id**: (optional) Security Zone (ZBFW) ID
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

        if not securityzone_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones/{}".format(api_version,
                                                                               tenant_id,
                                                                               securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def servicebindingmaps(self, servicebindingmap_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get getServiceBindingMapList

          **Parameters:**:

          - **servicebindingmap_id**: (optional) Service Binding Map ID
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

        if not servicebindingmap_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def serviceendpoints(self, serviceendpoint_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get ServiceEndpointList

          **Parameters:**:

          - **serviceendpoint_id**: (optional) Service Endpoint ID
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

        if not serviceendpoint_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints".format(api_version,
                                                                               tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def servicelabels(self, servicelabel_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get getServiceLabelList

          **Parameters:**:

          - **servicelabel_id**: (optional) Service Label ID
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

        if not servicelabel_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels/{}".format(api_version,
                                                                               tenant_id,
                                                                               servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_extensions(self, site_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all site level extensions from NB

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: (optional) Extension ID
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

        if not extension_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id,
                                                                                     extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_status(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        GET Site_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/status".format(api_version,
                                                                          tenant_id,
                                                                          site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def siteciphers(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        Get Site Ciphers

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/siteciphers".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sites(self, site_id=None, tenant_id=None, api_version="v4.1"):
        """
        Get Sites of a tenant

          **Parameters:**:

          - **site_id**: (optional) Site ID
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

        if not site_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites".format(api_version,
                                                                    tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                       tenant_id,
                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sitesecurityzones(self, site_id, sitesecurityzone_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site security zones

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: (optional) Site Security Zone ID
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

        if not sitesecurityzone_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snmpagents(self, site_id, element_id, snmpagent_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get SNMP Agent on an element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: (optional) SNMP Agent ID
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

        if not snmpagent_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmpagents".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def snmptraps(self, site_id, element_id, snmptrap_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get All SNMP Trap on an element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: (optional) SNMP Trap ID
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

        if not snmptrap_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmptraps".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def software_status(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        GET Software_Status API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/software/status".format(api_version,
                                                                                      tenant_id,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def state(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        GET State API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/state".format(api_version,
                                                                            tenant_id,
                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def state_vpnlinks(self, vpnlink_id, tenant_id=None, api_version="v2.0"):
        """
        GET State_Vpnlinks API Function

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/{}/state".format(api_version,
                                                                            tenant_id,
                                                                            vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def staticroutes(self, site_id, element_id, staticroute_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Staticroutes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: (optional) Static Route ID
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

        if not staticroute_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                                   tenant_id,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sys_metrics_monitor(self, tenant_id=None, api_version="v2.0"):
        """
        GET Sys_Metrics_Monitor API Function

          **Parameters:**:

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
        return self._parent_class.rest_call(url, "get")

    def syslogservers(self, site_id, element_id, syslogserver_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Syslogservers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: (optional)
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

        if not syslogserver_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_access(self, access_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get full invocation trail for given tenant

          **Parameters:**:

          - **access_id**: (optional) Access ID
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

        if not access_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/access".format(api_version,
                                                                     tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/access/{}".format(api_version,
                                                                        tenant_id,
                                                                        access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_anynetlinks(self, anynetlink_id, tenant_id=None, api_version="v3.0"):
        """
        GET Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/anynetlinks/{}".format(api_version,
                                                                         tenant_id,
                                                                         anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_api_versions(self, tenant_id=None, api_version="v2.0"):
        """
        Get API versions for given apiVersions

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/api_versions".format(api_version,
                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_clients(self, tenant_id=None, api_version="v2.0"):
        """
        Get esp tenant clients details for tenant id

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients".format(api_version,
                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_elementpassageconfigs(self, tenant_id=None, api_version="v2.0"):
        """
        GET Tenant_Elementpassageconfigs API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementpassageconfigs".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_operators(self, operator_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get a list of tenant operators

          **Parameters:**:

          - **operator_id**: (optional) Operator ID
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

        if not operator_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators".format(api_version,
                                                                        tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}".format(api_version,
                                                                           tenant_id,
                                                                           operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_passages(self, tenant_id=None, api_version="v2.0"):
        """
        GET Tenant_Passages API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/passages".format(api_version,
                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_permissions(self, permission_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get a list of custom permissions

          **Parameters:**:

          - **permission_id**: (optional) Permission ID
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

        if not permission_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/permissions".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/permissions/{}".format(api_version,
                                                                             tenant_id,
                                                                             permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenantpassageconfigs(self, tenant_id=None, api_version="v2.0"):
        """
        GET Tenantpassageconfigs API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/tenantpassageconfigs".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenants(self, tenant_id=None, api_version="v2.0"):
        """
        GET Tenants API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}".format(api_version,
                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def users(self, user_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Users API Function

          **Parameters:**:

          - **user_id**: (optional) User ID
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

        if not user_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/users".format(api_version,
                                                                    tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/users/{}".format(api_version,
                                                                       tenant_id,
                                                                       user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicense_status(self, vfflicense_id, tenant_id=None, api_version="v2.0"):
        """
        GET Vfflicense_Status API Function

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/status".format(api_version,
                                                                                tenant_id,
                                                                                vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicense_tokens(self, vfflicense_id, token_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Tokens for Tenant

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **token_id**: (optional) Token ID
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

        if not token_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/tokens".format(api_version,
                                                                                    tenant_id,
                                                                                    vfflicense_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/tokens/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       vfflicense_id,
                                                                                       token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicenses(self, vfflicense_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all License for Tenant

          **Parameters:**:

          - **vfflicense_id**: (optional) Virtual Form Factor License ID
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

        if not vfflicense_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}".format(api_version,
                                                                             tenant_id,
                                                                             vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vpnlinks_status(self, vpnlink_id, tenant_id=None, api_version="v2.0"):
        """
        GET Vpnlinks_Status API Function

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/{}/status".format(api_version,
                                                                             tenant_id,
                                                                             vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfacelabels(self, waninterfacelabel_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get WAN interface labels for a tenant.

          **Parameters:**:

          - **waninterfacelabel_id**: (optional) WAN Interface Label ID
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

        if not waninterfacelabel_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfaces(self, site_id, waninterface_id=None, tenant_id=None, api_version="v2.1"):
        """
        GET Waninterfaces API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: (optional) WAN Interface ID
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

        if not waninterface_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfaces_status(self, site_id, waninterface_id, tenant_id=None, api_version="v2.1"):
        """
        GET Waninterfaces_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/{}/status".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wannetworks(self, wannetwork_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET all tenant WAN networks

          **Parameters:**:

          - **wannetwork_id**: (optional) WAN Network ID
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

        if not wannetwork_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks/{}".format(api_version,
                                                                             tenant_id,
                                                                             wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanoverlaychannels(self, wanoverlaychannel_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Wanoverlaychannels API Function

          **Parameters:**:

          - **wanoverlaychannel_id**: (optional) WAN Overlay Channel ID
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

        if not wanoverlaychannel_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlaychannels".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlaychannels/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    wanoverlaychannel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanoverlays(self, wanoverlay_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get app/wan contexts

          **Parameters:**:

          - **wanoverlay_id**: (optional) WAN Overlay ID
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

        if not wanoverlay_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlays".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlays/{}".format(api_version,
                                                                             tenant_id,
                                                                             wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def wanpaths(self, site_id, tenant_id=None, api_version="v3.0"):
        """
        GET Wanpaths API Function

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/wanpaths".format(api_version,
                                                                            tenant_id,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    access_t = tenant_access
    """ Backwards-compatibility alias of `access_t` to `tenant_access`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    api_versions_t = tenant_api_versions
    """ Backwards-compatibility alias of `api_versions_t` to `tenant_api_versions`"""

    clients_t = tenant_clients
    """ Backwards-compatibility alias of `clients_t` to `tenant_clients`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

    elementpassageconfigs_t = tenant_elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_t` to `tenant_elementpassageconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    passages_t = tenant_passages
    """ Backwards-compatibility alias of `passages_t` to `tenant_passages`"""

    permissions_clients_d = esp_operator_permissions
    """ Backwards-compatibility alias of `permissions_clients_d` to `esp_operator_permissions`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    status_coreroutepeers_i = corerouterpeers_status_single
    """ Backwards-compatibility alias of `status_coreroutepeers_i` to `corerouterpeers_status_single`"""

    status_coreroutepeers_s = corerouterpeers_status
    """ Backwards-compatibility alias of `status_coreroutepeers_s` to `corerouterpeers_status`"""

    status_edgeroutepeers_i = edgerouterpeers_status_single
    """ Backwards-compatibility alias of `status_edgeroutepeers_i` to `edgerouterpeers_status_single`"""

    status_edgeroutepeers_s = edgerouterpeers_status
    """ Backwards-compatibility alias of `status_edgeroutepeers_s` to `edgerouterpeers_status`"""

    status_hubclustermembers = hubclustermember_status
    """ Backwards-compatibility alias of `status_hubclustermembers` to `hubclustermember_status`"""

    status_i = hubcluster_status
    """ Backwards-compatibility alias of `status_i` to `hubcluster_status`"""

    status_interfaces = interfaces_status
    """ Backwards-compatibility alias of `status_interfaces` to `interfaces_status`"""

    status_policysets = policysets_status
    """ Backwards-compatibility alias of `status_policysets` to `policysets_status`"""

    status_s = site_status
    """ Backwards-compatibility alias of `status_s` to `site_status`"""

    status_software = software_status
    """ Backwards-compatibility alias of `status_software` to `software_status`"""

    status_vfflicenses = vfflicense_status
    """ Backwards-compatibility alias of `status_vfflicenses` to `vfflicense_status`"""

    status_vpnlinks = vpnlinks_status
    """ Backwards-compatibility alias of `status_vpnlinks` to `vpnlinks_status`"""

    status_waninterfaces = waninterfaces_status
    """ Backwards-compatibility alias of `status_waninterfaces` to `waninterfaces_status`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

    # "XYZ_single" compatibility maps below, mapping what is available previously
    # with a deprecated message.

    def access_elementusers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `access_elementusers_single` to `access_elementusers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: access_elementusers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use access_elementusers() instead.")
        return self.access_elementusers(*args, **kwargs)

    def appdefs_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `appdefs_single` to `appdefs`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: appdefs_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use appdefs() instead.")
        return self.appdefs(*args, **kwargs)

    def appdefs_version_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `appdefs_version_single` to `appdefs_version`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: appdefs_version_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use appdefs_version() instead.")
        return self.appdefs_version(*args, **kwargs)

    def coreroutepeers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `coreroutepeers_single` to `coreroutepeers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: coreroutepeers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use coreroutepeers() instead.")
        return self.coreroutepeers(*args, **kwargs)

    def dhcpservers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `dhcpservers_single` to `dhcpservers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: dhcpservers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use dhcpservers() instead.")
        return self.dhcpservers(*args, **kwargs)

    def edgeroutepeers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `edgeroutepeers_single` to `edgeroutepeers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: edgeroutepeers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use edgeroutepeers() instead.")
        return self.edgeroutepeers(*args, **kwargs)

    def element_extensions_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `element_extensions_single` to `element_extensions`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: element_extensions_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use element_extensions() instead.")
        return self.element_extensions(*args, **kwargs)

    def element_images_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `element_images_single` to `element_images`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: element_images_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use element_images() instead.")
        return self.element_images(*args, **kwargs)

    def element_passages_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `element_passages_single` to `element_passages`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: element_passages_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use element_passages() instead.")
        return self.element_passages(*args, **kwargs)

    def elementaccessconfigs_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `elementaccessconfigs_single` to `elementaccessconfigs`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: elementaccessconfigs_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use elementaccessconfigs() instead.")
        return self.elementaccessconfigs(*args, **kwargs)

    def elements_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `elements_single` to `elements`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: elements_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use elements() instead.")
        return self.elements(*args, **kwargs)

    def elementusers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `elementusers_single` to `elementusers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: elementusers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use elementusers() instead.")
        return self.elementusers(*args, **kwargs)

    def globalprefixfilters_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `globalprefixfilters_single` to `globalprefixfilters`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: globalprefixfilters_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use globalprefixfilters() instead.")
        return self.globalprefixfilters(*args, **kwargs)

    def hubclustermembers_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `hubclustermembers_single` to `hubclustermembers`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: hubclustermembers_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use hubclustermembers() instead.")
        return self.hubclustermembers(*args, **kwargs)

    def hubclusters_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `hubclusters_single` to `hubclusters`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: hubclusters_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use hubclusters() instead.")
        return self.hubclusters(*args, **kwargs)

    def idps_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `idps_single` to `idps`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: idps_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use idps() instead.")
        return self.idps(*args, **kwargs)

    def interfaces_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `interfaces_single` to `interfaces`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: interfaces_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use interfaces() instead.")
        return self.interfaces(*args, **kwargs)

    def lannetworks_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `lannetworks_single` to `lannetworks`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: lannetworks_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use lannetworks() instead.")
        return self.lannetworks(*args, **kwargs)

    def localprefixfilters_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `localprefixfilters_single` to `localprefixfilters`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: localprefixfilters_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use localprefixfilters() instead.")
        return self.localprefixfilters(*args, **kwargs)

    def machines_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `machines_single` to `machines`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: machines_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use machines() instead.")
        return self.machines(*args, **kwargs)

    def networkcontexts_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `networkcontexts_single` to `networkcontexts`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: networkcontexts_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use networkcontexts() instead.")
        return self.networkcontexts(*args, **kwargs)

    def pathgroups_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `pathgroups_single` to `pathgroups`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: pathgroups_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use pathgroups() instead.")
        return self.pathgroups(*args, **kwargs)

    def policyrules_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `policyrules_single` to `policyrules`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: policyrules_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use policyrules() instead.")
        return self.policyrules(*args, **kwargs)

    def policysets_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `policysets_single` to `policysets`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: policysets_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use policysets() instead.")
        return self.policysets(*args, **kwargs)

    def prefixfilters_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `prefixfilters_single` to `prefixfilters`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: prefixfilters_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use prefixfilters() instead.")
        return self.prefixfilters(*args, **kwargs)

    def roles_clients_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `roles_clients_single` to `roles_clients`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: roles_clients_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use roles_clients() instead.")
        return self.roles_clients(*args, **kwargs)

    def roles_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `roles_single` to `roles`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: roles_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use roles() instead.")
        return self.roles(*args, **kwargs)

    def securitypolicyrules_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `securitypolicyrules_single` to `securitypolicyrules`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: securitypolicyrules_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use securitypolicyrules() instead.")
        return self.securitypolicyrules(*args, **kwargs)

    def securitypolicysets_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `securitypolicysets_single` to `securitypolicysets`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: securitypolicysets_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use securitypolicysets() instead.")
        return self.securitypolicysets(*args, **kwargs)

    def securityzones_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `securityzones_single` to `securityzones`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: securityzones_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use securityzones() instead.")
        return self.securityzones(*args, **kwargs)

    def servicebindingmaps_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `servicebindingmaps_single` to `servicebindingmaps`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: servicebindingmaps_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use servicebindingmaps() instead.")
        return self.servicebindingmaps(*args, **kwargs)

    def serviceendpoints_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `serviceendpoints_single` to `serviceendpoints`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: serviceendpoints_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use serviceendpoints() instead.")
        return self.serviceendpoints(*args, **kwargs)

    def servicelabels_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `servicelabels_single` to `servicelabels`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: servicelabels_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use servicelabels() instead.")
        return self.servicelabels(*args, **kwargs)

    def site_extensions_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `site_extensions_single` to `site_extensions`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: site_extensions_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use site_extensions() instead.")
        return self.site_extensions(*args, **kwargs)

    def sites_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `sites_single` to `sites`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: sites_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use sites() instead.")
        return self.sites(*args, **kwargs)

    def sitesecurityzones_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `sitesecurityzones_single` to `sitesecurityzones`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: sitesecurityzones_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use sitesecurityzones() instead.")
        return self.sitesecurityzones(*args, **kwargs)

    def snmpagents_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `snmpagents_single` to `snmpagents`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: snmpagents_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use snmpagents() instead.")
        return self.snmpagents(*args, **kwargs)

    def snmptraps_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `snmptraps_single` to `snmptraps`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: snmptraps_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use snmptraps() instead.")
        return self.snmptraps(*args, **kwargs)

    def staticroutes_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `staticroutes_single` to `staticroutes`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: staticroutes_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use staticroutes() instead.")
        return self.staticroutes(*args, **kwargs)

    def tenant_access_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `tenant_access_single` to `tenant_access`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: tenant_access_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use tenant_access() instead.")
        return self.tenant_access(*args, **kwargs)

    def tenant_operators_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `tenant_operators_single` to `tenant_operators`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: tenant_operators_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use tenant_operators() instead.")
        return self.tenant_operators(*args, **kwargs)

    def tenant_permissions_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `tenant_permissions_single` to `tenant_permissions`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: tenant_permissions_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use tenant_permissions() instead.")
        return self.tenant_permissions(*args, **kwargs)

    def users_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `users_single` to `users`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: users_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use users() instead.")
        return self.users(*args, **kwargs)

    def vfflicense_tokens_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `vfflicense_tokens_single` to `vfflicense_tokens`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: vfflicense_tokens_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use vfflicense_tokens() instead.")
        return self.vfflicense_tokens(*args, **kwargs)

    def vfflicenses_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `vfflicenses_single` to `vfflicenses`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: vfflicenses_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use vfflicenses() instead.")
        return self.vfflicenses(*args, **kwargs)

    def waninterfacelabels_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `waninterfacelabels_single` to `waninterfacelabels`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: waninterfacelabels_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use waninterfacelabels() instead.")
        return self.waninterfacelabels(*args, **kwargs)

    def waninterfaces_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `waninterfaces_single` to `waninterfaces`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: waninterfaces_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use waninterfaces() instead.")
        return self.waninterfaces(*args, **kwargs)

    def wannetworks_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `wannetworks_single` to `wannetworks`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: wannetworks_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use wannetworks() instead.")
        return self.wannetworks(*args, **kwargs)

    def wanoverlaychannels_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `wanoverlaychannels_single` to `wanoverlaychannels`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: wanoverlaychannels_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use wanoverlaychannels() instead.")
        return self.wanoverlaychannels(*args, **kwargs)

    def wanoverlays_single(self, *args, **kwargs):
        """
        Backwards-compatibility alias of `wanoverlays_single` to `wanoverlays`.

        **TO BE REMOVED** on Sept 1, 2018.

        """
        api_logger.warning("WARN: wanoverlays_single() is deprecated, and will be removed on Sept 1, 2018."
                           " Use wanoverlays() instead.")
        return self.wanoverlays(*args, **kwargs)

