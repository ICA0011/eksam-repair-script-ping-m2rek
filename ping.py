import requests

def check_server_status():
    a = requests.get(url)
    if a = 200:
        return True
    else:
        return False
