from colorama import Fore, Style
import socket
from datetime import datetime

RED = Fore.RED
RESET = Style.RESET_ALL

def scan_port(ip, port, timeout=2):
    """Проверяет открыт ли порт"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def get_service_name(port):
    """Определяет сервис по порту"""
    services = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        111: 'RPCbind',
        135: 'MSRPC',
        139: 'NetBIOS',
        143: 'IMAP',
        443: 'HTTPS',
        445: 'SMB',
        993: 'IMAPS',
        995: 'POP3S',
        1433: 'MSSQL',
        1521: 'Oracle DB',
        1723: 'PPTP',
        3306: 'MySQL',
        3389: 'RDP',
        5432: 'PostgreSQL',
        5900: 'VNC',
        6379: 'Redis',
        8080: 'HTTP-Alt',
        27017: 'MongoDB'
    }
    return services.get(port, 'Unknown')

def run(target):
    """Сканирует топ-20 популярных портов"""
    try:
        ip = socket.gethostbyname(target)
    except:
        return {"error": "Could not resolve target"}
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 
                    143, 443, 445, 993, 995, 1433, 1521, 1723, 
                    3306, 3389, 5432, 5900, 6379, 8080, 27017]
    
    results = {'ip': ip, 'open_ports': []}
    
    print(f"  {RED}[*] Scanning {ip}...{RESET}")
    
    for port in common_ports:
        if scan_port(ip, port):
            service = get_service_name(port)
            results['open_ports'].append({'port': port, 'service': service})
    
    return results

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    if not data['open_ports']:
        print(f"  {RED}[-] No open ports found{RESET}")
        return
    
    print(f"  {RED}[+] Open ports:{RESET}")
    for p in data['open_ports']:
        print(f"      {RED}[{p['port']}]{RESET} {p['service']}")
