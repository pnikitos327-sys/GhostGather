from colorama import Fore, Style
import subprocess
import re

RED = Fore.RED
RESET = Style.RESET_ALL

def run_traceroute(target):
    """Выполняет трассировку до цели"""
    try:
        # Используем команду traceroute
        result = subprocess.run(['traceroute', '-n', '-m', '20', target], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            return {"error": "Traceroute failed"}
        
        lines = result.stdout.strip().split('\n')
        hops = []
        
        for line in lines[1:]:  # Пропускаем заголовок
            parts = line.split()
            if len(parts) >= 4:
                hop_num = parts[0]
                # Извлекаем IP адреса
                ips = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
                if ips:
                    hops.append({
                        'hop': hop_num,
                        'ips': ips
                    })
        
        return {'target': target, 'hops': hops}
    except subprocess.TimeoutExpired:
        return {"error": "Traceroute timed out"}
    except:
        return {"error": "Traceroute unavailable"}

def run(target):
    return run_traceroute(target)

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    if not data['hops']:
        print(f"  {RED}[-] No hops found{RESET}")
        return
    
    print(f"  {RED}[+] Traceroute to {data['target']}:{RESET}")
    for hop in data['hops']:
        ips_str = ', '.join(hop['ips'])
        print(f"      {RED}{hop['hop']}{RESET} {ips_str}")
