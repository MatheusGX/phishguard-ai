from .input_validation import validate_url
from services import feature_extractor
from services import risk_scoring

def analyze_url(url: str):
    is_valid, result = validate_url(url)

    if not is_valid:
        return {
            'url': url,
            'valid': False,
            'reason': result
        }
    sanitized_url = result

    features = feature_extractor(sanitized_url)
    score, classification = risk_scoring(features)

    return{
        "url": sanitized_url,
        "score": score,
        "classification": classification,
        "features": features
    }
    