#!/usr/bin/env python
"""
CloudGenix Python SDK - GET

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

    def anynetlinks_correlationevents(self, anynetlink_id, tenant_id=None, api_version="v2.1"):
        """
        GET Anynetlinks_Correlationevents API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/anynetlinks/{}/correlationevents".format(api_version,
                                                                                           tenant_id,
                                                                                           anynetlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs(self, appdef_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get all application definitions

          **Parameters:**:

          - **appdef_id**: (optional) Application Definition ID
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

        if not appdef_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs".format(api_version,
                                                                      tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}".format(api_version,
                                                                         tenant_id,
                                                                         appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs_overrides(self, appdef_id, override_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get application definition overrides for system appdef

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: (optional) AppDef Override ID
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

        if not override_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides".format(api_version,
                                                                                   tenant_id,
                                                                                   appdef_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      appdef_id,
                                                                                      override_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs_version(self, appdefs_version_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get application version for a tenant

          **Parameters:**:

          - **appdefs_version_id**: (optional) Application Definition Version ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

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

    def application_probe(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get application probe configuration of element

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/application_probe".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def auditlog(self, auditlog_id=None, tenant_id=None, api_version="v2.1"):
        """
        GET Auditlog API Function

          **Parameters:**:

          - **auditlog_id**: (optional) Audit Log ID
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

        if not auditlog_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/auditlog".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/auditlog/{}".format(api_version,
                                                                          tenant_id,
                                                                          auditlog_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def authtokens(self, operator_id, authtoken_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get a list of auth tokens

          **Parameters:**:

          - **operator_id**: Operator ID
          - **authtoken_id**: (optional) Static AUTH_TOKEN ID
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

    def bfdpeers(self, site_id, tenant_id=None, api_version="v3.0"):
        """
        GET Bfdpeers API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/bfdpeers".format(api_version,
                                                                            tenant_id,
                                                                            site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgpconfigs(self, site_id, element_id, bgpconfig_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get all BGP configs from NB

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgpconfig_id**: (optional) BGP Configuration ID
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

        if not bgpconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgpconfigs".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgpconfigs/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id,
                                                                                                 bgpconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers(self, site_id, element_id, bgppeer_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get all BGP Peer configs from NB

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: (optional) BGP Peer ID
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

        if not bgppeer_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id,
                                                                                               bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers_advertisedprefixes(self, site_id, element_id, bgppeer_id, tenant_id=None, api_version="v2.0"):
        """
        GET Bgppeers_Advertisedprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}/advertisedprefixes".format(api_version,
                                                                                                              tenant_id,
                                                                                                              site_id,
                                                                                                              element_id,
                                                                                                              bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers_discoveredprefixes(self, site_id, element_id, bgppeer_id, tenant_id=None, api_version="v2.0"):
        """
        GET Bgppeers_Discoveredprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}/discoveredprefixes".format(api_version,
                                                                                                              tenant_id,
                                                                                                              site_id,
                                                                                                              element_id,
                                                                                                              bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers_reachableprefixes(self, site_id, element_id, bgppeer_id, tenant_id=None, api_version="v2.0"):
        """
        GET Bgppeers_Reachableprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}/reachableprefixes".format(api_version,
                                                                                                             tenant_id,
                                                                                                             site_id,
                                                                                                             element_id,
                                                                                                             bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def bgppeers_status(self, site_id, element_id, tenant_id=None, api_version="v2.1"):
        """
        GET Bgppeers_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/status".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def certificates(self, entitie_id, tenant_id=None, api_version="v2.0"):
        """
        GET Certificates API Function

          **Parameters:**:

          - **entitie_id**: Entitie ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/entities/{}/certificates".format(api_version,
                                                                                   tenant_id,
                                                                                   entitie_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def certificates_revoked(self, tenant_id=None, api_version="v2.0"):
        """
        GET Certificates_Revoked API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/certificates/revoked".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def clients_base_roles(self, client_id, tenant_id=None, api_version="v2.0"):
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

    def clients_machines(self, client_id, machine_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all machines of tenant

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: (optional) Machine ID
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

        if not machine_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/machines".format(api_version,
                                                                                  tenant_id,
                                                                                  client_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/machines/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     client_id,
                                                                                     machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def clients_roles(self, client_id, role_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get a list of client custom roles

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **role_id**: (optional) Role ID
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

    def dhcpservers(self, site_id, dhcpserver_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all DHCPServers for a Tenant on a site

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: (optional) DHCP Server ID
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

    def dnsserviceprofiles(self, dnsserviceprofile_id=None, tenant_id=None, api_version="v2.0"):
        """
        Read all DNS service profiles

          **Parameters:**:

          - **dnsserviceprofile_id**: (optional) DNS Service Profile ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not dnsserviceprofile_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    dnsserviceprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsserviceroles(self, dnsservicerole_id=None, tenant_id=None, api_version="v2.0"):
        """
        Read all DNS service roles

          **Parameters:**:

          - **dnsservicerole_id**: (optional) DNS Service Role ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not dnsservicerole_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles".format(api_version,
                                                                              tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 dnsservicerole_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsservices(self, site_id, element_id, dnsservice_id=None, tenant_id=None, api_version="v2.0"):
        """
        Read all DNS service configs

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **dnsservice_id**: (optional) DNS Service ID 
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not dnsservice_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/dnsservices".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/dnsservices/{}".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id,
                                                                                                  element_id,
                                                                                                  dnsservice_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_bgppeers_status(self, site_id, element_id, bgppeer_id, tenant_id=None, api_version="v2.1"):
        """
        GET Element_Bgppeers_Status API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}/status".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id,
                                                                                                  element_id,
                                                                                                  bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_extensions(self, site_id, element_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element level extensions

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
        Get existing machine images

          **Parameters:**:

          - **element_image_id**: (optional) Element Code Image ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

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

    def element_waninterfaces_state(self, site_id, element_id, waninterface_id, tenant_id=None, api_version="v2.1"):
        """
        Get Element WAN interface status

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/waninterfaces/{}/state".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementaccessconfigs(self, element_id, elementaccessconfig_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get all element ElementAccess Config

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **elementaccessconfig_id**: (optional) Element Access Config ID
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

    def elements(self, element_id=None, tenant_id=None, api_version="v2.4"):
        """
        Get all elements of a tenant in a site

          **Parameters:**:

          - **element_id**: (optional) Element (Device) ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.4)

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

    def elements_correlationevents(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        GET Elements_Correlationevents API Function

          **Parameters:**:

          - **site_id**: Site ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/correlationevents".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementsecurityzones(self, site_id, element_id, securityzone_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get element security zones

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
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
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/securityzones".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/securityzones/{}".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    securityzone_id)

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

    def elementusers_password(self, elementuser_id, tenant_id=None, api_version="v2.0"):
        """
        GET Elementusers_Password API Function

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

    def esp_operator_permissions_client(self, operator_id, client_id, tenant_id=None, api_version="v2.1"):
        """
        Get client permissions

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
        return self._parent_class.rest_call(url, "get")

    def eventcodes(self, tenant_id=None, api_version="v2.0"):
        """
        GET Eventcodes API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcodes".format(api_version,
                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, eventcorrelationpolicyrule_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Eventcorrelationpolicyrules API Function

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **eventcorrelationpolicyrule_id**: (optional) Event Correlation Policy Rule ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not eventcorrelationpolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules".format(api_version,
                                                                                                                        tenant_id,
                                                                                                                        eventcorrelationpolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules/{}".format(api_version,
                                                                                                                           tenant_id,
                                                                                                                           eventcorrelationpolicyset_id,
                                                                                                                           eventcorrelationpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def eventcorrelationpolicysets(self, eventcorrelationpolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Eventcorrelationpolicysets API Function

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: (optional) Event Correlation Policy Set ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not eventcorrelationpolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets".format(api_version,
                                                                                         tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def events(self, event_id, tenant_id=None, api_version="v2.2"):
        """
        GET Events API Function

          **Parameters:**:

          - **event_id**: Event ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/events/{}".format(api_version,
                                                                    tenant_id,
                                                                    event_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def externalcaconfigs(self, externalcaconfig_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Externalcaconfigs API Function

          **Parameters:**:

          - **externalcaconfig_id**: (optional) External CA Config ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not externalcaconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/externalcaconfigs".format(api_version,
                                                                                tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/externalcaconfigs/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   externalcaconfig_id)

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
        Get a list of all the hardware bypasses in element

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

    def idps(self, idp_id=None, tenant_id=None, api_version="v3.2"):
        """
        Get all idps

          **Parameters:**:

          - **idp_id**: (optional) SAML IDentity provider configuration ID
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

        if not idp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/idps".format(api_version,
                                                                   tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/idps/{}".format(api_version,
                                                                      tenant_id,
                                                                      idp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces(self, site_id, element_id, interface_id=None, tenant_id=None, api_version="v4.10"):
        """
        Get element interfaces

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: (optional) Interface ID
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

    def interfaces_correlationevents(self, site_id, element_id, interface_id, tenant_id=None, api_version="v2.0"):
        """
        GET Interfaces_Correlationevents API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/correlationevents".format(api_version,
                                                                                                               tenant_id,
                                                                                                               site_id,
                                                                                                               element_id,
                                                                                                               interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces_status(self, site_id, element_id, interface_id, tenant_id=None, api_version="v3.2"):
        """
        Get interface status

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/status".format(api_version,
                                                                                                    tenant_id,
                                                                                                    site_id,
                                                                                                    element_id,
                                                                                                    interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfix(self, site_id, element_id, ipfix_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfix API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **ipfix_id**: (optional) IPFix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/ipfix".format(api_version,
                                                                                         tenant_id,
                                                                                         site_id,
                                                                                         element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/ipfix/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id,
                                                                                            ipfix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixcollectorcontexts(self, ipfixcollectorcontext_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfixcollectorcontexts API Function

          **Parameters:**:

          - **ipfixcollectorcontext_id**: (optional) IPFix Collector Context ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixcollectorcontext_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts".format(api_version,
                                                                                     tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        ipfixcollectorcontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixfiltercontexts(self, ipfixfiltercontext_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfixfiltercontexts API Function

          **Parameters:**:

          - **ipfixfiltercontext_id**: (optional) IPFix Filter Context ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixfiltercontext_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts".format(api_version,
                                                                                  tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     ipfixfiltercontext_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixglobalprefixes(self, ipfixglobalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfixglobalprefixes API Function

          **Parameters:**:

          - **ipfixglobalprefix_id**: (optional) IPFix Global Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes".format(api_version,
                                                                                  tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     ipfixglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixprofiles(self, ipfixprofile_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfixprofiles API Function

          **Parameters:**:

          - **ipfixprofile_id**: (optional) IPFix Profile ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixprofile_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles/{}".format(api_version,
                                                                               tenant_id,
                                                                               ipfixprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipfixtemplates(self, ipfixtemplate_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ipfixtemplates API Function

          **Parameters:**:

          - **ipfixtemplate_id**: (optional) IPFix Template ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixtemplate_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates".format(api_version,
                                                                             tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates/{}".format(api_version,
                                                                                tenant_id,
                                                                                ipfixtemplate_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ipsecprofiles(self, ipsecprofile_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get IPSECProfileList

          **Parameters:**:

          - **ipsecprofile_id**: (optional) IPSEC Profile ID
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

        if not ipsecprofile_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles/{}".format(api_version,
                                                                               tenant_id,
                                                                               ipsecprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def lannetworks(self, site_id, lannetwork_id=None, tenant_id=None, api_version="v3.1"):
        """
        Get LAN networks

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: (optional) LAN Network ID
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

    def localprefixset(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        GET Localprefixset API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/localprefixset".format(api_version,
                                                                                  tenant_id,
                                                                                  site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def login(self, api_version="v2.0"):
        """
        GET Login API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/login".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get", sensitive=True)

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

    def machines(self, machine_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all machines of a tenant

          **Parameters:**:

          - **machine_id**: (optional) Machine ID
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

        if not machine_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}".format(api_version,
                                                                          tenant_id,
                                                                          machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machines_software_status(self, machine_id, software_id, status_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Machine Software Statuses

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: Software ID
          - **status_id**: (optional) Software Status ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not status_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/software/{}/status".format(api_version,
                                                                                             tenant_id,
                                                                                             machine_id,
                                                                                             software_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/software/{}/status/{}".format(api_version,
                                                                                                tenant_id,
                                                                                                machine_id,
                                                                                                software_id,
                                                                                                status_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aggregates(self, tenant_id=None, api_version="v3.0"):
        """
        GET Monitor_Aggregates API Function

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

    def monitor_bulk_metrics(self, bulk_metric_id, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Bulk_Metrics API Function

          **Parameters:**:

          - **bulk_metric_id**: Bulk Metric ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

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

    def monitor_metrics(self, metric_id, tenant_id=None, api_version="v2.2"):
        """
        GET Monitor_Metrics API Function

          **Parameters:**:

          - **metric_id**: Metric ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/metrics/{}".format(api_version,
                                                                             tenant_id,
                                                                             metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_object_stats(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Object_Stats API Function

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

    def monitor_sys_metrics(self, tenant_id=None, api_version="v2.1"):
        """
        GET Monitor_Sys_Metrics API Function

          **Parameters:**:

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/sys_metrics".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natglobalprefixes(self, natglobalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Global NAT prefixes.

          **Parameters:**:

          - **natglobalprefix_id**: (optional) NAT Global Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes".format(api_version,
                                                                                tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   natglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natlocalprefixes(self, natlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get NAT local prefixes.

          **Parameters:**:

          - **natlocalprefix_id**: (optional) NAT Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natlocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes".format(api_version,
                                                                               tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicypools(self, natpolicypool_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get NAT Policy Pools.

          **Parameters:**:

          - **natpolicypool_id**: (optional) NAT Policy Pool ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natpolicypool_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools".format(api_version,
                                                                             tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools/{}".format(api_version,
                                                                                tenant_id,
                                                                                natpolicypool_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicyrules(self, natpolicyset_id, natpolicyrule_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get policy rules of policy set

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **natpolicyrule_id**: (optional) NAT Policy Rule ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natpolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/natpolicyrules".format(api_version,
                                                                                              tenant_id,
                                                                                              natpolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/natpolicyrules/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 natpolicyset_id,
                                                                                                 natpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicysets(self, natpolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all NAT policy sets of tenant.

          **Parameters:**:

          - **natpolicyset_id**: (optional) NAT Policy Set ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natpolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}".format(api_version,
                                                                               tenant_id,
                                                                               natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicysets_status(self, natpolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Get a specific NAT policy set status of tenant.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/status".format(api_version,
                                                                                  tenant_id,
                                                                                  natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natpolicysetstacks(self, natpolicysetstack_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all NAT policy Set stacks of tenant.

          **Parameters:**:

          - **natpolicysetstack_id**: (optional) NAT Policy Set Stack ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natpolicysetstack_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    natpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natzones(self, natzone_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Nat Policy Zones.

          **Parameters:**:

          - **natzone_id**: (optional) NAT Zone ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natzone_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones/{}".format(api_version,
                                                                          tenant_id,
                                                                          natzone_id)

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

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Network policy global prefixes.

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: (optional) Network Policy Global Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not networkpolicyglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes".format(api_version,
                                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get network policy rules of tenant

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: (optional) Network Policy Rule ID
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

        if not networkpolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules".format(api_version,
                                                                                                      tenant_id,
                                                                                                      networkpolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules/{}".format(api_version,
                                                                                                         tenant_id,
                                                                                                         networkpolicyset_id,
                                                                                                         networkpolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicysets(self, networkpolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all network policy sets of tenant.

          **Parameters:**:

          - **networkpolicyset_id**: (optional) Network Policy Set ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not networkpolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets".format(api_version,
                                                                                tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicysets_status(self, networkpolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Get a specific network policy set status of tenant.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/status".format(api_version,
                                                                                      tenant_id,
                                                                                      networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicysetstacks(self, networkpolicysetstack_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all network policy set stacks of tenant.

          **Parameters:**:

          - **networkpolicysetstack_id**: (optional) Network Policy Set Stack ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not networkpolicysetstack_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks".format(api_version,
                                                                                     tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        networkpolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ntp(self, element_id, ntp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element NTP

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **ntp_id**: (optional) NTP Configuration ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ntp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/ntp".format(api_version,
                                                                              tenant_id,
                                                                              element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/ntp/{}".format(api_version,
                                                                                 tenant_id,
                                                                                 element_id,
                                                                                 ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ntp_status(self, element_id, ntp_id, tenant_id=None, api_version="v2.0"):
        """
        GET Ntp_Status API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/ntp/{}/status".format(api_version,
                                                                                    tenant_id,
                                                                                    element_id,
                                                                                    ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def operator_sessions(self, operator_id, session_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all sessions for operator id belonging to a tenant id

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: (optional) User Session ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

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
        Get all otp access configs.

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

    def pathgroups(self, pathgroup_id=None, tenant_id=None, api_version="v2.1"):
        """
        get all Path Groups for a tenant.

          **Parameters:**:

          - **pathgroup_id**: (optional) Path Group ID (for network service/DC routing)
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

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Priority policy prefixes.

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: (optional) Priority Policy Global Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicyglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes".format(api_version,
                                                                                           tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get priority policy rules of tenant

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: (optional) Priority Policy Rule ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/prioritypolicyrules".format(api_version,
                                                                                                        tenant_id,
                                                                                                        prioritypolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/prioritypolicyrules/{}".format(api_version,
                                                                                                           tenant_id,
                                                                                                           prioritypolicyset_id,
                                                                                                           prioritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicysets(self, prioritypolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all priority policy sets of tenant.

          **Parameters:**:

          - **prioritypolicyset_id**: (optional) Priority Policy Set ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicysets_status(self, prioritypolicyset_id, tenant_id=None, api_version="v2.0"):
        """
        Get a specific priority policy set status of tenant.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/status".format(api_version,
                                                                                       tenant_id,
                                                                                       prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicysetstacks(self, prioritypolicysetstack_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Priority policy set stacks of tenant.

          **Parameters:**:

          - **prioritypolicysetstack_id**: (optional) Priority Policy Stack ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicysetstack_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks".format(api_version,
                                                                                      tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks/{}".format(api_version,
                                                                                         tenant_id,
                                                                                         prioritypolicysetstack_id)

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

    def reports(self, tenant_id=None, api_version="v2.0"):
        """
        GET Reports API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/reports".format(api_version,
                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def reportsdir(self, tenant_id=None, api_version="v2.0"):
        """
        GET Reportsdir API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/reportsdir".format(api_version,
                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def roles(self, role_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get a list of custom roles

          **Parameters:**:

          - **role_id**: (optional) Role ID
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

        if not role_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/roles".format(api_version,
                                                                    tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/roles/{}".format(api_version,
                                                                       tenant_id,
                                                                       role_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_aspathaccesslists(self, site_id, element_id, routing_aspathaccesslist_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Access List for Element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_aspathaccesslist_id**: (optional) Routing AS-PATH Access List ID
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

        if not routing_aspathaccesslist_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists".format(api_version,
                                                                                                             tenant_id,
                                                                                                             site_id,
                                                                                                             element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists/{}".format(api_version,
                                                                                                                tenant_id,
                                                                                                                site_id,
                                                                                                                element_id,
                                                                                                                routing_aspathaccesslist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_ipcommunitylists(self, site_id, element_id, routing_ipcommunitylist_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Community List for Element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_ipcommunitylist_id**: (optional) Routing IP Community List ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not routing_ipcommunitylist_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists".format(api_version,
                                                                                                            tenant_id,
                                                                                                            site_id,
                                                                                                            element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists/{}".format(api_version,
                                                                                                               tenant_id,
                                                                                                               site_id,
                                                                                                               element_id,
                                                                                                               routing_ipcommunitylist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_prefixlists(self, site_id, element_id, routing_prefixlist_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Prefix List for Element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_prefixlist_id**: (optional) Routing IP Prefix List ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not routing_prefixlist_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id,
                                                                                                       element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists/{}".format(api_version,
                                                                                                          tenant_id,
                                                                                                          site_id,
                                                                                                          element_id,
                                                                                                          routing_prefixlist_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def routing_routemaps(self, site_id, element_id, routing_routemap_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Route Map for Element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **routing_routemap_id**: (optional) Routing Route Map ID
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

        if not routing_routemap_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps".format(api_version,
                                                                                                     tenant_id,
                                                                                                     site_id,
                                                                                                     element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps/{}".format(api_version,
                                                                                                        tenant_id,
                                                                                                        site_id,
                                                                                                        element_id,
                                                                                                        routing_routemap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps(self, sdwanapp_id=None, tenant_id=None, api_version="v2.2"):
        """
        GET Sdwanapps API Function

          **Parameters:**:

          - **sdwanapp_id**: (optional) SDWAN Application ID
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

        if not sdwanapp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps".format(api_version,
                                                                        tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}".format(api_version,
                                                                           tenant_id,
                                                                           sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_appstatus(self, sdwanapp_id, appstatus_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Appstatus API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **appstatus_id**: SDWAN App Status ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/appstatus/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    sdwanapp_id,
                                                                                    appstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_appstatus_connectivity(self, sdwanapp_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Appstatus_Connectivity API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/appstatus/connectivity".format(api_version,
                                                                                              tenant_id,
                                                                                              sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_appstatus_icon(self, sdwanapp_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Appstatus_Icon API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/appstatus/icon".format(api_version,
                                                                                      tenant_id,
                                                                                      sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_appstatus_metadata(self, sdwanapp_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Appstatus_Metadata API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/appstatus/metadata".format(api_version,
                                                                                          tenant_id,
                                                                                          sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_configs(self, sdwanapp_id, config_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **config_id**: (optional) SDWAN App Config ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not config_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/configs".format(api_version,
                                                                                   tenant_id,
                                                                                   sdwanapp_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/configs/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      sdwanapp_id,
                                                                                      config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def sdwanapps_status(self, sdwanapp_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sdwanapps_Status API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/status".format(api_version,
                                                                              tenant_id,
                                                                              sdwanapp_id)

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

    def servicebindingmaps(self, servicebindingmap_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get getServiceBindingMapList

          **Parameters:**:

          - **servicebindingmap_id**: (optional) Service Binding Map ID
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

        if not servicebindingmap_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    servicebindingmap_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def serviceendpoints(self, serviceendpoint_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get ServiceEndpointList

          **Parameters:**:

          - **serviceendpoint_id**: (optional) Service Endpoint ID
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

    def site_anynetlinks(self, site_id, anynetlink_id, tenant_id=None, api_version="v2.0"):
        """
        GET Site_Anynetlinks API Function

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

    def site_extensions(self, site_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all site level extensions

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

    def site_natlocalprefixes(self, site_id, natlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site NAT prefixes

          **Parameters:**:

          - **site_id**: Site ID
          - **natlocalprefix_id**: (optional) NAT Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not natlocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/natlocalprefixes".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/natlocalprefixes/{}".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           natlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site Network policy prefix associations

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: (optional) Network Policy Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not networkpolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/networkpolicylocalprefixes".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     site_id,
                                                                                                     networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site Priority policy prefix associations

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: (optional) Priority Policy Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                                   tenant_id,
                                                                                                   site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      prioritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_status(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        Get site status

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
        Get site ciphers

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

    def sites(self, site_id=None, tenant_id=None, api_version="v4.5"):
        """
        Get Sites of a tenant

          **Parameters:**:

          - **site_id**: (optional) Site ID
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

        if not site_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites".format(api_version,
                                                                    tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}".format(api_version,
                                                                       tenant_id,
                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_correlationevents(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        GET Site_correlationevents API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/correlationevents".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Site_ipfixlocalprefixes API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **ipfixlocalprefix_id**: (optional) IPFix Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixlocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ipfixlocalprefixes".format(api_version,
                                                                                          tenant_id,
                                                                                          site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             ipfixlocalprefix_id)

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

    def software(self, machine_id, software_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Machine Software

          **Parameters:**:

          - **machine_id**: Machine ID
          - **software_id**: (optional) Software ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not software_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/software".format(api_version,
                                                                                   tenant_id,
                                                                                   machine_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/software/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      machine_id,
                                                                                      software_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def software_state(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get the software upgrade configuration of an element

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/software/state".format(api_version,
                                                                                     tenant_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def software_status(self, element_id, tenant_id=None, api_version="v2.1"):
        """
        Get all software upgrade status (up to 5) started by the tenant user

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/software/status".format(api_version,
                                                                                      tenant_id,
                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def spokeclusters(self, site_id, spokecluster_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all spokeclusters

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: (optional) Spoke Cluster ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not spokecluster_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def spokeclusters_status(self, site_id, spokecluster_id, tenant_id=None, api_version="v2.0"):
        """
        Get Spoke Cluster Status.

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters/{}/status".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def state(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get element state

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

    def staticroutes(self, site_id, element_id, staticroute_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get static routes

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: (optional) Static Route ID
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

    def staticroutes_status(self, site_id, element_id, staticroute_id, tenant_id=None, api_version="v2.1"):
        """
        GET Staticroutes Status API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}/status".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def syslogservers(self, site_id, element_id, syslogserver_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get Syslog Servers on an element

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: (optional) SYSLOG server ID
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

    def templates_ntp(self, ntp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all existing NTP Template of tenant.

          **Parameters:**:

          - **ntp_id**: (optional) NTP Configuration ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ntp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/templates/ntp".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/templates/ntp/{}".format(api_version,
                                                                               tenant_id,
                                                                               ntp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_anynetlinks(self, anynetlink_id, tenant_id=None, api_version="v3.2"):
        """
        GET Tenant_Anynetlinks API Function

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

    def tenant_extensions(self, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all extensions from NB

          **Parameters:**:

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
            url = str(cur_ctlr) + "/{}/api/tenants/{}/extensions".format(api_version,
                                                                         tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/extensions/{}".format(api_version,
                                                                            tenant_id,
                                                                            extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Tenant_Ipfixlocalprefixes API Function

          **Parameters:**:

          - **ipfixlocalprefix_id**: (optional) IPFix Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ipfixlocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    ipfixlocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_networkpolicylocalprefixes(self, networkpolicylocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Network Policy local prefixes.

          **Parameters:**:

          - **networkpolicylocalprefix_id**: (optional) Network Policy Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not networkpolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes".format(api_version,
                                                                                         tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes/{}".format(api_version,
                                                                                            tenant_id,
                                                                                            networkpolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_operators(self, operator_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get a list of tenant operators

          **Parameters:**:

          - **operator_id**: (optional) Operator ID
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

    def tenant_prioritypolicylocalprefixes(self, prioritypolicylocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Priority Policy local prefixes.

          **Parameters:**:

          - **prioritypolicylocalprefix_id**: (optional) Priority Policy Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prioritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             prioritypolicylocalprefix_id)

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
        Get tenant details for tenant id

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

    def toolkitsessions(self, tenant_id=None, api_version="v2.0"):
        """
        GET Toolkitsessions API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/toolkitsessions".format(api_version,
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
        Get status for Vff License

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
        Get all Tenant Vff License Tokens

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
        Get all Vff Licenses for Tenant

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

    def vpnlinks_state(self, vpnlink_id, tenant_id=None, api_version="v2.0"):
        """
        Get the VPNLink admin state

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

    def vpnlinks_status(self, vpnlink_id, tenant_id=None, api_version="v2.1"):
        """
        Get the VPNLink status

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/{}/status".format(api_version,
                                                                             tenant_id,
                                                                             vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfacelabels(self, waninterfacelabel_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get WAN interface labels for a tenant

          **Parameters:**:

          - **waninterfacelabel_id**: (optional) WAN Interface Label ID
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

        if not waninterfacelabel_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfaces(self, site_id, waninterface_id=None, tenant_id=None, api_version="v2.6"):
        """
        Get all Site WAN interfaces

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: (optional) WAN Interface ID
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
        Get a specific Site WAN interface status

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

    def wannetworks(self, wannetwork_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all tenant WAN networks

          **Parameters:**:

          - **wannetwork_id**: (optional) WAN Network ID
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

    def wantinterfaces_correlationevents(self, site_id, waninterface_id, tenant_id=None, api_version="v2.0"):
        """
        GET Wantinterfaces_Correlationevents API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: WAN Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/waninterfaces/{}/correlationevents".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      waninterface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ws_extensions(self, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Ws_Extensions API Function

          **Parameters:**:

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
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions".format(api_version,
                                                                            tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions/{}".format(api_version,
                                                                               tenant_id,
                                                                               extension_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    advertisedprefixes_bgppeers = bgppeers_advertisedprefixes
    """ Backwards-compatibility alias of `advertisedprefixes_bgppeers` to `bgppeers_advertisedprefixes`"""

    aggregates_monitor = monitor_aggregates
    """ Backwards-compatibility alias of `aggregates_monitor` to `monitor_aggregates`"""

    anynetlinks_s = site_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_s` to `site_anynetlinks`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    api_versions_t = tenant_api_versions
    """ Backwards-compatibility alias of `api_versions_t` to `tenant_api_versions`"""

    appstatus_sdwanapps = sdwanapps_appstatus
    """ Backwards-compatibility alias of `appstatus_sdwanapps` to `sdwanapps_appstatus`"""

    base_roles_clients = clients_base_roles
    """ Backwards-compatibility alias of `base_roles_clients` to `clients_base_roles`"""

    bulk_metrics_monitor = monitor_bulk_metrics
    """ Backwards-compatibility alias of `bulk_metrics_monitor` to `monitor_bulk_metrics`"""

    clients_t = tenant_clients
    """ Backwards-compatibility alias of `clients_t` to `tenant_clients`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    connectivity_appstatus_sdwanapps = sdwanapps_appstatus_connectivity
    """ Backwards-compatibility alias of `connectivity_appstatus_sdwanapps` to `sdwanapps_appstatus_connectivity`"""

    correlationevents_anynetlinks = anynetlinks_correlationevents
    """ Backwards-compatibility alias of `correlationevents_anynetlinks` to `anynetlinks_correlationevents`"""

    correlationevents_e = elements_correlationevents
    """ Backwards-compatibility alias of `correlationevents_e` to `elements_correlationevents`"""

    correlationevents_interfaces = interfaces_correlationevents
    """ Backwards-compatibility alias of `correlationevents_interfaces` to `interfaces_correlationevents`"""

    correlationevents_s = site_correlationevents
    """ Backwards-compatibility alias of `correlationevents_s` to `site_correlationevents`"""

    correlationevents_waninterfaces = wantinterfaces_correlationevents
    """ Backwards-compatibility alias of `correlationevents_waninterfaces` to `wantinterfaces_correlationevents`"""

    discoveredprefixes_bgppeers = bgppeers_discoveredprefixes
    """ Backwards-compatibility alias of `discoveredprefixes_bgppeers` to `bgppeers_discoveredprefixes`"""

    elementpassageconfigs_e = elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_e` to `elementpassageconfigs`"""

    elementpassageconfigs_t = tenant_elementpassageconfigs
    """ Backwards-compatibility alias of `elementpassageconfigs_t` to `tenant_elementpassageconfigs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_t = tenant_extensions
    """ Backwards-compatibility alias of `extensions_t` to `tenant_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    icon_appstatus_sdwanapps = sdwanapps_appstatus_icon
    """ Backwards-compatibility alias of `icon_appstatus_sdwanapps` to `sdwanapps_appstatus_icon`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    machines_c = clients_machines
    """ Backwards-compatibility alias of `machines_c` to `clients_machines`"""

    metadata_appstatus_sdwanapps = sdwanapps_appstatus_metadata
    """ Backwards-compatibility alias of `metadata_appstatus_sdwanapps` to `sdwanapps_appstatus_metadata`"""

    metrics_monitor = monitor_metrics
    """ Backwards-compatibility alias of `metrics_monitor` to `monitor_metrics`"""

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

    object_stats_monitor = monitor_object_stats
    """ Backwards-compatibility alias of `object_stats_monitor` to `monitor_object_stats`"""

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    passages_e = element_passages
    """ Backwards-compatibility alias of `passages_e` to `element_passages`"""

    passages_t = tenant_passages
    """ Backwards-compatibility alias of `passages_t` to `tenant_passages`"""

    password_elementusers = elementusers_password
    """ Backwards-compatibility alias of `password_elementusers` to `elementusers_password`"""

    permissions_clients_d = esp_operator_permissions
    """ Backwards-compatibility alias of `permissions_clients_d` to `esp_operator_permissions`"""

    permissions_clients_o = esp_operator_permissions_client
    """ Backwards-compatibility alias of `permissions_clients_o` to `esp_operator_permissions_client`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    reachableprefixes_bgppeers = bgppeers_reachableprefixes
    """ Backwards-compatibility alias of `reachableprefixes_bgppeers` to `bgppeers_reachableprefixes`"""

    revoked_certificates = certificates_revoked
    """ Backwards-compatibility alias of `revoked_certificates` to `certificates_revoked`"""

    roles_clients = clients_roles
    """ Backwards-compatibility alias of `roles_clients` to `clients_roles`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    state_software = software_state
    """ Backwards-compatibility alias of `state_software` to `software_state`"""

    state_vpnlinks = vpnlinks_state
    """ Backwards-compatibility alias of `state_vpnlinks` to `vpnlinks_state`"""

    state_waninterfaces_e = element_waninterfaces_state
    """ Backwards-compatibility alias of `state_waninterfaces_e` to `element_waninterfaces_state`"""

    status_bgppeers = bgppeers_status
    """ Backwards-compatibility alias of `status_bgppeers` to `bgppeers_status`"""

    status_bgppeers_i = element_bgppeers_status
    """ Backwards-compatibility alias of `status_bgppeers_i` to `element_bgppeers_status`"""

    status_hubclustermembers = hubclustermember_status
    """ Backwards-compatibility alias of `status_hubclustermembers` to `hubclustermember_status`"""

    status_i = hubcluster_status
    """ Backwards-compatibility alias of `status_i` to `hubcluster_status`"""

    status_interfaces = interfaces_status
    """ Backwards-compatibility alias of `status_interfaces` to `interfaces_status`"""

    status_natpolicysets = natpolicysets_status
    """ Backwards-compatibility alias of `status_natpolicysets` to `natpolicysets_status`"""

    status_networkpolicysets = networkpolicysets_status
    """ Backwards-compatibility alias of `status_networkpolicysets` to `networkpolicysets_status`"""

    status_ntp = ntp_status
    """ Backwards-compatibility alias of `status_ntp` to `ntp_status`"""

    status_policysets = policysets_status
    """ Backwards-compatibility alias of `status_policysets` to `policysets_status`"""

    status_prioritypolicysets = prioritypolicysets_status
    """ Backwards-compatibility alias of `status_prioritypolicysets` to `prioritypolicysets_status`"""

    status_s = site_status
    """ Backwards-compatibility alias of `status_s` to `site_status`"""

    status_sdwanapps = sdwanapps_status
    """ Backwards-compatibility alias of `status_sdwanapps` to `sdwanapps_status`"""

    status_software_e = software_status
    """ Backwards-compatibility alias of `status_software_e` to `software_status`"""

    status_software_m = machines_software_status
    """ Backwards-compatibility alias of `status_software_m` to `machines_software_status`"""

    status_spokeclusters = spokeclusters_status
    """ Backwards-compatibility alias of `status_spokeclusters` to `spokeclusters_status`"""

    status_vfflicenses = vfflicense_status
    """ Backwards-compatibility alias of `status_vfflicenses` to `vfflicense_status`"""

    status_vpnlinks = vpnlinks_status
    """ Backwards-compatibility alias of `status_vpnlinks` to `vpnlinks_status`"""

    status_waninterfaces = waninterfaces_status
    """ Backwards-compatibility alias of `status_waninterfaces` to `waninterfaces_status`"""

    sys_metrics_monitor = monitor_sys_metrics
    """ Backwards-compatibility alias of `sys_metrics_monitor` to `monitor_sys_metrics`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

    toolkitsessions_t = toolkitsessions
    """ Backwards-compatibility alias of `toolkitsessions_t` to `toolkitsessions`"""

