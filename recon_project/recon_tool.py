from subdomain_enum import get_subdomains
from dir_bruteforce import bruteforce_directories

def save_to_file(filename, lines):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"[+] Results saved to {filename}")
    except Exception as e:
        print(f"[-] Failed to save file: {e}")

def main_menu():
    while True:
        print("\n==== Recon Tool Menu ====")
        print("1. Enumerate Subdomains")
        print("2. Bruteforce Directories")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            domain = input("Enter domain (example.com): ")
            subdomains = get_subdomains(domain)
            print(f"\n[+] Found {len(subdomains)} subdomains:\n")
            for sub in subdomains:
                print(" -", sub)

            save = input("\nDo you want to save the subdomains to a file? (y/n): ").lower()
            if save == 'y':
                filename = input("Enter filename to save output: ")
                save_to_file(filename, subdomains)

        elif choice == '2':
            url = input("Enter full subdomain URL (e.g. https://admin.example.com): ")
            wordlist_path = input("Path to wordlist (e.g. wordlists/common.txt): ")

            # Capture output inside bruteforce_directories or here
            print(f"[+] Brute forcing directories on {url}...\n")
            # Let’s capture found paths inside a list here
            found_paths = []

            def custom_print(path_result):
                print(path_result)
                found_paths.append(path_result)

            # You need to modify bruteforce_directories to accept a callback for printing, or
            # we can monkey patch print temporarily (hacky), better modify the function:
            bruteforce_directories(url, wordlist_path, print_callback=custom_print)

            save = input("\nDo you want to save the bruteforce results to a file? (y/n): ").lower()
            if save == 'y':
                filename = input("Enter filename to save output: ")
                save_to_file(filename, found_paths)

        elif choice == '3':
            print("Goodbye! 👋")
            break

        else:
            print("[-] Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

