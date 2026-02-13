import os
import json
import logging
from logging import getLogger
from datetime import datetime
from .input_validation import validate_url
from services.risk_scoring import calculate_risk
from logging.handlers import RotatingFileHandler
from models.phishing_model import PhishingModel
from services.feature_extractor import extract_features

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "analysis.json")

# Configuração de logs
logger = getLogger("analysis_logger")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_FILE)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

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

    # Heurística
    features = extract_features(sanitized_url)
    score, classification = calculate_risk(features)
    
    # Machine Learning
    ml_output = ml_model.predict(sanitized_url)
    if ml_output is None:
        ml_result = "Modelo não disponível"
        ml_probability = 0
    else:
        ml_prediction ,ml_probability = ml_output
        if ml_probability >= 0.90: 
            score += 20
            ml_result = "Phishing"
        elif ml_probability <= 0.10:
            ml_result = "Legítimo"
        else:
            ml_result = "Inconclusivo"
    
    score = min(score, 100) # Limita o score a 100

    # Recalcula a classificação final após ML
    if score >= 70:
        classification = "Phishing"
        explanation = "A URL apresenta características fortemente associadas a phishing, como domínio suspeito, uso de IP, presença de palavras-chave comuns em ataques, etc."
    elif score >= 40:
        classification = "Suspeito"
        explanation = "A URL possui algumas características que podem indicar risco, como uso de subdomínios, presença de caracteres especiais, ou outras anomalias."
    else:
        classification = "Legitimo"
        explanation = "A URL não apresenta características comuns em ataques de phishing e é considerada de baixo risco."

    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "url": sanitized_url,
        "score": score,
        "classification": classification,
        "features": features,
        "explanation": explanation,
        "ml_probability": round(ml_probability* 100,2)
    }

    logger.info(json.dumps(log_entry, ensure_ascii=False))

    return{
        "url": sanitized_url,
        "score": score,
        "classification": classification,
        "features": features,
        "explanation": explanation,
        "ml_prediction": ml_result,
        "ml_probability": round(ml_probability* 100,2)
    }
    