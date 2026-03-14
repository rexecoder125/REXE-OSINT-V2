import dns.resolver

def lookup():

    domain = input("Enter domain: ")

    print("\nDNS Lookup Results:\n")

    for qtype in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, qtype)
            for r in answers:
                print(f"{qtype}: {r}")
        except:
            pass
