import ssl
import socket
import datetime
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def get_ssl_info(domain, port=443):
    """Получает информацию о SSL-сертификате домена."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return {
                    "subject": dict(x[0] for x in cert.get('subject', [])),
                    "issuer": dict(x[0] for x in cert.get('issuer', [])),
                    "not_before": cert.get('notBefore'),
                    "not_after": cert.get('notAfter'),
                    "version": cert.get('version'),
                    "serial": cert.get('serialNumber')
                }
    except Exception as e:
        return {"error": str(e)}

def run(target):
    """Запускает получение SSL-сертификата."""
    return get_ssl_info(target)

def output(data):
    """Выводит информацию о SSL-сертификате."""
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] SSL error: {data['error']}{RESET}")
        return

    if not data or isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] SSL data not available{RESET}")
        return

    subject = data.get('subject', {})
    issuer = data.get('issuer', {})
    not_before = data.get('not_before')
    not_after = data.get('not_after')

    print(f"  {RED}[+] SSL Certificate:{RESET}")
    print(f"      Subject: {subject.get('commonName', 'N/A')}")
    print(f"      Issuer: {issuer.get('commonName', 'N/A')}")
    print(f"      Valid from: {not_before}")
    print(f"      Valid until: {not_after}")