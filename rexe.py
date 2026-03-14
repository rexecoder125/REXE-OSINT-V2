import os
from modules.username_lookup import username_lookup
from modules.instagram_finder import instaFinder
from modules.subdomain_finder import get_subdomains
from modules.vuln_scanner import vuln_scan
from modules.ip_map import ip_map
from modules.darkweb_email import darkweb_check

def menu():
    os.system("clear")

    print("""
 ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██║   ██║██║  ██║█████╗  ██████╔╝
██║     ██║   ██║██║  ██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

        Coder OSINT TOOL v2
        Developer: rexe
""")

    print("""
1) Username Lookup
2) Instagram Finder
3) Subdomain Finder
4) Website Vulnerability Scan
5) IP Location Map
6) Dark Web Email Check
0) Exit
""")

    choice = input("Select Option: ")

    if choice == "1":
        u = input("Enter username: ")
        print(username_lookup(u))

    elif choice == "2":
        u = input("Instagram username: ")
        print(instaFinder(u))

    elif choice == "3":
        d = input("Domain: ")
        print(get_subdomains(d))

    elif choice == "4":
        url = input("Website URL: ")
        print(vuln_scan(url))

    elif choice == "5":
        ip = input("IP: ")
        print(ip_map(ip))

    elif choice == "6":
        email = input("Email: ")
        print(darkweb_check(email))

    elif choice == "0":
        exit()

menu()
