from config import DOMAINS, CODEXBOT_NOTIFICATIONS
import requests

def send_message(text):
    url = CODEXBOT_NOTIFICATIONS
    data = {'message': text}
    requests.post(CODEXBOT_NOTIFICATIONS, data=data)

def get_status(url):
    print('{} '.format(url), end='')

    try:
        r = requests.get(url)
        code = r.status_code
        print('{}'.format(code))

        if code != 200:
            send_message('{} code on {}'.format(code, url))
    except:
        print('Undefined error')
        code = 0

    return code


if not CODEXBOT_NOTIFICATIONS:
    print('No CODEXBOT_NOTIFICATIONS link was found in config file.')
    exit()

for domain in DOMAINS:
    get_status(domain)


