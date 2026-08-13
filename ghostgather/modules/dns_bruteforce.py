import socket
from colorama import Fore, Style

RED = Fore.RED
RESET = Style.RESET_ALL

COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk",
    "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test",
    "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn", "ns3",
    "mail2", "new", "mysql", "old", "lists", "support", "mobile", "mx", "static",
    "docs", "beta", "shop", "sql", "secure", "demo", "cp", "calendar", "wiki",
    "web", "media", "email", "images", "img", "download", "dns", "piwik", "stats",
    "dashboard", "portal", "manage", "start", "info", "apps", "video", "sip",
    "dns2", "api", "cdn", "mssql", "remote", "server", "ftp2", "stage", "store",
    "help", "services", "client", "clients", "database", "backup", "gateway",
    "member", "members", "auth", "login", "signin", "signup", "register",
    "account", "my", "app", "cloud", "files", "drive", "sync", "mailbox",
    "webmail2", "cp2", "panel", "admin2", "sys", "system", "webapp", "hub",
    "community", "forums", "chat", "stream", "live", "radio", "tv", "video2",
    "player", "api2", "rest", "graphql", "ws", "socket", "mqtt", "iot",
    "staging", "dev2", "test2", "sandbox", "internal", "corp", "office",
    "exchange", "outlook", "sharepoint", "lync", "skype", "teams",
    "jira", "confluence", "bitbucket", "git", "svn", "jenkins", "sonar",
    "monitor", "monitoring", "metrics", "logs", "kibana", "elastic", "elk",
    "grafana", "prometheus", "alert", "alerts", "status", "uptime", "health",
    "config", "conf", "settings", "setup", "install", "update", "upgrade",
    "patch", "release", "build", "ci", "cd", "deploy", "deployment", "prod",
    "prod2", "prod3", "prod4", "prod5", "prod6", "prod7", "prod8", "prod9"
]

def resolve_subdomain(subdomain, domain):
    full_domain = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(full_domain)
        return full_domain, ip
    except socket.gaierror:
        return None

def run(target):
    results = []
    for sub in COMMON_SUBDOMAINS:
        resolved = resolve_subdomain(sub, target)
        if resolved:
            results.append(resolved)
    return results

def output(data):
    if not data:
        print(f"  {RED}[-] No subdomains found{RESET}")
        return
    print(f"  {RED}[+] Found {len(data)} subdomains:{RESET}")
    for sub, ip in data:
        print(f"      {sub} -> {ip}")