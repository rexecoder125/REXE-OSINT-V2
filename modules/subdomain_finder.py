import requests

def get_subdomains(domain):
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    data = requests.get(url).text.split("\n")
    return [line.split(",")[0] for line in data if line]
