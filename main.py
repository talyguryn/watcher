from __future__ import print_function
from config import DOMAINS, CODEXBOT_NOTIFICATIONS
import urllib
import urllib2

def send_message(text):
    url = CODEXBOT_NOTIFICATIONS
    data = urllib.urlencode({'message': text})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

def get_status(url):
    req = urllib2.Request(url)
    print('{} '.format(url), end='')

    try:
        response = urllib2.urlopen(req)
        code = response.code
        print('{}'.format(code))
    except urllib2.URLError as e:
        code = e.code
        print('{} cause '.format(code), end='')
        print(e.reason)

    if code != 200:
        send_message('{} code on {}'.format(code, url))

    return code


if not CODEXBOT_NOTIFICATIONS:
    print('No CODEXBOT_NOTIFICATIONS link was found in config file.')
    exit()

for domain in DOMAINS:
    get_status(domain)


