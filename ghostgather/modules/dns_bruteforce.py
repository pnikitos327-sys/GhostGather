from colorama import Fore, Style
RED = Fore.RED
RESET = Style.RESET_ALL

def run(target):
    return {"error": "Module dns_bruteforce not configured"}

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
    else:
        print(f"  {RED}[+] dns_bruteforce data not available{RESET}")
