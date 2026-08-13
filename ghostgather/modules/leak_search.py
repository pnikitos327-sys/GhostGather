import urllib.request
import json
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def check_leaks(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        req = urllib.request.Request(url, headers={'User-Agent': 'GhostGather/1.0'})
        response = urllib.request.urlopen(req, timeout=5)
        data = json.loads(response.read().decode('utf-8'))
        leaks = [item['Name'] for item in data]
        return leaks
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return []  # Не найдено утечек
        return {"error": f"Leak API error: {e.code}"}
    except Exception as e:
        return {"error": str(e)}

def run(target):
    return check_leaks(target)

def output(data):
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    if not data:
        print(f"  {RED}[+] No leaks found{RESET}")
        return
    print(f"  {RED}[+] Leaks found: {len(data)}{RESET}")
    for leak in data:
        print(f"      {leak}")