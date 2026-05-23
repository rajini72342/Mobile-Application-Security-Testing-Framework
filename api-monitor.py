import requests
from colorama import Fore

TARGET_URL = "https://example.com/api/login"

payload = {
    "username": "admin",
    "password": "password123"
}

headers = {
    "User-Agent": "MobileSecurityFramework"
}

try:
    response = requests.post(
        TARGET_URL,
        json=payload,
        headers=headers
    )

    print(Fore.GREEN + "[+] Status:", str(response.status_code))
    print(Fore.CYAN + response.text)

except Exception as e:
    print(Fore.RED + f"[-] Error: {e}")