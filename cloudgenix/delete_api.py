#!/usr/bin/env python
"""
CloudGenix Python SDK - DELETE

**Author:** CloudGenix

**Copyright:** (c) 2017-2021 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2021 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017-2021 CloudGenix, Inc

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

    def appdefs(self, appdef_id, tenant_id=None, api_version="v2.3"):
        """
        Delete a application definition

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

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

    def appdefs_overrides(self, appdef_id, override_id, tenant_id=None, api_version="v2.2"):
        """
        Delete application definition overrides for system appdef

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: AppDef Override ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  appdef_id,
                                                                                  override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def authtokens(self, operator_id, authtoken_id, tenant_id=None, api_version="v2.1"):
        """
        Delete an auth token

          **Parameters:**:

          - **operator_id**: Operator ID
          - **authtoken_id**: Static AUTH_TOKEN ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/authtokens/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     operator_id,
                                                                                     authtoken_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def bgppeers(self, site_id, element_id, bgppeer_id, tenant_id=None, api_version="v2.2"):
        """
        Delete BGP Peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id,
                                                                                           bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dhcpservers(self, site_id, dhcpserver_id, tenant_id=None, api_version="v2.1"):
        """
        Delete DHCPServer for a Tenant on a site

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: DHCP Server ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/dhcpservers/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id,
                                                                                  dhcpserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsserviceprofiles(self, dnsserviceprofile_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a DNS service profile

          **Parameters:**:

          - **dnsserviceprofile_id**: DNS Service Profile ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles/{}".format(api_version,
                                                                                tenant_id,
                                                                                dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsserviceroles(self, dnsservicerole_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a DNS service role

          **Parameters:**:

          - **dnsservicerole_id**: DNS Service Role ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles/{}".format(api_version,
                                                                             tenant_id,
                                                                             dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def dnsservices(self, site_id, element_id, dnsservice_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a DNS service config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: DNS Service ID 
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id,
                                                                                              dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def element_extensions(self, site_id, element_id, extension_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a specific extension associated with an element

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

    def element_toolkitsessions(self, element_id, toolkitsession_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Element_Toolkitsessions API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **toolkitsession_id**: Toolkit Session ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/toolkitsessions/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         element_id,
                                                                                         toolkitsession_id)

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

    def elementsecurityzones(self, site_id, element_id, securityzone_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing security zone

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                securityzone_id)

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

    def esp_operator_permissions_client(self, operator_id, client_id, tenant_id=None, api_version="v2.1"):
        """
        Delete esp operator permissions assigned under a client

          **Parameters:**:

          - **operator_id**: Operator ID
          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/clients/{}/permissions".format(api_version,
                                                                                              tenant_id,
                                                                                              operator_id,
                                                                                              client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Eventcorrelationpolicyrules API Function

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: Event Correlation Policy Rule ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                       tenant_id,
                                                                                                                       eventcorrelationpolicyset_id,
                                                                                                                       eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Eventcorrelationpolicysets API Function

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def externalcaconfigs(self, externalcaconfig_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: External CA Config ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/externalcaconfigs/{}".format(api_version,
                                                                               tenant_id,
                                                                               externalcaconfig_id)

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

    def idps(self, idp_id, tenant_id=None, api_version="v3.2"):
        """
        Delete idp

          **Parameters:**:

          - **idp_id**: SAML IDentity provider configuration ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.2)

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

    def interfaces(self, site_id, element_id, interface_id, tenant_id=None, api_version="v4.10"):
        """
        Delete an element interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.10)

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

    def ipfix(self, site_id, element_id, ipfix_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfix API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: IPFix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        element_id,
                                                                                        ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfixcollectorcontexts API Function

          **Parameters:**:

          - **ipfixcollectorcontext_id**: IPFix Collector Context ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixfiltercontexts(self, ipfixfiltercontext_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfixfiltercontexts API Function

          **Parameters:**:

          - **ipfixfiltercontext_id**: IPFix Filter Context ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixglobalprefixes(self, ipfixglobalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfixglobalprefixes API Function

          **Parameters:**:

          - **ipfixglobalprefix_id**: IPFix Global Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixprofiles(self, ipfixprofile_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfixprofiles API Function

          **Parameters:**:

          - **ipfixprofile_id**: IPFix Profile ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles/{}".format(api_version,
                                                                           tenant_id,
                                                                           ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipfixtemplates(self, ipfixtemplate_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ipfixtemplates API Function

          **Parameters:**:

          - **ipfixtemplate_id**: IPFix Template ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates/{}".format(api_version,
                                                                            tenant_id,
                                                                            ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def ipsecprofiles(self, ipsecprofile_id, tenant_id=None, api_version="v2.1"):
        """
        Delete a IPSEC Profile

          **Parameters:**:

          - **ipsecprofile_id**: IPSEC Profile ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles/{}".format(api_version,
                                                                           tenant_id,
                                                                           ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def lannetworks(self, site_id, lannetwork_id, tenant_id=None, api_version="v3.1"):
        """
        Delete an existing LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: LAN Network ID
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

    def natglobalprefixes(self, natglobalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a NAT Global Prefix.

          **Parameters:**:

          - **natglobalprefix_id**: NAT Global Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes/{}".format(api_version,
                                                                               tenant_id,
                                                                               natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natlocalprefixes(self, natlocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a NAT local prefix.

          **Parameters:**:

          - **natlocalprefix_id**: NAT Local Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes/{}".format(api_version,
                                                                              tenant_id,
                                                                              natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicypools(self, natpolicypool_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a NAT Policy Pool.

          **Parameters:**:

          - **natpolicypool_id**: NAT Policy Pool ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools/{}".format(api_version,
                                                                            tenant_id,
                                                                            natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id, tenant_id=None, api_version="v2.0"):
        """
        Delete NAT policy rule of tenant.

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: NAT Policy Rule ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             natpolicyset_id,
                                                                                             natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicysets(self, natpolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Delete NAT policy set.

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}".format(api_version,
                                                                           tenant_id,
                                                                           natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natpolicysetstacks(self, natpolicysetstack_id, tenant_id=None, api_version="v2.0"):
        """
        Delete NAT Policy Set Stack.

          **Parameters:**:

          - **natpolicysetstack_id**: NAT Policy Set Stack ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks/{}".format(api_version,
                                                                                tenant_id,
                                                                                natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def natzones(self, natzone_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Nat Policy Zone.

          **Parameters:**:

          - **natzone_id**: NAT Zone ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones/{}".format(api_version,
                                                                      tenant_id,
                                                                      natzone_id)

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

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Network Policy Global Prefix.

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: Network Policy Global Prefix ID
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
        return self._parent_class.rest_call(url, "delete")

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id, tenant_id=None, api_version="v2.1"):
        """
        Delete network policy rule of tenant.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: Network Policy Rule ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     networkpolicyset_id,
                                                                                                     networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def networkpolicysets(self, networkpolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Delete Network Policy Set.

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
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
        return self._parent_class.rest_call(url, "delete")

    def networkpolicysetstacks(self, networkpolicysetstack_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a NetworkPolicySetStack

          **Parameters:**:

          - **networkpolicysetstack_id**: Network Policy Set Stack ID
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
        return self._parent_class.rest_call(url, "delete")

    def operator_sessions(self, operator_id, session_id, tenant_id=None, api_version="v2.0"):
        """
        Delete session for tenant_id, operator id, and session id

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: User Session ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/sessions/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   operator_id,
                                                                                   session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def pathgroups(self, pathgroup_id, tenant_id=None, api_version="v2.1"):
        """
        Delete A Path Group of a tenant.

          **Parameters:**:

          - **pathgroup_id**: Path Group ID (for network service/DC routing)
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

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Priority Policy Global Prefix.

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: Priority Policy Global Prefix ID
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
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id, tenant_id=None, api_version="v2.0"):
        """
        Delete priority policy rule of tenant.

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: Priority Policy Rule ID
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
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicysets(self, prioritypolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Prioritypolicysets API Function

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
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
        return self._parent_class.rest_call(url, "delete")

    def prioritypolicysetstacks(self, prioritypolicysetstack_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a PriorityPolicySetStack

          **Parameters:**:

          - **prioritypolicysetstack_id**: Priority Policy Stack ID
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
        return self._parent_class.rest_call(url, "delete")

    def roles(self, role_id, tenant_id=None, api_version="v2.1"):
        """
        Delete a custom role

          **Parameters:**:

          - **role_id**: Role ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/roles/{}".format(api_version,
                                                                   tenant_id,
                                                                   role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id, tenant_id=None, api_version="v2.1"):
        """
        Delete Access List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: Routing AS-PATH Access List ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                            tenant_id,
                                                                                                            site_id,
                                                                                                            element_id,
                                                                                                            routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id, tenant_id=None, api_version="v2.0"):
        """
        Delete Community List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: Routing IP Community List ID
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
        return self._parent_class.rest_call(url, "delete")

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id, tenant_id=None, api_version="v2.0"):
        """
        Delete Prefix List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: Routing IP Prefix List ID
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
        return self._parent_class.rest_call(url, "delete")

    def routing_routemaps(self, site_id, element_id, routing_routemap_id, tenant_id=None, api_version="v2.1"):
        """
        Delete Route Map

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: Routing Route Map ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def sdwanapps_configs(self, sdwanapp_id, config_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: SDWAN App Config ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/configs/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  sdwanapp_id,
                                                                                  config_id)

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

    def servicebindingmaps(self, servicebindingmap_id, tenant_id=None, api_version="v2.1"):
        """
        Delete a Service Binding Map

          **Parameters:**:

          - **servicebindingmap_id**: Service Binding Map ID
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
        return self._parent_class.rest_call(url, "delete")

    def serviceendpoints(self, serviceendpoint_id, tenant_id=None, api_version="v2.2"):
        """
        Delete a Service Endpoint

          **Parameters:**:

          - **serviceendpoint_id**: Service Endpoint ID
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
        Delete a specific extension associated with a site

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

    def site_natlocalprefixes(self, site_id, natlocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing Site NAT prefix

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: NAT Local Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id,
                                                                                       natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing Site Network Policy local prefix association

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
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
        return self._parent_class.rest_call(url, "delete")

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing Site Priority Policy local prefix association

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
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
        return self._parent_class.rest_call(url, "delete")

    def sites(self, site_id, tenant_id=None, api_version="v4.5"):
        """
        Delete a site

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                   tenant_id,
                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Site_ipfixlocalprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         ipfixlocalprefix_id)

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

    def spokeclusters(self, site_id, spokecluster_id, tenant_id=None, api_version="v2.0"):
        """
        Delete spoke cluster.

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def staticroutes(self, site_id, element_id, staticroute_id, tenant_id=None, api_version="v2.1"):
        """
        Delete static route

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def syslogservers(self, site_id, element_id, syslogserver_id, tenant_id=None, api_version="v2.1"):
        """
        delete Syslog Server

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: SYSLOG server ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id,
                                                                                                syslogserver_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def templates_ntp(self, ntp_id, tenant_id=None, api_version="v2.0"):
        """
        Delete an existing NTP Template

          **Parameters:**:

          - **ntp_id**: NTP Configuration ID
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
        return self._parent_class.rest_call(url, "delete")

    def tenant_anynetlinks(self, anynetlink_id, tenant_id=None, api_version="v3.2"):
        """
        DELETE Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.2)

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

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Tenant_Ipfixlocalprefixes API Function

          **Parameters:**:

          - **ipfixlocalprefix_id**: IPFix Local Prefix ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                tenant_id,
                                                                                ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Network Policy local prefix.

          **Parameters:**:

          - **networkpolicylocalprefix_id**: Network Policy Local Prefix ID
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
        return self._parent_class.rest_call(url, "delete")

    def tenant_operators(self, operator_id, tenant_id=None, api_version="v2.1"):
        """
        Delete a tenant operator

          **Parameters:**:

          - **operator_id**: Operator ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}".format(api_version,
                                                                       tenant_id,
                                                                       operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    def tenant_permissions(self, permission_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a tenant custom permission

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

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id, tenant_id=None, api_version="v2.0"):
        """
        Delete a Priority Policy local prefix.

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: Priority Policy Local Prefix ID
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

    def waninterfaces(self, site_id, waninterface_id, tenant_id=None, api_version="v2.6"):
        """
        Delete existing WAN interface

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.6)

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

    def wannetworks(self, wannetwork_id, tenant_id=None, api_version="v2.1"):
        """
        Delete an existing WAN

          **Parameters:**:

          - **wannetwork_id**: WAN Network ID
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

    def ws_extensions(self, extension_id, tenant_id=None, api_version="v2.0"):
        """
        DELETE Ws_Extensions API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions/{}".format(api_version,
                                                                           tenant_id,
                                                                           extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "delete")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    networkpolicylocalprefixes_s = site_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_s` to `site_networkpolicylocalprefixes`"""

    networkpolicylocalprefixes_t = tenant_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_t` to `tenant_networkpolicylocalprefixes`"""

    ntp_templates = templates_ntp
    """ Backwards-compatibility alias of `ntp_templates` to `templates_ntp`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    toolkitsessions_e = element_toolkitsessions
    """ Backwards-compatibility alias of `toolkitsessions_e` to `element_toolkitsessions`"""

