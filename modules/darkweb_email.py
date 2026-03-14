import requests

def darkweb_check(email):
    api = f"https://api.protonmail.com/breached/{email}"
    r = requests.get(api)
    return r.json() if r.status_code == 200 else None
