from os import strerror
import requests

def check_server_status(url: str):
    while True:
        try:
            a = requests.get(url)
            if a.status_code == 200:
                return True

        except Exception:
            return False
