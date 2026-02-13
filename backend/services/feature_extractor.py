import re
import tldextract

suspicious_keywords = [
    'login', 'secure', 'account', 'update', 'verify', 'bank', 'paypal',
    'ebay', 'free', 'click', 'winner', 'prize', 'offer', 'bonus', 'limited',
    'urgent', 'important', 'confirm', 'password', 'signin', 
    'admin', 'support', 'help', 'service', 'webscr', 'cmd', 'redirect', 
    'submit', 'access', 'client', 'server', 'webmail', 'mail', 
    'email', 'user', 'users', 'customer', 'customers', 'security',
    'verification', 'accounts', 'banking', 'update', 'upgrade', 'reward', 
    'gift', 'restore', 'images', 'img', 'dispute', 'alibaba', 'webnode', 'wp', 
    'resolution', 'site', 'giveaway', '000webhostapp', 'js', 'css', 'php', 'view']

def extract_features(url):
    extracted = tldextract.extract(url)

    features = {
        'length': len(url),
        'has_ip': bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)),
        'num_subdomains': len(extracted.subdomain.split('.')) if extracted.subdomain else 0,
        'has_https': url.startswith('https'),
        'count_@': url.count('@'),
        'count_hyphen': url.count('-'),
        'count_dot': url.count('.'),
        'count_www': url.count('www'),
        'count_digits': sum(c.isdigit() for c in url),
        'count_underscore': url.count('_'),
        'suspicious_keywords': sum(1 for keyword in suspicious_keywords if keyword in url.lower())
    }

    return features