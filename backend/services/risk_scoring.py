def calculate_risk(features):
    score = 0

    if features['length'] > 75:
        score += 20
    
    if features['has_ip']:
        score += 25

    if features['count_@'] > 0:
        score += 10

    if features['count_hyphen'] > 0:
        score += 10

    if features['count_dot'] > 3:
        score += 5

    if features['count_www'] > 0:
        score += 5

    if features['count_digits'] > 5:
        score += 10

    if features['count_underscore'] > 0:
        score += 5

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