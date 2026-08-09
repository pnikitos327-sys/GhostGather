from colorama import Fore, Style
import re

RED = Fore.RED
RESET = Style.RESET_ALL

def clean_phone(phone):
    """Очищает номер телефона"""
    if not phone:
        return ""
    cleaned = re.sub(r'[^0-9+]', '', phone.strip())
    return cleaned

def get_phone_info(phone):
    """Определяет страну и оператора по номеру"""
    phone = clean_phone(phone)
    
    # Простая база кодов стран
    country_codes = {
        '7': 'Russia/Kazakhstan',
        '1': 'USA/Canada',
        '44': 'UK',
        '49': 'Germany',
        '33': 'France',
        '86': 'China',
        '91': 'India',
        '81': 'Japan',
        '55': 'Brazil',
        '61': 'Australia',
    }
    
    info = {
        'phone': phone,
        'country': 'Unknown',
        'operator': 'Unknown',
        'valid': False
    }
    
    # Определяем страну
    if phone.startswith('+'):
        code = phone[1:3]
        if code in country_codes:
            info['country'] = country_codes[code]
            info['valid'] = True
        elif phone[1:2] in country_codes:
            info['country'] = country_codes[phone[1:2]]
            info['valid'] = True
    
    # Российские операторы (простейшая проверка)
    if phone.startswith('+7') or phone.startswith('8') or phone.startswith('79'):
        operators = {
            '910': 'MTS',
            '911': 'MTS',
            '912': 'MTS',
            '913': 'MTS',
            '914': 'MTS',
            '915': 'MTS',
            '916': 'MTS',
            '917': 'MTS',
            '918': 'MTS',
            '919': 'MTS',
            '920': 'MegaFon',
            '921': 'MegaFon',
            '922': 'MegaFon',
            '923': 'MegaFon',
            '924': 'MegaFon',
            '925': 'MegaFon',
            '926': 'MegaFon',
            '927': 'MegaFon',
            '928': 'MegaFon',
            '929': 'MegaFon',
            '930': 'Beeline',
            '931': 'Beeline',
            '932': 'Beeline',
            '933': 'Beeline',
            '934': 'Beeline',
            '935': 'Beeline',
            '936': 'Beeline',
            '937': 'Beeline',
            '938': 'Beeline',
            '939': 'Beeline',
            '950': 'Tele2',
            '951': 'Tele2',
            '952': 'Tele2',
            '953': 'Tele2',
            '954': 'Tele2',
            '955': 'Tele2',
            '956': 'Tele2',
            '957': 'Tele2',
            '958': 'Tele2',
            '959': 'Tele2',
        }
        
        # Извлекаем 3 цифры после кода
        clean_num = re.sub(r'[^0-9]', '', phone)
        if len(clean_num) >= 3:
            code = clean_num[-10:-7] if len(clean_num) >= 10 else clean_num[:3]
            if code in operators:
                info['operator'] = operators[code]
    
    return info

def run(target):
    phone = clean_phone(target)
    if not phone:
        return {"error": "Invalid phone number"}
    
    info = get_phone_info(phone)
    return info

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] Phone: {data['phone']}{RESET}")
    print(f"  {RED}[+] Country: {data['country']}{RESET}")
    if data['operator'] != 'Unknown':
        print(f"  {RED}[+] Operator: {data['operator']}{RESET}")
    if data['valid']:
        print(f"  {RED}[+] Status: Valid format{RESET}")
    else:
        print(f"  {RED}[-] Status: Unknown format{RESET}")
