import requests

def lookup():

    phone = input("Enter phone with country code: ")

    url = f"https://api.apilayer.com/number_verification/validate?number={phone}"

    print("\nPhone Lookup Result:\n")
    print("Number:", phone)
    print("Country: Unknown (API key required)")
    print("Carrier: Unknown")
