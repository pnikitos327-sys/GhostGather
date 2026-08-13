#!/usr/bin/env python3
import sys
from colorama import init, Fore, Style
from ghostgather.banner import print_banner
from ghostgather.core.history import history
from ghostgather.modules import shodan, ipstack, whois, dns, ssl
from ghostgather.modules.subdomains import find_subdomains
from ghostgather.modules.reverse_dns import reverse_dns
from ghostgather.modules.abuseipdb import run as abuse_run, output as abuse_output
from ghostgather.modules.headers import run as headers_run, output as headers_output
from ghostgather.modules.portscan import run as portscan_run, output as portscan_output
from ghostgather.modules.techdetect import run as tech_run, output as tech_output
from ghostgather.modules.username_search import run as username_run, output as username_output, clean_username
from ghostgather.modules.geoip import run as geoip_run, output as geoip_output
from ghostgather.modules.traceroute import run as traceroute_run, output as traceroute_output
from ghostgather.modules.dns_bruteforce import run as dns_bruteforce_run, output as dns_bruteforce_output
from ghostgather.modules.ssl_vulns import run as ssl_vulns_run, output as ssl_vulns_output
from ghostgather.modules.phone_search import run as phone_run, output as phone_output
from ghostgather.modules.email_search import run as email_run, output as email_output
from ghostgather.modules.leak_search import run as leak_run, output as leak_output
from ghostgather.modules.telegram import run as telegram_run, output as telegram_output
from ghostgather.core.utils import clean_target, is_valid_ip, is_valid_domain, detect_target_type
from ghostgather.core.rotator import rotator

init(autoreset=True)

RED = Fore.RED
RESET = Style.RESET_ALL

def print_success(msg):
    print(f"{RED}[+] {msg}{RESET}")

def print_error(msg):
    print(f"{RED}[-] {msg}{RESET}")

def print_info(msg):
    print(f"{RED}[>] {msg}{RESET}")

def process_target(target):
    target = clean_target(target)
    target_type = detect_target_type(target)
    print(f"\n{RED}[=] Target: {target} ({target_type}){RESET}")
    rotator.wait()

    if target_type == 'ip':
        print_info("Shodan")
        shodan_data = shodan.run(target)
        shodan.output(shodan_data)
        print_info("GeoIP")
        geoip_data = geoip_run(target)
        geoip_output(geoip_data)
        print_info("Reverse DNS")
        reverse_dns(target)
        print_info("Port Scan")
        ports = portscan_run(target)
        portscan_output(ports)
        print_info("Traceroute")
        trace_data = traceroute_run(target)
        traceroute_output(trace_data)
        print_info("AbuseIPDB")
        abuse_data = abuse_run(target)
        abuse_output(abuse_data)

    elif target_type == 'domain':
        print_info("WHOIS")
        whois_data = whois.run(target)
        whois.output(whois_data)
        print_info("DNS Records")
        dns_data = dns.run(target)
        dns.output(dns_data)
        print_info("SSL Certificate")
        ssl_data = ssl.run(target)
        ssl.output(ssl_data)
        print_info("SSL Vulnerabilities")
        ssl_vulns_data = ssl_vulns_run(target)
        ssl_vulns_output(ssl_vulns_data)
        print_info("Subdomains")
        find_subdomains(target)
        print_info("DNS Bruteforce")
        dns_bruteforce_results = dns_bruteforce_run(target)
        dns_bruteforce_output(dns_bruteforce_results)
        print_info("HTTP Headers")
        headers_data = headers_run(target)
        headers_output(headers_data)
        print_info("Technology Detection")
        tech = tech_run(target)
        tech_output(tech)

    elif target_type == 'email':
        print_info("Email Check")
        email_data = email_run(target)
        email_output(email_data)
        print_info("Leak Search")
        leak_data = leak_run(target)
        leak_output(leak_data)

    elif target_type == 'phone':
        print_info("Phone Lookup")
        phone_data = phone_run(target)
        phone_output(phone_data)

    else:
        print_info("Username Search")
        username_data = username_run(target)
        username_output(username_data)
        print_info("Telegram")
        tg_data = telegram_run(target)
        telegram_output(tg_data)

    print(f"\n{RED}[+] Scan complete{RESET}")

def main():
    print_banner()
    print()
    while True:
        try:
            target = input(f"{RED}[GHOSTGATHER] >> {RESET}").strip()
            if not target:
                continue
            if target.lower() in ['exit', 'quit', '0']:
                print_success("Goodbye!")
                break
            process_target(target)
        except KeyboardInterrupt:
            print(f"\n{RED}[!] Interrupted{RESET}")
            break
        except Exception as e:
            print_error(f"Error: {e}")
        print()

if __name__ == "__main__":
    sys.exit(main())
