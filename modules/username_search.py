import requests

sites = [
    "https://instagram.com/{}",
    "https://github.com/{}",
    "https://twitter.com/{}",
    "https://tiktok.com/@{}",
    "https://reddit.com/user/{}",
    "https://pinterest.com/{}",
    "https://soundcloud.com/{}",
    "https://www.quora.com/profile/{}",
    "https://www.snapchat.com/add/{}",
]

def search():
    user = input("Enter username: ")

    print("\nSearching username across 20+ sites...\n")

    for site in sites:
        url = site.format(user)
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print("[FOUND] ", url)
            else:
                print("[NOT FOUND] ", url)
        except:
            print("[ERROR] ", url)
