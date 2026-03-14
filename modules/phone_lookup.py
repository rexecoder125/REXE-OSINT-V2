import requests

def lookup():

    phone = input("Enter phone number with country code: ")

    print("\nFetching phone info...\n")

    url = f"https://api.apilayer.com/number_verification/validate?number={phone}"

    # Public free API without key
    data = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=free&phone={phone}").json()

    print("Country:", data.get("country"))
    print("Location:", data.get("location"))
    print("Carrier:", data.get("carrier"))
    print("Type:", data.get("type"))
