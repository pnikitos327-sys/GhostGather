import whois
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def get_whois(domain):
    """Получает WHOIS информацию через библиотеку python-whois"""
    try:
        w = whois.whois(domain)
        
        info = {
            'domain': domain,
            'registrar': w.registrar,
            'creation_date': w.creation_date,
            'expiration_date': w.expiration_date,
            'name_servers': w.name_servers,
            'org': w.org,
            'country': w.country,
            'emails': w.emails
        }
        return info
    except Exception as e:
        return {"error": f"WHOIS error: {str(e)}"}

def run(target):
    return get_whois(target)

def output(data):
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return

    if not data or not data.get('registrar'):
        print(f"  {RED}[-] Could not get WHOIS data{RESET}")
        return

    print(f"  {RED}[+] WHOIS info:{RESET}")
    print(f"      Domain: {data.get('domain', 'N/A')}")
    print(f"      Registrar: {data.get('registrar', 'N/A')}")
    if data.get('creation_date'):
        print(f"      Created: {data['creation_date']}")
    if data.get('expiration_date'):
        print(f"      Expires: {data['expiration_date']}")
    if data.get('org'):
        print(f"      Organization: {data['org']}")
    if data.get('country'):
        print(f"      Country: {data['country']}")
    if data.get('name_servers'):
        print(f"      Name Servers: {', '.join(data['name_servers'])}")
    if data.get('emails'):
        print(f"      Emails: {', '.join(data['emails'])}")