#!/usr/bin/env python
"""
CloudGenix Python SDK - PATCH

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


class Patch(object):
    """
    CloudGenix API - PATCH requests

    Object to handle making Patch requests via shared Requests Session.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def tenant_operators(self, operator_id, data, tenant_id=None, api_version="v2.2"):
        """
        Patch a tenant operator (v2.2)

          **Parameters:**:

          - **operator_id**: Operator ID
          - **data**: Dictionary containing data to PATCH as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.2)

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
               - **description:**  Type: string 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **disallow_permissions:**           
                   - **value:**  Type: string 
               - **id:**  Type: string 
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
           - **disable_idp_login:**  Type: boolean 
           - **disabled:**  Type: boolean 
           - **disabled_reason:**  Type: string 
           - **email:**  Type: string 
           - **email_iam:**  Type: string 
           - **email_validated:**  Type: boolean 
           - **enable_session_ip_lock:**  Type: boolean 
           - **first_name:**  Type: string 
           - **from_esp:**  Type: boolean 
           - **from_esp_name:**  Type: string 
           - **from_esp_tenant_id:**  Type: string 
           - **inactive:**  Type: boolean 
           - **inactive_reason:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **is_locked:**  Type: boolean 
           - **is_system_owned:**  Type: boolean 
           - **last_login:**  Type: string 
           - **last_name:**  Type: string 
           - **linked_accounts:**           
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **failed_login_attempts:**  Type: integer 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **provider_key:**  Type: string 
               - **provider_value:**  Type: string 
               - **provider_value_updated_on:**  Type: integer 
               - **region:**  Type: string 
               - **tenant_id:**  Type: string 
           - **migration_state:**           
           - **phone_numbers:**           
               - **country_code:**  Type: integer 
               - **local_extension:**  Type: integer 
               - **number:**  Type: integer 
               - **types:**           
                   - **value:**  Type: string 
           - **region:**  Type: string 
           - **roles:**           
               - **name:**  Type: string 
           - **secondary_emails:**           
               - **email:**  Type: string 
           - **settings:**  Type: string 
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}/operators/{}".format(api_version,
                                                                       tenant_id,
                                                                       operator_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "patch", data=data)

    def tenants(self, data, tenant_id=None, api_version="v2.5"):
        """
        Patch tenant (v2.5)

          **Parameters:**:

          - **data**: Dictionary containing data to PATCH as JSON
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.5)

          **Payload Attributes:** 

           - **address:**           
               - **city:**  Type: string 
               - **country:**  Type: string 
               - **post_code:**  Type: string 
               - **state:**  Type: string 
               - **street:**  Type: string 
               - **street2:**  Type: string 
           - **canonical_name:**  Type: string 
           - **clients:**  [Type: string] 
           - **csp_tenant_id:**  Type: string 
           - **description:**  Type: string 
           - **disabled:**  Type: string 
           - **disabled_reason:**  Type: string 
           - **inactive:**  Type: string 
           - **inactive_reason:**  Type: string 
           - **ipv4_list:**           
               - **ipv4:**  Type: string 
           - **is_esp:**  Type: boolean 
           - **is_pa_iot_security_license:**  Type: boolean 
           - **is_support:**  Type: boolean 
           - **name:**  Type: string 
           - **operator:**           
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
               - **disable_idp_login:**  Type: boolean 
               - **disabled:**  Type: boolean 
               - **disabled_reason:**  Type: string 
               - **email:**  Type: string 
               - **email_iam:**  Type: string 
               - **email_validated:**  Type: boolean 
               - **enable_session_ip_lock:**  Type: boolean 
               - **first_name:**  Type: string 
               - **from_esp:**  Type: boolean 
               - **from_esp_name:**  Type: string 
               - **from_esp_tenant_id:**  Type: string 
               - **id:**  Type: string 
               - **inactive:**  Type: boolean 
               - **inactive_reason:**  Type: string 
               - **ipv4_list:**           
                   - **ipv4:**  Type: string 
               - **is_locked:**  Type: boolean 
               - **is_system_owned:**  Type: boolean 
               - **last_login:**  Type: string 
               - **last_name:**  Type: string 
               - **linked_accounts:**           
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **failed_login_attempts:**  Type: integer 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **provider_key:**  Type: string 
                   - **provider_value:**  Type: string 
                   - **provider_value_updated_on:**  Type: integer 
                   - **region:**  Type: string 
                   - **tenant_id:**  Type: string 
               - **migration_state:**           
               - **name:**  Type: string 
               - **phone_numbers:**           
                   - **country_code:**  Type: integer 
                   - **local_extension:**  Type: integer 
                   - **number:**  Type: integer 
                   - **types:**           
                       - **value:**  Type: string 
               - **region:**  Type: string 
               - **roles:**           
                   - **name:**  Type: string 
               - **secondary_emails:**           
                   - **email:**  Type: string 
               - **settings:**  Type: string 
               - **tenant_id:**  Type: string 
           - **pan_account_id:**  Type: string 
           - **pan_tenant_id:**  Type: string 
           - **password_policy:**           
               - **enable_failed_login_attempts:**  Type: boolean 
               - **enable_failed_login_time_delay:**  Type: boolean 
               - **enable_maximum_password_length:**  Type: boolean 
               - **enable_minimum_password_length:**  Type: boolean 
               - **enable_password_aging:**  Type: boolean 
               - **enable_password_identity_difference:**  Type: boolean 
               - **enable_password_no_reuse_count:**  Type: boolean 
               - **enable_session_ip_lock:**  Type: boolean 
               - **enable_two_lower_case_letters:**  Type: boolean 
               - **enable_two_numbers:**  Type: boolean 
               - **enable_two_special_characters:**  Type: boolean 
               - **enable_two_upper_case_letters:**  Type: boolean 
               - **failed_login_attempts:**  Type: integer 
               - **maximum_password_length:**  Type: integer 
               - **minimum_password_length:**  Type: integer 
               - **password_aging_days:**  Type: integer 
               - **password_aging_notification:**  Type: integer 
               - **password_no_reuse_count:**  Type: integer 
               - **special_characters:**  Type: string 
               - **special_characters_regex:**  Type: string 
           - **phone_numbers:**           
               - **country_code:**  Type: integer 
               - **local_extension:**  Type: integer 
               - **number:**  Type: integer 
               - **types:**           
                   - **value:**  Type: string 
           - **prisma_access_tenant_id:**  Type: string 
           - **provider_data:**           
               - **certificate:**           
                   - **certificate:**  Type: string 
                   - **certificate_expiry_utc:**  Type: integer 
                   - **certificate_type:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **issued_by:**           
                       - **common_name:**  Type: string 
                       - **country:**  Type: string 
                       - **location:**  Type: string 
                       - **organization:**  Type: string 
                       - **organization_unit:**  Type: string 
                       - **state:**  Type: string 
                   - **issued_to:**           
                       - **common_name:**  Type: string 
                       - **country:**  Type: string 
                       - **location:**  Type: string 
                       - **organization:**  Type: string 
                       - **organization_unit:**  Type: string 
                       - **state:**  Type: string 
                   - **parent_id:** 
                   - **region:**  Type: string 
                   - **serial_number:**  Type: string 
                   - **tenant_id:**  Type: string 
                   - **version:**  Type: string 
               - **password_hash:**  Type: string 
               - **provider:**           
                   - **canonical_name:**  Type: string 
                   - **description:**  Type: string 
                   - **disabled:**  Type: boolean 
                   - **disabled_reason:**  Type: string 
                   - **id:**  Type: string 
                   - **inactive:**  Type: boolean 
                   - **inactive_reason:**  Type: string 
                   - **map_external_group:**  Type: object 
                   - **name:**  Type: string 
                   - **protocol:**           
                   - **region:**  Type: string 
                   - **template:**  Type: string 
                   - **tenant_id:**  Type: string 
               - **salt:**  Type: string 
               - **security:**  Type: string 
           - **region:**  Type: string 
           - **sase_at:**  Type: string 
           - **telemetry_region:**  Type: string 
           - **tenant_id:**  Type: string 
           - **tsg_id:**  Type: string 
           - **tsg_instances:**           
               - **app_id:**  Type: string 
               - **region:**  Type: string 
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

        url = str(cur_ctlr) + "/{}/api/tenants/{}".format(api_version,
                                                          tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.rest_call(url, "patch", data=data)

    # Public Digest compatibility maps below, mapping what is available via
    # /v2.0/permissions API versus what is used in this SDK.

    operators_t = tenant_operators
    """ Backwards-compatibility alias of `operators_t` to `tenant_operators`"""

