#!/usr/bin/env python
"""
CloudGenix Explicit CA Certificate Bundle for API calls (CA Pinning).

**Author:** CloudGenix

**Copyright:** (c) 2017, 2018 CloudGenix, Inc

**License:** MIT
"""
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

# DigiCert Global Root G2
# verisign class 3 public primary certification authority - g4
# VeriSign Universal Root Certification Authority
CG_CA_BUNDLE = b"-----BEGIN CERTIFICATE-----\n" \
               b"MIIDjjCCAnagAwIBAgIQAzrx5qcRqaC7KGSxHQn65TANBgkqhkiG9w0BAQsFADBh\n" \
               b"MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3\n" \
               b"d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBH\n" \
               b"MjAeFw0xMzA4MDExMjAwMDBaFw0zODAxMTUxMjAwMDBaMGExCzAJBgNVBAYTAlVT\n" \
               b"MRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5j\n" \
               b"b20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IEcyMIIBIjANBgkqhkiG\n" \
               b"9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzfNNNx7a8myaJCtSnX/RrohCgiN9RlUyfuI\n" \
               b"2/Ou8jqJkTx65qsGGmvPrC3oXgkkRLpimn7Wo6h+4FR1IAWsULecYxpsMNzaHxmx\n" \
               b"1x7e/dfgy5SDN67sH0NO3Xss0r0upS/kqbitOtSZpLYl6ZtrAGCSYP9PIUkY92eQ\n" \
               b"q2EGnI/yuum06ZIya7XzV+hdG82MHauVBJVJ8zUtluNJbd134/tJS7SsVQepj5Wz\n" \
               b"tCO7TG1F8PapspUwtP1MVYwnSlcUfIKdzXOS0xZKBgyMUNGPHgm+F6HmIcr9g+UQ\n" \
               b"vIOlCsRnKPZzFBQ9RnbDhxSJITRNrw9FDKZJobq7nMWxM4MphQIDAQABo0IwQDAP\n" \
               b"BgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUTiJUIBiV\n" \
               b"5uNu5g/6+rkS7QYXjzkwDQYJKoZIhvcNAQELBQADggEBAGBnKJRvDkhj6zHd6mcY\n" \
               b"1Yl9PMWLSn/pvtsrF9+wX3N3KjITOYFnQoQj8kVnNeyIv/iPsGEMNKSuIEyExtv4\n" \
               b"NeF22d+mQrvHRAiGfzZ0JFrabA0UWTW98kndth/Jsw1HKj2ZL7tcu7XUIOGZX1NG\n" \
               b"Fdtom/DzMNU+MeKNhJ7jitralj41E6Vf8PlwUHBHQRFXGU7Aj64GxJUTFy8bJZ91\n" \
               b"8rGOmaFvE7FBcf6IKshPECBV1/MUReXgRPTqh5Uykw7+U0b6LJ3/iyK5S9kJRaTe\n" \
               b"pLiaWN0bfVKfjllDiIGknibVb63dDcY3fe0Dkhvld1927jyNxF1WW6LZZm6zNTfl\n" \
               b"MrY=\n" \
               b"-----END CERTIFICATE-----\n" \
               b"-----BEGIN CERTIFICATE-----\n" \
               b"MIIDhDCCAwqgAwIBAgIQL4D+I4wOIg9IZxIokYesszAKBggqhkjOPQQDAzCByjEL\n" \
               b"MAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZW\n" \
               b"ZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNyBWZXJpU2ln\n" \
               b"biwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxWZXJp\n" \
               b"U2lnbiBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0aG9y\n" \
               b"aXR5IC0gRzQwHhcNMDcxMTA1MDAwMDAwWhcNMzgwMTE4MjM1OTU5WjCByjELMAkG\n" \
               b"A1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZWZXJp\n" \
               b"U2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwNyBWZXJpU2lnbiwg\n" \
               b"SW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MUUwQwYDVQQDEzxWZXJpU2ln\n" \
               b"biBDbGFzcyAzIFB1YmxpYyBQcmltYXJ5IENlcnRpZmljYXRpb24gQXV0aG9yaXR5\n" \
               b"IC0gRzQwdjAQBgcqhkjOPQIBBgUrgQQAIgNiAASnVnp8Utpkmw4tXNherJI9/gHm\n" \
               b"GUo9FANL+mAnINmDiWn6VMaaGF5VKmTeBvaNSjutEDxlPZCIBIngMGGzrl0Bp3ve\n" \
               b"fLK+ymVhAIau2o970ImtTR1ZmkGxvEeA3J5iw/mjgbIwga8wDwYDVR0TAQH/BAUw\n" \
               b"AwEB/zAOBgNVHQ8BAf8EBAMCAQYwbQYIKwYBBQUHAQwEYTBfoV2gWzBZMFcwVRYJ\n" \
               b"aW1hZ2UvZ2lmMCEwHzAHBgUrDgMCGgQUj+XTGoasjY5rw8+AatRIGCx7GS4wJRYj\n" \
               b"aHR0cDovL2xvZ28udmVyaXNpZ24uY29tL3ZzbG9nby5naWYwHQYDVR0OBBYEFLMW\n" \
               b"kf3upm7ktS5Jj4d4gYDs5bG1MAoGCCqGSM49BAMDA2gAMGUCMGYhDBgmYFo4e1ZC\n" \
               b"4Kf8NoRRkSAsdk1DPcQdhCPQrNZ8NQbOzWm9kA3bbEhCHQ6qQgIxAJw9SDkjOVga\n" \
               b"FRJZap7v1VmyHVIsmXHNxynfGyphe3HR3vPA5Q06Sqotp9iGKt0uEA==\n" \
               b"-----END CERTIFICATE-----\n" \
               b"-----BEGIN CERTIFICATE-----\n" \
               b"MIIEuTCCA6GgAwIBAgIQQBrEZCGzEyEDDrvkEhrFHTANBgkqhkiG9w0BAQsFADCB\n" \
               b"vTELMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQL\n" \
               b"ExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMTowOAYDVQQLEzEoYykgMjAwOCBWZXJp\n" \
               b"U2lnbiwgSW5jLiAtIEZvciBhdXRob3JpemVkIHVzZSBvbmx5MTgwNgYDVQQDEy9W\n" \
               b"ZXJpU2lnbiBVbml2ZXJzYWwgUm9vdCBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTAe\n" \
               b"Fw0wODA0MDIwMDAwMDBaFw0zNzEyMDEyMzU5NTlaMIG9MQswCQYDVQQGEwJVUzEX\n" \
               b"MBUGA1UEChMOVmVyaVNpZ24sIEluYy4xHzAdBgNVBAsTFlZlcmlTaWduIFRydXN0\n" \
               b"IE5ldHdvcmsxOjA4BgNVBAsTMShjKSAyMDA4IFZlcmlTaWduLCBJbmMuIC0gRm9y\n" \
               b"IGF1dGhvcml6ZWQgdXNlIG9ubHkxODA2BgNVBAMTL1ZlcmlTaWduIFVuaXZlcnNh\n" \
               b"bCBSb290IENlcnRpZmljYXRpb24gQXV0aG9yaXR5MIIBIjANBgkqhkiG9w0BAQEF\n" \
               b"AAOCAQ8AMIIBCgKCAQEAx2E3XrEBNNti1xWb/1hajCMj1mCOkdeQmIN65lgZOIzF\n" \
               b"9uVkhbSicfvtvbnazU0AtMgtc6XHaXGVHzk8skQHnOgO+k1KxCHfKWGPMiJhgsWH\n" \
               b"H26MfF8WIFFE0XBPV+rjHOPMee5Y2A7Cs0WTwCznmhcrewA3ekEzeOEz4vMQGn+H\n" \
               b"LL729fdC4uW/h2KJXwBL38Xd5HVEMkE6HnFuacsLdUYI0crSK5XQz/u5QGtkjFdN\n" \
               b"/BMReYTtXlT2NJ8IAfMQJQYXStrxHXpma5hgZqTZ79IugvHw7wnqRMkVauIDbjPT\n" \
               b"rJ9VAMf2CGqUuV/c4DPxhGD5WycRtPwW8rtWaoAljQIDAQABo4GyMIGvMA8GA1Ud\n" \
               b"EwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEGMG0GCCsGAQUFBwEMBGEwX6FdoFsw\n" \
               b"WTBXMFUWCWltYWdlL2dpZjAhMB8wBwYFKw4DAhoEFI/l0xqGrI2Oa8PPgGrUSBgs\n" \
               b"exkuMCUWI2h0dHA6Ly9sb2dvLnZlcmlzaWduLmNvbS92c2xvZ28uZ2lmMB0GA1Ud\n" \
               b"DgQWBBS2d/ppSEefUxLVwuoHMnYH0ZcHGTANBgkqhkiG9w0BAQsFAAOCAQEASvj4\n" \
               b"sAPmLGd75JR3Y8xuTPl9Dg3cyLk1uXBPY/ok+myDjEedO2Pzmvl2MpWRsXe8rJq+\n" \
               b"seQxIcaBlVZaDrHC1LGmWazxY8u4TB1ZkErvkBYoH1quEPuBUDgMbMzxPcP1Y+Oz\n" \
               b"4yHJJDnp/RVmRvQbEdBNc6N9Rvk97ahfYtTxP/jgdFcrGJ2BtMQo2pSXpXDrrB2+\n" \
               b"BxHw1dvd5Yzw1TKwg+ZX4o+/vqGqvz0dtdQ46tewXDpPaj+PwGZsY6rp2aQW9IHR\n" \
               b"lRQOfc2VNNnSj3BzgXucfr2YYdhFh5iQxeuGMMY1v/D/w1WIg0vvBZIGcfK4mJO3\n" \
               b"7M2CYfE45k+XmCpajQ==\n" \
               b"-----END CERTIFICATE-----\n"
"""
The license for the content in CA Root certificates may differ from the license the code file they are contained in.
For more info, see the CA certificate page corosponding to the root CA certificate:
  
  * <https://www.digicert.com/digicert-root-certificates.htm>
  * <https://www.symantec.com/theme/roots>
"""
