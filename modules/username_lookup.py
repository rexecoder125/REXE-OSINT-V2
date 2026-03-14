import requests

SITES = [
    "https://www.instagram.com/{}",
    "https://www.facebook.com/{}",
    "https://www.twitter.com/{}",
    "https://www.github.com/{}",
    "https://www.reddit.com/user/{}",
    "https://{}.tumblr.com",
]

def username_lookup(username):
    result = {}
    for site in SITES:
        url = site.format(username)
        try:
            r = requests.get(url, timeout=4)
            result[url] = "FOUND" if r.status_code == 200 else "NOT FOUND"
        except:
            result[url] = "ERROR"
    return result
