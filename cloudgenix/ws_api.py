#!/usr/bin/env python
"""
CloudGenix Python SDK - WebSocket Functions

**Author:** CloudGenix

**Copyright:** (c) 2017-2021 CloudGenix, Inc

**License:** MIT
"""
import logging

__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2021, 2019 CloudGenix, Inc"
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
"""`logging.getlogger` object to enable debug printing via `cloudgenix.API.set_debug`"""


class WebSockets(object):
    """
    CloudGenix Python SDK - WebSocket Functions

    Object to handle WebSocket operations.
    """

    # placeholder for parent class namespace
    _parent_class = None

    def toolkit_session(self, element_id, tenant_id=None, api_version="v2.0", cols=207, rows=53, **kwargs):
        """
        Open a Toolkit Session WebSocket

          **Parameters:**:

          - **element_id**: Element ID
          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)
          - **cols**: Optional: Integer, Number of columns for terminal (default 207)
          - **rows**: Optional: Integer, Number of rows for terminal (default 53)
          - **&ast;&ast;kwargs**: Optional: Additional Keyword Arguments to pass to `websockets.client.Connect()`

        **Returns:** `websockets.client.Connect` object.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        # set controller, converting protocol to wss
        wss_ctlr = self._parent_class.controller.replace('https://', 'wss://', 1)

        url = str(wss_ctlr) + "/{}/api/tenants/{}/elements/{}/ws/toolkitsessions?cols={}&rows={}" \
                              "".format(api_version, tenant_id, element_id, cols, rows)

        api_logger.debug("URL = %s", url)
        return self._parent_class.websocket_call(url, **kwargs)

    def default(self, tenant_id=None, api_version="v2.0", **kwargs):
        """
        Open the default Tenant WebSocket for use in multiple functions.

          **Parameters:**:

          - **tenant_id**: Tenant ID
          - **api_version**: API version to use (default v2.0)
          - **&ast;&ast;kwargs**: Optional: Additional Keyword Arguments to pass to `websockets.client.Connect()`

        **Returns:** `websockets.client.Connect` object.
        """

        if tenant_id is None and self._parent_class.tenant_id:
            # Pull tenant_id from parent namespace cache.
            tenant_id = self._parent_class.tenant_id
        elif not tenant_id:
            # No value for tenant_id.
            raise TypeError("tenant_id is required but not set or cached.")
        # set controller, converting protocol to wss
        wss_ctlr = self._parent_class.controller.replace('https://', 'wss://', 1)

        url = str(wss_ctlr) + "/{}/api/tenants/{}/ws" \
                              "".format(api_version, tenant_id)

        api_logger.debug("URL = %s", url)
        return self._parent_class.websocket_call(url, **kwargs)
