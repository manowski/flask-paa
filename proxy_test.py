#!/usr/bin/env python
print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
    '$ sudo pip install six');
print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
    'YOURPASS, please contact sales@brightdata.com')
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
if sys.version_info[0]==2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler(
            {'http': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225',
            'https': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225'}))
    print(opener.open('http://lumtest.com/myip.json').read())
if sys.version_info[0]==3:
    import requests
    s = requests.Session()
    proxies = {'http': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225'}
            # 'https': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225'}
    response = s.get(
              'https://www.google.com?q=audi',
             
              proxies=proxies,
          )
    print(response.text)
    # opener = urllib.request.build_opener(
    #     urllib.request.ProxyHandler(
    #         {'http': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225',
    #         'https': 'http://brd-customer-hl_e4d957e0-zone-zone2-country-td:dr5e2sr1rk92@zproxy.lum-superproxy.io:22225'}))
    # print(opener.open().read())
#___________________________________________________________
# import requests


# proxies = {'http': 'http://173.82.34.3:1994'}
# s = requests.session()
# s.proxies.update(proxies)
# response = s.get(
#   url='https://www.google.com/search?q=audi&gl=us'
#   # params={
#   #     'api_key': 'f39e239a-55f1-40b0-b53d-c28d2f9dc469',
#   #     'url': 'https://www.google.com/search?q=zzz', 
#   # },
# )

# print('Response Body: ', response.content)
#______________________________________________________________
# response = requests.get(
#   url='https://proxy.scrapeops.io/v1/',
#   params={
#       'api_key': 'f39e239a-55f1-40b0-b53d-c28d2f9dc469',
#       'url': 'https://www.google.com/search?q=zzz', 
#   },
# )

# print('Response Body: ', response.content)

# response = requests.get(
#   url='https://proxy.scrapeops.io/v1/',
#   params={
#       'api_key': 'f39e239a-55f1-40b0-b53d-c28d2f9dc469',
#       'url': 'https://www.google.com/search?q=zzz', 
#   },
# )

# print('Response Body: ', response.content)

# response = requests.get(
#   url='https://proxy.scrapeops.io/v1/',
#   params={
#       'api_key': 'f39e239a-55f1-40b0-b53d-c28d2f9dc469',
#       'url': 'https://www.google.com/search?q=zzz', 
#   },
# )

# print('Response Body: ', response.content)

# response = requests.get(
#   url='https://proxy.scrapeops.io/v1/',
#   params={
#       'api_key': 'f39e239a-55f1-40b0-b53d-c28d2f9dc469',
#       'url': 'https://www.google.com/search?q=zzz', 
#   },
# )

# print('Response Body: ', response.content)