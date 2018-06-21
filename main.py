from config import DOMAINS, WEBHOOK
import requests
from requests.exceptions import SSLError, ConnectionError


class NotOK(Exception):
    pass


def send_message(text):
    url = WEBHOOK
    data = {
        'message': text,
        'disable_web_page_preview': True
    }
    requests.post(url, data=data)


def get_status(domain):
    is_site_available = False
    url = domain['url']

    load_time = None
    page_size = None

    try:
        r = requests.get(url)
        code = r.status_code
        if code != 200:
            raise NotOK(code)

        is_site_available = True

        load_time = r.elapsed.total_seconds()
        page_size = round(len(r.content) / 1024, 3)

    except NotOK as e:
        print(e)
        code = '{} code'.format(e)

    except SSLError as e:
        print(e)
        code = 'SSL error'

    except ConnectionError as e:
        print(e)
        code = 'Connection refused'

    except Exception as e:
        print(e)
        code = 'Undefined error'

    if not is_site_available:
        message = "🚨 {} on {}".format(code, url)

        try:
            if domain['message']:
                message += "\n{}".format(domain['message'])
        except:
            pass

        send_message(message)

    print('{} -> {}'.format(url, code))

    if load_time:
        print('Time: {} s'.format(load_time))

    if page_size:
        print('Size: {} KB'.format(page_size))

    print()

    return code


if not WEBHOOK:
    print('No WEBHOOK link was found in config file.')
    exit()

for domain in DOMAINS:
    get_status(domain)


