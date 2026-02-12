from .input_validation import validate_url
from services.feature_extractor import extract_features
from services.risk_scoring import calculate_risk
from models.phishing_model import PhishingModel

ml_model = PhishingModel()

def analyze_url(url: str):
    is_valid, result = validate_url(url)

    if not is_valid:
        return {
            'url': url,
            'valid': False,
            'reason': result
        }
    sanitized_url = result

    # Heuristica
    features = extract_features(sanitized_url)
    score, classification = calculate_risk(features)
    
    # Machine Learning
    ml_output = ml_model.predict(sanitized_url)
    print(f"ML Output: {ml_output}")
    if ml_output is None:
        ml_result = "Modelo não disponível"
        ml_probability = 0
    else:
        ml_prediction, ml_probability = ml_output
        if ml_prediction == 1:
            score += 25
            ml_result = "Phishing"
        else:
            ml_result = "Legítimo"
            ml_probability = 1 - ml_probability # Probabilidade de ser legítimo
    
    score = min(score, 100) # Limita o score a 100

    # Recaulcula a classifição final após ML
    if score >= 70:
        classification = "phishing"
    elif score >= 40:
        classification = "suspeito"
    else:
        classification = "legitimo"

    return{
        "url": sanitized_url,
        "score": score,
        "classification": classification,
        "features": features,
        "ml_prediction": ml_result,
        "ml_probability": round(ml_probability* 100,2)
    }
    