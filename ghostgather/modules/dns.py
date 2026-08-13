from colorama import Fore, Style
import subprocess
import re

RED = Fore.RED
RESET = Style.RESET_ALL

def get_dns_records(domain):
    """Получает DNS записи через dig/nslookup"""
    records = {'domain': domain}
    
    try:
        # A record
        result = subprocess.run(['dig', '+short', domain, 'A'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout:
            records['A'] = result.stdout.strip().split('\n')
        
        # NS records
        result = subprocess.run(['dig', '+short', domain, 'NS'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout:
            records['NS'] = result.stdout.strip().split('\n')
        
        # MX records
        result = subprocess.run(['dig', '+short', domain, 'MX'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout:
            records['MX'] = result.stdout.strip().split('\n')
        
        # TXT records
        result = subprocess.run(['dig', '+short', domain, 'TXT'], 
                              capture_output=True, text=True, timeout=5)
        if result.stdout:
            records['TXT'] = result.stdout.strip().split('\n')
        
        if not records.get('A') and not records.get('NS'):
            return {"error": "Could not get DNS records"}
        
        return records
    except:
        return {"error": "DNS service unavailable"}

def run(target):
    return get_dns_records(target)

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] Domain: {data['domain']}{RESET}")
    if 'A' in data:
        print(f"  {RED}[+] A Records:{RESET}")
        for record in data['A']:
            print(f"      {record}")
    if 'NS' in data:
        print(f"  {RED}[+] NS Records:{RESET}")
        for record in data['NS']:
            print(f"      {record}")
    if 'MX' in data:
        print(f"  {RED}[+] MX Records:{RESET}")
        for record in data['MX']:
            print(f"      {record}")
    if 'TXT' in data:
        print(f"  {RED}[+] TXT Records:{RESET}")
        for record in data['TXT']:
            print(f"      {record}")
