from os import strerror
import requests

def check_server_status(url: str):
    while True:
        try:
            a = requests.get(url)
            if a.status_code == 200:
                print('OK')
                return True

        except Exception:
            print('NOK')
            return False

check_server_status('http://itcollege.ee')