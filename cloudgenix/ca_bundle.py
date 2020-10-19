#!/usr/bin/env python
"""
CloudGenix Explicit CA Certificate Bundle for API calls (CA Pinning).

**Author:** CloudGenix

**Copyright:** (c) 2017-2020 CloudGenix, Inc

**License:** MIT
"""
__author__ = "CloudGenix Developer Support <developers@cloudgenix.com>"
__email__ = "developers@cloudgenix.com"
__copyright__ = "Copyright (c) 2017-2020 CloudGenix, Inc"
__license__ = """
    MIT License

    Copyright (c) 2017-2020 CloudGenix, Inc

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
               b"-----END CERTIFICATE-----\n"\
               b"-----BEGIN CERTIFICATE-----\n"\
               b"MIIFiTCCA3GgAwIBAgIQZN+1WMr1hpVLEjM/La0d9jANBgkqhkiG9w0BAQsFADBX\n"\
               b"MQswCQYDVQQGEwJVUzEfMB0GA1UEChMWUGFsbyBBbHRvIE5ldHdvcmtzIEluYzEn\n"\
               b"MCUGA1UEAxMeUGFsbyBBbHRvIE5ldHdvcmtzIEluYyBSb290IENBMB4XDTE1MTAw\n"\
               b"NzIxNDQ1NFoXDTM1MTAwNzIxNTE0MlowVzELMAkGA1UEBhMCVVMxHzAdBgNVBAoT\n"\
               b"FlBhbG8gQWx0byBOZXR3b3JrcyBJbmMxJzAlBgNVBAMTHlBhbG8gQWx0byBOZXR3\n"\
               b"b3JrcyBJbmMgUm9vdCBDQTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIB\n"\
               b"ALxxMafelzkheljFgA22w1Ng0bMTS+mjjZCx4eUwKpneTWAY1FMOC56da0F+uYoL\n"\
               b"2NUKqQ8pg/hT0ua+4q5y4MZ9NnR/LMrhfNDJ9vAOOJ6n0zZtIdBipKj5TfhdAOOX\n"\
               b"FJj6Qgm9+nDAKC2tDdlEEme/rMVpgGkWO7oS03EdfSmQw5ytfQsRVBdEWuMOxoNH\n"\
               b"D0x2TtDbnBYB5HfMIgwPZeQgr7XyVKBZvkDU0hQ33XnNcLqpc/9ZdKDD5mPrgDQV\n"\
               b"vTai4EDqEAbs72ZEr3+LwvL1jVEVW+4gcB4aWpEaHhnFR1Hmgao8dDCCScDMWod0\n"\
               b"4qiBFIbBETikHihJTXZkuaikTtPBvlIauZ0d0aZroN54HtTD2FWvKRFbcBXlV727\n"\
               b"diG3fL1twRZ6mAiPXiKOikCubX19B4ZuZ3rp9WP38IyFkW/x3rTOFk2kthy75Zw2\n"\
               b"JVS/6ebv0XwtMyNQKFJE5K2hlt588zs1rZT5+k+TAIgyNGied6mRtzS1yO5qc8bi\n"\
               b"lMn0JvMGLCV42KnpB17AfvVnWR520jDBulgPwYOKL+tiOKMiaRRU441AKN08FY3Q\n"\
               b"qRTmr04REpLTBjo7vyktimT0D/R6Fjutb8cDhck/kXyZ2IXNZ7tTrfK1C+TWj25d\n"\
               b"kjbMemrDBjfq0yyTCcAaUE8spDR4PCWSy0bPGgRooDnLAgMBAAGjUTBPMAsGA1Ud\n"\
               b"DwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBRtHWMHo92KvO9jzgay\n"\
               b"YMpp3LLGWjAQBgkrBgEEAYI3FQEEAwIBADANBgkqhkiG9w0BAQsFAAOCAgEAjUMB\n"\
               b"3KN2QIsIolDI9PcQstVWg6EvLyzLRaY67Z5JmjnKCnZhjuu0NcYhdgqDuRE/zgG4\n"\
               b"47bu3+eoRHdqqy4eTvS3DFHmQoCItKkxv6V7K6CjCJTFjcgA8QcWeGPSyFOwiBhZ\n"\
               b"IhKzZnzdDZrrKzzRoj6vkMkiVxWNx3nUbGicqjOvC/ks1XTlen6yHk3EMK/tf9rq\n"\
               b"rPMkEPdwNY95ylEGOT89h2EnjDVbKMMhZNyeVqzlLFdTzFGaUQE0SqHYr9Yr90sB\n"\
               b"9+uSs22qzbwrUAtu2tWykXJR3Fz1LLUMz2MoUM7rH2Jv/fqulwSAPClC3AtASGrC\n"\
               b"Y7L6Xl6ZzhWPqFC7mjxSH76egZcWphDfcNCppglfnNyM0xh/fKKifvLVhAkYBNSh\n"\
               b"yOv6BuJLyzUo3tNjqMpWPpOVEXQa4I4tD8JQD1CDYS2YrGrDWSkiEf+t2aLE5QkW\n"\
               b"mjNy6nOfoS0BEr1Zi+imlqgtKEfdl631osAATo4VzNLR5kF8Q4wvltUUYnQkzUm0\n"\
               b"+8wvFpjg842crHtwpdyy4ERlll2bGXEVhj06DxyUAhzIKdDQUdiUhkRgZdceAsvc\n"\
               b"m4nctCDD+BOuq/Iv9h3rcnjvirHJ/2HSm48t50fmK5jKXrH/z2DsSxhWSsEjxqJR\n"\
               b"KNsRVnN03VKtOjHgTFvoDZPZ0nzIlwEJREuOV1w=\n"\
               b"-----END CERTIFICATE-----\n"



"""
The license for the content in CA Root certificates may differ from the license the code file they are contained in.
For more info, see the CA certificate page corosponding to the root CA certificate:
  
  * <https://www.digicert.com/digicert-root-certificates.htm>
"""
