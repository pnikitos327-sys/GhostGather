import ipaddress
import re

def clean_target(value: str) -> str:
    if value is None:
        return ""
    value = str(value).strip()
    cleaned = []
    for ch in value:
        o = ord(ch)
        if 32 <= o <= 126:
            cleaned.append(ch)
    value = "".join(cleaned).strip()
    value = value.replace("http://", "").replace("https://", "")
    value = value.split("/")[0]
    value = value.split("?")[0]
    value = value.strip().lower()
    return value

def is_valid_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(clean_target(value))
        return True
    except ValueError:
        return False

def is_valid_domain(value: str) -> bool:
    value = clean_target(value)
    pattern = r"^(?!-)[a-z0-9-]{1,63}(?<!-)(\.[a-z0-9-]{1,63})+$"
    return re.fullmatch(pattern, value) is not None

def detect_target_type(value: str) -> str:
    value = clean_target(value)
    if is_valid_ip(value):
        return 'ip'
    if is_valid_domain(value):
        return 'domain'
    if '@' in value and '.' in value.split('@')[1]:
        return 'email'
    if value.startswith('+') or value.replace('+', '').isdigit():
        return 'phone'
    return 'username'
