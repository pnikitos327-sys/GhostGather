import urllib.request
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def run(domain):
    try:
        url = f"http://{domain}"
        req = urllib.request.Request(url, method='HEAD')
        response = urllib.request.urlopen(req, timeout=5)
        headers = dict(response.headers)
        return headers
    except:
        return {"error": "Could not get headers"}

def output(data):
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    print(f"  {RED}[+] HTTP Headers:{RESET}")
    for key, value in data.items():
        print(f"      {key}: {value}")