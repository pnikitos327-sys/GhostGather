import socket
from colorama import Fore, Style
from ghostgather.core.utils import clean_target, is_valid_ip
RED = Fore.RED
RESET = Style.RESET_ALL

def print_data(label, value):
    print(f"  {RED}{label}:{RESET} {RED}{value}{RESET}")

def print_error(msg):
    print(f"  {RED}[-] {msg}{RESET}")

def reverse_dns(ip):
    ip = clean_target(ip)
    if not is_valid_ip(ip):
        print_error("Invalid IP address")
        return
    try:
        host, aliases, addresses = socket.gethostbyaddr(ip)
        print_data("Hostname", host)
    except socket.herror:
        print_error("No PTR record found")
