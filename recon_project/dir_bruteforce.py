import requests

def bruteforce_directories(url, wordlist_path):
    print(f"[+] Brute forcing directories on {url}")
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                directory = line.strip()
                target_url = f"{url.rstrip('/')}/{directory}"
                try:
                    response = requests.get(target_url, timeout=5)
                    if response.status_code == 200:
                        print(f"[FOUND] {target_url}")
                except requests.RequestException:
                    pass
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {wordlist_path}")

