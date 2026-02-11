import re
import tldextract

suspicious_keywords = ['login', 'secure', 'account', 'update', 'verify', 'bank', 'paypal', 'ebay']

def extract_features(url):
    extracted = tldextract.extract(url)

    features = {
        'length': len(url),
        'has_ip': bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)),
        'num_subdomains': len(extracted.subdomain.split('.')) if extracted.subdomain else 0,
        'has_https': url.startswith('https'),
        'suspicious_keywords': sum(1 for keyword in suspicious_keywords if keyword in url.lower())
    }

    return features