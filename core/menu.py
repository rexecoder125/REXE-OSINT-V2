from modules import username_search
from modules import ip_tracker
from modules import email_breach
from modules import phone_lookup
from modules import website_scanner
from modules import dns_lookup
from modules import port_scanner

def menu():

    print("""
[1] Username Search
[2] IP Tracker
[3] Email Breach
[4] Phone Lookup
[5] Website Scanner
[6] DNS Lookup
[7] Port Scanner
[0] Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        username_search.search()

    elif choice == "2":
        ip_tracker.lookup()

    elif choice == "3":
        email_breach.check()

    elif choice == "4":
        phone_lookup.lookup()

    elif choice == "5":
        website_scanner.info()

    elif choice == "6":
        dns_lookup.lookup()

    elif choice == "7":
        port_scanner.scan()

    elif choice == "0":
        exit()
