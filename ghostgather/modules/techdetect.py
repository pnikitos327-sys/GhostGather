from colorama import Fore, Style
RED = Fore.RED
RESET = Style.RESET_ALL

def run(target):
    return {"error": "Module techdetect not configured"}

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
    else:
        print(f"  {RED}[+] techdetect data not available{RESET}")
