from colorama import Fore, Style
import urllib.request
import re

RED = Fore.RED
RESET = Style.RESET_ALL

def get_whois(domain):
    """Получает WHOIS информацию через бесплатный сервис"""
    try:
        url = f"https://who.is/whois/{domain}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        html = response.read().decode('utf-8')
        
        # Простой парсинг основных полей
        info = {'domain': domain}
        
        # Ищем Registrar
        registrar_match = re.search(r'Registrar:.*?<[^>]+>([^<]+)', html, re.IGNORECASE)
        if registrar_match:
            info['registrar'] = registrar_match.group(1).strip()
        
        # Ищем Creation Date
        created_match = re.search(r'Creation Date:.*?<[^>]+>([^<]+)', html, re.IGNORECASE)
        if created_match:
            info['created'] = created_match.group(1).strip()
        
        # Ищем Expiration Date
        expiry_match = re.search(r'Expiration Date:.*?<[^>]+>([^<]+)', html, re.IGNORECASE)
        if expiry_match:
            info['expires'] = expiry_match.group(1).strip()
        
        # Ищем Name Servers
        ns_match = re.search(r'Name Server:.*?<[^>]+>([^<]+)', html, re.IGNORECASE)
        if ns_match:
            info['nameservers'] = ns_match.group(1).strip()
        
        if not info.get('registrar'):
            return {"error": "Could not get WHOIS data"}
        
        return info
    except:
        return {"error": "WHOIS service unavailable"}

def run(target):
    return get_whois(target)

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] Domain: {data['domain']}{RESET}")
    if 'registrar' in data:
        print(f"  {RED}[+] Registrar: {data['registrar']}{RESET}")
    if 'created' in data:
        print(f"  {RED}[+] Created: {data['created']}{RESET}")
    if 'expires' in data:
        print(f"  {RED}[+] Expires: {data['expires']}{RESET}")
    if 'nameservers' in data:
        print(f"  {RED}[+] Nameservers: {data['nameservers']}{RESET}")
