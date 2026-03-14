import requests

def vuln_scan(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    tests = {
        "Clickjacking": ("X-Frame-Options",),
        "CSP": ("Content-Security-Policy",),
        "HSTS": ("Strict-Transport-Security",),
        "XSS Protection": ("X-XSS-Protection",)
    }

    r = requests.get(url, headers=headers)
    result = {}

    for test, header in tests.items():
        result[test] = "SAFE" if header[0] in r.headers else "⚠ NOT PROTECTED"

    return result
