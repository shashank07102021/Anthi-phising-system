import re
import validators
import socket
from urllib.parse import urlparse

def get_target_ip(url):
    try:
        domain =urlparse(url).netloc
        ip=socket.gethostbyname(domain)
        return ip 
    except Exception as e:
        return "could not resolve ip"

def check_url(url):
    if not validators.url(url):
        return "❌ Invalid URL format"

    suspicious_keywords = ['login', 'verify', 'account', 'bank', 'secure', 'update', 'confirm']
    shortening_services = ['bit.ly', 'tinyurl.com', 't.co', 'is.gd', 'ow.ly']
    risk_score = 0

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path

    # Rule 1: Shortened URL
    for short in shortening_services:
        if short in domain:
            risk_score += 2
            break

    # Rule 2: Suspicious keywords only in PATH
    for word in suspicious_keywords:
        if word in path.lower():
            risk_score += 2

    # Rule 3: IP address in URL
    ip_pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        risk_score += 3

    # Rule 4: Hyphen/dot count
    if domain.count('-') > 3 or domain.count('.') > 5:
        risk_score += 1

    # Score results
    if risk_score >= 5:
        return "Phishing"
    elif risk_score >= 3:
        return "Suspicious"
    else:
        return "Safe"
# Sample test
if __name__ == "__main__":
    while True:
        user_url = input("\nEnter a URL to scan (or type 'exit'): ")
        if user_url.lower() == "exit":
            break
        result = check_url(user_url)
        print("Result:", result)
