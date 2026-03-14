import requests

def lookup():

    ip = input("Enter IP Address: ")

    print("\nFetching IP info...\n")

    url = f"https://ipinfo.io/{ip}/json"
    res = requests.get(url).json()

    print("IP:", res.get("ip"))
    print("City:", res.get("city"))
    print("Region:", res.get("region"))
    print("Country:", res.get("country"))
    print("Location:", res.get("loc"))
    print("Org:", res.get("org"))
    print("Timezone:", res.get("timezone"))
