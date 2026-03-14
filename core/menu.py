from modules import username_search, ip_tracker, email_breach

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

    choice = input("Select: ")

    if choice == "1":
        username_search.search()

    elif choice == "2":
        ip_tracker.lookup()

    elif choice == "3":
        email_breach.check()
