import requests

def get_subdomains(domain):
    print(f"[+] Searching hackertarget.com for subdomains of: {domain}")
    try:
        url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
        response = requests.get(url, timeout=10)
        if "error" in response.text.lower():
            raise Exception("No subdomains found or blocked.")
        lines = response.text.strip().split("\n")
        subdomains = [line.split(",")[0] for line in lines if domain in line]
        return sorted(set(subdomains))
    except Exception as e:
        print(f"[-] Error: {e}")
        return []

