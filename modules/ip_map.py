import requests

def ip_map(ip):
    url = f"http://ip-api.com/json/{ip}"
    data = requests.get(url).json()
    return {
        "country": data["country"],
        "city": data["city"],
        "lat": data["lat"],
        "lon": data["lon"],
        "map": f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
    }
