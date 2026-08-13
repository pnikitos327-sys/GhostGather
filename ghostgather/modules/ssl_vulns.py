import ssl
import socket
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def check_ssl_vulns(domain):
    vulnerabilities = []
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Проверка версии TLS
                version = ssock.version()
                if 'TLSv1.0' in version:
                    vulnerabilities.append("TLS 1.0 detected (vulnerable)")
                if 'TLSv1.1' in version:
                    vulnerabilities.append("TLS 1.1 detected (vulnerable)")
                if 'SSLv2' in version or 'SSLv3' in version:
                    vulnerabilities.append("SSLv2/SSLv3 detected (CRITICAL)")

                # Проверка шифров
                cipher = ssock.cipher()
                if cipher:
                    cipher_name = cipher[0]
                    if 'RC4' in cipher_name:
                        vulnerabilities.append("RC4 cipher detected (weak)")
                    if 'DES' in cipher_name:
                        vulnerabilities.append("DES cipher detected (weak)")

        return vulnerabilities if vulnerabilities else ["No obvious SSL vulnerabilities found"]

    except Exception as e:
        return {"error": f"SSL vuln check error: {str(e)}"}

def run(target):
    return check_ssl_vulns(target)

def output(data):
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    print(f"  {RED}[+] SSL Vulnerabilities:{RESET}")
    for item in data:
        print(f"      {item}")