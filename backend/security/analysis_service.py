from .input_validation import validate_url
from services.feature_extractor import extract_features
from services.risk_scoring import calculate_risk

def analyze_url(url: str):
    is_valid, result = validate_url(url)

    if not is_valid:
        return {
            'url': url,
            'valid': False,
            'reason': result
        }
    sanitized_url = result

    features = extract_features(sanitized_url)
    score, classification = calculate_risk(features)

    return{
        "url": sanitized_url,
        "score": score,
        "classification": classification,
        "features": features
    }
    