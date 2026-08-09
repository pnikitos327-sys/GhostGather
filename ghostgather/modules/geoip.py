from colorama import Fore, Style
import urllib.request
import json

RED = Fore.RED
RESET = Style.RESET_ALL

def get_geoip(ip):
    """Получает геоданные по IP через бесплатный API"""
    try:
        # Используем бесплатный API ip-api.com
        url = f"http://ip-api.com/json/{ip}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        data = json.loads(response.read().decode())
        
        if data.get('status') == 'success':
            return {
                'ip': ip,
                'country': data.get('country', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'region': data.get('regionName', 'Unknown'),
                'isp': data.get('isp', 'Unknown'),
                'org': data.get('org', 'Unknown'),
                'lat': data.get('lat', 0),
                'lon': data.get('lon', 0),
                'timezone': data.get('timezone', 'Unknown')
            }
        return {"error": "Could not get geoip data"}
    except:
        return {"error": "GeoIP service unavailable"}

def run(target):
    return get_geoip(target)

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] IP: {data['ip']}{RESET}")
    print(f"  {RED}[+] Country: {data['country']}{RESET}")
    print(f"  {RED}[+] Region: {data['region']}{RESET}")
    print(f"  {RED}[+] City: {data['city']}{RESET}")
    print(f"  {RED}[+] ISP: {data['isp']}{RESET}")
    print(f"  {RED}[+] Organization: {data['org']}{RESET}")
    print(f"  {RED}[+] Timezone: {data['timezone']}{RESET}")
    print(f"  {RED}[+] Coordinates: {data['lat']}, {data['lon']}{RESET}")
