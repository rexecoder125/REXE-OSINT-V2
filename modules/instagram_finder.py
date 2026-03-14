import requests

def instaFinder(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=1"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if r.status_code != 200:
        return None

    data = r.json()
    return {
        "full_name": data["graphql"]["user"]["full_name"],
        "bio": data["graphql"]["user"]["biography"],
        "followers": data["graphql"]["user"]["edge_followed_by"]["count"],
        "following": data["graphql"]["user"]["edge_follow"]["count"],
        "profile_pic": data["graphql"]["user"]["profile_pic_url_hd"],
    }
