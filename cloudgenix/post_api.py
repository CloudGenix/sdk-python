#!/usr/bin/env python
"""
CloudGenix Python SDK - POST

**Author:** CloudGenix

**Copyright:** (c) 2017-2022 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2022 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017-2022 CloudGenix, Inc

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

    def access_elementusers(self, elementuser_id, data, tenant_id=None, api_version="v2.1"):
        """
        Grant Specific role to Element user on specific element

          **Parameters:**:

          - **elementuser_id**: Element User ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_id:**  Type: string 

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

    def anynetlinks_correlationevents_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        POST Anynetlinks_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/anynetlinks/correlationevents/query".format(api_version,
                                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def apnprofiles(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create an APN Profile

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **apn:**  Type: string 
           - **authentication:**  Type: string 
           - **clear_password:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **password:**  Type: string 
           - **tags:**  [Type: string] 
           - **user_name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/apnprofiles".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def apnprofiles_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of apn profiles that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **apn:**  Type: string 
           - **authentication:**  Type: string 
           - **clear_password:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **password:**  Type: string 
           - **tags:**  [Type: string] 
           - **user_name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/apnprofiles/query".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs(self, data, tenant_id=None, api_version="v2.4"):
        """
        Create a application definition

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 

           - **abbreviation:**  Type: string 
           - **aggregate_flows:**  Type: boolean 
           - **app_type:**  Type: string 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **display_name:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**  [Type: object] 
           - **is_deprecated:**  Type: boolean 
           - **network_scan_application:**  Type: boolean 
           - **order_number:**  Type: integer 
           - **overrides_allowed:**  Type: boolean 
           - **p_category:**  Type: string 
           - **p_parent_id:**  Type: string 
           - **p_sub_category:**  Type: string 
           - **parent_id:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **supported_engines:**  Type: string 
           - **system_app_overridden:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tcp_rules:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**  [Type: object] 
           - **use_parentapp_network_policy:**  Type: boolean 

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

    def appdefs_overrides(self, appdef_id, data, tenant_id=None, api_version="v2.3"):
        """
        Create a application definition overrides for system appdef

          **Parameters:**:

          - **appdef_id**: Application Definition ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **aggregate_flows:**  Type: boolean 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**           
               - **dest_filters:**  [Type: string] 
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **protocol:**  Type: string 
               - **src_filters:**  [Type: string] 
           - **override_default_ip_rules:**  Type: boolean 
           - **override_default_tcp_rules:**  Type: boolean 
           - **override_default_udp_rules:**  Type: boolean 
           - **override_domains:**  Type: boolean 
           - **overrides_disable:**  Type: boolean 
           - **p_category:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **tags:**  [Type: string] 
           - **tcp_rules:**           
               - **client_filters:**  [Type: string] 
               - **client_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **server_filters:**  [Type: string] 
               - **server_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **server_prefixes:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**           
               - **dest_prefixes:**  [Type: string] 
               - **dscp:**           
                   - **value:**  Type: integer 
               - **udp_filters:**  [Type: string] 
               - **udp_port:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
           - **use_parentapp_network_policy:**  Type: boolean 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/appdefs/{}/overrides".format(api_version,
                                                                               tenant_id,
                                                                               appdef_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def appdefs_query(self, data, tenant_id=None, api_version="v2.4"):
        """
        Queries db for limit number of app defs that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 

           - **abbreviation:**  Type: string 
           - **aggregate_flows:**  Type: boolean 
           - **app_type:**  Type: string 
           - **app_unreachability_detection:**  Type: boolean 
           - **category:**  Type: string 
           - **conn_idle_timeout:**  Type: integer 
           - **description:**  Type: string 
           - **display_name:**  Type: string 
           - **domains:**  [Type: string] 
           - **ingress_traffic_pct:**  Type: integer 
           - **ip_rules:**  [Type: object] 
           - **is_deprecated:**  Type: boolean 
           - **network_scan_application:**  Type: boolean 
           - **order_number:**  Type: integer 
           - **overrides_allowed:**  Type: boolean 
           - **parent_id:**  Type: string 
           - **path_affinity:**  Type: string 
           - **session_timeout:**  Type: integer 
           - **system_app_overridden:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tcp_rules:**  [Type: string] 
           - **transfer_type:**  Type: string 
           - **udp_rules:**  [Type: object] 
           - **use_parentapp_network_policy:**  Type: boolean 

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

    def auditlog_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        POST Auditlog_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/auditlog/query".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def authtokens(self, operator_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create an auth token

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **expires_utc_ms:**  Type: integer 
           - **is_system_owned:**  Type: boolean 
           - **roles:**           
               - **name:**  Type: string 
           - **session_key_c:**  Type: string 
           - **x_auth_token:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/authtokens".format(api_version,
                                                                                  tenant_id,
                                                                                  operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers(self, site_id, element_id, data, tenant_id=None, api_version="v2.2"):
        """
        Create BGP peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **bgp_config:**           
               - **adv_interval:**  Type: integer 
               - **hold_time:**  Type: integer 
               - **keepalive_time:**  Type: integer 
               - **local_as_num:**  Type: string 
               - **md5_secret:**  Type: string 
               - **multi_hop_limit:**  Type: integer 
               - **peer_auth_type:**  Type: string 
               - **peer_retry_time:**  Type: integer 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **peer_ip:**  Type: string 
           - **peer_type:**  Type: string 
           - **remote_as_num:**  Type: string 
           - **route_map_in_id:**  Type: string 
           - **route_map_out_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **update_source:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id,
                                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers_operations(self, site_id, element_id, bgppeer_id, data, tenant_id=None, api_version="v2.0"):
        """
        Reset BGP peer config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **bgppeer_id**: BGP Peer ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **value:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/{}/operations".format(api_version,
                                                                                                      tenant_id,
                                                                                                      site_id,
                                                                                                      element_id,
                                                                                                      bgppeer_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def bgppeers_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.2"):
        """
        Queries db for limit number of BGP peers that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **bgp_config:**           
               - **adv_interval:**  Type: integer 
               - **hold_time:**  Type: integer 
               - **keepalive_time:**  Type: integer 
               - **local_as_num:**  Type: string 
               - **md5_secret:**  Type: string 
               - **multi_hop_limit:**  Type: integer 
               - **peer_auth_type:**  Type: string 
               - **peer_retry_time:**  Type: integer 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **peer_ip:**  Type: string 
           - **peer_type:**  Type: string 
           - **remote_as_num:**  Type: string 
           - **route_map_in_id:**  Type: string 
           - **route_map_out_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **update_source:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/bgppeers/query".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id,
                                                                                              element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_module_firmware_status_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query the cellular module firmware upgrade status of all tenant elements

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/cellular_module_firmware/status/query".format(api_version,
                                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def cellular_modules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of cellular modules that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **element_id:**  Type: string 
           - **gps_enable:**  Type: boolean 
           - **name:**  Type: string 
           - **primary_sim:**  Type: integer 
           - **radio_on:**  Type: boolean 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/cellular_modules/query".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def certificate_operations(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Start CIC renewal process for an element device

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **parameters:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/certificate_operations".format(api_version,
                                                                                             tenant_id,
                                                                                             element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_login(self, client_id, data, tenant_id=None, api_version="v2.0"):
        """
        Login api for esp client

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **email:**  Type: string 
           - **logout_others:**  Type: boolean 
           - **password:**  Type: string 
           - **requestId:**  Type: string 

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

    def clients_logout(self, data, tenant_id=None, api_version="v2.0"):
        """
        Logout api for esp client. Reverts back to esp session

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **disallowed_permissions:**  Type: object 
           - **operator_id:**  Type: string 
           - **permissions:**  Type: object 
           - **redirect_region:**  Type: string 
           - **redirect_urlpath:**  Type: string 
           - **redirect_x_auth_token:**  Type: string 
           - **resource_role_map:**  [Type: object] 
           - **resource_uri_map:**  Type: object 
           - **resource_version_map:**  Type: object 
           - **tenant_id:**  Type: string 
           - **version_exceptions_map:**  [Type: object] 
           - **x_auth_token:**  Type: string 

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

    def clients_machines_query(self, client_id, data, tenant_id=None, api_version="v2.2"):
        """
        Query and get all machines allocated by ESP to a client tenant

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **deleted_count:**  Type: integer 
           - **deleted_ids:**  [Type: string] 
           - **next_query:**  Type: object 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/machines/query".format(api_version,
                                                                                    tenant_id,
                                                                                    client_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Get esp tenant clients details for tenant id

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **canonical_name:**  Type: string 
           - **clients:**  [Type: string] 
           - **is_esp:**  Type: boolean 
           - **name:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/query".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def clients_reallocate(self, client_id, machine_id, data, tenant_id=None, api_version="v2.2"):
        """
        Reallocate a specific machine from one client tenant to another, both client tenants are clients of the same ESP.

          **Parameters:**:

          - **client_id**: ESP/MSP Client ID (typically their tenant_id)
          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           - **renew_state:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/clients/{}/machines/{}/reallocate".format(api_version,
                                                                                            tenant_id,
                                                                                            client_id,
                                                                                            machine_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def demstatus_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query ADEM status

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **dem_enabled:**  Type: boolean 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/demstatus/query".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dhcpservers(self, site_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new dhcp server configuration for a subnet

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **broadcast_address:**  Type: string 
           - **custom_options:**           
               - **option_definition:**  Type: string 
               - **option_value:**  Type: string 
               - **vendor_class_identifier:**  Type: string 
           - **default_lease_time:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **dns_servers:**  [Type: string] 
           - **domain_name:**  Type: string 
           - **gateway:**  Type: string 
           - **ip_ranges:**           
               - **end_ip:**  Type: string 
               - **start_ip:**  Type: string 
           - **max_lease_time:**  Type: integer 
           - **network_context_id:**  Type: string 
           - **static_mappings:**           
               - **ip_address:**  Type: string 
               - **mac:**  Type: string 
               - **name:**  Type: string 
           - **subnet:**  Type: string 
           - **tags:**  [Type: string] 

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

    def dnsserviceprofiles(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new DNS service profile

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **authoritative_config:**           
               - **caa_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **tag:**  Type: string 
                   - **value:**  Type: string 
               - **cname_records:**           
                   - **name:**  [Type: string] 
                   - **target:**  Type: string 
                   - **ttl:**  Type: integer 
               - **dns_resource_records:**           
                   - **hex_data:**  Type: string 
                   - **name:**  Type: string 
                   - **rr_number:**  Type: integer 
               - **host_records:**           
                   - **domain_names:**  [Type: string] 
                   - **ipv4_address:**  Type: string 
                   - **ipv6_address:**  Type: string 
                   - **ttl:**  Type: integer 
               - **mx_host_records:**           
                   - **hostname:**  Type: string 
                   - **mx_name:**  Type: string 
                   - **preference:**  Type: integer 
               - **naptr_records:**           
                   - **flags:**  Type: string 
                   - **name:**  Type: string 
                   - **order:**  Type: integer 
                   - **preference:**  Type: integer 
                   - **regexp:**  Type: string 
                   - **replacement:**  Type: string 
                   - **service:**  Type: string 
               - **peers:**  [Type: string] 
               - **ptr_records:**           
                   - **name:**  Type: string 
                   - **target:**  Type: string 
               - **secondary_servers:**  [Type: string] 
               - **servers:**           
                   - **dnsservicerole_id:**  Type: string 
                   - **domain_name:**  Type: string 
               - **soa:**           
                   - **expiry:**  Type: integer 
                   - **host_master:**  Type: string 
                   - **refresh:**  Type: integer 
                   - **retry:**  Type: integer 
                   - **serial_number:**  Type: integer 
               - **srv_hosts:**           
                   - **domain_name:**  Type: string 
                   - **port:**  Type: integer 
                   - **priority:**  Type: integer 
                   - **protocol:**  Type: string 
                   - **service:**  Type: string 
                   - **target:**  Type: integer 
                   - **weight:**  Type: integer 
               - **synth_domains:**           
                   - **domain:**  Type: string 
                   - **end_ipaddress:**  Type: string 
                   - **ipaddress_prefix:**  Type: string 
                   - **prefix:**  Type: string 
                   - **start_ipaddress:**  Type: string 
               - **ttl:**  Type: integer 
               - **txt_records:**           
                   - **domain_name:**  Type: string 
                   - **texts:**  [Type: string] 
               - **zones:**           
                   - **domain_name:**  Type: string 
                   - **exclude_prefix:**  [Type: string] 
                   - **include_prefix:**  [Type: string] 
           - **cache_config:**           
               - **cache_size:**  Type: integer 
               - **disable_negative_caching:**  Type: boolean 
               - **max_cache_ttl:**  Type: integer 
               - **min_cache_ttl:**  Type: integer 
               - **negative_cache_ttl:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **dns_forward_config:**           
               - **dns_servers:**           
                   - **dnsserver_ip:**  Type: string 
                   - **dnsserver_port:**  Type: integer 
                   - **domain_names:**  [Type: string] 
                   - **forward_dnsservicerole_id:**  Type: string 
                   - **ip_prefix:**  Type: string 
                   - **source_port:**  Type: integer 
               - **max_source_port:**  Type: integer 
               - **min_source_port:**  Type: integer 
               - **send_to_all_dns_servers:**  Type: boolean 
           - **dns_queries_metadata:**           
               - **add_client_mac:**           
                   - **mac_encoding_format:**  Type: string 
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dns_rebind_config:**           
               - **enable_localhost_rebind:**  Type: boolean 
               - **rebind_domains:**  [Type: string] 
               - **stop_dns_rebind_privateip:**  Type: boolean 
           - **dns_response_overrides:**           
               - **aliases:**           
                   - **mask:**  Type: integer 
                   - **original_end_ip:**  Type: string 
                   - **original_ip:**  Type: string 
                   - **original_start_ip:**  Type: string 
                   - **replace_ip:**  Type: string 
               - **bogus_nx_domains:**  [Type: string] 
               - **disable_private_ip_lookups:**  Type: boolean 
               - **ignore_ip_addresses:**  [Type: string] 
               - **local_ttl:**  Type: integer 
               - **max_ttl:**  Type: integer 
           - **dnssec_config:**           
               - **disable_dnssec_timecheck:**  Type: boolean 
               - **dns_check_unsigned:**  Type: boolean 
               - **enabled:**  Type: boolean 
               - **trust_anchors:**           
                   - **class:**  Type: string 
                   - **domain:**  Type: string 
                   - **key_digest:**           
                       - **algorithm:**  Type: integer 
                       - **digest:**  Type: string 
                       - **digest_type:**  Type: integer 
                       - **key_tag:**  Type: integer 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **edns_packet_max:**  Type: integer 
           - **enable_dns_loop_detection:**  Type: boolean 
           - **enable_dnssec_proxy:**  Type: boolean 
           - **enable_strict_domain_name:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **listen_dnsservicerole_id:**  Type: string 
           - **listen_port:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsserviceprofiles_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query DNS service profile based on parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceprofiles/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsserviceroles(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new DNS service role

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsserviceroles_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query DNS service role based on parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsserviceroles/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsservices(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new DNS service config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **cache_config:**           
               - **cache_size:**  Type: integer 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **dns_queries_metadata:**           
               - **add_customer_premises_equipment:**           
                   - **identifier_text:**  Type: string 
                   - **type:**  Type: string 
               - **add_subnets:**           
                   - **ipv4_address:**  Type: string 
                   - **ipv4_prefix_length:**  Type: integer 
                   - **ipv6_address:**  Type: string 
                   - **ipv6_prefix_length:**  Type: integer 
           - **dnsservice_profile_id:**  Type: string 
           - **dnsservicerole_bindings:**           
               - **dnsservicerole_id:**  Type: string 
               - **interfaces:**           
                   - **admin_state_changed:**  Type: boolean 
                   - **admin_up:**  Type: boolean 
                   - **attached_lan_networks:**           
                       - **lan_network_id:**  Type: string 
                       - **vlan_id:**  Type: integer 
                   - **bound_interfaces:**           
                       - **interface_id:**  Type: string 
                       - **type:**  Type: string 
                   - **cellular_config:**           
                       - **apn_config:**           
                           - **apn:**  Type: string 
                           - **authentication:**  Type: string 
                           - **clear_password:**  Type: boolean 
                           - **password:**  Type: string 
                           - **password_encrypted:**  Type: string 
                           - **user_name:**  Type: string 
                       - **apn_etag:**  Type: integer 
                       - **apnprofile_id:**  Type: string 
                       - **auto_apn:**  Type: boolean 
                       - **parent_module_id:**  Type: string 
                       - **parent_sim_slot_number:**  Type: integer 
                   - **config_state:**  Type: string 
                   - **description:**  Type: string 
                   - **devicemgmt_policysetstack_id:**  Type: string 
                   - **dhcp_relay:**           
                       - **enabled:**  Type: boolean 
                       - **option_82:**           
                           - **circuit_id:**  Type: string 
                           - **enabled:**  Type: boolean 
                           - **reforwarding_policy:**  Type: string 
                           - **remote_id:**  Type: string 
                       - **server_ips:**  [Type: string] 
                       - **source_interface:**  Type: string 
                   - **directed_broadcast:**  Type: boolean 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **element_etag:**  Type: integer 
                   - **element_id:**  Type: string 
                   - **element_port_admin_up:**  Type: boolean 
                   - **ethernet_port:**           
                       - **full_duplex:**  Type: boolean 
                       - **speed:**  Type: integer 
                   - **id:**  Type: string 
                   - **ifType:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **ipfixcollectorcontext_id:**  Type: string 
                   - **ipfixfiltercontext_id:**  Type: string 
                   - **ipv4_config:**           
                       - **dhcp_config:**           
                           - **client_id:**  Type: string 
                           - **hostname:**  Type: string 
                       - **dns_v4_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **pppoe_config:**           
                           - **chap_passwd:**  Type: string 
                           - **chap_user:**  Type: string 
                           - **set_route:**  Type: boolean 
                       - **routes:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **static_config:**           
                           - **address:**  Type: string 
                       - **type:**  Type: string 
                   - **ipv6_config:**           
                       - **dhcp_config:**           
                           - **client_id:**  Type: string 
                           - **hostname:**  Type: string 
                       - **dns_v6_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **routes:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **static_config:**           
                           - **address:**  Type: string 
                       - **type:**  Type: string 
                   - **is2kFlag:**  Type: boolean 
                   - **is_parent:**  Type: boolean 
                   - **is_service_link_parent:**  Type: boolean 
                   - **lan_state_propagation:**  Type: boolean 
                   - **mac_address:**  Type: string 
                   - **mtu:**  Type: integer 
                   - **multicast_config:**           
                       - **dr_priority:**  Type: integer 
                       - **igmp_static_joins:**           
                           - **igmp_static_grp_ipv4:**  Type: string 
                           - **igmp_static_src_ipv4:**  Type: string 
                       - **igmp_version:**  Type: string 
                       - **multicast_enabled:**  Type: boolean 
                   - **name:**  Type: string 
                   - **nat_address:**  Type: string 
                   - **nat_address_v6:**  Type: string 
                   - **nat_pools:**           
                       - **ipv4_ranges:**           
                           - **end:**  Type: string 
                           - **start:**  Type: string 
                       - **nat_pool_id:**  Type: string 
                   - **nat_port:**  Type: integer 
                   - **nat_port_v6:**  Type: integer 
                   - **nat_zone_id:**  Type: string 
                   - **network_context_id:**  Type: string 
                   - **parent:**  Type: string 
                   - **pppoe_config:**           
                       - **host_uniq:**  Type: string 
                       - **parent:**  Type: string 
                       - **password:**  Type: string 
                       - **reconnection_delay:**  Type: integer 
                       - **service_name:**  Type: string 
                       - **username:**  Type: string 
                   - **propagation_state_changed:**  Type: boolean 
                   - **region:**  Type: string 
                   - **relay_changed:**  Type: boolean 
                   - **sb_api_version:**  Type: string 
                   - **scope:**  Type: string 
                   - **secondary_ip_configs:**           
                       - **ipv4_address:**  Type: string 
                       - **scope:**  Type: string 
                   - **service_link_config:**           
                       - **gre_config:**           
                           - **csum:**  Type: boolean 
                           - **keepalive_enable:**  Type: boolean 
                           - **keepalive_fail_count:**  Type: integer 
                           - **keepalive_interval:**  Type: integer 
                       - **ipsec_config:**           
                           - **authentication:**           
                               - **certificate:**  Type: string 
                               - **ikev1_params:**           
                                   - **xauth_id:**  Type: string 
                                   - **xauth_secret:**  Type: string 
                                   - **xauth_secret_encrypted:**  Type: string 
                                   - **xauth_secret_hash:**  Type: string 
                                   - **xauth_type:**  Type: string 
                               - **local_ca_certificate:**  Type: string 
                               - **local_id:**  Type: string 
                               - **local_id_custom:**  Type: string 
                               - **passphrase:**  Type: string 
                               - **passphrase_encrypted:**  Type: string 
                               - **private_key:**  Type: string 
                               - **private_key_encrypted:**  Type: string 
                               - **remote_ca_certificate:**  Type: string 
                               - **remote_id:**  Type: string 
                               - **secret:**  Type: string 
                               - **secret_encrypted:**  Type: string 
                               - **secret_hash:**  Type: string 
                               - **type:**  Type: string 
                               - **x509Objects:**           
                                   - **certHolder:**  Type: object 
                                   - **certificate:**  Type: string 
                                   - **is_local_ca_cert_set:**  Type: boolean 
                                   - **is_remote_ca_cert_set:**  Type: boolean 
                                   - **keyPair:**  Type: object 
                                   - **local_ca_certificate:**  Type: string 
                                   - **local_ca_certs_set:**  [Type: object] 
                                   - **passphrase:**  Type: string 
                                   - **private_key:**  Type: string 
                                   - **remote_ca_certificate:**  Type: string 
                                   - **remote_ca_certs_set:**  [Type: object] 
                           - **ipsec_profile_id:**  Type: string 
                       - **last_parent:**  Type: string 
                       - **parent:**  Type: string 
                       - **peer:**           
                           - **hostname:**  Type: string 
                           - **ip_addresses:**  [Type: string] 
                       - **security_service_endpoint_id:**  Type: string 
                       - **service_endpoint_id:**  Type: string 
                       - **type:**  Type: string 
                   - **site_id:**  Type: string 
                   - **site_wan_interface_ids:**  [Type: string] 
                   - **state_id:**           
                       - **cellular_state:**           
                           - **active:**  Type: boolean 
                           - **apn_info:**           
                               - **apn:**  Type: string 
                               - **authentication:**  Type: string 
                       - **device:**  Type: string 
                       - **disabled:**  Type: boolean 
                       - **disabled_reason:**  Type: string 
                       - **dns_v4_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **dns_v6_config:**           
                           - **name_servers:**  [Type: string] 
                           - **search:**  [Type: string] 
                       - **element_id:**  Type: string 
                       - **extended_state:**  Type: string 
                       - **id:**  Type: string 
                       - **ike_algo:**  Type: string 
                       - **ike_last_rekeyed:**  Type: integer 
                       - **ike_next_rekey:**  Type: integer 
                       - **inactive:**  Type: boolean 
                       - **inactive_reason:**  Type: string 
                       - **index:**  Type: integer 
                       - **ipsec_algo:**  Type: string 
                       - **ipsec_last_rekeyed:**  Type: integer 
                       - **ipsec_next_rekey:**  Type: integer 
                       - **ipv4_addresses:**  [Type: string] 
                       - **ipv4_addresses_changed:**  Type: boolean 
                       - **ipv6_addresses:**  [Type: string] 
                       - **ipv6_addresses_changed:**  Type: boolean 
                       - **last_state_change:**  Type: integer 
                       - **link_local_address:**  Type: string 
                       - **local_tunnel_v4_addr:**  Type: string 
                       - **mac_address:**  Type: string 
                       - **name:**  Type: string 
                       - **negotiated_mtu:**  Type: integer 
                       - **operational_state:**  Type: string 
                       - **operational_state_changed:**  Type: boolean 
                       - **port:**           
                           - **end:**  Type: string 
                           - **start:**  Type: string 
                       - **region:**  Type: string 
                       - **remote_host_name:**  Type: string 
                       - **remote_v4_addr:**  Type: string 
                       - **routes:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **routes_v6:**           
                           - **destination:**  Type: string 
                           - **via:**  Type: string 
                       - **secondary_ipv4_addresses:**  [Type: string] 
                       - **state:**  Type: boolean 
                       - **tenant_id:**  Type: string 
                   - **static_arp_configs:**           
                       - **ipv4_address:**  Type: string 
                       - **mac_address:**  Type: string 
                   - **sub_interface:**           
                       - **vlan_id:**  Type: integer 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
                   - **tmpPortType:**  Type: string 
                   - **type:**  Type: string 
                   - **use_relay:**  Type: boolean 
                   - **used_for:**  Type: string 
                   - **vlan_ids:**  [Type: integer] 
                   - **wan_network_id:**  Type: string 
           - **domains_to_addresses:**           
               - **domain_names:**  [Type: string] 
               - **ipv4_address:**  Type: string 
               - **ipv6_address:**  Type: string 
           - **domains_to_interfaces:**           
               - **domain_names:**  [Type: string] 
               - **interface_id:**  Type: string 
           - **element_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **max_concurrent_dns_queries:**  Type: integer 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **upperCaseName:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/dnsservices".format(api_version,
                                                                                           tenant_id,
                                                                                           site_id,
                                                                                           element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def dnsservices_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query DNS service config based on parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/dnsservices/query".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_bulk_config_state_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Get element config/state info for queried elements from NB

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **items:**  [Type: object] 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/bulk_config_state/query".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def element_correlationevents_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Element_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/correlationevents/query".format(api_version,
                                                                                           tenant_id)

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

          **Payload Attributes:** 

           - **conf:**  Type: object 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

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

    def element_extensions_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Query element level extensions that match query params

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

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

    def element_query(self, data, tenant_id=None, api_version="v2.5"):
        """
        Queries db for limit number of elements that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 


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

    def elementaccessconfigs(self, element_id, data, tenant_id=None, api_version="v2.2"):
        """
        POST Elementaccessconfigs API Function

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


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

    def elementsecurityzones(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between element and security zone.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **interface_ids:**  [Type: string] 
           - **lannetwork_ids:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **waninterface_ids:**  [Type: string] 
           - **wanoverlay_ids:**  [Type: string] 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/securityzones".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementsecurityzones_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query element security zones.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **interface_ids:**  [Type: string] 
           - **lannetwork_ids:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 
           - **waninterface_ids:**  [Type: string] 
           - **wanoverlay_ids:**  [Type: string] 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elementsecurityzones/query".format(api_version,
                                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def elementusers(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create Element User

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **is_tenant_level:**  Type: boolean 
           - **login_id:**  Type: string 
           - **role:**  Type: string 
           - **tenant_id:**  Type: string 
           - **username:**  Type: string 

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

    def entitlements(self, operator_id, session_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Entitlements API Function

          **Parameters:**:

          - **operator_id**: Operator ID
          - **session_id**: User Session ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}/sessions/{}/actionservice/appportal/api/v1/entitlements".format(api_version,
                                                                                                                               tenant_id,
                                                                                                                               operator_id,
                                                                                                                               session_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicyrules(self, eventcorrelationpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create event correlation policyrule configuration

          **Parameters:**:

          - **eventcorrelationpolicyset_id**: Event Correlation Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **end_time:**  Type: integer 
           - **escalation_rules:**           
               - **flap_rule:**           
                   - **flap_duration:**  Type: integer 
                   - **flap_rate:**  Type: integer 
               - **standing_rule:**           
                   - **priority:**  Type: string 
                   - **standing_for:**  Type: integer 
           - **event_codes:**  [Type: string] 
           - **name:**  Type: string 
           - **priority:**  Type: string 
           - **resource_ids:**  [Type: string] 
           - **resource_type:**  Type: string 
           - **start_time:**  Type: integer 
           - **sub_resource_type:**  Type: string 
           - **suppress:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/{}/eventcorrelationpolicyrules".format(api_version,
                                                                                                                    tenant_id,
                                                                                                                    eventcorrelationpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicyrules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of event correlation policyrules that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **end_time:**  Type: integer 
           - **escalation_rules:**           
               - **flap_rule:**           
                   - **flap_duration:**  Type: integer 
                   - **flap_rate:**  Type: integer 
               - **standing_rule:**           
                   - **priority:**  Type: string 
                   - **standing_for:**  Type: integer 
           - **event_codes:**  [Type: string] 
           - **name:**  Type: string 
           - **policyset_id:**  Type: string 
           - **priority:**  Type: string 
           - **resource_ids:**  [Type: string] 
           - **resource_type:**  Type: string 
           - **start_time:**  Type: integer 
           - **sub_resource_type:**  Type: string 
           - **suppress:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicyrules/query".format(api_version,
                                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of event correlation policysets that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_policyset:**  Type: boolean 
           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **severity_priority_mapping:**           
               - **priority:**  Type: string 
               - **severity:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets".format(api_version,
                                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def eventcorrelationpolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of event correlation policysets that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **active_policyset:**  Type: boolean 
           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **severity_priority_mapping:**           
               - **priority:**  Type: string 
               - **severity:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/eventcorrelationpolicysets/query".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def events_query(self, data, tenant_id=None, api_version="v3.5"):
        """
        POST Events_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.5)

          **Payload Attributes:** 


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

    def events_summary(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Events_Summary API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/events/summary".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def externalcaconfigs(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Externalcaconfigs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/externalcaconfigs".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def fips_mode_change_operations(self, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Change Mode of an element from FIPS to Non-FIPS or vice-versa.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **parameters:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/{}/fips_mode_change_operations".format(api_version,
                                                                                                  tenant_id,
                                                                                                  element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def globalprefixfilters(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new global prefix filter.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **filters:**           
               - **type:**  Type: string 
           - **name:**  Type: string 

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

    def globalprefixfilters_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query DB for the list of params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/globalprefixfilters/query".format(api_version,
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

          **Payload Attributes:** 

           - **headend1_site_ids:**  [Type: string] 
           - **headend2_site_ids:**  [Type: string] 
           - **hub_element_id:**  Type: string 
           - **load_factors:**           
               - **alarm_threshold:**  Type: integer 
               - **allocated:**  Type: integer 
               - **subscription_factor:**  Type: number 
               - **threshold:**           
                   - **critical_alarm:**  Type: integer 
                   - **major_alarm:**  Type: integer 
                   - **subscription_factor:**  Type: number 
               - **type:**  Type: string 

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

          **Payload Attributes:** 

           - **admin_up:**  Type: boolean 
           - **load_alarm_threshold:**  Type: integer 
           - **name:**  Type: string 
           - **subscription_factor:**  Type: number 

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

    def interfaces(self, site_id, element_id, data, tenant_id=None, api_version="v4.12"):
        """
        Create a Interface

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.12)

          **Payload Attributes:** 

           - **admin_up:**  Type: boolean 
           - **attached_lan_networks:**           
               - **lan_network_id:**  Type: string 
               - **vlan_id:**  Type: integer 
           - **bound_interfaces:**  [Type: string] 
           - **bypass_pair:**           
               - **lan:**  Type: string 
               - **lan_state_propagation:**  Type: boolean 
               - **use_relay:**  Type: boolean 
               - **wan:**  Type: string 
           - **cellular_config:**           
               - **apn_config:**           
                   - **apn:**  Type: string 
                   - **authentication:**  Type: string 
                   - **clear_password:**  Type: boolean 
                   - **password:**  Type: string 
                   - **password_encrypted:**  Type: string 
                   - **user_name:**  Type: string 
               - **apn_etag:**  Type: integer 
               - **apnprofile_id:**  Type: string 
               - **auto_apn:**  Type: boolean 
               - **parent_module_id:**  Type: string 
               - **parent_sim_slot_number:**  Type: integer 
           - **description:**  Type: string 
           - **devicemgmt_policysetstack_id:**  Type: string 
           - **dhcp_relay:**           
               - **enabled:**  Type: boolean 
               - **option_82:**           
                   - **circuit_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **reforwarding_policy:**  Type: string 
                   - **remote_id:**  Type: string 
               - **server_ips:**  [Type: string] 
               - **source_interface:**  Type: string 
           - **directed_broadcast:**  Type: boolean 
           - **ethernet_port:**           
               - **full_duplex:**  Type: boolean 
               - **speed:**  Type: integer 
           - **ipfixcollectorcontext_id:**  Type: string 
           - **ipfixfiltercontext_id:**  Type: string 
           - **ipv4_config:**           
               - **dhcp_config:**           
                   - **client_id:**  Type: string 
                   - **hostname:**  Type: string 
               - **dns_v4_config:**           
                   - **name_servers:**  [Type: string] 
                   - **search:**  [Type: string] 
               - **pppoe_config:**           
                   - **chap_passwd:**  Type: string 
                   - **chap_user:**  Type: string 
                   - **set_route:**  Type: boolean 
               - **routes:**           
                   - **destination:**  Type: string 
                   - **via:**  Type: string 
               - **static_config:**           
                   - **address:**  Type: string 
               - **type:**  Type: string 
           - **ipv6_config:**           
               - **dhcp_config:**           
                   - **client_id:**  Type: string 
                   - **hostname:**  Type: string 
               - **dns_v6_config:**           
                   - **name_servers:**  [Type: string] 
                   - **search:**  [Type: string] 
               - **routes:**           
                   - **destination:**  Type: string 
                   - **via:**  Type: string 
               - **static_config:**           
                   - **address:**  Type: string 
               - **type:**  Type: string 
           - **mac_address:**  Type: string 
           - **mtu:**  Type: integer 
           - **multicast_config:**           
               - **igmp_version:**  Type: string 
               - **multicast_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **nat_address:**  Type: string 
           - **nat_address_v6:**  Type: string 
           - **nat_pools:**           
               - **ipv4_ranges:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **nat_pool_id:**  Type: string 
           - **nat_port:**  Type: integer 
           - **nat_port_v6:**  Type: integer 
           - **nat_zone_id:**  Type: string 
           - **network_context_id:**  Type: string 
           - **parent:**  Type: string 
           - **pppoe_config:**           
               - **host_uniq:**  Type: string 
               - **parent:**  Type: string 
               - **password:**  Type: string 
               - **reconnection_delay:**  Type: integer 
               - **service_name:**  Type: string 
               - **username:**  Type: string 
           - **scope:**  Type: string 
           - **secondary_ip_configs:**           
               - **ipv4_address:**  Type: string 
               - **scope:**  Type: string 
           - **service_link_config:**           
               - **gre_config:**           
                   - **csum:**  Type: boolean 
                   - **keepalive_enable:**  Type: boolean 
                   - **keepalive_fail_count:**  Type: integer 
                   - **keepalive_interval:**  Type: integer 
               - **ipsec_config:**           
                   - **authentication:**           
                       - **certificate:**  Type: string 
                       - **ikev1_params:**           
                           - **xauth_id:**  Type: string 
                           - **xauth_secret:**  Type: string 
                           - **xauth_secret_encrypted:**  Type: string 
                           - **xauth_secret_hash:**  Type: string 
                           - **xauth_type:**  Type: string 
                       - **local_ca_certificate:**  Type: string 
                       - **local_id:**  Type: string 
                       - **local_id_custom:**  Type: string 
                       - **passphrase:**  Type: string 
                       - **passphrase_encrypted:**  Type: string 
                       - **private_key:**  Type: string 
                       - **private_key_encrypted:**  Type: string 
                       - **remote_ca_certificate:**  Type: string 
                       - **remote_id:**  Type: string 
                       - **secret:**  Type: string 
                       - **secret_encrypted:**  Type: string 
                       - **secret_hash:**  Type: string 
                       - **type:**  Type: string 
                       - **x509Objects:**           
                           - **certHolder:**  Type: object 
                           - **certificate:**  Type: string 
                           - **is_local_ca_cert_set:**  Type: boolean 
                           - **is_remote_ca_cert_set:**  Type: boolean 
                           - **keyPair:**  Type: object 
                           - **local_ca_certificate:**  Type: string 
                           - **local_ca_certs_set:**  [Type: object] 
                           - **passphrase:**  Type: string 
                           - **private_key:**  Type: string 
                           - **remote_ca_certificate:**  Type: string 
                           - **remote_ca_certs_set:**  [Type: object] 
                   - **ipsec_profile_id:**  Type: string 
               - **last_parent:**  Type: string 
               - **parent:**  Type: string 
               - **peer:**           
                   - **hostname:**  Type: string 
                   - **ip_addresses:**  [Type: string] 
               - **service_endpoint_id:**  Type: string 
               - **type:**  Type: string 
           - **site_wan_interface_ids:**  [Type: string] 
           - **static_arp_configs:**           
               - **ipv4_address:**  Type: string 
               - **mac_address:**  Type: string 
           - **sub_interface:**           
               - **vlan_id:**  Type: integer 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **used_for:**  Type: string 

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

    def interfaces_correlationevents_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Interfaces_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/interfaces/correlationevents/query".format(api_version,
                                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def interfaces_query(self, data, tenant_id=None, api_version="v4.12"):
        """
        Queries db for limit number of interfaces that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.12)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/interfaces/query".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfix(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix Config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixprofile_id:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/ipfix".format(api_version,
                                                                                     tenant_id,
                                                                                     site_id,
                                                                                     element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfix_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix configs that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **element_id:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixprofile_id:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfix/query".format(api_version,
                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixcollectorcontexts(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix Collector context

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixcollectorcontexts_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix collector context that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixcollectorcontexts/query".format(api_version,
                                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixfiltercontexts(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix Filter context

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixfiltercontexts_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix filter context that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixfiltercontexts/query".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixglobalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix Global prefix

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixglobalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Ipfixglobalprefixes_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixglobalprefixes/query".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixlocalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix site prefix association that match query

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixprofiles(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix Profile

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **collector_config:**           
               - **host:**  Type: string 
               - **host_port:**  Type: integer 
               - **ipfixcollectorcontext_id:**  Type: string 
               - **max_message_size:**  Type: integer 
               - **protocol:**  Type: string 
           - **description:**  Type: string 
           - **export_cache_timeout:**  Type: integer 
           - **filters:**           
               - **app_def_ids:**  [Type: string] 
               - **dst_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **dst_prefixes_id:**  Type: string 
               - **ipfixfiltercontext_ids:**  [Type: string] 
               - **priority_traffic_types:**  [Type: string] 
               - **protocols:**  [Type: string] 
               - **rtp_transport_type:**  Type: string 
               - **src_ports:**           
                   - **end:**  Type: string 
                   - **start:**  Type: string 
               - **src_prefixes_id:**  Type: string 
               - **wan_path_direction:**  Type: string 
           - **ipfixtemplate_id:**  Type: string 
           - **name:**  Type: string 
           - **sampler:**           
               - **algorithm:**  Type: string 
               - **time_interval:**  Type: integer 
               - **time_spacing:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixprofiles_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix profiles that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixprofiles/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixtemplates(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix template

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **flow_fields:**  [Type: string] 
           - **generate_biflow:**  Type: boolean 
           - **name:**  Type: string 
           - **option_export_timeout:**  Type: integer 
           - **options:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **template_export_timeout:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipfixtemplates_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of ipfix templates that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixtemplates/query".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipsecprofiles(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new IPSEC Profile

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **authentication:**           
               - **certificate:**  Type: string 
               - **ikev1_params:**           
                   - **xauth_id:**  Type: string 
                   - **xauth_secret:**  Type: string 
                   - **xauth_secret_encrypted:**  Type: string 
                   - **xauth_secret_hash:**  Type: string 
                   - **xauth_type:**  Type: string 
               - **local_ca_certificate:**  Type: string 
               - **local_id:**  Type: string 
               - **local_id_custom:**  Type: string 
               - **passphrase:**  Type: string 
               - **passphrase_encrypted:**  Type: string 
               - **private_key:**  Type: string 
               - **private_key_encrypted:**  Type: string 
               - **remote_ca_certificate:**  Type: string 
               - **remote_id:**  Type: string 
               - **secret:**  Type: string 
               - **secret_encrypted:**  Type: string 
               - **secret_hash:**  Type: string 
               - **type:**  Type: string 
               - **x509Objects:**           
                   - **certHolder:**  Type: object 
                   - **certificate:**  Type: string 
                   - **is_local_ca_cert_set:**  Type: boolean 
                   - **is_remote_ca_cert_set:**  Type: boolean 
                   - **keyPair:**  Type: object 
                   - **local_ca_certificate:**  Type: string 
                   - **local_ca_certs_set:**  [Type: object] 
                   - **passphrase:**  Type: string 
                   - **private_key:**  Type: string 
                   - **remote_ca_certificate:**  Type: string 
                   - **remote_ca_certs_set:**  [Type: object] 
           - **description:**  Type: string 
           - **dpd_delay:**  Type: integer 
           - **dpd_enable:**  Type: boolean 
           - **dpd_timeout:**  Type: integer 
           - **esp_group:**           
               - **force_encapsulation:**  Type: boolean 
               - **lifetime:**  Type: integer 
               - **mode:**  Type: string 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
           - **ike_group:**           
               - **aggressive:**  Type: boolean 
               - **key_exchange:**  Type: string 
               - **lifetime:**  Type: integer 
               - **port:**  Type: integer 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
               - **reauth:**  Type: boolean 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ipsecprofiles_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of tenant level ipsec profiles that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **authentication:**           
               - **certificate:**  Type: string 
               - **ikev1_params:**           
                   - **xauth_id:**  Type: string 
                   - **xauth_secret:**  Type: string 
                   - **xauth_secret_encrypted:**  Type: string 
                   - **xauth_secret_hash:**  Type: string 
                   - **xauth_type:**  Type: string 
               - **local_ca_certificate:**  Type: string 
               - **local_id:**  Type: string 
               - **local_id_custom:**  Type: string 
               - **passphrase:**  Type: string 
               - **passphrase_encrypted:**  Type: string 
               - **private_key:**  Type: string 
               - **private_key_encrypted:**  Type: string 
               - **remote_ca_certificate:**  Type: string 
               - **remote_id:**  Type: string 
               - **secret:**  Type: string 
               - **secret_encrypted:**  Type: string 
               - **secret_hash:**  Type: string 
               - **type:**  Type: string 
               - **x509Objects:**           
                   - **certHolder:**  Type: object 
                   - **certificate:**  Type: string 
                   - **is_local_ca_cert_set:**  Type: boolean 
                   - **is_remote_ca_cert_set:**  Type: boolean 
                   - **keyPair:**  Type: object 
                   - **local_ca_certificate:**  Type: string 
                   - **local_ca_certs_set:**  [Type: object] 
                   - **passphrase:**  Type: string 
                   - **private_key:**  Type: string 
                   - **remote_ca_certificate:**  Type: string 
                   - **remote_ca_certs_set:**  [Type: object] 
           - **description:**  Type: string 
           - **dpd_delay:**  Type: integer 
           - **dpd_enable:**  Type: boolean 
           - **dpd_timeout:**  Type: integer 
           - **esp_group:**           
               - **force_encapsulation:**  Type: boolean 
               - **lifetime:**  Type: integer 
               - **mode:**  Type: string 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
           - **ike_group:**           
               - **aggressive:**  Type: boolean 
               - **key_exchange:**  Type: string 
               - **lifetime:**  Type: integer 
               - **port:**  Type: integer 
               - **proposals:**           
                   - **dh_groups:**  Type: string 
                   - **encryption:**  Type: string 
                   - **hash:**  Type: string 
               - **reauth:**  Type: boolean 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipsecprofiles/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def lannetworks(self, site_id, data, tenant_id=None, api_version="v3.1"):
        """
        Create a new LAN

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_config:**           
               - **default_routers:**  [Type: string] 
               - **dhcp_relay:**           
                   - **enabled:**  Type: boolean 
                   - **option_82:**           
                       - **circuit_id:**  Type: string 
                       - **enabled:**  Type: boolean 
                       - **reforwarding_policy:**  Type: string 
                       - **remote_id:**  Type: string 
                   - **server_ips:**  [Type: string] 
                   - **source_interface:**  Type: string 
               - **dhcp_server:**           
                   - **domain_name:**  Type: string 
                   - **domain_name_servers:**  [Type: string] 
                   - **ip_address_pool:**           
                       - **end:**  Type: string 
                       - **start:**  Type: string 
                   - **lease_expiry_time:**  Type: integer 
                   - **lease_renew_time:**  Type: integer 
               - **prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 

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

    def lannetworks_query(self, data, tenant_id=None, api_version="v3.1"):
        """
        Query db for Site LAN networks that match query parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_config:**           
               - **default_routers:**  [Type: string] 
               - **dhcp_relay:**           
                   - **enabled:**  Type: boolean 
                   - **option_82:**           
                       - **circuit_id:**  Type: string 
                       - **enabled:**  Type: boolean 
                       - **reforwarding_policy:**  Type: string 
                       - **remote_id:**  Type: string 
                   - **server_ips:**  [Type: string] 
                   - **source_interface:**  Type: string 
               - **dhcp_server:**           
                   - **domain_name:**  Type: string 
                   - **domain_name_servers:**  [Type: string] 
                   - **ip_address_pool:**           
                       - **end:**  Type: string 
                       - **start:**  Type: string 
                   - **lease_expiry_time:**  Type: integer 
                   - **lease_renew_time:**  Type: integer 
               - **prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/lannetworks/query".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def localprefixfilters(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new local prefix filter.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

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

    def localprefixfilters_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query DB for the list of params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/localprefixfilters/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def login(self, data, api_version="v2.0"):
        """
        Login api

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/login".format(api_version)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data, sensitive=True)

    def machine_upgrade_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Machine Upgrade Config

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machine_upgrade/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def machines_query(self, data, tenant_id=None, api_version="v2.2"):
        """
        Query and get machines of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **pki_op:**           - **renew_state:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

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

    def monitor_aggregates(self, data, tenant_id=None, api_version="v3.0"):
        """
        POST Monitor_Aggregates API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 


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
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_aggregates_healthscore(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Healthscore API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates/healthscore".format(api_version,
                                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_aggregates_multicast_mroute(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Multicast_Mroute API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates/multicast/mroute".format(api_version,
                                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_aggregates_multicast_wan_neighbor(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Aggregates_Multicast_Wan_Neighbor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/aggregates/multicast/wan_neighbor".format(api_version,
                                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_bulk_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Bulk_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/bulk_metrics".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_cellular_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Cellular_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


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
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_cellular_metrics_topn(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Cellular_Metrics_Topn API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/cellular_metrics/topn".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_flows(self, data, tenant_id=None, api_version="v3.6"):
        """
        POST Monitor_Flows API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.6)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/flows".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_insights(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Insights API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/insights".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_insightslist(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Insightslist API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/insightslist".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_lqm_point_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Lqm_Point_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/lqm_point_metrics".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_metrics(self, data, tenant_id=None, api_version="v2.2"):
        """
        POST Monitor_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/metrics".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_network_point_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/network_point_metrics".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_network_point_metrics_bw(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics_Bw API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/network_point_metrics_bw".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_network_point_metrics_hs(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Network_Point_Metrics_Hs API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/network_point_metrics_hs".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_object_stats(self, data, tenant_id=None, api_version="v2.3"):
        """
        POST Monitor_Object_Stats API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 


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
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_qos_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Qos_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


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
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_sys_metrics(self, data, tenant_id=None, api_version="v2.1"):
        """
        POST Monitor_Sys_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 


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
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_sys_metrics_topn(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Topn_Sys_Metrics_Monitor API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/sys_metrics/topn".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_sys_point_metrics(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Monitor_Sys_Point_Metrics API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/sys_point_metrics".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def monitor_topn(self, data, tenant_id=None, api_version="v3.1"):
        """
        POST Monitor_Topn API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.cdl_url

        url = str(cur_ctlr) + "/{}/api/tenants/{}/monitor/topn".format(api_version,
                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastdynamicrps_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Multicastdynamicrps_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastdynamicrps/query".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastigmpmemberships_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Multicastigmpmemberships_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastigmpmemberships/query".format(api_version,
                                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastpeergroups(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Multicastpeergroups API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastpeergroups".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastroutes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Multicast route table

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **element_id:**  Type: string 
           - **mroutes:**           
               - **element_rp:**  Type: boolean 
               - **flags:**  Type: string 
               - **group:**  Type: string 
               - **incoming_interface:**  Type: string 
               - **outgoing_interfaces:**  [Type: string] 
               - **rp_address:**  Type: string 
               - **source:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastroutes/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastrps(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Creates Multicast RP config

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **groups:**           
               - **ipv4_prefix:**  Type: string 
               - **is_active_rp:**  Type: boolean 
           - **ipv4_address:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/multicastrps".format(api_version,
                                                                                            tenant_id,
                                                                                            site_id,
                                                                                            element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastrps_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Multicastrps_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastrps/query".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicaststatus_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Multicast status information

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **address:**  Type: string 
           - **element_id:**  Type: string 
           - **interface_id:**  Type: string 
           - **name:**  Type: string 
           - **pim_neighbors:**           
               - **address:**  Type: string 
               - **dr:**  Type: boolean 
               - **dr_prio:**  Type: string 
               - **expires:**  Type: string 
               - **uptime:**  Type: string 
           - **site_id:**  Type: string 
           - **state:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicaststatus/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def multicastwanstatus_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Multicastwanstatus_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/multicastwanstatus/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natglobalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NAT global prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natglobalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Global Prefixes.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natglobalprefixes/query".format(api_version,
                                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natlocalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NAT local prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natlocalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query site local prefixes.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natlocalprefixes/query".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicypools(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NATPolicy Pool.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicypools_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query NAT policy pools.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicypools/query".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicyrules(self, natpolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NAT Policy Rule

          **Parameters:**:

          - **natpolicyset_id**: NAT Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **actions:**           
               - **nat_pool_id:**  Type: string 
               - **port:**  Type: integer 
               - **protocols:**  [Type: string] 
               - **type:**  Type: string 
           - **description:**  Type: string 
           - **destination_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **destination_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **destination_prefixes_id:**  Type: string 
           - **destination_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **destination_zone_id:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **enabled:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **natpolicypools:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **policyset_id:**  Type: string 
           - **protocol:**  Type: integer 
           - **region:**  Type: string 
           - **source_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **source_prefixes:**           
               - **description:**  Type: string 
               - **id:**  Type: string 
               - **ipv4_prefixes:**  [Type: string] 
               - **name:**  Type: string 
               - **tags:**  [Type: string] 
           - **source_prefixes_id:**  Type: string 
           - **source_zone:**           
               - **default_for_public_interfaces:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **region:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **source_zone_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/{}/natpolicyrules".format(api_version,
                                                                                          tenant_id,
                                                                                          natpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicyrules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query NAT policy rules.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **actions:**           
               - **nat_pool_id:**  Type: string 
               - **port:**  Type: integer 
               - **protocols:**  [Type: string] 
               - **type:**  Type: string 
           - **description:**  Type: string 
           - **destination_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **destination_prefixes_id:**  Type: string 
           - **destination_zone_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_id:**  Type: string 
           - **protocol:**  Type: integer 
           - **source_ports:**           
               - **from:**  Type: integer 
               - **to:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **source_zone_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicyrules/query".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NAT Policy Set

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **destination_zone_policyrule_order:**  [Type: string] 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **policy_req_version:**  Type: string 
           - **policy_rules:**           
               - **actions:**           
                   - **nat_pool_id:**  Type: string 
                   - **port:**  Type: integer 
                   - **protocols:**  [Type: string] 
                   - **type:**  Type: string 
               - **description:**  Type: string 
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **destination_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **destination_prefixes_id:**  Type: string 
               - **destination_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **destination_zone_id:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **natpolicypools:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **policyset_id:**  Type: string 
               - **protocol:**  Type: integer 
               - **region:**  Type: string 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **source_prefixes:**           
                   - **description:**  Type: string 
                   - **id:**  Type: string 
                   - **ipv4_prefixes:**  [Type: string] 
                   - **name:**  Type: string 
                   - **tags:**  [Type: string] 
               - **source_prefixes_id:**  Type: string 
               - **source_zone:**           
                   - **default_for_public_interfaces:**  Type: boolean 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **source_zone_id:**  Type: string 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **source_zone_policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 
           - **update_order:**  Type: boolean 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query policy sets.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **description:**  Type: string 
           - **destination_zone_policyrule_order:**  [Type: string] 
           - **name:**  Type: string 
           - **source_zone_policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysets/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysetstacks(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NATPolicySet Stack

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natpolicysetstacks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query policyset stacks.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natpolicysetstacks/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natzones(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Nat Policy Zone.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_for_public_interfaces:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones".format(api_version,
                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def natzones_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query NAT policy zones.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_for_public_interfaces:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/natzones/query".format(api_version,
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

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

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

    def networkcontexts_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of network contexts that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkcontexts/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyglobalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new global prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes".format(api_version,
                                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyglobalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Network Global Prefixes.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyglobalprefixes/query".format(api_version,
                                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicylocalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query site network prefix association.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes/query".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyrules(self, networkpolicyset_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new NetworkPolicyRule

          **Parameters:**:

          - **networkpolicyset_id**: Network Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/{}/networkpolicyrules".format(api_version,
                                                                                                  tenant_id,
                                                                                                  networkpolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicyrules_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Query Network policy rules.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **policyset_id:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicyrules/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NetworkPolicySet

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **name:**  Type: string 
           - **policy_req_version:**  Type: string 
           - **policy_rules:**           
               - **app_def_ids:**  [Type: string] 
               - **description:**  Type: string 
               - **destination_prefixes_id:**  Type: string 
               - **enabled:**  Type: boolean 
               - **id:**  Type: string 
               - **name:**  Type: string 
               - **network_context_id:**  Type: string 
               - **order_number:**  Type: integer 
               - **paths_allowed:**           
                   - **active_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
                   - **backup_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
                   - **l3_failure_paths:**           
                       - **label:**  Type: string 
                       - **path_type:**  Type: string 
               - **service_context:**           
                   - **active_service_label_id:**  Type: string 
                   - **active_service_label_type:**  Type: string 
                   - **backup_service_label_id:**  Type: string 
                   - **backup_service_label_type:**  Type: string 
                   - **type:**  Type: string 
               - **source_prefixes_id:**  Type: string 
               - **tags:**  [Type: string] 
           - **region:**  Type: string 
           - **send_to_element:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Network policy sets.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysets/query".format(api_version,
                                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysetstacks(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NetworkPolicySetStack

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset:**           
               - **clone_from:**  Type: string 
               - **defaultrule_policyset:**  Type: boolean 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_req_version:**  Type: string 
               - **policy_rules:**           
                   - **app_def_ids:**  [Type: string] 
                   - **description:**  Type: string 
                   - **destination_prefixes_id:**  Type: string 
                   - **enabled:**  Type: boolean 
                   - **id:**  Type: string 
                   - **name:**  Type: string 
                   - **network_context_id:**  Type: string 
                   - **order_number:**  Type: integer 
                   - **paths_allowed:**           
                       - **active_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **backup_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                       - **l3_failure_paths:**           
                           - **label:**  Type: string 
                           - **path_type:**  Type: string 
                   - **service_context:**           
                       - **active_service_label_id:**  Type: string 
                       - **active_service_label_type:**  Type: string 
                       - **backup_service_label_id:**  Type: string 
                       - **backup_service_label_type:**  Type: string 
                       - **type:**  Type: string 
                   - **source_prefixes_id:**  Type: string 
                   - **tags:**  [Type: string] 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **legacy_policystack:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **policysets:**           
               - **clone_from:**  Type: string 
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **name:**  Type: string 
               - **policy_rules:**           
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **name:**  Type: string 
                   - **policyset_id:**  Type: string 
                   - **region:**  Type: string 
                   - **tags:**  [Type: string] 
                   - **tenant_id:**  Type: string 
               - **region:**  Type: string 
               - **send_to_element:**  Type: boolean 
               - **tags:**  [Type: string] 
               - **tenant_id:**  Type: string 
           - **region:**  Type: string 
           - **tags:**  [Type: string] 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networkpolicysetstacks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query network policyset stacks.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicysetstacks/query".format(api_version,
                                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def networks_bulk_config_state_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Get all config/state info for given network from NB

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networks/bulk_config_state/query".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyglobalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create an Security Policy V2 Global Prefix

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicyglobalprefixes".format(api_version,
                                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyglobalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Security Policy V2 Global Prefixes of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicyglobalprefixes/query".format(api_version,
                                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicylocalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create an Security Policy V2 Local Prefix

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicylocalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query security policy v2 local prefix site associations of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicylocalprefixes/query".format(api_version,
                                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyrules(self, ngfwsecuritypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Security Policy V2 Rule under a policy set

          **Parameters:**:

          - **ngfwsecuritypolicyset_id**: NGFW Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefix_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **services:**           
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **protocol:**  Type: integer 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
           - **source_prefix_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets/{}/ngfwsecuritypolicyrules".format(api_version,
                                                                                                            tenant_id,
                                                                                                            ngfwsecuritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicyrules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query security policy v2 rules of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefix_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **policyset_id:**  Type: string 
           - **services:**           
               - **destination_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
               - **protocol:**  Type: integer 
               - **source_ports:**           
                   - **from:**  Type: integer 
                   - **to:**  Type: integer 
           - **source_prefix_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicyrules/query".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Security Policy V2 Set

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query security policy v2 sets of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **clone_from:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysets/query".format(api_version,
                                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysetstacks(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Security Policy V2 Set Stack

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysetstacks".format(api_version,
                                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ngfwsecuritypolicysetstacks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Security Policy V2 Set stacks of a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ngfwsecuritypolicysetstacks/query".format(api_version,
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

          **Payload Attributes:** 

           - **challenge_phrase:**  Type: string 
           - **response_phrase:**  Type: string 

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

    def password_change(self, data, tenant_id=None, api_version="v2.0"):
        """
        Allows one to change password

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **oldPassword:**  Type: string 
           - **password:**  Type: string 
           - **repeatPassword:**  Type: string 

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

    def pathgroups(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create a Path Group for a tenant.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **paths:**           
               - **label:**  Type: string 
               - **path_type:**  Type: string 

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

    def pathgroups_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of network contexts that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **paths:**           
               - **label:**  Type: string 
               - **path_type:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/pathgroups/query".format(api_version,
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

          **Payload Attributes:** 

           - **app_def_id:**  Type: string 
           - **app_def_name:**  Type: string 
           - **default_rule:**  Type: boolean 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **lan_network_ids:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_num:**  Type: integer 
           - **region:**  Type: string 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 
           - **site_paths_allowed:**           
               - **wn_name:**  Type: string 
               - **wp_type:**  Type: string 
           - **tenant_id:**  Type: string 

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

    def policyrules_query(self, data, tenant_id=None, api_version="v3.1"):
        """
        Queries db for policyrules that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **app_def_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **paths_allowed:**           
               - **active_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **backup_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
               - **l3_failure_paths:**           
                   - **label:**  Type: string 
                   - **path_type:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_num:**  Type: integer 
           - **service_context:**           
               - **active_service_label_id:**  Type: string 
               - **active_service_label_type:**  Type: string 
               - **backup_service_label_id:**  Type: string 
               - **backup_service_label_type:**  Type: string 
               - **type:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policyrules/query".format(api_version,
                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policysets(self, data, tenant_id=None, api_version="v3.0"):
        """
        Create a new Policy Set

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_num:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **default_policy:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 

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

    def policysets_bulk_config_state_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Get all config/state info across all policysets from NB

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/policysets/bulk_config_state/query".format(api_version,
                                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def policysets_query(self, data, tenant_id=None, api_version="v3.0"):
        """
        Queries db for policysets that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_num:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **default_policy:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 

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

    def prefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Prefixes_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prefixes/query".format(api_version,
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

          **Payload Attributes:** 

           - **filters:**           
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 

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

          **Payload Attributes:** 

           - **query_params:**           
               - **zone_id:**  Type: string 

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

    def prioritypolicyglobalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new global prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes".format(api_version,
                                                                                       tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicyglobalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Priority Global Prefixes.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyglobalprefixes/query".format(api_version,
                                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicylocalprefixes_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query site priority prefix association.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes/query".format(api_version,
                                                                                            tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicyrules(self, prioritypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new PriorityPolicyRule

          **Parameters:**:

          - **prioritypolicyset_id**: Priority Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **dscp:**           
               - **value:**  Type: integer 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **priority_number:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/{}/prioritypolicyrules".format(api_version,
                                                                                                    tenant_id,
                                                                                                    prioritypolicyset_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicyrules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Priority policy rules.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **app_def_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_prefixes_id:**  Type: string 
           - **dscp:**           
               - **value:**  Type: integer 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **order_number:**  Type: integer 
           - **policyset_id:**  Type: string 
           - **priority_number:**  Type: integer 
           - **source_prefixes_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicyrules/query".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new PriorityPolicySet

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_number:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **clone_from:**  Type: string 
           - **default_rule_dscp_mappings:**           
               - **dscp:**  [Type: integer] 
               - **priority_number:**  Type: integer 
               - **transfer_type:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **template:**  Type: boolean 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Priority policy sets.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **bandwidth_allocation_schemes:**           
               - **bandwidth_range:**           
                   - **high:**  Type: number 
                   - **low:**  Type: number 
               - **business_priorities:**           
                   - **bandwidth_allocation:**  Type: number 
                   - **bandwidth_split_per_type:**           
                       - **bulk:**  Type: number 
                       - **rt_audio:**  Type: number 
                       - **rt_video:**  Type: number 
                       - **transactional:**  Type: number 
                   - **priority_number:**  Type: integer 
           - **business_priority_names:**           
               - **priority_name:**  Type: string 
               - **priority_num:**  Type: integer 
           - **clone_from:**  Type: string 
           - **default_rule_dscp_mappings:**           
               - **dscp:**  [Type: integer] 
               - **priority_number:**  Type: integer 
               - **transfer_type:**  Type: string 
           - **defaultrule_policyset:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **template:**  Type: boolean 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysets/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysetstacks(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new PriorityPolicySetStack

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks".format(api_version,
                                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prioritypolicysetstacks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query priority policyset stacks.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_policysetstack:**  Type: boolean 
           - **defaultrule_policyset_id:**  Type: string 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyset_ids:**  [Type: string] 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicysetstacks/query".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismaaccess_configs(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a Prisma Access Config with remote networks and security processing node

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **remote_networks:**           
               - **remote_network_names:**  [Type: string] 
               - **spn_name:**  Type: string 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prismaaccess_configs".format(api_version,
                                                                                        tenant_id,
                                                                                        site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def prismaaccess_configs_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Prisma Access config

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **remote_networks:**           
               - **remote_network_names:**  [Type: string] 
               - **spn_name:**  Type: string 
           - **site_id:**  Type: string 
           - **tenant_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prismaaccess_configs/query".format(api_version,
                                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def recovery_tokens(self, machine_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create a Recovery Token for Fips change mode

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **hardware_id:**  Type: string 
           - **ion_token:**  Type: string 
           - **is_used:**  Type: boolean 
           - **secret_token:**  Type: string 
           - **token_validity_in_hour:**  Type: integer 
           - **valid_till_secs:**  Type: integer 

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
        return self._parent_class.rest_call(url, "post", data=data)

    def reports_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Reports_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/reports/query".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def reportsdir_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Reportsdir_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/reportsdir/query".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def roles(self, data, tenant_id=None, api_version="v2.1"):
        """
        Add a custom role

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **custom_permissions:**           
               - **allowed_after_ms:**  Type: integer 
               - **allowed_before_ms:**  Type: integer 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **disallow_permission:**  Type: boolean 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **region:**  Type: string 
               - **tenant_id:**  Type: string 
               - **value:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permissions:**           
               - **value:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **is_system_owned:**  Type: boolean 
           - **name:**  Type: string 
           - **permissions:**           
               - **value:**  Type: string 
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **tenant_id:**  Type: string 

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

    def routing_aspathaccesslists(self, site_id, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create AS-Path Access List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **as_path_regex_list:**           
               - **as_path_regex:**  Type: string 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists".format(api_version,
                                                                                                         tenant_id,
                                                                                                         site_id,
                                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_aspathaccesslists_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of access lists that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **as_path_regex_list:**           
               - **as_path_regex:**  Type: string 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_aspathaccesslists/query".format(api_version,
                                                                                                               tenant_id,
                                                                                                               site_id,
                                                                                                               element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_ipcommunitylists(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create IP Community List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **community_list:**           
               - **community_str:**  Type: string 
               - **permit:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists".format(api_version,
                                                                                                        tenant_id,
                                                                                                        site_id,
                                                                                                        element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_ipcommunitylists_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of community lists that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **community_list:**           
               - **community_str:**  Type: string 
               - **permit:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_ipcommunitylists/query".format(api_version,
                                                                                                              tenant_id,
                                                                                                              site_id,
                                                                                                              element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_prefixlists(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create IP Prefix List

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **prefix_filter_list:**           
               - **ge:**  Type: integer 
               - **le:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **prefix:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists".format(api_version,
                                                                                                   tenant_id,
                                                                                                   site_id,
                                                                                                   element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_prefixlists_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of prefix lists that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **prefix_filter_list:**           
               - **ge:**  Type: integer 
               - **le:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **prefix:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_prefixlists/query".format(api_version,
                                                                                                         tenant_id,
                                                                                                         site_id,
                                                                                                         element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_routemaps(self, site_id, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create Route Map

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **route_map_entries:**           
               - **continue_entry:**  Type: string 
               - **match:**           
                   - **as_path_id:**  Type: string 
                   - **community_list_id:**  Type: string 
                   - **ip_next_hop_id:**  Type: string 
                   - **ip_prefix_list_id:**  Type: string 
                   - **tag:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **set:**           
                   - **as_path_prepend:**  Type: string 
                   - **community:**  Type: string 
                   - **ip_next_hop:**  Type: string 
                   - **local_preference:**  Type: integer 
                   - **tag:**  Type: integer 
                   - **weight:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps".format(api_version,
                                                                                                 tenant_id,
                                                                                                 site_id,
                                                                                                 element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def routing_routemaps_query(self, site_id, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of route maps that match query params.

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **auto_generated:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **route_map_entries:**           
               - **continue_entry:**  Type: string 
               - **match:**           
                   - **as_path_id:**  Type: string 
                   - **community_list_id:**  Type: string 
                   - **ip_next_hop_id:**  Type: string 
                   - **ip_prefix_list_id:**  Type: string 
                   - **tag:**  Type: integer 
               - **order:**  Type: integer 
               - **permit:**  Type: boolean 
               - **set:**           
                   - **as_path_prepend:**  Type: string 
                   - **community:**  Type: string 
                   - **ip_next_hop:**  Type: string 
                   - **local_preference:**  Type: integer 
                   - **tag:**  Type: integer 
                   - **weight:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/routing_routemaps/query".format(api_version,
                                                                                                       tenant_id,
                                                                                                       site_id,
                                                                                                       element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def rquery(self, data, tenant_id=None, api_version="v3.1"):
        """
        Query and get ESP machines across regions

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/machines/rquery".format(api_version,
                                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def sdwanapps_configs(self, sdwanapp_id, data, tenant_id=None, api_version="v2.0"):
        """
        POST Sdwanapps_Configs API Function

          **Parameters:**:

          - **sdwanapp_id**: SDWAN Application ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sdwanapps/{}/configs".format(api_version,
                                                                               tenant_id,
                                                                               sdwanapp_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicyruleorder(self, securitypolicyset_id, data, tenant_id=None, api_version="v2.0"):
        """
        Update a tenant security policy set.

          **Parameters:**:

          - **securitypolicyset_id**: Security Policy Set ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

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

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **application_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_filter_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **disabled_flag:**  Type: boolean 
           - **name:**  Type: string 
           - **source_filter_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 

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

    def securitypolicyrules_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of LAN networks that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **application_ids:**  [Type: string] 
           - **description:**  Type: string 
           - **destination_filter_ids:**  [Type: string] 
           - **destination_zone_ids:**  [Type: string] 
           - **disabled_flag:**  Type: boolean 
           - **name:**  Type: string 
           - **security_policyset_id:**  Type: string 
           - **source_filter_ids:**  [Type: string] 
           - **source_zone_ids:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicyrules/query".format(api_version,
                                                                                    tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def securitypolicysets(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new tenant security policy set.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

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

    def securitypolicysets_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of security policysets that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **policyrule_order:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securitypolicysets/query".format(api_version,
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

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

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

    def securityzones_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of security zones that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/securityzones/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicebindingmaps(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new Service Binding Map

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **is_default:**  Type: boolean 
           - **name:**  Type: string 
           - **service_bindings:**           
               - **service_endpoint_ids:**  [Type: string] 
               - **service_label_id:**  Type: string 
           - **tags:**  [Type: string] 

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

    def servicebindingmaps_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of service bindings that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **is_default:**  Type: boolean 
           - **name:**  Type: string 
           - **service_bindings:**           
               - **service_endpoint_ids:**  [Type: string] 
               - **service_label_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicebindingmaps/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def serviceendpoints(self, data, tenant_id=None, api_version="v2.3"):
        """
        Create a new Service Endpoint

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_up:**  Type: boolean 
           - **allow_enterprise_traffic:**  Type: boolean 
           - **description:**  Type: string 
           - **liveliness_probe:**           
               - **http:**           
                   - **failure_count:**  Type: integer 
                   - **http_status_codes:**  [Type: integer] 
                   - **interval:**  Type: integer 
                   - **url:**  Type: string 
               - **icmp_ping:**           
                   - **failure_count:**  Type: integer 
                   - **interval:**  Type: integer 
                   - **ip_addresses:**  [Type: string] 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **sase_properties:**           
               - **allocated_bandwidth_mbps:**  Type: integer 
               - **pa_compute_region_oid:**  Type: string 
           - **service_link_peers:**           
               - **hostnames:**  [Type: string] 
               - **ip_addresses:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

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

    def serviceendpoints_query(self, data, tenant_id=None, api_version="v2.3"):
        """
        Queries db for limit number of service bindings that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.3)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_up:**  Type: boolean 
           - **allow_enterprise_traffic:**  Type: boolean 
           - **description:**  Type: string 
           - **liveliness_probe:**           
               - **http:**           
                   - **failure_count:**  Type: integer 
                   - **http_status_codes:**  [Type: integer] 
                   - **interval:**  Type: integer 
                   - **url:**  Type: string 
               - **icmp_ping:**           
                   - **failure_count:**  Type: integer 
                   - **interval:**  Type: integer 
                   - **ip_addresses:**  [Type: string] 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **sase_properties:**           
               - **allocated_bandwidth_mbps:**  Type: integer 
               - **pa_compute_region_oid:**  Type: string 
           - **service_link_peers:**           
               - **hostnames:**  [Type: string] 
               - **ip_addresses:**  [Type: string] 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/serviceendpoints/query".format(api_version,
                                                                                 tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def servicelabels(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new Service Label

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **sase_properties:**           
               - **active_sase_label:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

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

    def servicelabels_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Queries db for limit number of service labels that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/servicelabels/query".format(api_version,
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

          **Payload Attributes:** 

           - **addresses:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **custom_roles:**           
               - **custom_permissions:**           
                   - **allowed_after_ms:**  Type: integer 
                   - **allowed_before_ms:**  Type: integer 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **disallow_permission:**  Type: boolean 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **value:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **name:**  Type: string 
               - **permissions:**           
                   - **value:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
           - **email:**  Type: string 
           - **enable_session_ip_lock:**  Type: boolean 
           - **first_name:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **last_name:**  Type: string 
           - **logout_others:**  Type: boolean 
           - **name:**  Type: string 
           - **password:**  Type: string 
           - **phone_numbers:**           
               - **country_code:**  Type: integer 
               - **local_extension:**  Type: integer 
               - **number:**  Type: integer 
               - **types:**           
                   - **value:**  Type: string 
           - **repeatPassword:**  Type: string 
           - **requestId:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **secondary_emails:**           
               - **email:**  Type: string 

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

    def site_bulk_config_state_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Get site config/state info for queried site from NB

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **count:**  Type: integer 
           - **items:**  [Type: object] 
           - **tenant_id:**  Type: string 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/bulk_config_state/query".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_correlationevents_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Site_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/correlationevents/query".format(api_version,
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

          **Payload Attributes:** 

           - **conf:**  Type: object 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

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

    def site_extensions_query(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Query site level extensions that match query params

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

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

    def site_ipfixlocalprefixes(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix site prefix association

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ipfixlocalprefixes".format(api_version,
                                                                                      tenant_id,
                                                                                      site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_lannetworks_query(self, site_id, data, tenant_id=None, api_version="v3.1"):
        """
        Query LAN networks that match query params

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **ipv4_config:**           
               - **default_routers:**  [Type: string] 
               - **dhcp_relay:**           
                   - **enabled:**  Type: boolean 
                   - **option_82:**           
                       - **circuit_id:**  Type: string 
                       - **enabled:**  Type: boolean 
                       - **reforwarding_policy:**  Type: string 
                       - **remote_id:**  Type: string 
                   - **server_ips:**  [Type: string] 
                   - **source_interface:**  Type: string 
               - **dhcp_server:**           
                   - **domain_name:**  Type: string 
                   - **domain_name_servers:**  [Type: string] 
                   - **ip_address_pool:**           
                       - **end:**  Type: string 
                       - **start:**  Type: string 
                   - **lease_expiry_time:**  Type: integer 
                   - **lease_renew_time:**  Type: integer 
               - **prefixes:**  [Type: string] 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 

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

    def site_natlocalprefixes(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and NAT Prefix.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/natlocalprefixes".format(api_version,
                                                                                    tenant_id,
                                                                                    site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_networkpolicylocalprefixes(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and Network local Prefix.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/networkpolicylocalprefixes".format(api_version,
                                                                                              tenant_id,
                                                                                              site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_ngfwsecuritypolicylocalprefixes(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create a security policy V2 local prefix site association

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/ngfwsecuritypolicylocalprefixes".format(api_version,
                                                                                                   tenant_id,
                                                                                                   site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_prioritypolicylocalprefixes(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and Priority local Prefix.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ipv4_prefixes:**  [Type: string] 
           - **prefix_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def site_query(self, data, tenant_id=None, api_version="v4.5"):
        """
        Queries db for limit number of sites that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.5)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_state:**  Type: string 
           - **description:**  Type: string 
           - **element_cluster_role:**  Type: string 
           - **extended_tags:**           
               - **key:**  Type: string 
               - **value:**  Type: string 
               - **value_type:**  Type: string 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **security_policyset_id:**  Type: string 
           - **service_binding:**  Type: string 
           - **tags:**  [Type: string] 

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

    def sites(self, data, tenant_id=None, api_version="v4.7"):
        """
        Create a site

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v4.7)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **admin_state:**  Type: string 
           - **description:**  Type: string 
           - **element_cluster_role:**  Type: string 
           - **extended_tags:**           
               - **key:**  Type: string 
               - **value:**  Type: string 
               - **value_type:**  Type: string 
           - **location:**           
               - **description:**  Type: string 
               - **latitude:**  Type: number 
               - **longitude:**  Type: number 
           - **multicast_peer_group_id:**  Type: string 
           - **name:**  Type: string 
           - **nat_policysetstack_id:**  Type: string 
           - **network_policysetstack_id:**  Type: string 
           - **policy_set_id:**  Type: string 
           - **priority_policysetstack_id:**  Type: string 
           - **security_policyset_id:**  Type: string 
           - **security_policysetstack_id:**  Type: string 
           - **service_binding:**  Type: string 
           - **tags:**  [Type: string] 

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

    def sitesecurityzones(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create an association between site and security zone.

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **networks:**           
               - **network_id:**  Type: string 
               - **network_type:**  Type: string 
           - **zone_id:**  Type: string 

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

    def sitesecurityzones_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query security zone for NB API.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **networks:**           
               - **network_id:**  Type: string 
               - **network_type:**  Type: string 
           - **zone_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sitesecurityzones/query".format(api_version,
                                                                                  tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def snmpagents(self, site_id, element_id, data, tenant_id=None, api_version="v2.1"):
        """
        Create SNMP Agent

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **system_contact:**  Type: string 
           - **system_location:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
               - **enabled:**  Type: boolean 
           - **v3_config:**           
               - **user_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 

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

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enabled:**  Type: boolean 
           - **server_ip:**  Type: string 
           - **source_interface:**  Type: string 
           - **tags:**  [Type: string] 
           - **v2_config:**           
               - **community:**  Type: string 
               - **enabled:**  Type: boolean 
           - **v3_config:**           
               - **user_access:**           
                   - **auth_phrase:**  Type: string 
                   - **auth_type:**  Type: string 
                   - **enc_phrase:**  Type: string 
                   - **enc_type:**  Type: string 
                   - **engine_id:**  Type: string 
                   - **security_level:**  Type: string 
                   - **user_name:**  Type: string 
           - **version:**  Type: string 

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

    def software_current_status_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Get the current image status of all the element

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/software/current_status/query".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def software_state_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Software_State_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/software/state/query".format(api_version,
                                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def software_status_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Query the software upgrade status of all tenant elements

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **active_image_id:**  Type: string 
           - **active_version:**  Type: string 
           - **download_interval:**  Type: integer 
           - **download_percent:**  Type: integer 
           - **element_id:**  Type: string 
           - **failure_info:**  Type: string 
           - **previous_image_id:**  Type: string 
           - **rollback_version:**  Type: string 
           - **scheduled_download:**  Type: string 
           - **scheduled_upgrade:**  Type: string 
           - **upgrade_image_id:**  Type: string 
           - **upgrade_interval:**  Type: integer 
           - **upgrade_state:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/software/status/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def softwarehistory_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for all software download done by a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/softwarehistory/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters(self, site_id, data, tenant_id=None, api_version="v2.0"):
        """
        Create Spoke Cluster

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **advertisement_interval:**  Type: number 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **preempt:**  Type: boolean 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters".format(api_version,
                                                                                 tenant_id,
                                                                                 site_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters_ops(self, site_id, spokecluster_id, data, tenant_id=None, api_version="v2.0"):
        """
        Handle operations on spokecluster.

          **Parameters:**:

          - **site_id**: Site ID
          - **spokecluster_id**: Spoke Cluster ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/spokeclusters/{}/operations".format(api_version,
                                                                                               tenant_id,
                                                                                               site_id,
                                                                                               spokecluster_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def spokeclusters_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Spoke Clusters.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **advertisement_interval:**  Type: number 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **preempt:**  Type: boolean 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/spokeclusters/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def staticroutes(self, site_id, element_id, data, tenant_id=None, api_version="v2.2"):
        """
        Create static route

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **address_family:**  Type: string 
           - **description:**  Type: string 
           - **destination_prefix:**  Type: string 
           - **name:**  Type: string 
           - **network_context_id:**  Type: string 
           - **nexthop_reachability_probe:**  Type: boolean 
           - **nexthops:**           
               - **admin_distance:**  Type: integer 
               - **nexthop_interface_id:**  Type: string 
               - **nexthop_ip:**  Type: string 
               - **self:**  Type: boolean 
           - **scope:**  Type: string 
           - **tags:**  [Type: string] 

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

    def status_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query and get element status objects for a tenant

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/elements/status/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def syslogserverprofiles(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create Syslog Server Profile

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_flow_logging:**  Type: boolean 
           - **name:**  Type: string 
           - **protocol:**  Type: string 
           - **remote_ca_certificate:**  Type: string 
           - **server_fqdn:**  Type: string 
           - **server_ip:**  Type: string 
           - **server_port:**  Type: integer 
           - **severity_level:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/syslogserverprofiles".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def syslogservers(self, site_id, element_id, data, tenant_id=None, api_version="v2.2"):
        """
        Create Syslog Server

          **Parameters:**:

          - **site_id**: Site ID
          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **enable_flow_logging:**  Type: boolean 
           - **enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **protocol:**  Type: string 
           - **remote_ca_certificate:**  Type: string 
           - **server_fqdn:**  Type: string 
           - **server_ip:**  Type: string 
           - **server_port:**  Type: integer 
           - **severity_level:**  Type: string 
           - **source_interface:**  Type: string 
           - **syslog_profile_id:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/sites/{}/elements/{}/syslogservers".format(api_version,
                                                                                             tenant_id,
                                                                                             site_id,
                                                                                             element_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def templates_ntp(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new NTP Template

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **default_template:**  Type: boolean 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **ntp_servers:**           
               - **host:**  Type: string 
               - **max_poll:**  Type: integer 
               - **min_poll:**  Type: integer 
               - **version:**  Type: integer 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/templates/ntp".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_anynetlinks(self, data, tenant_id=None, api_version="v3.4"):
        """
        POST Tenant_Anynetlinks API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.4)

          **Payload Attributes:** 


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

    def tenant_bgppeers_query(self, data, tenant_id=None, api_version="v2.2"):
        """
        Queries db for BGP peers that match query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **bgp_config:**           
               - **adv_interval:**  Type: integer 
               - **hold_time:**  Type: integer 
               - **keepalive_time:**  Type: integer 
               - **local_as_num:**  Type: string 
               - **md5_secret:**  Type: string 
               - **multi_hop_limit:**  Type: integer 
               - **peer_auth_type:**  Type: string 
               - **peer_retry_time:**  Type: integer 
           - **description:**  Type: string 
           - **name:**  Type: string 
           - **peer_ip:**  Type: string 
           - **peer_type:**  Type: string 
           - **remote_as_num:**  Type: string 
           - **route_map_in_id:**  Type: string 
           - **route_map_out_id:**  Type: string 
           - **scope:**  Type: string 
           - **shutdown:**  Type: boolean 
           - **tags:**  [Type: string] 
           - **update_source:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/bgppeers/query".format(api_version,
                                                                         tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_element_operations(self, element_id, data, tenant_id=None, api_version="v2.0"):
        """
        Handle operations on element.

          **Parameters:**:

          - **element_id**: Element (Device) ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **action:**  Type: string 
           - **parameters:**  [Type: string] 

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

    def tenant_extensions_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Queries db for limit number of tenant extensions that match the query params.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **conf:**  Type: object 
           - **disabled:**  Type: boolean 
           - **name:**  Type: string 
           - **namespace:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/extensions/query".format(api_version,
                                                                           tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_forgot_password_login(self, data, tenant_id=None, api_version="v2.0"):
        """
        Forgot password API

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **email:**  Type: string 

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

    def tenant_ipfixlocalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a IPFix local prefix

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ipfixlocalprefixes".format(api_version,
                                                                             tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_machine_operations(self, machine_id, data, tenant_id=None, api_version="v2.2"):
        """
        Update a specific machine of a tenant using operations

          **Parameters:**:

          - **machine_id**: Machine ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

          **Payload Attributes:** 

           - **connected:**  Type: boolean 
           - **console_conf_passphrase:**  Type: string 
           - **em_element_id:**  Type: string 
           - **esp_tenant_id:**  Type: string 
           - **hw_id:**  Type: string 
           - **image_version:**  Type: string 
           - **inventory_op:**  Type: string 
           - **machine_state:**  Type: string 
           - **manufacture_id:**  Type: string 
           - **model_name:**  Type: string 
           - **ordering_info:**  Type: string 
           - **owner_tenant_id:**  Type: string 
           - **pki_op:**           - **renew_state:**  Type: string 
           - **ship_state:**  Type: string 
           - **sl_no:**  Type: string 
           - **suspend_state:**  Type: string 
           - **tenant_id:**  Type: string 
           - **token:**  Type: string 

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

    def tenant_networkpolicylocalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new Network Policy local prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/networkpolicylocalprefixes".format(api_version,
                                                                                     tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_permissions(self, data, tenant_id=None, api_version="v2.0"):
        """
        Add a custom permission

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **allowed_after_ms:**  Type: integer 
           - **allowed_before_ms:**  Type: integer 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **disallow_permission:**  Type: boolean 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **value:**  Type: string 

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

    def tenant_prefixfilters_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query security prefix filter for NB API.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **filters:**           
               - **type:**  Type: string 
           - **prefix_filter_id:**  Type: string 
           - **site_id:**  Type: string 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prefixfilters/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_prioritypolicylocalprefixes(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create a new Priority Policy local prefix.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/prioritypolicylocalprefixes".format(api_version,
                                                                                      tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def tenant_waninterfaces_query(self, data, tenant_id=None, api_version="v2.7"):
        """
        Query db for Site WAN interfaces that match query parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.7)

          **Payload Attributes:** 

           - **bfd_mode:**  Type: string 
           - **bw_config_mode:**  Type: string 
           - **bwc_enabled:**  Type: boolean 
           - **cost:**  Type: integer 
           - **description:**  Type: string 
           - **label_id:**  Type: string 
           - **link_bw_down:**  Type: number 
           - **link_bw_up:**  Type: number 
           - **lqm_config:**           
               - **hub_site_ids:**  [Type: string] 
               - **inter_packet_gap:**  Type: integer 
               - **statistic:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_id:**  Type: string 
           - **site_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **use_lqm_for_non_hub_paths:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfaces/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def toolkitsessions_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Toolkitsessions_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/toolkitsessions/query".format(api_version,
                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def topology(self, data, tenant_id=None, api_version="v3.4"):
        """
        POST Topology API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v3.4)

          **Payload Attributes:** 


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

    def upgrade_status_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query Machine Upgrade Status

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/upgrade_status/query".format(api_version,
                                                                               tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def users(self, data, tenant_id=None, api_version="v2.0"):
        """
        Create an user identity.

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **first_name:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **last_name:**  Type: string 
           - **middle_name:**  Type: string 
           - **region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **user_dn:**  Type: string 
           - **user_fqn:**  Type: string 

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
        Query Tenant Vff License Tokens

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ion_key:**  Type: string 
           - **is_expired:**  Type: boolean 
           - **is_multiuse:**  Type: boolean 
           - **is_revoked:**  Type: boolean 
           - **is_used:**  Type: boolean 
           - **secret_key:**  Type: string 
           - **valid_till_secs:**  Type: integer 
           - **vfflicense_id:**  Type: string 

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
        Create Tenant Vff License Token

          **Parameters:**:

          - **vfflicense_id**: Virtual Form Factor License ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **ion_key:**  Type: string 
           - **is_expired:**  Type: boolean 
           - **is_multiuse:**  Type: boolean 
           - **is_revoked:**  Type: boolean 
           - **is_used:**  Type: boolean 
           - **secret_key:**  Type: string 
           - **valid_till_secs:**  Type: integer 
           - **vfflicense_id:**  Type: string 

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

    def vpnlinks_operations(self, vpnlink_id, data, tenant_id=None, api_version="v2.0"):
        """
        Perform an operation on a VPN link

          **Parameters:**:

          - **vpnlink_id**: VPN Link ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/vpnlinks/{}/operations".format(api_version,
                                                                                 tenant_id,
                                                                                 vpnlink_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def vpnlinks_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        Query db for VPNLinks that match query parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

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

    def waninterfacelabels_query(self, data, tenant_id=None, api_version="v2.4"):
        """
        Query db for site WAN interfaces that match query parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.4)

          **Payload Attributes:** 

           - **bwc_enabled:**  Type: boolean 
           - **description:**  Type: string 
           - **label:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **tags:**  [Type: string] 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **use_lqm_for_non_hub_paths:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfacelabels/query".format(api_version,
                                                                                   tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces(self, site_id, data, tenant_id=None, api_version="v2.7"):
        """
        Create a new Site WAN interface

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.7)

          **Payload Attributes:** 

           - **bfd_mode:**  Type: string 
           - **bw_config_mode:**  Type: string 
           - **bwc_enabled:**  Type: boolean 
           - **cost:**  Type: integer 
           - **description:**  Type: string 
           - **label_id:**  Type: string 
           - **link_bw_down:**  Type: number 
           - **link_bw_up:**  Type: number 
           - **lqm_config:**           
               - **hub_site_ids:**  [Type: string] 
               - **inter_packet_gap:**  Type: integer 
               - **statistic:**  Type: string 
           - **lqm_enabled:**  Type: boolean 
           - **name:**  Type: string 
           - **network_id:**  Type: string 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 
           - **use_for_application_reachability_probes:**  Type: boolean 
           - **use_for_controller_connections:**  Type: boolean 
           - **use_lqm_for_non_hub_paths:**  Type: boolean 
           - **vpnlink_configuration:**           
               - **keep_alive_failure_count:**  Type: integer 
               - **keep_alive_interval:**  Type: integer 

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

    def waninterfaces_correlationevents_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Waninterfaces_Correlationevents_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/waninterfaces/correlationevents/query".format(api_version,
                                                                                                tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def waninterfaces_query(self, site_id, data, tenant_id=None, api_version="v2.5"):
        """
        Query db for Site WAN interfaces that match query parameters

          **Parameters:**:

          - **site_id**: Site ID
          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

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

    def wannetworks(self, data, tenant_id=None, api_version="v2.1"):
        """
        Create a new WAN

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **provider_as_numbers:**  [Type: integer] 
           - **tags:**  [Type: string] 
           - **type:**  Type: string 

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

    def wannetworks_query(self, data, tenant_id=None, api_version="v2.1"):
        """
        Query db for WAN networks that match query parameters

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.1)

          **Payload Attributes:** 

           - **aggregate:**           
               - **field:**  Type: string 
               - **operator:**  Type: string 
           - **dest_page:**  Type: integer 
           - **getDeleted:**  Type: boolean 
           - **group_by:**  [Type: string] 
           - **last_query_ts:**  Type: integer 
           - **limit:**  Type: integer 
           - **next_query:**  Type: object 
           - **query_params:**  Type: object 
           - **retrieved_fields:**  [Type: string] 
           - **retrieved_fields_mask:**  Type: boolean 
           - **sort_params:**  Type: object 
           - **total_count:**  Type: integer 

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

          **Payload Attributes:** 

           - **description:**  Type: string 
           - **name:**  Type: string 
           - **vni:**  Type: integer 

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

    def ws_extensions(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Ws_Extensions API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions".format(api_version,
                                                                        tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    def ws_extensions_query(self, data, tenant_id=None, api_version="v2.0"):
        """
        POST Ws_Extensions_Query API Function

          **Parameters:**:

          - **data**: Dictionary containing data to POST as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)

          **Payload Attributes:** 


        **Returns:** requests.Response object extended with cgx_status and cgx_content properties.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        cur_ctlr = self._parent_class.controller

        url = str(cur_ctlr) + "/{}/api/tenants/{}/ws/extensions/query".format(api_version,
                                                                              tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "post", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    aggregates_monitor = monitor_aggregates
    """ Backwards-compatibility alias of `aggregates_monitor` to `monitor_aggregates`"""

    anynetlinks_t = tenant_anynetlinks
    """ Backwards-compatibility alias of `anynetlinks_t` to `tenant_anynetlinks`"""

    bulk_metrics_monitor = monitor_bulk_metrics
    """ Backwards-compatibility alias of `bulk_metrics_monitor` to `monitor_bulk_metrics`"""

    cellular_metrics_monitor = monitor_cellular_metrics
    """ Backwards-compatibility alias of `cellular_metrics_monitor` to `monitor_cellular_metrics`"""

    change_password = password_change
    """ Backwards-compatibility alias of `change_password` to `password_change`"""

    configs_sdwanapps = sdwanapps_configs
    """ Backwards-compatibility alias of `configs_sdwanapps` to `sdwanapps_configs`"""

    extensions_i = element_extensions
    """ Backwards-compatibility alias of `extensions_i` to `element_extensions`"""

    extensions_s = site_extensions
    """ Backwards-compatibility alias of `extensions_s` to `site_extensions`"""

    extensions_ws = ws_extensions
    """ Backwards-compatibility alias of `extensions_ws` to `ws_extensions`"""

    flows_monitor = monitor_flows
    """ Backwards-compatibility alias of `flows_monitor` to `monitor_flows`"""

    forgot_password_login_t = tenant_forgot_password_login
    """ Backwards-compatibility alias of `forgot_password_login_t` to `tenant_forgot_password_login`"""

    healthscore_aggregates_monitor = monitor_aggregates_healthscore
    """ Backwards-compatibility alias of `healthscore_aggregates_monitor` to `monitor_aggregates_healthscore`"""

    insights_monitor = monitor_insights
    """ Backwards-compatibility alias of `insights_monitor` to `monitor_insights`"""

    insightslist_monitor = monitor_insightslist
    """ Backwards-compatibility alias of `insightslist_monitor` to `monitor_insightslist`"""

    ipfixlocalprefixes_s = site_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_s` to `site_ipfixlocalprefixes`"""

    ipfixlocalprefixes_t = tenant_ipfixlocalprefixes
    """ Backwards-compatibility alias of `ipfixlocalprefixes_t` to `tenant_ipfixlocalprefixes`"""

    login_clients = clients_login
    """ Backwards-compatibility alias of `login_clients` to `clients_login`"""

    logout_clients = clients_logout
    """ Backwards-compatibility alias of `logout_clients` to `clients_logout`"""

    lqm_point_metrics_monitor = monitor_lqm_point_metrics
    """ Backwards-compatibility alias of `lqm_point_metrics_monitor` to `monitor_lqm_point_metrics`"""

    metrics_monitor = monitor_metrics
    """ Backwards-compatibility alias of `metrics_monitor` to `monitor_metrics`"""

    mroute_multicast_aggregates_monitor = monitor_aggregates_multicast_mroute
    """ Backwards-compatibility alias of `mroute_multicast_aggregates_monitor` to `monitor_aggregates_multicast_mroute`"""

    natlocalprefixes_s = site_natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_s` to `site_natlocalprefixes`"""

    natlocalprefixes_t = natlocalprefixes
    """ Backwards-compatibility alias of `natlocalprefixes_t` to `natlocalprefixes`"""

    network_point_metrics_bw_monitor = monitor_network_point_metrics_bw
    """ Backwards-compatibility alias of `network_point_metrics_bw_monitor` to `monitor_network_point_metrics_bw`"""

    network_point_metrics_hs_monitor = monitor_network_point_metrics_hs
    """ Backwards-compatibility alias of `network_point_metrics_hs_monitor` to `monitor_network_point_metrics_hs`"""

    network_point_metrics_monitor = monitor_network_point_metrics
    """ Backwards-compatibility alias of `network_point_metrics_monitor` to `monitor_network_point_metrics`"""

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

    object_stats_monitor = monitor_object_stats
    """ Backwards-compatibility alias of `object_stats_monitor` to `monitor_object_stats`"""

    operations_e = tenant_element_operations
    """ Backwards-compatibility alias of `operations_e` to `tenant_element_operations`"""

    operations_t = tenant_machine_operations
    """ Backwards-compatibility alias of `operations_t` to `tenant_machine_operations`"""

    ops_bgppeers = bgppeers_operations
    """ Backwards-compatibility alias of `ops_bgppeers` to `bgppeers_operations`"""

    ops_spokeclusters = spokeclusters_ops
    """ Backwards-compatibility alias of `ops_spokeclusters` to `spokeclusters_ops`"""

    ops_vpnlinks = vpnlinks_operations
    """ Backwards-compatibility alias of `ops_vpnlinks` to `vpnlinks_operations`"""

    overrides_appdefs = appdefs_overrides
    """ Backwards-compatibility alias of `overrides_appdefs` to `appdefs_overrides`"""

    permissions_t = tenant_permissions
    """ Backwards-compatibility alias of `permissions_t` to `tenant_permissions`"""

    prioritypolicylocalprefixes_s = site_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_s` to `site_prioritypolicylocalprefixes`"""

    prioritypolicylocalprefixes_t = tenant_prioritypolicylocalprefixes
    """ Backwards-compatibility alias of `prioritypolicylocalprefixes_t` to `tenant_prioritypolicylocalprefixes`"""

    qos_metrics_monitor = monitor_qos_metrics
    """ Backwards-compatibility alias of `qos_metrics_monitor` to `monitor_qos_metrics`"""

    query_apnprofiles = apnprofiles_query
    """ Backwards-compatibility alias of `query_apnprofiles` to `apnprofiles_query`"""

    query_appdefs = appdefs_query
    """ Backwards-compatibility alias of `query_appdefs` to `appdefs_query`"""

    query_auditlog = auditlog_query
    """ Backwards-compatibility alias of `query_auditlog` to `auditlog_query`"""

    query_bgppeers = bgppeers_query
    """ Backwards-compatibility alias of `query_bgppeers` to `bgppeers_query`"""

    query_bgppeers_t = tenant_bgppeers_query
    """ Backwards-compatibility alias of `query_bgppeers_t` to `tenant_bgppeers_query`"""

    query_bulk_config_state_e = element_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_e` to `element_bulk_config_state_query`"""

    query_bulk_config_state_networks = networks_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_networks` to `networks_bulk_config_state_query`"""

    query_bulk_config_state_policysets = policysets_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_policysets` to `policysets_bulk_config_state_query`"""

    query_bulk_config_state_s = site_bulk_config_state_query
    """ Backwards-compatibility alias of `query_bulk_config_state_s` to `site_bulk_config_state_query`"""

    query_cellular_modules = cellular_modules_query
    """ Backwards-compatibility alias of `query_cellular_modules` to `cellular_modules_query`"""

    query_clients = clients_query
    """ Backwards-compatibility alias of `query_clients` to `clients_query`"""

    query_correlationevents_anynetlinks = anynetlinks_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_anynetlinks` to `anynetlinks_correlationevents_query`"""

    query_correlationevents_e = element_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_e` to `element_correlationevents_query`"""

    query_correlationevents_interfaces = interfaces_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_interfaces` to `interfaces_correlationevents_query`"""

    query_correlationevents_s = site_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_s` to `site_correlationevents_query`"""

    query_correlationevents_waninterfaces = waninterfaces_correlationevents_query
    """ Backwards-compatibility alias of `query_correlationevents_waninterfaces` to `waninterfaces_correlationevents_query`"""

    query_current_status_software = software_current_status_query
    """ Backwards-compatibility alias of `query_current_status_software` to `software_current_status_query`"""

    query_demstatus = demstatus_query
    """ Backwards-compatibility alias of `query_demstatus` to `demstatus_query`"""

    query_dnsserviceprofiles = dnsserviceprofiles_query
    """ Backwards-compatibility alias of `query_dnsserviceprofiles` to `dnsserviceprofiles_query`"""

    query_dnsserviceroles = dnsserviceroles_query
    """ Backwards-compatibility alias of `query_dnsserviceroles` to `dnsserviceroles_query`"""

    query_dnsservices = dnsservices_query
    """ Backwards-compatibility alias of `query_dnsservices` to `dnsservices_query`"""

    query_e = element_query
    """ Backwards-compatibility alias of `query_e` to `element_query`"""

    query_elementsecurityzones = elementsecurityzones_query
    """ Backwards-compatibility alias of `query_elementsecurityzones` to `elementsecurityzones_query`"""

    query_eventcorrelationpolicyrules = eventcorrelationpolicyrules_query
    """ Backwards-compatibility alias of `query_eventcorrelationpolicyrules` to `eventcorrelationpolicyrules_query`"""

    query_eventcorrelationpolicysets = eventcorrelationpolicysets_query
    """ Backwards-compatibility alias of `query_eventcorrelationpolicysets` to `eventcorrelationpolicysets_query`"""

    query_events = events_query
    """ Backwards-compatibility alias of `query_events` to `events_query`"""

    query_extensions_i = element_extensions_query
    """ Backwards-compatibility alias of `query_extensions_i` to `element_extensions_query`"""

    query_extensions_s = site_extensions_query
    """ Backwards-compatibility alias of `query_extensions_s` to `site_extensions_query`"""

    query_extensions_t = tenant_extensions_query
    """ Backwards-compatibility alias of `query_extensions_t` to `tenant_extensions_query`"""

    query_extensions_ws = ws_extensions_query
    """ Backwards-compatibility alias of `query_extensions_ws` to `ws_extensions_query`"""

    query_globalprefixfilters = globalprefixfilters_query
    """ Backwards-compatibility alias of `query_globalprefixfilters` to `globalprefixfilters_query`"""

    query_interfaces = interfaces_query
    """ Backwards-compatibility alias of `query_interfaces` to `interfaces_query`"""

    query_ipfix = ipfix_query
    """ Backwards-compatibility alias of `query_ipfix` to `ipfix_query`"""

    query_ipfixcollectorcontexts = ipfixcollectorcontexts_query
    """ Backwards-compatibility alias of `query_ipfixcollectorcontexts` to `ipfixcollectorcontexts_query`"""

    query_ipfixfiltercontexts = ipfixfiltercontexts_query
    """ Backwards-compatibility alias of `query_ipfixfiltercontexts` to `ipfixfiltercontexts_query`"""

    query_ipfixglobalprefixes = ipfixglobalprefixes_query
    """ Backwards-compatibility alias of `query_ipfixglobalprefixes` to `ipfixglobalprefixes_query`"""

    query_ipfixlocalprefixes = ipfixlocalprefixes_query
    """ Backwards-compatibility alias of `query_ipfixlocalprefixes` to `ipfixlocalprefixes_query`"""

    query_ipfixprofiles = ipfixprofiles_query
    """ Backwards-compatibility alias of `query_ipfixprofiles` to `ipfixprofiles_query`"""

    query_ipfixtemplates = ipfixtemplates_query
    """ Backwards-compatibility alias of `query_ipfixtemplates` to `ipfixtemplates_query`"""

    query_ipsecprofiles = ipsecprofiles_query
    """ Backwards-compatibility alias of `query_ipsecprofiles` to `ipsecprofiles_query`"""

    query_lannetworks = site_lannetworks_query
    """ Backwards-compatibility alias of `query_lannetworks` to `site_lannetworks_query`"""

    query_lannetworks_t = lannetworks_query
    """ Backwards-compatibility alias of `query_lannetworks_t` to `lannetworks_query`"""

    query_localprefixfilters = localprefixfilters_query
    """ Backwards-compatibility alias of `query_localprefixfilters` to `localprefixfilters_query`"""

    query_m = machines_query
    """ Backwards-compatibility alias of `query_m` to `machines_query`"""

    query_machine_upgrade = machine_upgrade_query
    """ Backwards-compatibility alias of `query_machine_upgrade` to `machine_upgrade_query`"""

    query_machines_c = clients_machines_query
    """ Backwards-compatibility alias of `query_machines_c` to `clients_machines_query`"""

    query_multicastdynamicrps = multicastdynamicrps_query
    """ Backwards-compatibility alias of `query_multicastdynamicrps` to `multicastdynamicrps_query`"""

    query_multicastigmpmemberships = multicastigmpmemberships_query
    """ Backwards-compatibility alias of `query_multicastigmpmemberships` to `multicastigmpmemberships_query`"""

    query_multicastroutes = multicastroutes_query
    """ Backwards-compatibility alias of `query_multicastroutes` to `multicastroutes_query`"""

    query_multicastrps = multicastrps_query
    """ Backwards-compatibility alias of `query_multicastrps` to `multicastrps_query`"""

    query_multicaststatus = multicaststatus_query
    """ Backwards-compatibility alias of `query_multicaststatus` to `multicaststatus_query`"""

    query_multicastwanstatus = multicastwanstatus_query
    """ Backwards-compatibility alias of `query_multicastwanstatus` to `multicastwanstatus_query`"""

    query_natglobalprefixes = natglobalprefixes_query
    """ Backwards-compatibility alias of `query_natglobalprefixes` to `natglobalprefixes_query`"""

    query_natlocalprefixes = natlocalprefixes_query
    """ Backwards-compatibility alias of `query_natlocalprefixes` to `natlocalprefixes_query`"""

    query_natpolicypools = natpolicypools_query
    """ Backwards-compatibility alias of `query_natpolicypools` to `natpolicypools_query`"""

    query_natpolicyrules = natpolicyrules_query
    """ Backwards-compatibility alias of `query_natpolicyrules` to `natpolicyrules_query`"""

    query_natpolicysets = natpolicysets_query
    """ Backwards-compatibility alias of `query_natpolicysets` to `natpolicysets_query`"""

    query_natpolicysetstacks = natpolicysetstacks_query
    """ Backwards-compatibility alias of `query_natpolicysetstacks` to `natpolicysetstacks_query`"""

    query_natzones = natzones_query
    """ Backwards-compatibility alias of `query_natzones` to `natzones_query`"""

    query_networkcontexts = networkcontexts_query
    """ Backwards-compatibility alias of `query_networkcontexts` to `networkcontexts_query`"""

    query_networkpolicyglobalprefixes = networkpolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_networkpolicyglobalprefixes` to `networkpolicyglobalprefixes_query`"""

    query_networkpolicylocalprefixes = networkpolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_networkpolicylocalprefixes` to `networkpolicylocalprefixes_query`"""

    query_networkpolicyrules = networkpolicyrules_query
    """ Backwards-compatibility alias of `query_networkpolicyrules` to `networkpolicyrules_query`"""

    query_networkpolicysets = networkpolicysets_query
    """ Backwards-compatibility alias of `query_networkpolicysets` to `networkpolicysets_query`"""

    query_networkpolicysetstacks = networkpolicysetstacks_query
    """ Backwards-compatibility alias of `query_networkpolicysetstacks` to `networkpolicysetstacks_query`"""

    query_ngfwsecuritypolicyglobalprefixes = ngfwsecuritypolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicyglobalprefixes` to `ngfwsecuritypolicyglobalprefixes_query`"""

    query_ngfwsecuritypolicylocalprefixes = ngfwsecuritypolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicylocalprefixes` to `ngfwsecuritypolicylocalprefixes_query`"""

    query_ngfwsecuritypolicyrules = ngfwsecuritypolicyrules_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicyrules` to `ngfwsecuritypolicyrules_query`"""

    query_ngfwsecuritypolicysets = ngfwsecuritypolicysets_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicysets` to `ngfwsecuritypolicysets_query`"""

    query_ngfwsecuritypolicysetstacks = ngfwsecuritypolicysetstacks_query
    """ Backwards-compatibility alias of `query_ngfwsecuritypolicysetstacks` to `ngfwsecuritypolicysetstacks_query`"""

    query_pathgroups = pathgroups_query
    """ Backwards-compatibility alias of `query_pathgroups` to `pathgroups_query`"""

    query_policyrules = policyrules_query
    """ Backwards-compatibility alias of `query_policyrules` to `policyrules_query`"""

    query_policysets = policysets_query
    """ Backwards-compatibility alias of `query_policysets` to `policysets_query`"""

    query_prefixes = prefixes_query
    """ Backwards-compatibility alias of `query_prefixes` to `prefixes_query`"""

    query_prefixfilters = prefixfilters_query
    """ Backwards-compatibility alias of `query_prefixfilters` to `prefixfilters_query`"""

    query_prefixfilters_t = tenant_prefixfilters_query
    """ Backwards-compatibility alias of `query_prefixfilters_t` to `tenant_prefixfilters_query`"""

    query_prioritypolicyglobalprefixes = prioritypolicyglobalprefixes_query
    """ Backwards-compatibility alias of `query_prioritypolicyglobalprefixes` to `prioritypolicyglobalprefixes_query`"""

    query_prioritypolicylocalprefixes = prioritypolicylocalprefixes_query
    """ Backwards-compatibility alias of `query_prioritypolicylocalprefixes` to `prioritypolicylocalprefixes_query`"""

    query_prioritypolicyrules = prioritypolicyrules_query
    """ Backwards-compatibility alias of `query_prioritypolicyrules` to `prioritypolicyrules_query`"""

    query_prioritypolicysets = prioritypolicysets_query
    """ Backwards-compatibility alias of `query_prioritypolicysets` to `prioritypolicysets_query`"""

    query_prioritypolicysetstacks = prioritypolicysetstacks_query
    """ Backwards-compatibility alias of `query_prioritypolicysetstacks` to `prioritypolicysetstacks_query`"""

    query_prismaaccess_configs = prismaaccess_configs_query
    """ Backwards-compatibility alias of `query_prismaaccess_configs` to `prismaaccess_configs_query`"""

    query_reports = reports_query
    """ Backwards-compatibility alias of `query_reports` to `reports_query`"""

    query_reportsdir = reportsdir_query
    """ Backwards-compatibility alias of `query_reportsdir` to `reportsdir_query`"""

    query_routing_aspathaccesslists = routing_aspathaccesslists_query
    """ Backwards-compatibility alias of `query_routing_aspathaccesslists` to `routing_aspathaccesslists_query`"""

    query_routing_ipcommunitylists = routing_ipcommunitylists_query
    """ Backwards-compatibility alias of `query_routing_ipcommunitylists` to `routing_ipcommunitylists_query`"""

    query_routing_prefixlists = routing_prefixlists_query
    """ Backwards-compatibility alias of `query_routing_prefixlists` to `routing_prefixlists_query`"""

    query_routing_routemaps = routing_routemaps_query
    """ Backwards-compatibility alias of `query_routing_routemaps` to `routing_routemaps_query`"""

    query_s = site_query
    """ Backwards-compatibility alias of `query_s` to `site_query`"""

    query_securitypolicyrules = securitypolicyrules_query
    """ Backwards-compatibility alias of `query_securitypolicyrules` to `securitypolicyrules_query`"""

    query_securitypolicysets = securitypolicysets_query
    """ Backwards-compatibility alias of `query_securitypolicysets` to `securitypolicysets_query`"""

    query_securityzones = securityzones_query
    """ Backwards-compatibility alias of `query_securityzones` to `securityzones_query`"""

    query_servicebindingmaps = servicebindingmaps_query
    """ Backwards-compatibility alias of `query_servicebindingmaps` to `servicebindingmaps_query`"""

    query_serviceendpoints = serviceendpoints_query
    """ Backwards-compatibility alias of `query_serviceendpoints` to `serviceendpoints_query`"""

    query_servicelabels = servicelabels_query
    """ Backwards-compatibility alias of `query_servicelabels` to `servicelabels_query`"""

    query_sitesecurityzones_t = sitesecurityzones_query
    """ Backwards-compatibility alias of `query_sitesecurityzones_t` to `sitesecurityzones_query`"""

    query_softwarehistory = softwarehistory_query
    """ Backwards-compatibility alias of `query_softwarehistory` to `softwarehistory_query`"""

    query_spokeclusters_t = spokeclusters_query
    """ Backwards-compatibility alias of `query_spokeclusters_t` to `spokeclusters_query`"""

    query_state_software = software_state_query
    """ Backwards-compatibility alias of `query_state_software` to `software_state_query`"""

    query_status = status_query
    """ Backwards-compatibility alias of `query_status` to `status_query`"""

    query_status_cellular_module_firmware = cellular_module_firmware_status_query
    """ Backwards-compatibility alias of `query_status_cellular_module_firmware` to `cellular_module_firmware_status_query`"""

    query_status_software = software_status_query
    """ Backwards-compatibility alias of `query_status_software` to `software_status_query`"""

    query_tokens_vfflicenses = vff_token_query
    """ Backwards-compatibility alias of `query_tokens_vfflicenses` to `vff_token_query`"""

    query_toolkitsessions = toolkitsessions_query
    """ Backwards-compatibility alias of `query_toolkitsessions` to `toolkitsessions_query`"""

    query_upgrade_status = upgrade_status_query
    """ Backwards-compatibility alias of `query_upgrade_status` to `upgrade_status_query`"""

    query_vpnlinks = vpnlinks_query
    """ Backwards-compatibility alias of `query_vpnlinks` to `vpnlinks_query`"""

    query_waninterfacelabels = waninterfacelabels_query
    """ Backwards-compatibility alias of `query_waninterfacelabels` to `waninterfacelabels_query`"""

    query_waninterfaces = waninterfaces_query
    """ Backwards-compatibility alias of `query_waninterfaces` to `waninterfaces_query`"""

    query_waninterfaces_t = tenant_waninterfaces_query
    """ Backwards-compatibility alias of `query_waninterfaces_t` to `tenant_waninterfaces_query`"""

    query_wannetworks = wannetworks_query
    """ Backwards-compatibility alias of `query_wannetworks` to `wannetworks_query`"""

    reallocate_clients = clients_reallocate
    """ Backwards-compatibility alias of `reallocate_clients` to `clients_reallocate`"""

    summary_events = events_summary
    """ Backwards-compatibility alias of `summary_events` to `events_summary`"""

    sys_metrics_monitor = monitor_sys_metrics
    """ Backwards-compatibility alias of `sys_metrics_monitor` to `monitor_sys_metrics`"""

    sys_point_metrics_monitor = monitor_sys_point_metrics
    """ Backwards-compatibility alias of `sys_point_metrics_monitor` to `monitor_sys_point_metrics`"""

    tokens_vfflicenses = vfflicense_tokens
    """ Backwards-compatibility alias of `tokens_vfflicenses` to `vfflicense_tokens`"""

    topn_cellular_metrics_monitor = monitor_cellular_metrics_topn
    """ Backwards-compatibility alias of `topn_cellular_metrics_monitor` to `monitor_cellular_metrics_topn`"""

    topn_monitor = monitor_topn
    """ Backwards-compatibility alias of `topn_monitor` to `monitor_topn`"""

    topn_sys_metrics_monitor = monitor_sys_metrics_topn
    """ Backwards-compatibility alias of `topn_sys_metrics_monitor` to `monitor_sys_metrics_topn`"""

    wan_neighbor_multicast_aggregates_monitor = monitor_aggregates_multicast_wan_neighbor
    """ Backwards-compatibility alias of `wan_neighbor_multicast_aggregates_monitor` to `monitor_aggregates_multicast_wan_neighbor`"""

    elements_bulk_config_state_query = element_bulk_config_state_query
    """ Backwards-compatibility alias of `elements_bulk_config_state_query` to `element_bulk_config_state_query`"""

    elements_query = element_query
    """ Backwards-compatibility alias of `elements_query` to `element_query`"""

    sites_bulk_config_state_query = site_bulk_config_state_query
    """ Backwards-compatibility alias of `sites_bulk_config_state_query` to `site_bulk_config_state_query`"""

    sites_query = site_query
    """ Backwards-compatibility alias of `sites_query` to `site_query`"""

