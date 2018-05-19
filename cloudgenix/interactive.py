#!/usr/bin/env python
"""
CloudGenix Python Interactive SDK Helper functions

**Author:** CloudGenix

**Copyright:** (c) 2017, 2018 CloudGenix, Inc

**License:** MIT
"""
import getpass
import json
import logging
import time
import sys

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

# python 2 to 3 support
try:
    compat_input = raw_input
except NameError:
    compat_input = input

# python 2 and 3 handling
if sys.version_info < (3,):
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


class Interactive(object):
    """
    CloudGenix API - Interactive helper functions

    Object to help with interactive complex functions instead of raw API accesses
    """

    # placeholder for parent class namespace
    _parent_class = None

    def login(self, email=None, password=None):
        """
        Interactive login using the `cloudgenix.API` object. This function is more robust and handles SAML and MSP accounts.
        Expects interactive capability. if this is not available, use `cloudenix.API.post.login` directly.

        **Parameters:**:

          - **email**: Email to log in for, will prompt if not entered.
          - **password**: Password to log in with, will prompt if not entered. Ignored for SAML v2.0 users.

        **Returns:** Bool. In addition the function will mutate the `cloudgenix.API` constructor items as needed.
        """
        # if email not given in function, or if first login fails, prompt.

        if email is None:
            # If user is not set, pull from cache. If not in cache, prompt.
            if self._parent_class.email:
                email = self._parent_class.email
            else:
                email = compat_input("login: ")

        if password is None:
            # if pass not given on function, or if first login fails, prompt.
            if self._parent_class._password:
                password = self._parent_class._password
            else:
                password = getpass.getpass()

        # Try and login
        # For SAML 2.0 support, set the Referer URL prior to logging in.
        # add referer header to the session.
        self._parent_class.add_headers({'Referer': "{}/v2.0/api/login".format(self._parent_class.controller)})

        # call the login API.
        response = self._parent_class.post.login({"email": email, "password": password})

        if response.cgx_status:

            # Check for SAML 2.0 login
            if not response.cgx_content.get('x_auth_token'):
                urlpath = response.cgx_content.get("urlpath", "")
                request_id = response.cgx_content.get("requestId", "")
                if urlpath and request_id:
                    # SAML 2.0
                    print('SAML 2.0: To finish login open the following link in a browser\n\n{0}\n\n'.format(urlpath))
                    found_auth_token = False
                    for i in range(20):
                        print('Waiting for {0} seconds for authentication...'.format((20 - i) * 5))
                        saml_response = self.check_sso_login(email, request_id)
                        if saml_response.cgx_status and saml_response.cgx_content.get('x_auth_token'):
                            found_auth_token = True
                            break
                        # wait before retry.
                        time.sleep(5)
                    if not found_auth_token:
                        print("Login time expired! Please re-login.\n")
                        # log response when debug
                        try:
                            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", json.dumps(response, indent=4))
                        except (TypeError, ValueError):
                            # not JSON response, don't pretty print log.
                            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", str(response))
                        # print login error
                        print('Login failed, please try again', response)
                        # Flush command-line entered login info if failure.
                        self._parent_class.email = None
                        self._parent_class.password = None
                        return False

            api_logger.info('Login successful:')
            # if we got here, we either got an x_auth_token in the original login, or
            # we got an auth_token cookie set via SAML. Figure out which.
            auth_token = response.cgx_content.get('x_auth_token')
            if auth_token:
                # token in the original login (not saml) means region parsing has not been done.
                # do now, and recheck if cookie needs set.
                auth_region = self._parent_class.parse_region(response)
                self._parent_class.update_region_to_controller(auth_region)
                self._parent_class.reparse_login_cookie_after_region_update(response)
            # debug info if needed
            api_logger.debug("AUTH_TOKEN=%s", response.cgx_content.get('x_auth_token'))

            # Step 2: Get operator profile for tenant ID and other info.
            if self.interactive_update_profile_vars():

                # pull tenant detail
                if self._parent_class.tenant_id:

                    # add tenant values to API() object
                    if self.interactive_tenant_update_vars():

                        # Step 3: Check for ESP/MSP. If so, ask which tenant this session should be for.
                        if self._parent_class.is_esp:
                            # ESP/MSP!
                            choose_status, chosen_client_id = self.interactive_client_choice()

                            if choose_status:
                                # attempt to login as client
                                clogin_resp = self._parent_class.post.login_clients(chosen_client_id, {})

                                if clogin_resp.cgx_status:
                                    # login successful, update profile and tenant info
                                    c_profile = self.interactive_update_profile_vars()
                                    t_profile = self.interactive_tenant_update_vars()

                                    if c_profile and t_profile:
                                        # successful full client login.
                                        self._parent_class._password = None
                                        # remove referer header prior to continuing.
                                        self._parent_class.remove_header('Referer')
                                        return True

                                    else:
                                        if t_profile:
                                            print("ESP Client Tenant detail retrieval failed.")
                                        # clear password out of memory
                                        self._parent_class.email = None
                                        self._parent_class._password = None
                                        # remove referer header prior to continuing.
                                        self._parent_class.remove_header('Referer')
                                        return False

                                else:
                                    print("ESP Client Login failed.")
                                    # clear password out of memory
                                    self._parent_class.email = None
                                    self._parent_class._password = None
                                    # remove referer header prior to continuing.
                                    self._parent_class.remove_header('Referer')
                                    return False

                            else:
                                print("ESP Client Choice failed.")
                                # clear password out of memory
                                self._parent_class.email = None
                                self._parent_class._password = None
                                # remove referer header prior to continuing.
                                self._parent_class.remove_header('Referer')
                                return False

                        # successful!
                        # clear password out of memory
                        self._parent_class._password = None
                        # remove referer header prior to continuing.
                        self._parent_class.remove_header('Referer')
                        return True

                    else:
                        print("Tenant detail retrieval failed.")
                        # clear password out of memory
                        self._parent_class.email = None
                        self._parent_class._password = None
                        # remove referer header prior to continuing.
                        self._parent_class.remove_header('Referer')
                        return False

            else:
                # Profile detail retrieval failed
                self._parent_class.email = None
                self._parent_class._password = None
                return False

            api_logger.info("EMAIL = %s", self._parent_class.email)
            api_logger.info("USER_ID = %s", self._parent_class._user_id)
            api_logger.info("USER ROLES = %s", json.dumps(self._parent_class.roles))
            api_logger.info("TENANT_ID = %s", self._parent_class.tenant_id)
            api_logger.info("TENANT_NAME = %s", self._parent_class.tenant_name)
            api_logger.info("TOKEN_SESSION = %s", self._parent_class.token_session)

            # remove referer header prior to continuing.
            self._parent_class.remove_header('Referer')
        else:
            # log response when debug
            api_logger.debug("LOGIN_FAIL_RESPONSE = %s", json.dumps(response.cgx_content, indent=4))
            # print login error
            print('Login failed, please try again:', response.cgx_content)
            # Flush command-line entered login info if failure.
            self._parent_class.email = None
            self._parent_class.password = None

            # remove referer header prior to continuing.
            self._parent_class.remove_header('Referer')
        return False

    def use_token(self, token=None):
        """
        Function to use static AUTH_TOKEN as auth for the constructor instead of full login process.

        **Parameters:**:

          - **token**: Static AUTH_TOKEN

        **Returns:** Bool on success or failure. In addition the function will mutate the `cloudgenix.API`
                     constructor items as needed.
        """
        api_logger.info('use_token function:')

        # check token is a string.
        if not isinstance(token, (text_type, binary_type)):
            api_logger.debug('"token" was not a text-style string: {}'.format(text_type(token)))
            return False

        # Start setup of constructor.
        session = self._parent_class.expose_session()

        # clear cookies
        session.cookies.clear()

        # Static Token uses X-Auth-Token header instead of cookies.
        self._parent_class.add_headers({
            'X-Auth-Token': token
        })

        # Step 2: Get operator profile for tenant ID and other info.
        if self.interactive_update_profile_vars():

            # pull tenant detail
            if self._parent_class.tenant_id:

                # add tenant values to API() object
                if self.interactive_tenant_update_vars():

                    # Step 3: Check for ESP/MSP. If so, ask which tenant this session should be for.
                    if self._parent_class.is_esp:
                        # ESP/MSP!
                        choose_status, chosen_client_id = self.interactive_client_choice()

                        if choose_status:
                            # attempt to login as client
                            clogin_resp = self._parent_class.post.login_clients(chosen_client_id, {})

                            if clogin_resp.cgx_status:
                                # login successful, update profile and tenant info
                                c_profile = self.interactive_update_profile_vars()
                                t_profile = self.interactive_tenant_update_vars()

                                if c_profile and t_profile:
                                    # successful full client login.
                                    self._parent_class._password = None
                                    return True

                                else:
                                    if t_profile:
                                        print("ESP Client Tenant detail retrieval failed.")
                                    # clear password out of memory
                                    self._parent_class.email = None
                                    self._parent_class._password = None
                                    return False

                            else:
                                print("ESP Client Login failed.")
                                # clear password out of memory
                                self._parent_class.email = None
                                self._parent_class._password = None
                                return False

                        else:
                            print("ESP Client Choice failed.")
                            # clear password out of memory
                            self._parent_class.email = None
                            self._parent_class._password = None
                            return False

                    # successful!
                    # clear password out of memory
                    self._parent_class._password = None
                    return True

                else:
                    print("Tenant detail retrieval failed.")
                    # clear password out of memory
                    self._parent_class.email = None
                    self._parent_class._password = None
                    return False

        else:
            # Profile detail retrieval failed
            self._parent_class.email = None
            self._parent_class._password = None
            return False

        api_logger.info("EMAIL = %s", self._parent_class.email)
        api_logger.info("USER_ID = %s", self._parent_class._user_id)
        api_logger.info("USER ROLES = %s", json.dumps(self._parent_class.roles))
        api_logger.info("TENANT_ID = %s", self._parent_class.tenant_id)
        api_logger.info("TENANT_NAME = %s", self._parent_class.tenant_name)
        api_logger.info("TOKEN_SESSION = %s", self._parent_class.token_session)

        return True

    def interactive_tenant_update_vars(self):
        """
        Function to update the `cloudgenix.API` object with tenant login info. Run after login or client login.

        **Returns:** Boolean on success/failure,
        """
        api_logger.info('interactive_tenant_update_vars function:')
        tenant_resp = self._parent_class.get.tenants(self._parent_class.tenant_id)
        status = tenant_resp.cgx_status
        tenant_dict = tenant_resp.cgx_content

        if status:

            api_logger.debug("new tenant_dict: %s", tenant_dict)

            # Get Tenant info.
            self._parent_class.tenant_name = tenant_dict.get('name', self._parent_class.tenant_id)
            # is ESP/MSP?
            self._parent_class.is_esp = tenant_dict.get('is_esp')
            # grab tenant address for location.
            address_lookup = tenant_dict.get('address', None)
            if address_lookup:
                tenant_address = address_lookup.get('street', "") + ", "
                tenant_address += (str(address_lookup.get('street2', "")) + ", ")
                tenant_address += (str(address_lookup.get('city', "")) + ", ")
                tenant_address += (str(address_lookup.get('state', "")) + ", ")
                tenant_address += (str(address_lookup.get('post_code', "")) + ", ")
                tenant_address += (str(address_lookup.get('country', "")) + ", ")
            else:
                tenant_address = "Unknown"
            self._parent_class.address = tenant_address
            return True
        else:
            # update failed
            return False

    def interactive_update_profile_vars(self):
        """
        Function to update the `cloudgenix.API` object with profile info. Run after login or client login.

        **Returns:** Boolean on success/failure,
        """

        profile = self._parent_class.get.profile()

        if profile.cgx_status:

            # if successful, save tenant id and email info to cli state.
            self._parent_class.tenant_id = profile.cgx_content.get('tenant_id')
            self._parent_class.email = profile.cgx_content.get('email')
            self._parent_class._user_id = profile.cgx_content.get('id')
            self._parent_class.roles = profile.cgx_content.get('roles', [])
            self._parent_class.token_session = profile.cgx_content.get('token_session')

            return True

        else:
            print("Profile retrieval failed.")
            # clear password out of memory
            self._parent_class._password = None
            return False

    def interactive_client_choice(self):
        """
        Present a menu for user to select from ESP/MSP managed clients they have permission to.

        **Returns:** Tuple with (Boolean success, selected client ID).
        """

        clients = self._parent_class.get.clients_t()
        clients_perms = self._parent_class.get.permissions_clients_d(self._parent_class._user_id)

        client_status = clients.cgx_status
        clients_dict = clients.cgx_content
        c_perms_status = clients_perms.cgx_status
        c_perms_dict = clients_perms.cgx_content

        # Build MSP/ESP id-name dict, get list of allowed tenants.
        if client_status and c_perms_status:
            client_id_name = {}
            for client in clients_dict.get('items', []):
                if type(client) is dict:
                    # create client ID to name map table.
                    client_id_name[client.get('id', "err")] = client.get('canonical_name')

            # Valid clients w/permissions - create list of tuples for menu
            menu_list = []
            for client in c_perms_dict.get('items', []):
                if type(client) is dict:
                    # add entry
                    client_id = client.get('client_id')
                    # create tuple of ( client name, client id ) to append to list
                    menu_list.append(
                        (client_id_name.get(client_id, client_id), client_id)
                    )
            # empty menu?
            if not menu_list:
                # no clients
                print("No ESP/MSP clients allowed for user.")
                return False, {}

            # ask user to select client
            _, chosen_client_id = self.quick_menu("ESP/MSP Detected. Select a client to use:", "{0}) {1}", menu_list)

            return True, chosen_client_id

        else:
            print("ESP/MSP detail retrieval failed.")
            return False, {}

    def quick_menu(self, banner, list_line_format, choice_list):
        """
        Function to display a quick menu for user input

        **Parameters:**

          - **banner:** Text to display before menu
          - **list_line_format:** Print'ing string with format spots for index + tuple values
          - **choice_list:** List of tuple values that you want returned if selected (and printed)

        **Returns:** Tuple that was selected.
        """
        # Setup menu
        invalid = True
        menu_int = -1

        # loop until valid
        while invalid:
            print(banner)

            for item_index, item_value in enumerate(choice_list):
                print(list_line_format.format(item_index + 1, *item_value))

            menu_choice = compat_input("\nChoose a Number or (Q)uit: ")

            if str(menu_choice).lower() in ['q']:
                # exit
                print("Exiting..")
                # best effort logout
                self._parent_class.get.logout()
                sys.exit(0)

            # verify number entered
            try:
                menu_int = int(menu_choice)
                sanity = True
            except ValueError:
                # not a number
                print("ERROR: ", menu_choice)
                sanity = False

            # validate number chosen
            if sanity and 1 <= menu_int <= len(choice_list):
                invalid = False
            else:
                print("Invalid input, needs to be between 1 and {0}.\n".format(len(choice_list)))

        # return the choice_list tuple that matches the entry.
        return choice_list[int(menu_int) - 1]

    def check_sso_login(self, operator_email, request_id):
        """
        Login to the CloudGenix API, and see if SAML SSO has occurred.
        This function is used to check and see if SAML SSO has succeeded while waiting.

        **Parameters:**

          - **operator_email:** String with the username to log in with
          - **request_id:** String containing the SAML 2.0 Request ID from previous login attempt.

        **Returns:** Tuple (Boolean success, Token on success, JSON response on error.)
        """

        data = {
            "email": operator_email,
            "requestId": request_id
        }

        # If debug is set..
        api_logger.info('check_sso_login function:')

        response = self._parent_class.post.login(data=data)

        # If valid response, but no token.
        if not response.cgx_content.get('x_auth_token'):
            # no valid login yet.
            return response

        # update with token and region
        auth_region = self._parent_class.parse_region(response)
        self._parent_class.update_region_to_controller(auth_region)
        self._parent_class.reparse_login_cookie_after_region_update(response)

        return response

    def logout(self, force=False):
        """
        Interactive logout - ensures uid/tid cleared so `cloudgenix.API` object/ requests.Session can be re-used.

        **Parameters:**:

          - **force**: Bool, force logout API call, even when using a static AUTH_TOKEN.

        **Returns:** Bool of whether the operation succeeded.
        """
        # Extract requests session for manipulation.
        session = self._parent_class.expose_session()

        # if force = True, or token_session = None/False, call logout API.
        if force or not self._parent_class.token_session:
            # Call Logout
            result = self._parent_class.get.logout()
            if result.cgx_status:
                # clear info from session.
                self._parent_class.tenant_id = None
                self._parent_class.tenant_name = None
                self._parent_class.is_esp = None
                self._parent_class.client_id = None
                self._parent_class.address_string = None
                self._parent_class.email = None
                self._parent_class._user_id = None
                self._parent_class._password = None
                self._parent_class.roles = None
                self._parent_class.token_session = None
                # Cookies are removed via LOGOUT API call. if X-Auth-Token set, clear.
                if session.headers.get('X-Auth-Token'):
                    self._parent_class.remove_header('X-Auth-Token')

            return result.cgx_status

        else:
            # Token Session and not forced.
            api_logger.debug('TOKEN SESSION, LOGOUT API NOT CALLED.')
            # clear info from session.
            self._parent_class.tenant_id = None
            self._parent_class.tenant_name = None
            self._parent_class.is_esp = None
            self._parent_class.client_id = None
            self._parent_class.address_string = None
            self._parent_class.email = None
            self._parent_class._user_id = None
            self._parent_class._password = None
            self._parent_class.roles = None
            self._parent_class.token_session = None
            # if X-Auth-Token set, clear.
            if session.headers.get('X-Auth-Token'):
                self._parent_class.remove_header('X-Auth-Token')

            return True

    @staticmethod
    def jd(api_response):
        """
        JD (JSON Dump) function. Meant for quick pretty-printing of CloudGenix Response objects.

        Example: `jd(cgx_sess.get.sites())`

        **Returns:** No Return, directly prints all output.
        """
        try:
            # attempt to print the cgx_content. should always be a Dict if it exists.
            print(json.dumps(api_response.cgx_content, indent=4))
        except (TypeError, ValueError, AttributeError):
            # cgx_content did not exist, or was not JSON serializable. Try pretty printing the base obj.
            try:
                print(json.dumps(api_response, indent=4))
            except (TypeError, ValueError, AttributeError):
                # Same issue, just raw print the passed data. Let any exceptions happen here.
                print(api_response)
        return

    @staticmethod
    def quick_confirm(prompt, default_value):
        """
        Function to display a quick confirmation for user input

        **Parameters:**

          - **prompt:** Text to display before confirm
          - **default_value:** Default value for no entry

        **Returns:** 'y', 'n', or Default value.
        """
        valid = False
        value = default_value.lower()
        while not valid:
            input_val = compat_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                value = default_value.lower()
                valid = True
            else:
                try:
                    if input_val.lower() in ['y', 'n']:
                        value = input_val.lower()
                        valid = True
                    else:
                        print("ERROR: enter 'Y' or 'N'.")
                        valid = False

                except ValueError:
                    print("ERROR: enter 'Y' or 'N'.")
                    valid = False

        return value

    @staticmethod
    def quick_int_input(prompt, default_value, min_val=1, max_val=30):
        """
        Function to display a quick question for integer user input

        **Parameters:**

          - **prompt:** Text / question to display
          - **default_value:** Default value for no entry
          - **min_val:** Lowest allowed integer
          - **max_val:** Highest allowed integer

        **Returns:** integer or default_value.
        """
        valid = False
        num_val = default_value
        while not valid:
            input_val = compat_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                num_val = default_value
                valid = True
            else:
                try:
                    num_val = int(input_val)
                    if min_val <= num_val <= max_val:
                        valid = True
                    else:
                        print("ERROR: must be between {0} and {1}.".format(min, max))
                        valid = False

                except ValueError:
                    print("ERROR: must be a number.")
                    valid = False

        return num_val

    @staticmethod
    def quick_str_input(prompt, default_value):
        """
        Function to display a quick question for text input.

        **Parameters:**

          - **prompt:** Text / question to display
          - **default_value:** Default value for no entry

        **Returns:** text_type() or default_value.
        """
        valid = False
        str_val = default_value
        while not valid:
            input_val = raw_input(prompt + "[{0}]: ".format(default_value))

            if input_val == "":
                str_val = default_value
                valid = True
            else:
                try:
                    str_val = text_type(input_val)
                    valid = True

                except ValueError:
                    print("ERROR: must be text.")
                    valid = False

        return str_val
