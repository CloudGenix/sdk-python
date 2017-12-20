#!/usr/bin/env python
"""
CGNX API -> list sites, example proof of concept.

**Author:** CloudGenix

**Copyright:** (c) 2017 CloudGenix, Inc

**License:** MIT
"""
__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017 CloudGenix, Inc

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
# standard modules
import argparse
import json
import logging

# CloudGenix Python SDK
import cloudgenix

# Global Vars
SDK_VERSION = cloudgenix.version
SCRIPT_NAME = 'CloudGenix Python SDK demo'

# Set logging to use function name
logger = logging.getLogger(__name__)


############################################################################
# Begin Script, parse arguments.
############################################################################

# Parse arguments
parser = argparse.ArgumentParser(description="{0}.".format(SCRIPT_NAME))

# Allow Controller modification and debug level sets.
controller_group = parser.add_argument_group('API', 'These options change how this program connects to the API.')
controller_group.add_argument("--controller", "-C",
                              help="Controller URI, ex. https://api.cloudgenix.com:8443",
                              default=None)

controller_group.add_argument("--insecure", "-I", help="Disable SSL certificate and hostname verification",
                              dest='verify', action='store_false', default=True)

login_group = parser.add_argument_group('Login', 'These options allow skipping of interactive login')
login_group.add_argument("--email", "-E", help="Use this email as User Name instead of prompting",
                         default=None)
login_group.add_argument("--pass", "-PW", help="Use this Password instead of prompting",
                         default=None)

debug_group = parser.add_argument_group('Debug', 'These options enable debugging output')
debug_group.add_argument("--debug", "-D", help="Verbose Debug info, levels 0-2", type=int,
                         default=0)

args = vars(parser.parse_args())

if args['debug'] == 1:
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    logger.setLevel(logging.INFO)
elif args['debug'] >= 2:
    logging.basicConfig(level=logging.DEBUG,
                        format="%(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s")
    logger.setLevel(logging.DEBUG)
else:
    # Remove all handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # set logging level to default
    logger.setLevel(logging.WARNING)

############################################################################
# Instantiate API
############################################################################


cgx_session = cloudgenix.API(controller=args["controller"], ssl_verify=args["verify"])

# set debug
cgx_session.set_debug(args["debug"])


############################################################################
# Draw Interactive login banner, run interactive login including args above.
############################################################################

print("{0} v{1} ({2})\n".format(SCRIPT_NAME, SDK_VERSION, cgx_session.controller))

# interactive or cmd-line specified initial login

while cgx_session.tenant_name is None:
    cgx_session.interactive.login(args["email"], args["pass"])


############################################################################
# End Login handling, begin script..
############################################################################

# Get list of sites.
response = cgx_session.get.sites()

# status is a boolean based on success/failure. If success, print raw dictionary
if response.cgx_status:
    raw_sites_dict = response.cgx_content
    # Print as formatted JSON
    print(json.dumps(raw_sites_dict, indent=4))

# else, let user know something didn't work.
else:
    print("ERROR: ", json.dumps(response.cgx_content, indent=4))

# end of script, run logout to clear session.
print(cgx_session.get.logout().cgx_content)
