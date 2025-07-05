import re
import validators

def check_url(url):
    if not validators.url(url):
        return "❌ Invalid URL format"

    suspicious_keywords = ['login', 'verify', 'account', 'bank', 'secure', 'update', 'confirm']
    shortening_services = ['bit.ly', 'tinyurl.com', 't.co', 'is.gd', 'ow.ly']

    risk_score = 0

    # Rule 1: Shortened URL check
    for shortener in shortening_services:
        if shortener in url:
            risk_score += 2
            break

    # Rule 2: Check for suspicious keywords
    for word in suspicious_keywords:
        if word in url.lower():
            risk_score += 2

    # Rule 3: Check for IP address in domain
    ip_pattern = r"(http[s]?://)?(\d{1,3}\.){3}\d{1,3}"
    if re.match(ip_pattern, url):
        risk_score += 3

    # Rule 4: Too many hyphens or dots
    if url.count('-') > 3 or url.count('.') > 5:
        risk_score += 1

    # Decision based on score
    if risk_score >= 5:
        return "🚨 Phishing"
    elif risk_score >= 2:
        return "⚠️ Suspicious"
    else:
        return "✅ Safe"

# Sample test
if __name__ == "__main__":
    while True:
        user_url = input("\nEnter a URL to scan (or type 'exit'): ")
        if user_url.lower() == "exit":
            break
        result = check_url(user_url)
        print("Result:", result)
