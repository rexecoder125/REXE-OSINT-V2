import requests

def check():

    email = input("Enter email: ")

    print("\nChecking breaches...\n")

    url = f"https://api.eva.pingutil.com/email?email={email}"
    data = requests.get(url).json()

    print("Valid:", data["data"]["valid"])
    print("Disposable:", data["data"]["disposable"])
    print("Domain:", data["data"]["domain"])
