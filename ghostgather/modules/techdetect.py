import urllib.request
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

def run(domain):
    try:
        url = f"http://{domain}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req, timeout=5)
        headers = dict(response.headers)
        html = response.read().decode('utf-8', errors='ignore')

        tech = []

        # Сервер
        if 'server' in headers:
            tech.append(f"Server: {headers['server']}")

        # PHP
        if 'x-powered-by' in headers:
            tech.append(f"Powered by: {headers['x-powered-by']}")

        # WordPress
        if '/wp-content/' in html or 'wp-admin' in html:
            tech.append("WordPress")

        # Cloudflare
        if 'cf-ray' in headers or 'cloudflare' in headers.get('server', '').lower():
            tech.append("Cloudflare")

        # Nginx
        if 'nginx' in headers.get('server', '').lower():
            tech.append("Nginx")

        # Apache
        if 'apache' in headers.get('server', '').lower():
            tech.append("Apache")

        # React
        if 'react' in html.lower() or 'reactdom' in html.lower():
            tech.append("React")

        # jQuery
        if 'jquery' in html.lower():
            tech.append("jQuery")

        return tech if tech else ["No technologies detected"]

    except Exception as e:
        return {"error": f"Tech detection error: {str(e)}"}

def output(data):
    if isinstance(data, dict) and "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    print(f"  {RED}[+] Technologies:{RESET}")
    for item in data:
        print(f"      {item}")