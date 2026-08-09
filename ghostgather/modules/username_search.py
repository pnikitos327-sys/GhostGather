from colorama import Fore, Style
import re
import urllib.request
import json

RED = Fore.RED
RESET = Style.RESET_ALL

def clean_username(username):
    """Очищает имя пользователя"""
    if not username:
        return ""
    cleaned = re.sub(r'[^a-zA-Z0-9_.-]', '', username.strip())
    return cleaned

def check_social_media(username):
    """Проверяет наличие username на социальных платформах"""
    sites = {
        'GitHub': f'https://github.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://instagram.com/{username}',
        'Reddit': f'https://reddit.com/user/{username}',
        'YouTube': f'https://youtube.com/@{username}',
        'Pinterest': f'https://pinterest.com/{username}',
        'TikTok': f'https://tiktok.com/@{username}',
        'Twitch': f'https://twitch.tv/{username}',
        'Steam': f'https://steamcommunity.com/id/{username}',
        'Spotify': f'https://open.spotify.com/user/{username}',
    }
    
    found = []
    for site, url in sites.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=3)
            if response.getcode() == 200:
                found.append(f"  [+] {site}: {url}")
        except:
            pass
    
    return found

def run(target):
    username = clean_username(target)
    if not username:
        return {"error": "Invalid username"}
    
    results = {
        "username": username,
        "social_media": check_social_media(username)
    }
    return results

def output(data):
    if "error" in data:
        print(f"  {RED}[-] {data['error']}{RESET}")
        return
    
    print(f"  {RED}[+] Username: {data['username']}{RESET}")
    print(f"  {RED}[+] Found on:{RESET}")
    if data['social_media']:
        for site in data['social_media']:
            print(f"    {site}")
    else:
        print(f"    {RED}[-] Not found on common platforms{RESET}")
