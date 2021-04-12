#!/usr/bin/env python
"""
CloudGenix Explicit CA Certificate Bundle for API calls (CA Pinning).

**Author:** CloudGenix

**Copyright:** (c) 2017-2021 CloudGenix, Inc

**License:** MIT
"""
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

# DigiCert Global Root G2
# Palo Alto Networks Inc Root CA
# Go Daddy Root Certificate Authority - G2
# Starfield Root Certificate Authority - G2
# Go Daddy Class 2 Certification Authority
# Starfield Class 2 Certification Authority
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
               b"-----END CERTIFICATE-----\n"\
               b"-----BEGIN CERTIFICATE-----\n" \
               b"MIIDxTCCAq2gAwIBAgIBADANBgkqhkiG9w0BAQsFADCBgzELMAkGA1UEBhMCVVMx\n"\
               b"EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxGjAYBgNVBAoT\n"\
               b"EUdvRGFkZHkuY29tLCBJbmMuMTEwLwYDVQQDEyhHbyBEYWRkeSBSb290IENlcnRp\n"\
               b"ZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTA5MDkwMTAwMDAwMFoXDTM3MTIzMTIz\n"\
               b"NTk1OVowgYMxCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQH\n"\
               b"EwpTY290dHNkYWxlMRowGAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjExMC8GA1UE\n"\
               b"AxMoR28gRGFkZHkgUm9vdCBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkgLSBHMjCCASIw\n"\
               b"DQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL9xYgjx+lk09xvJGKP3gElY6SKD\n"\
               b"E6bFIEMBO4Tx5oVJnyfq9oQbTqC023CYxzIBsQU+B07u9PpPL1kwIuerGVZr4oAH\n"\
               b"/PMWdYA5UXvl+TW2dE6pjYIT5LY/qQOD+qK+ihVqf94Lw7YZFAXK6sOoBJQ7Rnwy\n"\
               b"DfMAZiLIjWltNowRGLfTshxgtDj6AozO091GB94KPutdfMh8+7ArU6SSYmlRJQVh\n"\
               b"GkSBjCypQ5Yj36w6gZoOKcUcqeldHraenjAKOc7xiID7S13MMuyFYkMlNAJWJwGR\n"\
               b"tDtwKj9useiciAF9n9T521NtYJ2/LOdYq7hfRvzOxBsDPAnrSTFcaUaz4EcCAwEA\n"\
               b"AaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYE\n"\
               b"FDqahQcQZyi27/a9BUFuIMGU2g/eMA0GCSqGSIb3DQEBCwUAA4IBAQCZ21151fmX\n"\
               b"WWcDYfF+OwYxdS2hII5PZYe096acvNjpL9DbWu7PdIxztDhC2gV7+AJ1uP2lsdeu\n"\
               b"9tfeE8tTEH6KRtGX+rcuKxGrkLAngPnon1rpN5+r5N9ss4UXnT3ZJE95kTXWXwTr\n"\
               b"gIOrmgIttRD02JDHBHNA7XIloKmf7J6raBKZV8aPEjoJpL1E/QYVN8Gb5DKj7Tjo\n"\
               b"2GTzLH4U/ALqn83/B2gX2yKQOC16jdFU8WnjXzPKej17CuPKf1855eJ1usV2GDPO\n"\
               b"LPAvTK33sefOT6jEm0pUBsV/fdUID+Ic/n4XuKxe9tQWskMJDE32p2u0mYRlynqI\n"\
               b"4uJEvlz36hz1\n"\
               b"-----END CERTIFICATE-----\n"\
               b"-----BEGIN CERTIFICATE-----\n"\
               b"MIID3TCCAsWgAwIBAgIBADANBgkqhkiG9w0BAQsFADCBjzELMAkGA1UEBhMCVVMx\n"\
               b"EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT\n"\
               b"HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xMjAwBgNVBAMTKVN0YXJmaWVs\n"\
               b"ZCBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTA5MDkwMTAwMDAw\n"\
               b"MFoXDTM3MTIzMTIzNTk1OVowgY8xCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6\n"\
               b"b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMSUwIwYDVQQKExxTdGFyZmllbGQgVGVj\n"\
               b"aG5vbG9naWVzLCBJbmMuMTIwMAYDVQQDEylTdGFyZmllbGQgUm9vdCBDZXJ0aWZp\n"\
               b"Y2F0ZSBBdXRob3JpdHkgLSBHMjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\n"\
               b"ggEBAL3twQP89o/8ArFvW59I2Z154qK3A2FWGMNHttfKPTUuiUP3oWmb3ooa/RMg\n"\
               b"nLRJdzIpVv257IzdIvpy3Cdhl+72WoTsbhm5iSzchFvVdPtrX8WJpRBSiUZV9Lh1\n"\
               b"HOZ/5FSuS/hVclcCGfgXcVnrHigHdMWdSL5stPSksPNkN3mSwOxGXn/hbVNMYq/N\n"\
               b"Hwtjuzqd+/x5AJhhdM8mgkBj87JyahkNmcrUDnXMN/uLicFZ8WJ/X7NfZTD4p7dN\n"\
               b"dloedl40wOiWVpmKs/B/pM293DIxfJHP4F8R+GuqSVzRmZTRouNjWwl2tVZi4Ut0\n"\
               b"HZbUJtQIBFnQmA4O5t78w+wfkPECAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAO\n"\
               b"BgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFHwMMh+n2TB/xH1oo2Kooc6rB1snMA0G\n"\
               b"CSqGSIb3DQEBCwUAA4IBAQARWfolTwNvlJk7mh+ChTnUdgWUXuEok21iXQnCoKjU\n"\
               b"sHU48TRqneSfioYmUeYs0cYtbpUgSpIB7LiKZ3sx4mcujJUDJi5DnUox9g61DLu3\n"\
               b"4jd/IroAow57UvtruzvE03lRTs2Q9GcHGcg8RnoNAX3FWOdt5oUwF5okxBDgBPfg\n"\
               b"8n/Uqgr/Qh037ZTlZFkSIHc40zI+OIF1lnP6aI+xy84fxez6nH7PfrHxBy22/L/K\n"\
               b"pL/QlwVKvOoYKAKQvVR4CSFx09F9HdkWsKlhPdAKACL8x3vLCWRFCztAgfd9fDL1\n"\
               b"mMpYjn0q7pBZc2T5NnReJaH1ZgUufzkVqSr7UIuOhWn0\n"\
               b"-----END CERTIFICATE-----\n"\
               b"-----BEGIN CERTIFICATE-----\n"\
               b"MIIEADCCAuigAwIBAgIBADANBgkqhkiG9w0BAQUFADBjMQswCQYDVQQGEwJVUzEh\n"\
               b"MB8GA1UEChMYVGhlIEdvIERhZGR5IEdyb3VwLCBJbmMuMTEwLwYDVQQLEyhHbyBE\n"\
               b"YWRkeSBDbGFzcyAyIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MB4XDTA0MDYyOTE3\n"\
               b"MDYyMFoXDTM0MDYyOTE3MDYyMFowYzELMAkGA1UEBhMCVVMxITAfBgNVBAoTGFRo\n"\
               b"ZSBHbyBEYWRkeSBHcm91cCwgSW5jLjExMC8GA1UECxMoR28gRGFkZHkgQ2xhc3Mg\n"\
               b"MiBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTCCASAwDQYJKoZIhvcNAQEBBQADggEN\n"\
               b"ADCCAQgCggEBAN6d1+pXGEmhW+vXX0iG6r7d/+TvZxz0ZWizV3GgXne77ZtJ6XCA\n"\
               b"PVYYYwhv2vLM0D9/AlQiVBDYsoHUwHU9S3/Hd8M+eKsaA7Ugay9qK7HFiH7Eux6w\n"\
               b"wdhFJ2+qN1j3hybX2C32qRe3H3I2TqYXP2WYktsqbl2i/ojgC95/5Y0V4evLOtXi\n"\
               b"EqITLdiOr18SPaAIBQi2XKVlOARFmR6jYGB0xUGlcmIbYsUfb18aQr4CUWWoriMY\n"\
               b"avx4A6lNf4DD+qta/KFApMoZFv6yyO9ecw3ud72a9nmYvLEHZ6IVDd2gWMZEewo+\n"\
               b"YihfukEHU1jPEX44dMX4/7VpkI+EdOqXG68CAQOjgcAwgb0wHQYDVR0OBBYEFNLE\n"\
               b"sNKR1EwRcbNhyz2h/t2oatTjMIGNBgNVHSMEgYUwgYKAFNLEsNKR1EwRcbNhyz2h\n"\
               b"/t2oatTjoWekZTBjMQswCQYDVQQGEwJVUzEhMB8GA1UEChMYVGhlIEdvIERhZGR5\n"\
               b"IEdyb3VwLCBJbmMuMTEwLwYDVQQLEyhHbyBEYWRkeSBDbGFzcyAyIENlcnRpZmlj\n"\
               b"YXRpb24gQXV0aG9yaXR5ggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQAD\n"\
               b"ggEBADJL87LKPpH8EsahB4yOd6AzBhRckB4Y9wimPQoZ+YeAEW5p5JYXMP80kWNy\n"\
               b"OO7MHAGjHZQopDH2esRU1/blMVgDoszOYtuURXO1v0XJJLXVggKtI3lpjbi2Tc7P\n"\
               b"TMozI+gciKqdi0FuFskg5YmezTvacPd+mSYgFFQlq25zheabIZ0KbIIOqPjCDPoQ\n"\
               b"HmyW74cNxA9hi63ugyuV+I6ShHI56yDqg+2DzZduCLzrTia2cyvk0/ZM/iZx4mER\n"\
               b"dEr/VxqHD3VILs9RaRegAhJhldXRQLIQTO7ErBBDpqWeCtWVYpoNz4iCxTIM5Cuf\n"\
               b"ReYNnyicsbkqWletNw+vHX/bvZ8=\n"\
               b"-----END CERTIFICATE-----\n"\
               b"-----BEGIN CERTIFICATE-----\n"\
               b"MIIEDzCCAvegAwIBAgIBADANBgkqhkiG9w0BAQUFADBoMQswCQYDVQQGEwJVUzEl\n"\
               b"MCMGA1UEChMcU3RhcmZpZWxkIFRlY2hub2xvZ2llcywgSW5jLjEyMDAGA1UECxMp\n"\
               b"U3RhcmZpZWxkIENsYXNzIDIgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMDQw\n"\
               b"NjI5MTczOTE2WhcNMzQwNjI5MTczOTE2WjBoMQswCQYDVQQGEwJVUzElMCMGA1UE\n"\
               b"ChMcU3RhcmZpZWxkIFRlY2hub2xvZ2llcywgSW5jLjEyMDAGA1UECxMpU3RhcmZp\n"\
               b"ZWxkIENsYXNzIDIgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwggEgMA0GCSqGSIb3\n"\
               b"DQEBAQUAA4IBDQAwggEIAoIBAQC3Msj+6XGmBIWtDBFk385N78gDGIc/oav7PKaf\n"\
               b"8MOh2tTYbitTkPskpD6E8J7oX+zlJ0T1KKY/e97gKvDIr1MvnsoFAZMej2YcOadN\n"\
               b"+lq2cwQlZut3f+dZxkqZJRRU6ybH838Z1TBwj6+wRir/resp7defqgSHo9T5iaU0\n"\
               b"X9tDkYI22WY8sbi5gv2cOj4QyDvvBmVmepsZGD3/cVE8MC5fvj13c7JdBmzDI1aa\n"\
               b"K4UmkhynArPkPw2vCHmCuDY96pzTNbO8acr1zJ3o/WSNF4Azbl5KXZnJHoe0nRrA\n"\
               b"1W4TNSNe35tfPe/W93bC6j67eA0cQmdrBNj41tpvi/JEoAGrAgEDo4HFMIHCMB0G\n"\
               b"A1UdDgQWBBS/X7fRzt0fhvRbVazc1xDCDqmI5zCBkgYDVR0jBIGKMIGHgBS/X7fR\n"\
               b"zt0fhvRbVazc1xDCDqmI56FspGowaDELMAkGA1UEBhMCVVMxJTAjBgNVBAoTHFN0\n"\
               b"YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xMjAwBgNVBAsTKVN0YXJmaWVsZCBD\n"\
               b"bGFzcyAyIENlcnRpZmljYXRpb24gQXV0aG9yaXR5ggEAMAwGA1UdEwQFMAMBAf8w\n"\
               b"DQYJKoZIhvcNAQEFBQADggEBAAWdP4id0ckaVaGsafPzWdqbAYcaT1epoXkJKtv3\n"\
               b"L7IezMdeatiDh6GX70k1PncGQVhiv45YuApnP+yz3SFmH8lU+nLMPUxA2IGvd56D\n"\
               b"eruix/U0F47ZEUD0/CwqTRV/p2JdLiXTAAsgGh1o+Re49L2L7ShZ3U0WixeDyLJl\n"\
               b"xy16paq8U4Zt3VekyvggQQto8PT7dL5WXXp59fkdheMtlb71cZBDzI0fmgAKhynp\n"\
               b"VSJYACPq4xJDKVtHCN2MQWplBqjlIapBtJUhlbl90TSrE9atvNziPTnNvT51cKEY\n"\
               b"WQPJIrSPnNVeKtelttQKbfi3QBFGmh95DmK/D5fs4C8fF5Q=\n"\
               b"-----END CERTIFICATE-----\n"

"""
The license for the content in CA Root certificates may differ from the license the code file they are contained in.
For more info, see the CA certificate page corresponding to the root CA certificate:
  * <https://www.digicert.com/digicert-root-certificates.htm>
  * <https://certs.godaddy.com/repository>
"""
