from colorama import Fore, Style
RED = Fore.RED
RESET = Style.RESET_ALL

def run(ip):
    return {"error": "Shodan API key not configured"}

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
    else:
        print(f"  {RED}[+] Shodan data not available{RESET}")
