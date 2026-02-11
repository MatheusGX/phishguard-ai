def calculate_risk(features):
    score = 0

    if features['length'] > 75:
        score += 20
    
    if features['has_ip']:
        score += 25

    if features['num_subdomains'] > 2:
        score += 15
    
    if not features['has_https']:
        score += 20
    
    score += features['suspicious_keywords'] * 10

    if score >= 70:
        classification = 'high risk Phishing'
    elif score >= 40:
        classification = 'suspicious Phishing'
    else:
        classification = 'legitimate'

    return score, classification