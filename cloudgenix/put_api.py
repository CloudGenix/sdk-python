#!/usr/bin/env python
"""
CloudGenix Python SDK - PUT

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


class Put(object):
    """
    CloudGenix API - PUT requests

    Object to handle making Put requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def access_elementusers(self, elementuser_id, access_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element user access.

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: Access ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs(self, appdef_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a custom application definition

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}".format(api_version,
                                                                     tenant_id,
                                                                     appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_overrides(self, appdef_id, override_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a application definition overrides for system appdef

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: AppDef Override ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  appdef_id,
                                                                                  override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def appdefs_version(self, appdefs_version_id, data, tenant_id=None, api_version="v2.0"):
        """
        Change standard apps version

          **Parameters:**:

          - **appdefs_version_id**: Application Definition Version ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs_version/{}".format(api_version,
                                                                             tenant_id,
                                                                             appdefs_version_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgpconfigs(self, site_id, element_id, bgpconfig_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates BGP config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgpconfig_id**: BGP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgpconfigs/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id,
                                                                                             bgpconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def bgppeers(self, site_id, element_id, bgppeer_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates BGP Peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def dhcpservers(self, site_id, dhcpserver_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Dhcpservers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def element_admin_state(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Element_Admin_State API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/admin_state".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def element_extensions(self, site_id, element_id, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update element level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def elementaccessconfigs(self, element_id, elementaccessconfig_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update an Access Config on particular element.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: Element Access Config ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/elementaccessconfigs/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              element_id,
                                                                                              elementaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elements(self, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Used for associations and element updates

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}".format(api_version,
                                                                      tenant_id,
                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def elementusers(self, elementuser_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element user.

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def enterpriseprefixset(self, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Enterpriseprefixset API Function

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def esp_operator_permissions_client(self, operator_id, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create or update esp operator permissions assigned under a client

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def events(self, event_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Events API Function

          **Parameters:**:

          - **event_id**: Event ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def globalprefixfilters(self, globalprefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a new global prefix filter.

          **Parameters:**:

          - **globalprefixfilter_id**: Global Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclustermembers(self, site_id, hubcluster_id, hubclustermember_id, data, tenant_id=None, api_version="v3.0"):
        """
        PUT Hubclustermembers API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **hubclustermember_id**: Hub Cluster Member ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def hubclusters(self, site_id, hubcluster_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update hub cluster

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def idps(self, idp_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update sso

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def interfaces(self, site_id, element_id, interface_id, data, tenant_id=None, api_version="v4.5"):
        """
        Provision an element interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.5)

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
        return self._parent_class.rest_call(url, "put", data=data)

    def ipsecprofiles(self, ipsecprofile_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a IPSECProfile

          **Parameters:**:

          - **ipsecprofile_id**: IPSEC Profile ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles/{}".format(api_version,
                                                                           tenant_id,
                                                                           ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def lannetworks(self, site_id, lannetwork_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update existing LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/lannetworks/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  lannetwork_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def localprefixfilters(self, localprefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a new local prefix filter.

          **Parameters:**:

          - **localprefixfilter_id**: Local Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def networkcontexts(self, networkcontext_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update LAN segment

          **Parameters:**:

          - **networkcontext_id**: Network Context ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a Network global prefix.

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: Network Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update network policy rule of tenant.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: Network Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     networkpolicyset_id,
                                                                                                     networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysets(self, networkpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Network Policy Set.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}".format(api_version,
                                                                               tenant_id,
                                                                               networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def networkpolicysetstacks(self, networkpolicysetstack_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a NetworkPolicySetStack

          **Parameters:**:

          - **networkpolicysetstack_id**: Network Policy Set Stack ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ntp(self, element_id, ntp_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing element NTP.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/ntp/{}".format(api_version,
                                                                             tenant_id,
                                                                             element_id,
                                                                             ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def ntp_templates(self, ntp_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing NTP Template

          **Parameters:**:

          - **ntp_id**: NTP Configuration ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/templates/ntp/{}".format(api_version,
                                                                           tenant_id,
                                                                           ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def otpaccessconfigs(self, otpaccessconfig_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an OTP Access for all elements under an Tenant.

          **Parameters:**:

          - **otpaccessconfig_id**: OTP Access configuration ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/otpaccessconfigs/{}".format(api_version,
                                                                              tenant_id,
                                                                              otpaccessconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def pathgroups(self, pathgroup_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update A Path Group of a tenant.

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups/{}".format(api_version,
                                                                        tenant_id,
                                                                        pathgroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def policyrules(self, policyset_id, policyrule_id, data, tenant_id=None, api_version="v3.1"):
        """
        Update policy rule of tenant.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **policyrule_id**: Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def policysets(self, policyset_id, data, tenant_id=None, api_version="v3.0"):
        """
        Update policy set.

          **Parameters:**:

          - **policyset_id**: Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def prefixfilters(self, site_id, prefixfilter_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security prefix filter

          **Parameters:**:

          - **site_id**: Site ID
          - **prefixfilter_id**: Prefix Filter ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Priority global prefix.

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: Priority Policy Global Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                          tenant_id,
                                                                                          prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update priority policy rule of tenant.

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: Priority Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                       tenant_id,
                                                                                                       prioritypolicyset_id,
                                                                                                       prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysets(self, prioritypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Priority Policy Set.

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}".format(api_version,
                                                                                tenant_id,
                                                                                prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def prioritypolicysetstacks(self, prioritypolicysetstack_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a PriorityPolicySetStack

          **Parameters:**:

          - **prioritypolicysetstack_id**: Priority Policy Stack ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     prioritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def roles(self, role_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a custom role

          **Parameters:**:

          - **role_id**: Role ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Access List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: Routing AS-PATH Access List ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                            tenant_id,
                                                                                                            site_id,
                                                                                                            element_id,
                                                                                                            routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Community List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: Routing IP Community List ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                           tenant_id,
                                                                                                           site_id,
                                                                                                           element_id,
                                                                                                           routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Prefix List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: Routing IP Prefix List ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def routing_routemaps(self, site_id, element_id, routing_routemap_id, data, tenant_id=None, api_version="v2.0"):
        """
        Updates Route Map

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: Routing Route Map ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicyrules(self, securitypolicyset_id, securitypolicyrule_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant security policy rule.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **securitypolicyrule_id**: Security Policy Rule ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def securitypolicysets(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant security policy set.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def securityzones(self, securityzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security zone

          **Parameters:**:

          - **securityzone_id**: Security Zone (ZBFW) ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def servicebindingmaps(self, servicebindingmap_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a ServiceBindingMap

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/{}".format(api_version,
                                                                                tenant_id,
                                                                                servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def serviceendpoints(self, serviceendpoint_id, data, tenant_id=None, api_version="v2.1"):
        """
        Update a ServiceEndpoint

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/{}".format(api_version,
                                                                              tenant_id,
                                                                              serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def servicelabels(self, servicelabel_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a ServiceLabel

          **Parameters:**:

          - **servicelabel_id**: Service Label ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def site_admin_state(self, site_id, data, tenant_id=None, api_version="v3.0"):
        """
        PUT Site_Admin_State API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/admin_state".format(api_version,
                                                                               tenant_id,
                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_extensions(self, site_id, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update site level extension configuration

          **Parameters:**:

          - **site_id**: Site ID
          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing Site Network policy local prefix

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing Site Priority policy local prefix

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id,
                                                                                                  prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def siteciphers(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Site Cipher

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def sites(self, site_id, data, tenant_id=None, api_version="v4.2"):
        """
        Update an existing site

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                   tenant_id,
                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def sitesecurityzones(self, site_id, sitesecurityzone_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing security zone

          **Parameters:**:

          - **site_id**: Site ID
          - **sitesecurityzone_id**: Site Security Zone ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def snmpagents(self, site_id, element_id, snmpagent_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update SNMP Agent

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: SNMP Agent ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def snmptraps(self, site_id, element_id, snmptrap_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update SNMP Trap

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmptrap_id**: SNMP Trap ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def state(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT State API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def state_vpnlinks(self, vpnlink_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT State_Vpnlinks API Function

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def staticroutes(self, site_id, element_id, staticroute_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Staticroutes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def syslogservers(self, site_id, element_id, syslogserver_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Syslog Server

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: SYSLOG server ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_anynetlinks(self, anynetlink_id, data, tenant_id=None, api_version="v3.0"):
        """
        PUT Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Network Policy local prefix.

          **Parameters:**:

          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_operators(self, operator_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant operator

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_permissions(self, permission_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a custom permission

          **Parameters:**:

          - **permission_id**: Permission ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a  Priority Policy local prefix.

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def tenants(self, data, tenant_id=None, api_version="v2.0"):
        """
        Update tenant

          **Parameters:**:

          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def users(self, user_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Users API Function

          **Parameters:**:

          - **user_id**: User ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def vfflicense_tokens(self, vfflicense_id, token_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update Token and mark is_revoked as true/false

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **token_id**: Token ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/tokens/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   vfflicense_id,
                                                                                   token_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfacelabels(self, waninterfacelabel_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Waninterfacelabels API Function

          **Parameters:**:

          - **waninterfacelabel_id**: WAN Interface Label ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/{}".format(api_version,
                                                                                tenant_id,
                                                                                waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    def waninterfaces(self, site_id, waninterface_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update the site WAN interface

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **data**: Dictionary containing data to PUT as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

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
        return self._parent_class.rest_call(url, "put", data=data)

    def wannetworks(self, wannetwork_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update an existing WAN

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def wanoverlays(self, wanoverlay_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update app/wan context

          **Parameters:**:

          - **wanoverlay_id**: WAN Overlay ID
          - **data**: Dictionary containing data to PUT as JSON
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
        return self._parent_class.rest_call(url, "put", data=data)

    def ws_extensions(self, extension_id, data, tenant_id=None, api_version="v2.0"):
        """
        PUT Ws_Extensions API Function

          **Parameters:**:

          - **extension_id**: Extension ID
          - **data**: Dictionary containing data to PUT as JSON
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions/{}".format(api_version,
                                                                           tenant_id,
                                                                           extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "put", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    admin_state_i = element_admin_state
    """ Backwards-compatibility alias of `admin_state_i` to `element_admin_state`"""

    admin_state_s = site_admin_state
    """ Backwards-compatibility alias of `admin_state_s` to `site_admin_state`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    networkpolicylocalprefixes_s = site_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_s` to `site_networkpolicylocalprefixes`"""

    networkpolicylocalprefixes_t = tenant_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_t` to `tenant_networkpolicylocalprefixes`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

