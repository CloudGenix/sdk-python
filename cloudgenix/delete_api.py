#!/usr/bin/env python
"""
CloudGenix Python SDK - DELETE

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


class Delete(object):
    """
    CloudGenix API - DELETE requests

    Object to handle making Delete requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def access_elementusers(self, elementuser_id, access_id, tenant_id=None, api_version="v2.0"):
        """
        Delete element user Access

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: Access ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/access/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    elementuser_id,
                                                                                    access_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def appdefs(self, appdef_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an application definition

          **Parameters:**:

          - **appdef_id**: Application Definition ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}".format(api_version,
                                                                     tenant_id,
                                                                     appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def base_permissions(self, base_permission_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Base_Permissions API Function

          **Parameters:**:

          - **base_permission_id**: 
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/base_permissions/{}".format(api_version,
                                                                              tenant_id,
                                                                              base_permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def base_permissions_clients(self, client_id, base_permission_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Base_Permissions_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **base_permission_id**: 
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/base_permissions/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         client_id,
                                                                                         base_permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def coreroutepeers(self, site_id, coreroutepeer_id, tenant_id=None, api_version="v2.1"):
        """
        Deletes core route peer config

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/coreroutepeers/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id,
                                                                                     coreroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dhcpservers(self, site_id, dhcpserver_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Dhcpservers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def edgeroutepeers(self, site_id, edgeroutepeer_id, tenant_id=None, api_version="v2.1"):
        """
        Deletes WAN edge route peer config

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/edgeroutepeers/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id,
                                                                                     edgeroutepeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_extensions(self, site_id, element_id, extension_id, tenant_id=None, api_version="v2.0"):
        """
        Delete specific extension

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: Extension ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/extensions/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_passages(self, element_id, passage_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Element_Passages API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **passage_id**: Passage Configuration ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/passages/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  element_id,
                                                                                  passage_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementpassageconfigs(self, element_id, elementpassageconfig_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Elementpassageconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementpassageconfig_id**: Element Passage Configuration ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementpassageconfigs/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               element_id,
                                                                                               elementpassageconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def elementusers(self, elementuser_id, tenant_id=None, api_version="v2.0"):
        """
        Delete element user 

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}".format(api_version,
                                                                          tenant_id,
                                                                          elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def esp_operator_permissions_client(self, operator_id, client_id, tenant_id=None, api_version="v2.0"):
        """
        Delete esp operator permissions assigned under a client

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
        return self._parent_class.rest_call(url, "delete")

    def esp_tenant_permissions(self, client_id, permission_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Esp_Tenant_Permissions API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **permission_id**: Permission ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/permissions/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    client_id,
                                                                                    permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def globalprefixfilters(self, globalprefixfilter_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a global prefix filter.

          **Parameters:**:

          - **globalprefixfilter_id**: Global Prefix Filter ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 globalprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, tenant_id=None, api_version="v3.0"):
        """
        Deletes specific hub cluster member.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}/hubclustermembers/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id,
                                                                                                       hubcluster_id,
                                                                                                       hubclustermember_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def hubclusters(self, site_id, hubcluster_id, tenant_id=None, api_version="v3.0"):
        """
        Delete hub cluster

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubclusters/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  hubcluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def idps(self, idp_id, tenant_id=None, api_version="v2.0"):
        """
        Delete idp

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/idps/{}".format(api_version,
                                                                  tenant_id,
                                                                  idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def interfaces(self, site_id, element_id, interface_id, tenant_id=None, api_version="v4.1"):
        """
        Delete an element interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def lannetworks(self, site_id, lannetwork_id, tenant_id=None, api_version="v2.0"):
        """
        Delete existing LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def localprefixfilters(self, localprefixfilter_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a local prefix filter.

          **Parameters:**:

          - **localprefixfilter_id**: Local Prefix Filter ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters/{}".format(api_version,
                                                                                tenant_id,
                                                                                localprefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkcontexts(self, networkcontext_id, tenant_id=None, api_version="v2.0"):
        """
        Delete LAN segment

          **Parameters:**:

          - **networkcontext_id**: Network Context ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts/{}".format(api_version,
                                                                             tenant_id,
                                                                             networkcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def pathgroups(self, pathgroup_id, tenant_id=None, api_version="v2.0"):
        """
        Delete A Path Group of a tenant.

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups/{}".format(api_version,
                                                                        tenant_id,
                                                                        pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def policyrules(self, policyset_id, policyrule_id, tenant_id=None, api_version="v3.1"):
        """
        Delete policy rule of tenant.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: Policy Rule ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}/policyrules/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       policyset_id,
                                                                                       policyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def policysets(self, policyset_id, tenant_id=None, api_version="v3.0"):
        """
        Delete policy set.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/{}".format(api_version,
                                                                        tenant_id,
                                                                        policyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def prefixfilters(self, site_id, prefixfilter_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing security prefix filter

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: Prefix Filter ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prefixfilters/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    prefixfilter_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def roles(self, role_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Roles API Function

          **Parameters:**:

          - **role_id**: Role ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/roles/{}".format(api_version,
                                                                   tenant_id,
                                                                   role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def roles_clients(self, client_id, role_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Roles_Clients API Function

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **role_id**: Role ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/roles/{}".format(api_version,
                                                                              tenant_id,
                                                                              client_id,
                                                                              role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a security policyrule.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: Security Policy Rule ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}/securitypolicyrules/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       securitypolicyset_id,
                                                                                                       securitypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securitypolicysets(self, securitypolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a security policyset.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/{}".format(api_version,
                                                                                tenant_id,
                                                                                securitypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def securityzones(self, securityzone_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing security zone

          **Parameters:**:

          - **securityzone_id**: Security Zone (ZBFW) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones/{}".format(api_version,
                                                                           tenant_id,
                                                                           securityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def servicebindingmaps(self, servicebindingmap_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Service Binding Map

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/{}".format(api_version,
                                                                                tenant_id,
                                                                                servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def serviceendpoints(self, serviceendpoint_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Service Endpoint

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/{}".format(api_version,
                                                                              tenant_id,
                                                                              serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def servicelabels(self, servicelabel_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Service Label

          **Parameters:**:

          - **servicelabel_id**: Service Label ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels/{}".format(api_version,
                                                                           tenant_id,
                                                                           servicelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_extensions(self, site_id, extension_id, tenant_id=None, api_version="v2.0"):
        """
        Delete specific extension

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: Extension ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/extensions/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id,
                                                                                 extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sites(self, site_id, tenant_id=None, api_version="v4.1"):
        """
        Delete a site

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                   tenant_id,
                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sitesecurityzones(self, site_id, sitesecurityzone_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing security zone

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: Site Security Zone ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/sitesecurityzones/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        sitesecurityzone_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def snmpagents(self, site_id, element_id, snmpagent_id, tenant_id=None, api_version="v2.0"):
        """
        delete SNMP Agent

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: SNMP Agent ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmpagents/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             snmpagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def snmptraps(self, site_id, element_id, snmptrap_id, tenant_id=None, api_version="v2.0"):
        """
        delete SNMP Trap

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: SNMP Trap ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/snmptraps/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            snmptrap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def staticroutes(self, site_id, element_id, staticroute_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Staticroutes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_anynetlinks(self, anynetlink_id, tenant_id=None, api_version="v3.0"):
        """
        DELETE Tenant_Anynetlinks API Function

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
        return self._parent_class.rest_call(url, "delete")

    def tenant_operators(self, operator_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a tenant operator

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}".format(api_version,
                                                                       tenant_id,
                                                                       operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_permissions(self, permission_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Tenant_Permissions API Function

          **Parameters:**:

          - **permission_id**: Permission ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/permissions/{}".format(api_version,
                                                                         tenant_id,
                                                                         permission_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenantpassageconfigs(self, tenantpassageconfig_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Tenantpassageconfigs API Function

          **Parameters:**:

          - **tenantpassageconfig_id**: Tenant Passage Config ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/tenantpassageconfigs/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  tenantpassageconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def users(self, user_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Users API Function

          **Parameters:**:

          - **user_id**: User ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/users/{}".format(api_version,
                                                                   tenant_id,
                                                                   user_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def waninterfaces(self, site_id, waninterface_id, tenant_id=None, api_version="v2.1"):
        """
        DELETE Waninterfaces API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def wannetworks(self, wannetwork_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing WAN

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wannetworks/{}".format(api_version,
                                                                         tenant_id,
                                                                         wannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def wanoverlays(self, wanoverlay_id, tenant_id=None, api_version="v2.0"):
        """
        Delete app/wan context

          **Parameters:**:

          - **wanoverlay_id**: WAN Overlay ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/wanoverlays/{}".format(api_version,
                                                                         tenant_id,
                                                                         wanoverlay_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_clients_t = esp_tenant_permissions
    """ Backwards-compatibility alias of `permissions_clients_t` to `esp_tenant_permissions`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

