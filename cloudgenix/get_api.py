#!/usr/bin/env python
"""
CloudGenix Python SDK - GET

**Author:** CloudGenix

**Copyright:** (c) 2017-2023 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2023 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017-2023 CloudGenix, Inc

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

    def apnprofiles(self, apnprofile_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all APN Profiles (v2.0)

          **Parameters:**:

          - **apnprofile_id**: (optional) APN Profile ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not apnprofile_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/apnprofiles".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/apnprofiles/{}".format(api_version,
                                                                             tenant_id,
                                                                             apnprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def appdefs(self, appdef_id=None, tenant_id=None, api_version="v2.5"):
        """
        Get all application definitions (v2.5)

          **Parameters:**:

          - **appdef_id**: (optional) Application Definition ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

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

    def appdefs_overrides(self, appdef_id, override_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get application definition overrides for system appdef (v2.3)

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **override_id**: (optional) AppDef Override ID
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
        Get application version for a tenant (v2.0)

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
        Get application probe configuration of element (v2.0)

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
        Get a list of auth tokens (v2.1)

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
        Get a list of tenant base permissions (v2.0)

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
        Get a list of tenant base roles (v2.0)

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
        Get all BGP configs from NB (v2.2)

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
        Get all BGP Peer configs from NB (v2.2)

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

    def cellular_module_images(self, cellular_module_image_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get existing element cellular module images (v2.1)

          **Parameters:**:

          - **cellular_module_image_id**: (optional) Cellular Module Image ID
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

        if not cellular_module_image_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/cellular_module_images".format(api_version,
                                                                                     tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/cellular_module_images/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        cellular_module_image_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def cellular_modules_sim_security(self, element_id, cellular_module_id, sim_security_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all cellular modules sim security info (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **sim_security_id**: (optional) SIM Security ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not sim_security_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}/sim_security".format(api_version,
                                                                                                           tenant_id,
                                                                                                           element_id,
                                                                                                           cellular_module_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}/sim_security/{}".format(api_version,
                                                                                                              tenant_id,
                                                                                                              element_id,
                                                                                                              cellular_module_id,
                                                                                                              sim_security_id)

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
        GET Revoked_Certificates API Function

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
        Get a list of client base roles (v2.0)

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

    def clients_machines(self, client_id, machine_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get all machines allocated by ESP to a client tenant (v2.3)

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: (optional) Machine ID
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
        Get a list of client custom roles (v2.1)

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

    def demstatus(self, site_id, demstatus_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all ADEM status for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **demstatus_id**: (optional) DEM Status ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not demstatus_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/demstatus".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/demstatus/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id,
                                                                                    demstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def deviceidconfigs(self, site_id, deviceidconfig_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Deviceidconfigs API Function

          **Parameters:**:

          - **site_id**: Site ID
          - **deviceidconfig_id**: (optional) Device Id Config ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not deviceidconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/deviceidconfigs".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/deviceidconfigs/{}".format(api_version,
                                                                                          tenant_id,
                                                                                          site_id,
                                                                                          deviceidconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dhcpservers(self, site_id, dhcpserver_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get all DHCPServers for a Tenant on a site (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **dhcpserver_id**: (optional) DHCP Server ID
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

    def directoryservices(self, tenant_id=None, api_version="v2.0"):
        """
        GET Directoryservices API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryservices".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryservices_domainstatus(self, directoryservice_id, domainstatus_id, tenant_id=None, api_version="v2.0"):
        """
        GET Directoryservices_Domainstatus API Function

          **Parameters:**:

          - **directoryservice_id**: Directory Service ID
          - **domainstatus_id**: Domain Status ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryservices/{}/domainstatus/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               directoryservice_id,
                                                                                               domainstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryservices_status(self, tenant_id=None, api_version="v2.0"):
        """
        GET Directoryservices_Status API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryservices/status".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryusergroups(self, directoryusergroup_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Directoryusergroups API Function

          **Parameters:**:

          - **directoryusergroup_id**: (optional) Directory User Group ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not directoryusergroup_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryusergroups".format(api_version,
                                                                                  tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryusergroups/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     directoryusergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def directoryusers(self, directoryuser_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Directoryusers API Function

          **Parameters:**:

          - **directoryuser_id**: (optional) Directory User ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not directoryuser_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryusers".format(api_version,
                                                                             tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/directoryusers/{}".format(api_version,
                                                                                tenant_id,
                                                                                directoryuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def dnsserviceprofiles(self, dnsserviceprofile_id=None, tenant_id=None, api_version="v2.1"):
        """
        Read all DNS service profiles (v2.1)

          **Parameters:**:

          - **dnsserviceprofile_id**: (optional) DNS Service Profile ID
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
        Read all DNS service roles (v2.0)

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
        Read all DNS service configs (v2.0)

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

    def element_cellular_modules(self, element_id, cellular_module_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all cellular modules (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: (optional) Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not cellular_module_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules".format(api_version,
                                                                                           tenant_id,
                                                                                           element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              element_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_cellular_modules_firmware(self, element_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                                   tenant_id,
                                                                                                   element_id,
                                                                                                   cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_cellular_modules_firmware_status(self, element_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module firmware configuration status (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}/firmware/status".format(api_version,
                                                                                                          tenant_id,
                                                                                                          element_id,
                                                                                                          cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_cellular_modules_status(self, element_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module status (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/cellular_modules/{}/status".format(api_version,
                                                                                                 tenant_id,
                                                                                                 element_id,
                                                                                                 cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_correlationevents(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        GET Element_Correlationevents API Function

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

    def element_extensions(self, site_id, element_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element level extensions (v2.0)

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

    def element_images(self, element_image_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get existing machine images (v2.2)

          **Parameters:**:

          - **element_image_id**: (optional) Element Code Image ID
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

    def element_state(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get element state (v2.0)

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

    def element_status(self, element_id, tenant_id=None, api_version="v2.2"):
        """
        Get specific element status for a tenant (v2.2)

          **Parameters:**:

          - **element_id**: Element (Device) ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/status".format(api_version,
                                                                             tenant_id,
                                                                             element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def element_waninterfaces_state(self, site_id, element_id, waninterface_id, tenant_id=None, api_version="v2.1"):
        """
        Get Element WAN interface status (v2.1)

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
        Get all Element Access Configs (v2.2)

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
        Get specific element's Access State (v2.0)

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

    def elements(self, element_id=None, tenant_id=None, api_version="v3.0"):
        """
        Get Elements of a tenant (v3.0)

          **Parameters:**:

          - **element_id**: (optional) Element (Device) ID
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

        if not element_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements".format(api_version,
                                                                       tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}".format(api_version,
                                                                          tenant_id,
                                                                          element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementsecurityzones(self, site_id, element_id, securityzone_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get element security zones (v2.0)

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

    def elementusers(self, elementuser_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all element User (v2.1)

          **Parameters:**:

          - **elementuser_id**: (optional) Element User ID
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

        if not elementuser_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers".format(api_version,
                                                                           tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}".format(api_version,
                                                                              tenant_id,
                                                                              elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def elementusers_access(self, elementuser_id, access_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all accesses for a particular user (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **access_id**: (optional) Access ID
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

    def elementusers_password(self, elementuser_id, tenant_id=None, api_version="v2.1"):
        """
        Get element user password (v2.1)

          **Parameters:**:

          - **elementuser_id**: Element User ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementusers/{}/password".format(api_version,
                                                                                   tenant_id,
                                                                                   elementuser_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def enterpriseprefixset(self, tenant_id=None, api_version="v2.1"):
        """
        GET Enterpriseprefixset API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/enterpriseprefixset".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def esp(self, tenant_id=None, api_version="v2.0"):
        """
        Get esp tenant details for tenant id (v2.0)

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
        Get esp operator permissions assigned under all clients (v2.0)

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
        Get esp operator permissions assigned under a client (v2.1)

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
        Get all event correlation policyrules (v2.0)

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
        Get all event correlation policysets (v2.0)

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

    def events(self, event_id, tenant_id=None, api_version="v2.3"):
        """
        GET Events API Function

          **Parameters:**:

          - **event_id**: Event ID
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
        Get global prefix filters. (v2.0)

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
        Get a list of all the hardware bypasses in element (v2.0)

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

    def hubclustermember_status(self, site_id, hubcluster_id, hubclustermember_id, tenant_id=None, api_version="v3.0"):
        """
        Get specific hub cluster member state. (v3.0)

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
        Get all hub cluster members (v3.0)

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

    def hubclusters(self, site_id, hubcluster_id=None, tenant_id=None, api_version="v4.0"):
        """
        Get all hub clusters (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: (optional) Hub (DC) Cluster ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.0)

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

    def hubclusters_status(self, site_id, hubcluster_id, tenant_id=None, api_version="v4.0"):
        """
        Get hub cluster status (v4.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **hubcluster_id**: Hub (DC) Cluster ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.0)

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

    def idps(self, idp_id=None, tenant_id=None, api_version="v3.3"):
        """
        Get all idps (v3.3)

          **Parameters:**:

          - **idp_id**: (optional) SAML IDentity provider configuration ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.3)

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

    def interface_authentication_status(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get all interface authentication status for an element (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/interface_authentication/status".format(api_version,
                                                                                                      tenant_id,
                                                                                                      element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interface_multicastigmpmemberships(self, site_id, element_id, interface_id, multicastigmpmembership_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast IGMP group membership info (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **multicastigmpmembership_id**: (optional) Multicast IGMP Membership ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastigmpmembership_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/multicastigmpmemberships".format(api_version,
                                                                                                                          tenant_id,
                                                                                                                          site_id,
                                                                                                                          element_id,
                                                                                                                          interface_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/multicastigmpmemberships/{}".format(api_version,
                                                                                                                             tenant_id,
                                                                                                                             site_id,
                                                                                                                             element_id,
                                                                                                                             interface_id,
                                                                                                                             multicastigmpmembership_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces(self, site_id, element_id, interface_id=None, tenant_id=None, api_version="v4.15"):
        """
        Get all Cellular Interfaces (v4.15)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: (optional) Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.15)

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

    def interfaces_multicaststatus(self, site_id, element_id, interface_id, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast status info (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/interfaces/{}/multicaststatus".format(api_version,
                                                                                                             tenant_id,
                                                                                                             site_id,
                                                                                                             element_id,
                                                                                                             interface_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def interfaces_status(self, site_id, element_id, interface_id, tenant_id=None, api_version="v3.5"):
        """
        Get interface status (v3.5)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **interface_id**: Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.5)

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
        Get all IPFix config (v2.0)

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
        Get all IPFix collector context (v2.0)

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
        Get all IPFix filter context (v2.0)

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
        Get all IPFix global prefix (v2.0)

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
        Get all IPFix Profiles (v2.0)

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
        Get all IPFix templates (v2.0)

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
        Get IPSECProfileList (v2.1)

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

    def lannetworks(self, site_id, lannetwork_id=None, tenant_id=None, api_version="v3.2"):
        """
        Get LAN networks (v3.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **lannetwork_id**: (optional) LAN Network ID
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

    def lldp_neighbors_status(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get all lldp neighbors status for an element (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/lldp_neighbors/status".format(api_version,
                                                                                            tenant_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def localprefixfilters(self, localprefixfilter_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get local prefix filters. (v2.0)

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

    def mac_addresses_status(self, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get mac addresses status for a tenant (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/mac_addresses/status".format(api_version,
                                                                                           tenant_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_cellular_modules(self, machine_id, cellular_module_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all cellular modules (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: (optional) Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not cellular_module_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/cellular_modules".format(api_version,
                                                                                           tenant_id,
                                                                                           machine_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/cellular_modules/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              machine_id,
                                                                                              cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_cellular_modules_firmware(self, machine_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module firmware configuration (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/cellular_modules/{}/firmware".format(api_version,
                                                                                                   tenant_id,
                                                                                                   machine_id,
                                                                                                   cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_cellular_modules_firmware_status(self, machine_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module firmware configuration status (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/cellular_modules/{}/firmware/status".format(api_version,
                                                                                                          tenant_id,
                                                                                                          machine_id,
                                                                                                          cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machine_cellular_modules_status(self, machine_id, cellular_module_id, tenant_id=None, api_version="v2.0"):
        """
        Get cellular module status (v2.0)

          **Parameters:**:

          - **machine_id**: Machine ID
          - **cellular_module_id**: Cellular Module ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/cellular_modules/{}/status".format(api_version,
                                                                                                 tenant_id,
                                                                                                 machine_id,
                                                                                                 cellular_module_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def machines(self, machine_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get all machines of a tenant (v2.3)

          **Parameters:**:

          - **machine_id**: (optional) Machine ID
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
        Get all Machine Software Statuses (v2.0)

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

    def machinesystemstatus(self, machine_id, tenant_id=None, api_version="v2.1"):
        """
        Get Machine system status for a tenant (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/machinesystemstatus".format(api_version,
                                                                                          tenant_id,
                                                                                          machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aaa_metrics(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Aaa_Metrics API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aaa_metrics".format(api_version,
                                                                              tenant_id)

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aiops_aggregates(self, tenant_id=None, api_version="v2.1"):
        """
        GET Monitor_Aiops_Aggregates API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aiops/aggregates".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aiops_anomaly(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Aiops_Anomaly API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aiops/anomaly".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aiops_forecast(self, tenant_id=None, api_version="v2.1"):
        """
        GET Monitor_Aiops_Forecast API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aiops/forecast".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aiops_health(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Aiops_Health API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aiops/health".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_aiops_object_stats(self, tenant_id=None, api_version="v2.1"):
        """
        GET Monitor_Aiops_Object_Stats API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aiops/object_stats".format(api_version,
                                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_application_qos_metrics(self, qos_metric_id, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Application_Qos_Metrics API Function

          **Parameters:**:

          - **qos_metric_id**: QoS Metric ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/application/qos_metrics/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             qos_metric_id)

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/bulk_metrics/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  bulk_metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_cellular_metrics(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Cellular_Metrics API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/cellular_metrics".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_metrics(self, metric_id, tenant_id=None, api_version="v2.3"):
        """
        GET Monitor_Metrics API Function

          **Parameters:**:

          - **metric_id**: Metric ID
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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/metrics/{}".format(api_version,
                                                                             tenant_id,
                                                                             metric_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_object_stats(self, tenant_id=None, api_version="v2.5"):
        """
        GET Monitor_Object_Stats API Function

          **Parameters:**:

          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/object_stats".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_qos_metrics(self, tenant_id=None, api_version="v2.0"):
        """
        GET Monitor_Qos_Metrics API Function

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/qos_metrics".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def monitor_sys_metrics(self, tenant_id=None, api_version="v2.3"):
        """
        GET Monitor_Sys_Metrics API Function

          **Parameters:**:

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
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/sys_metrics".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def mstp_instances(self, site_id, element_id, mstp_instance_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all MSTP Instances (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: (optional) MSTP Instance ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not mstp_instance_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/mstp_instances".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id,
                                                                                                  element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/mstp_instances/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     site_id,
                                                                                                     element_id,
                                                                                                     mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def mstp_instances_status(self, site_id, element_id, mstp_instance_id, tenant_id=None, api_version="v2.0"):
        """
        Get MSTP Instance status for a specific id (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **mstp_instance_id**: MSTP Instance ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/mstp_instances/{}/status".format(api_version,
                                                                                                        tenant_id,
                                                                                                        site_id,
                                                                                                        element_id,
                                                                                                        mstp_instance_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastdynamicrps(self, site_id, element_id, multicastdynamicrp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast dynamic RPs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastdynamicrp_id**: (optional) Multicast Dynamic RP ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastdynamicrp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastdynamicrps".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id,
                                                                                                       element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastdynamicrps/{}".format(api_version,
                                                                                                          tenant_id,
                                                                                                          site_id,
                                                                                                          element_id,
                                                                                                          multicastdynamicrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastglobalconfigs(self, site_id, element_id, multicastglobalconfig_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Multicast configs (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastglobalconfig_id**: (optional) Multicast Global Config ID
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

        if not multicastglobalconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastglobalconfigs".format(api_version,
                                                                                                          tenant_id,
                                                                                                          site_id,
                                                                                                          element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastglobalconfigs/{}".format(api_version,
                                                                                                             tenant_id,
                                                                                                             site_id,
                                                                                                             element_id,
                                                                                                             multicastglobalconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastpeergroups(self, multicastpeergroup_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get multicast peer groups (v2.1)

          **Parameters:**:

          - **multicastpeergroup_id**: (optional) Multicast Peer Group ID
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

        if not multicastpeergroup_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastpeergroups".format(api_version,
                                                                                  tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastpeergroups/{}".format(api_version,
                                                                                     tenant_id,
                                                                                     multicastpeergroup_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastprotocolparameters(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast Protocol Parameters (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastprotocolparameters".format(api_version,
                                                                                                           tenant_id,
                                                                                                           site_id,
                                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastroutes(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast routes (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastroutes".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastrps(self, site_id, element_id, multicastrp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast RP configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastrp_id**: (optional) Multicast RP ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastrp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastrps".format(api_version,
                                                                                                tenant_id,
                                                                                                site_id,
                                                                                                element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastrps/{}".format(api_version,
                                                                                                   tenant_id,
                                                                                                   site_id,
                                                                                                   element_id,
                                                                                                   multicastrp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastsourcesiderps(self, site_id, multicastsourcesiderp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get multicast source side RPs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiderp_id**: (optional) Multicast Source Side RP ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastsourcesiderp_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/multicastsourcesiderps".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/multicastsourcesiderps/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 multicastsourcesiderp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastsourcesiteconfigs(self, site_id, multicastsourcesiteconfig_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get multicast source site configs (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **multicastsourcesiteconfig_id**: (optional) Multicast Source Site Config ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastsourcesiteconfig_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/multicastsourcesiteconfigs".format(api_version,
                                                                                                  tenant_id,
                                                                                                  site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/multicastsourcesiteconfigs/{}".format(api_version,
                                                                                                     tenant_id,
                                                                                                     site_id,
                                                                                                     multicastsourcesiteconfig_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def multicastwanstatus(self, site_id, element_id, multicastwanstatus_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Multicast WAN status (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **multicastwanstatus_id**: (optional) Multicast WAN Status ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not multicastwanstatus_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastwanstatus".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastwanstatus/{}".format(api_version,
                                                                                                         tenant_id,
                                                                                                         site_id,
                                                                                                         element_id,
                                                                                                         multicastwanstatus_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def natglobalprefixes(self, natglobalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Global NAT prefixes. (v2.0)

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
        Get NAT local prefixes. (v2.0)

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
        Get NAT Policy Pools. (v2.0)

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
        Get policy rules of policy set (v2.0)

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
        Get all NAT policy sets of tenant. (v2.0)

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
        Get a specific NAT policy set status of tenant. (v2.0)

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
        Get all NAT policy Set stacks of tenant. (v2.0)

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
        Get Nat Policy Zones. (v2.0)

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
        Get LAN segments (v2.0)

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

    def networkpolicyglobalprefixes(self, networkpolicyglobalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Network policy global prefixes. (v2.1)

          **Parameters:**:

          - **networkpolicyglobalprefix_id**: (optional) Network Policy Global Prefix ID
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

        if not networkpolicyglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes".format(api_version,
                                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             networkpolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def networkpolicyrules(self, networkpolicyset_id, networkpolicyrule_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get network policy rules of tenant (v2.2)

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **networkpolicyrule_id**: (optional) Network Policy Rule ID
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
        Get all network policy sets of tenant. (v2.0)

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
        Get a specific network policy set status of tenant. (v2.0)

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
        Get all network policy set stacks of tenant. (v2.0)

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

    def ngfwsecuritypolicyglobalprefixes(self, ngfwsecuritypolicyglobalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Security Policy V2 Global Prefixes for a tenant (v2.1)

          **Parameters:**:

          - **ngfwsecuritypolicyglobalprefix_id**: (optional) NGFW Security Policy Global Prefix ID
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

        if not ngfwsecuritypolicyglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicyglobalprefixes".format(api_version,
                                                                                               tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicyglobalprefixes/{}".format(api_version,
                                                                                                  tenant_id,
                                                                                                  ngfwsecuritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicylocalprefixes(self, ngfwsecuritypolicylocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Local Prefixes for a tenant (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicylocalprefix_id**: (optional) NGFW Security Policy Local Prefix ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                              tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                                 tenant_id,
                                                                                                 ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, ngfwsecuritypolicyrule_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Security Policy V2 Rules under a policy set (v2.1)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **ngfwsecuritypolicyrule_id**: (optional) NGFW Security Policy Rule ID
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

        if not ngfwsecuritypolicyrule_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules".format(api_version,
                                                                                                                tenant_id,
                                                                                                                ngfwsecuritypolicyset_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules/{}".format(api_version,
                                                                                                                   tenant_id,
                                                                                                                   ngfwsecuritypolicyset_id,
                                                                                                                   ngfwsecuritypolicyrule_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicysets(self, ngfwsecuritypolicyset_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Sets by tenant ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: (optional) NGFW Security Policy Set ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicyset_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets".format(api_version,
                                                                                     tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets/{}".format(api_version,
                                                                                        tenant_id,
                                                                                        ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ngfwsecuritypolicysetstacks(self, ngfwsecuritypolicysetstack_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Security Policy V2 Set Stacks by tenant ID (v2.0)

          **Parameters:**:

          - **ngfwsecuritypolicysetstack_id**: (optional) NGFW Security Policy Set Stack ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not ngfwsecuritypolicysetstack_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysetstacks".format(api_version,
                                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysetstacks/{}".format(api_version,
                                                                                             tenant_id,
                                                                                             ngfwsecuritypolicysetstack_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def ntp(self, element_id, ntp_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all element NTP (v2.0)

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
        Get specific element NTP (v2.0)

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

    def openapi(self, api_version="v2.0"):
        """
        GET Openapi API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/openapi".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def openapi_json(self, api_version="v2.0"):
        """
        GET Openapi_Json API Function

          **Parameters:**:

          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/openapi.json".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def operator_sessions(self, operator_id, session_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all sessions for operator id belonging to a tenant id (v2.0)

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
        Get all otp access configs. (v2.0)

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
        get all Path Groups for a tenant. (v2.1)

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
        Get list of permitted APIs that the current operator can invoke (v2.0)

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
        Get policy rules of tenant (v3.1)

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
        Get all policy sets of tenant. (v3.0)

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
        Get a specific policy set status of tenant. (v3.0)

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

    def port_vlan_members(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get switch port to VLAN port mapping information for an element (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/port_vlan_members".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prefixfilters(self, site_id, prefixfilter_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site security filters (v2.0)

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

    def prioritypolicyglobalprefixes(self, prioritypolicyglobalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Priority policy prefixes. (v2.1)

          **Parameters:**:

          - **prioritypolicyglobalprefix_id**: (optional) Priority Policy Global Prefix ID
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

        if not prioritypolicyglobalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes".format(api_version,
                                                                                           tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes/{}".format(api_version,
                                                                                              tenant_id,
                                                                                              prioritypolicyglobalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def prioritypolicyrules(self, prioritypolicyset_id, prioritypolicyrule_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get priority policy rules of tenant (v2.1)

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **prioritypolicyrule_id**: (optional) Priority Policy Rule ID
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
        Get all priority policy sets of tenant. (v2.0)

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
        Get a specific priority policy set status of tenant. (v2.0)

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
        Get all Priority policy set stacks of tenant. (v2.0)

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

    def prismaaccess_configs(self, site_id, prismaaccess_config_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Prisma Access Configs for a site (v2.0)

          **Parameters:**:

          - **site_id**: Site ID
          - **prismaaccess_config_id**: (optional) Prisma Acceess Config ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not prismaaccess_config_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prismaaccess_configs".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prismaaccess_configs/{}".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               prismaaccess_config_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def profile(self, api_version="v2.1"):
        """
        Get current user profile (v2.1)

          **Parameters:**:

          - **api_version**: API version to use (default v2.1)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/profile".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def radii(self, element_id, radii_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all radius configuration of an element in a tenant (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: (optional) Radii ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not radii_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/radii".format(api_version,
                                                                                tenant_id,
                                                                                element_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/radii/{}".format(api_version,
                                                                                   tenant_id,
                                                                                   element_id,
                                                                                   radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def radii_status(self, element_id, radii_id, tenant_id=None, api_version="v2.0"):
        """
        Get specific radius configuration status for a radius config corresponding to a tenant and element (v2.0)

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **radii_id**: Radii ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/radii/{}/status".format(api_version,
                                                                                      tenant_id,
                                                                                      element_id,
                                                                                      radii_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def recovery_tokens(self, machine_id, tenant_id=None, api_version="v2.1"):
        """
        Get recovery token for a machine (v2.1)

          **Parameters:**:

          - **machine_id**: Machine ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/{}/recovery_tokens".format(api_version,
                                                                                      tenant_id,
                                                                                      machine_id)

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
        Get a list of custom roles (v2.1)

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
        Get all Access List for Element (v2.1)

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
        Get all Community List for Element (v2.0)

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
        Get all Prefix List for Element (v2.0)

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
        Get all Route Map for Element (v2.1)

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
        Get tenant security policy rules. (v2.0)

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
        Get tenant security policy sets. (v2.0)

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
        Get security zones (v2.0)

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
        Get getServiceBindingMapList (v2.1)

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

    def serviceendpoints(self, serviceendpoint_id=None, tenant_id=None, api_version="v2.3"):
        """
        Get ServiceEndpointList (v2.3)

          **Parameters:**:

          - **serviceendpoint_id**: (optional) Service Endpoint ID
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

        if not serviceendpoint_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints".format(api_version,
                                                                               tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/{}".format(api_version,
                                                                                  tenant_id,
                                                                                  serviceendpoint_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def servicelabels(self, servicelabel_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get getServiceLabelList (v2.1)

          **Parameters:**:

          - **servicelabel_id**: (optional) Service Label ID
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

    def site_correlationevents(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        GET Sites_Correlationevents API Function

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

    def site_extensions(self, site_id, extension_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all site level extensions (v2.0)

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

    def site_hubserviceendpoints(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        Get HubServiceEndpoint for a Site of a given tenant by tenant ID and site ID (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/hubserviceendpoints".format(api_version,
                                                                                       tenant_id,
                                                                                       site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_ipfixlocalprefixes(self, site_id, ipfixlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all IPFix site prefix association (v2.0)

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

    def site_natlocalprefixes(self, site_id, natlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get site NAT prefixes (v2.0)

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

    def site_networkpolicylocalprefixes(self, site_id, networkpolicylocalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get site Network policy prefix associations (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **networkpolicylocalprefix_id**: (optional) Network Policy Local Prefix ID
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

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, ngfwsecuritypolicylocalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all security policy v2 local prefix site association for a site (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **ngfwsecuritypolicylocalprefix_id**: (optional) NGFW Security Policy Local Prefix ID
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

        if not ngfwsecuritypolicylocalprefix_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ngfwsecuritypolicylocalprefixes/{}".format(api_version,
                                                                                                          tenant_id,
                                                                                                          site_id,
                                                                                                          ngfwsecuritypolicylocalprefix_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_prioritypolicylocalprefixes(self, site_id, prioritypolicylocalprefix_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get site Priority policy prefix associations (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **prioritypolicylocalprefix_id**: (optional) Priority Policy Local Prefix ID
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

    def site_serviceconnections(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        GET Site_Serviceconnections API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/serviceconnections".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def site_status(self, site_id, tenant_id=None, api_version="v2.0"):
        """
        Get site status (v2.0)

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
        Get site ciphers (v2.0)

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

    def sites(self, site_id=None, tenant_id=None, api_version="v4.7"):
        """
        Get all sites of a tenant (v4.7)

          **Parameters:**:

          - **site_id**: (optional) Site ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.7)

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
        Get site security zones (v2.0)

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

    def snmpagents(self, site_id, element_id, snmpagent_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get SNMP Agent on an element (v2.1)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **snmpagent_id**: (optional) SNMP Agent ID
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
        Get All SNMP Trap on an element (v2.0)

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
        Get all Machine Software (v2.0)

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
        Get the software upgrade configuration of an element (v2.0)

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
        Get all software upgrade status (up to 5) started by the tenant user (v2.1)

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
        Get all spokeclusters (v2.0)

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
        Get Spoke Cluster Status. (v2.0)

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

    def staticroutes(self, site_id, element_id, staticroute_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get static routes (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: (optional) Static Route ID
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

    def staticroutes_status(self, site_id, element_id, staticroute_id, tenant_id=None, api_version="v2.2"):
        """
        Get static route status (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **staticroute_id**: Static Route ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/staticroutes/{}/status".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      staticroute_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def syslogserverprofiles(self, syslogserverprofile_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Syslog Server Profiles (v2.0)

          **Parameters:**:

          - **syslogserverprofile_id**: (optional) Sys Log Server Profile ID 
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not syslogserverprofile_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/syslogserverprofiles".format(api_version,
                                                                                   tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/syslogserverprofiles/{}".format(api_version,
                                                                                      tenant_id,
                                                                                      syslogserverprofile_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def syslogservers(self, site_id, element_id, syslogserver_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get Syslog Servers on an element (v2.2)

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **syslogserver_id**: (optional) SYSLOG server ID
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
        Get all existing NTP Template of tenant. (v2.0)

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

    def tenant_anynetlinks(self, anynetlink_id, tenant_id=None, api_version="v3.4"):
        """
        GET Tenant_Anynetlinks API Function

          **Parameters:**:

          - **anynetlink_id**: Anynet (Secure Fabric) Link ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.4)

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
        Get API versions for given apiVersions (v2.0)

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
        Get esp tenant clients details for tenant id (v2.0)

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
        Get all extensions from NB (v2.0)

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

    def tenant_hubserviceendpoints(self, tenant_id=None, api_version="v2.0"):
        """
        Get HubServiceEndpoints of a tenant (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/hubserviceendpoints".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def tenant_ipfixlocalprefixes(self, ipfixlocalprefix_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all IPFix local prefix (v2.0)

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
        Get Network Policy local prefixes. (v2.0)

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

    def tenant_operators(self, operator_id=None, tenant_id=None, api_version="v2.2"):
        """
        Get a list of tenant operators (v2.2)

          **Parameters:**:

          - **operator_id**: (optional) Operator ID
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
        Get a list of custom permissions (v2.0)

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
        Get Priority Policy local prefixes. (v2.0)

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

    def tenant_serviceconnections(self, tenant_id=None, api_version="v2.0"):
        """
        GET Tenant_Serviceconnections API Function

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceconnections".format(api_version,
                                                                             tenant_id)

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

    def tenants(self, tenant_id=None, api_version="v2.5"):
        """
        Get tenant details for tenant id (v2.5)

          **Parameters:**:

          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

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

    def useridagents(self, useridagent_id=None, tenant_id=None, api_version="v2.0"):
        """
        GET Useridagents API Function

          **Parameters:**:

          - **useridagent_id**: (optional) User Id Agent ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        if not useridagent_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/useridagents".format(api_version,
                                                                           tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/useridagents/{}".format(api_version,
                                                                              tenant_id,
                                                                              useridagent_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def users(self, user_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get Users. (v2.0)

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

    def vfflicense_status(self, vfflicense_id, tenant_id=None, api_version="v2.1"):
        """
        Get status for Vff License (v2.1)

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}/status".format(api_version,
                                                                                tenant_id,
                                                                                vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vfflicense_tokens(self, vfflicense_id, token_id=None, tenant_id=None, api_version="v2.0"):
        """
        Get all Tenant Vff License Tokens (v2.0)

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

    def vfflicenses(self, vfflicense_id=None, tenant_id=None, api_version="v2.1"):
        """
        Get all Vff Licenses for Tenant (v2.1)

          **Parameters:**:

          - **vfflicense_id**: (optional) Virtual Form Factor License ID
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

        if not vfflicense_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses".format(api_version,
                                                                          tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/vfflicenses/{}".format(api_version,
                                                                             tenant_id,
                                                                             vfflicense_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vlan_port_members(self, site_id, element_id, tenant_id=None, api_version="v2.0"):
        """
        Get VLAN to switch port mapping information for an element (v2.0)

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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/vlan_port_members".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def vpnlinks_state(self, vpnlink_id, tenant_id=None, api_version="v2.0"):
        """
        Get the VPNLink admin state (v2.0)

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
        Get the VPNLink status (v2.1)

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

    def waninterfacelabels(self, waninterfacelabel_id=None, tenant_id=None, api_version="v2.4"):
        """
        Get WAN interface labels for a tenant (v2.4)

          **Parameters:**:

          - **waninterfacelabel_id**: (optional) WAN Interface Label ID
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

        if not waninterfacelabel_id:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels".format(api_version,
                                                                                 tenant_id)
        else:
            url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/{}".format(api_version,
                                                                                    tenant_id,
                                                                                    waninterfacelabel_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "get")

    def waninterfaces(self, site_id, waninterface_id=None, tenant_id=None, api_version="v2.7"):
        """
        Get all Site WAN interfaces (v2.7)

          **Parameters:**:

          - **site_id**: Site ID
          - **waninterface_id**: (optional) WAN Interface ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.7)

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
        Get a specific Site WAN interface status (v2.1)

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
        Get all tenant WAN networks (v2.1)

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
        Get app/wan contexts (v2.0)

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

    aaa_metrics_monitor = monitor_aaa_metrics
    """ Backwards-compatibility alias of `aaa_metrics_monitor` to `monitor_aaa_metrics`"""

    access_elementusers = elementusers_access
    """ Backwards-compatibility alias of `access_elementusers` to `elementusers_access`"""

    advertisedprefixes_bgppeers = bgppeers_advertisedprefixes
    """ Backwards-compatibility alias of `advertisedprefixes_bgppeers` to `bgppeers_advertisedprefixes`"""

    aggregates_aiops_monitor = monitor_aiops_aggregates
    """ Backwards-compatibility alias of `aggregates_aiops_monitor` to `monitor_aiops_aggregates`"""

    aggregates_monitor = monitor_aggregates
    """ Backwards-compatibility alias of `aggregates_monitor` to `monitor_aggregates`"""

    anomaly_aiops_monitor = monitor_aiops_anomaly
    """ Backwards-compatibility alias of `anomaly_aiops_monitor` to `monitor_aiops_anomaly`"""

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

    cellular_metrics_monitor = monitor_cellular_metrics
    """ Backwards-compatibility alias of `cellular_metrics_monitor` to `monitor_cellular_metrics`"""

    cellular_modules_e = element_cellular_modules
    """ Backwards-compatibility alias of `cellular_modules_e` to `element_cellular_modules`"""

    cellular_modules_m = machine_cellular_modules
    """ Backwards-compatibility alias of `cellular_modules_m` to `machine_cellular_modules`"""

    clients_t = tenant_clients
    """ Backwards-compatibility alias of `clients_t` to `tenant_clients`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    connectivity_appstatus_sdwanapps = sdwanapps_appstatus_connectivity
    """ Backwards-compatibility alias of `connectivity_appstatus_sdwanapps` to `sdwanapps_appstatus_connectivity`"""

    correlationevents_anynetlinks = anynetlinks_correlationevents
    """ Backwards-compatibility alias of `correlationevents_anynetlinks` to `anynetlinks_correlationevents`"""

    correlationevents_e = element_correlationevents
    """ Backwards-compatibility alias of `correlationevents_e` to `element_correlationevents`"""

    correlationevents_interfaces = interfaces_correlationevents
    """ Backwards-compatibility alias of `correlationevents_interfaces` to `interfaces_correlationevents`"""

    correlationevents_s = site_correlationevents
    """ Backwards-compatibility alias of `correlationevents_s` to `site_correlationevents`"""

    correlationevents_waninterfaces = wantinterfaces_correlationevents
    """ Backwards-compatibility alias of `correlationevents_waninterfaces` to `wantinterfaces_correlationevents`"""

    discoveredprefixes_bgppeers = bgppeers_discoveredprefixes
    """ Backwards-compatibility alias of `discoveredprefixes_bgppeers` to `bgppeers_discoveredprefixes`"""

    domainstatus_directoryservices = directoryservices_domainstatus
    """ Backwards-compatibility alias of `domainstatus_directoryservices` to `directoryservices_domainstatus`"""

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

    firmware_cellular_modules_e = element_cellular_modules_firmware
    """ Backwards-compatibility alias of `firmware_cellular_modules_e` to `element_cellular_modules_firmware`"""

    firmware_cellular_modules_m = machine_cellular_modules_firmware
    """ Backwards-compatibility alias of `firmware_cellular_modules_m` to `machine_cellular_modules_firmware`"""

    forecast_aiops_monitor = monitor_aiops_forecast
    """ Backwards-compatibility alias of `forecast_aiops_monitor` to `monitor_aiops_forecast`"""

    health_aiops_monitor = monitor_aiops_health
    """ Backwards-compatibility alias of `health_aiops_monitor` to `monitor_aiops_health`"""

    hubserviceendpoints_s = site_hubserviceendpoints
    """ Backwards-compatibility alias of `hubserviceendpoints_s` to `site_hubserviceendpoints`"""

    hubserviceendpoints_t = tenant_hubserviceendpoints
    """ Backwards-compatibility alias of `hubserviceendpoints_t` to `tenant_hubserviceendpoints`"""

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

    multicastigmpmemberships_interfaces = interface_multicastigmpmemberships
    """ Backwards-compatibility alias of `multicastigmpmemberships_interfaces` to `interface_multicastigmpmemberships`"""

    multicaststatus_interfaces = interfaces_multicaststatus
    """ Backwards-compatibility alias of `multicaststatus_interfaces` to `interfaces_multicaststatus`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    networkpolicylocalprefixes_s = site_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_s` to `site_networkpolicylocalprefixes`"""

    networkpolicylocalprefixes_t = tenant_networkpolicylocalprefixes
    """ Backwards-compatibility alias of `networkpolicylocalprefixes_t` to `tenant_networkpolicylocalprefixes`"""

    ngfwsecuritypolicylocalprefixes_s = site_ngfwsecuritypolicylocalprefixes
    """ Backwards-compatibility alias of `ngfwsecuritypolicylocalprefixes_s` to `site_ngfwsecuritypolicylocalprefixes`"""

    ngfwsecuritypolicylocalprefixes_t = ngfwsecuritypolicylocalprefixes
    """ Backwards-compatibility alias of `ngfwsecuritypolicylocalprefixes_t` to `ngfwsecuritypolicylocalprefixes`"""

    ntp_templates = templates_ntp
    """ Backwards-compatibility alias of `ntp_templates` to `templates_ntp`"""

    object_stats_aiops_monitor = monitor_aiops_object_stats
    """ Backwards-compatibility alias of `object_stats_aiops_monitor` to `monitor_aiops_object_stats`"""

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

    qos_metrics_application_monitor = monitor_application_qos_metrics
    """ Backwards-compatibility alias of `qos_metrics_application_monitor` to `monitor_application_qos_metrics`"""

    qos_metrics_monitor = monitor_qos_metrics
    """ Backwards-compatibility alias of `qos_metrics_monitor` to `monitor_qos_metrics`"""

    reachableprefixes_bgppeers = bgppeers_reachableprefixes
    """ Backwards-compatibility alias of `reachableprefixes_bgppeers` to `bgppeers_reachableprefixes`"""

    revoked_certificates = certificates_revoked
    """ Backwards-compatibility alias of `revoked_certificates` to `certificates_revoked`"""

    roles_clients = clients_roles
    """ Backwards-compatibility alias of `roles_clients` to `clients_roles`"""

    serviceconnections_s = site_serviceconnections
    """ Backwards-compatibility alias of `serviceconnections_s` to `site_serviceconnections`"""

    serviceconnections_t = tenant_serviceconnections
    """ Backwards-compatibility alias of `serviceconnections_t` to `tenant_serviceconnections`"""

    sessions_t = operator_sessions
    """ Backwards-compatibility alias of `sessions_t` to `operator_sessions`"""

    sim_security_cellular_modules = cellular_modules_sim_security
    """ Backwards-compatibility alias of `sim_security_cellular_modules` to `cellular_modules_sim_security`"""

    state = element_state
    """ Backwards-compatibility alias of `state` to `element_state`"""

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

    status_cellular_modules_e = element_cellular_modules_status
    """ Backwards-compatibility alias of `status_cellular_modules_e` to `element_cellular_modules_status`"""

    status_cellular_modules_m = machine_cellular_modules_status
    """ Backwards-compatibility alias of `status_cellular_modules_m` to `machine_cellular_modules_status`"""

    status_directoryservices = directoryservices_status
    """ Backwards-compatibility alias of `status_directoryservices` to `directoryservices_status`"""

    status_e = element_status
    """ Backwards-compatibility alias of `status_e` to `element_status`"""

    status_firmware_cellular_modules_e = element_cellular_modules_firmware_status
    """ Backwards-compatibility alias of `status_firmware_cellular_modules_e` to `element_cellular_modules_firmware_status`"""

    status_firmware_cellular_modules_m = machine_cellular_modules_firmware_status
    """ Backwards-compatibility alias of `status_firmware_cellular_modules_m` to `machine_cellular_modules_firmware_status`"""

    status_hubclustermembers = hubclustermember_status
    """ Backwards-compatibility alias of `status_hubclustermembers` to `hubclustermember_status`"""

    status_i = hubclusters_status
    """ Backwards-compatibility alias of `status_i` to `hubclusters_status`"""

    status_interface_authentication = interface_authentication_status
    """ Backwards-compatibility alias of `status_interface_authentication` to `interface_authentication_status`"""

    status_interfaces = interfaces_status
    """ Backwards-compatibility alias of `status_interfaces` to `interfaces_status`"""

    status_lldp_neighbors = lldp_neighbors_status
    """ Backwards-compatibility alias of `status_lldp_neighbors` to `lldp_neighbors_status`"""

    status_mac_addresses = mac_addresses_status
    """ Backwards-compatibility alias of `status_mac_addresses` to `mac_addresses_status`"""

    status_mstp_instances = mstp_instances_status
    """ Backwards-compatibility alias of `status_mstp_instances` to `mstp_instances_status`"""

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

    status_radii = radii_status
    """ Backwards-compatibility alias of `status_radii` to `radii_status`"""

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

    status_staticroutes = staticroutes_status
    """ Backwards-compatibility alias of `status_staticroutes` to `staticroutes_status`"""

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

    elements_correlationevents = element_correlationevents
    """ Backwards-compatibility alias of `elements_correlationevents` to `element_correlationevents`"""

    hubcluster_status = hubclusters_status
    """ Backwards-compatibility alias of `hubcluster_status` to `hubclusters_status`"""

