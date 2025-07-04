import re

def is_phishing_url(url):
    phishing_keywords = ["login", "update", "verify", "account", "banking", "secure", "ebay", "paypal", "webscr"]
    for keyword in phishing_keywords:
        if re.search(keyword, url, re.IGNORECASE):
            return True
    return False

url = input("Enter a URL to check: ")
if is_phishing_url(url):
    print("⚠️ Warning: This URL may be a phishing link.")
else:
    print("✅ This URL looks safe (based on basic keyword check).")
