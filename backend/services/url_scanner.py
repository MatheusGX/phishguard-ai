from services.feature_extractor import extract_features
from services.risk_scoring import calculate_risk

def scan_url(url):
    features = extract_features(url)
    score, classification = calculate_risk(features)
    return {
        "url": url,
        "score": score,
        "classification": classification,
        "features": features
    }