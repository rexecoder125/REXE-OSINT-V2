import os

def info():

    domain = input("Enter website URL: ")

    print("\nScanning website...\n")
    os.system(f"whois {domain}")
    print("\nDNS Records:\n")
    os.system(f"nslookup {domain}")
