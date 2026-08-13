from colorama import Fore, Style
import re
import hashlib

RED = Fore.RED
RESET = Style.RESET_ALL

def run(target):
    email = target.strip().lower()
    if '@' not in email:
        return {"error": "Invalid email format"}
    
    domain = email.split('@')[1]
    username = email.split('@')[0]
    
    # Проверка на распространенные провайдеры
    providers = {
        'gmail.com': 'Google',
        'yahoo.com': 'Yahoo',
        'mail.ru': 'Mail.ru',
        'yandex.ru': 'Yandex',
        'hotmail.com': 'Microsoft',
        'outlook.com': 'Microsoft',
        'icloud.com': 'Apple',
        'protonmail.com': 'ProtonMail',
        'rambler.ru': 'Rambler'
    }
    
    info = {
        'email': email,
        'username': username,
        'domain': domain,
        'provider': providers.get(domain, 'Unknown'),
        'md5_hash': hashlib.md5(email.encode()).hexdigest(),
        'valid_format': True
    }
    
    return info

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] Email: {data['email']}{RESET}")
    print(f"  {RED}[+] Username: {data['username']}{RESET}")
    print(f"  {RED}[+] Domain: {data['domain']}{RESET}")
    print(f"  {RED}[+] Provider: {data['provider']}{RESET}")
    print(f"  {RED}[+] MD5: {data['md5_hash']}{RESET}")
