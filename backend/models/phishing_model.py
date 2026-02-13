import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "backend/models/model.pkl"
VECTORIZER_PATH = "backend/models/vectorizer.pkl"

class PhishingModel:
    def __init__(self):
        self.model = None
        self.vectorizer = None

        if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
            self.model = joblib.load(MODEL_PATH)
            self.vectorizer = joblib.load(VECTORIZER_PATH)

    def train(self, dataset_path):

        print("A carregar o dataset...")
        data = pd.read_csv(dataset_path, nrows=200000)

        data.columns = ["url", "label"]

        data["label"] = data["label"].map({
            "phishing": 1,
            "malware": 1,
            "defacement": 1,
            "benign": 0
        })

        data = data.dropna()

        # Diagnostivo do dataset
        print("Distribuição após mapeamento:")
        print(data["label"].value_counts())

        data["url"] =data["url"].str.lower()
        #garantir que as URLs comecem com http:// ou https://
        data["url"] = data["url"].apply(lambda x: x if x.startswith("http://") or x.startswith("https://") else "http://" + x)

        x = data["url"]
        y = data["label"]

        print("A vetorizar URLs...")

        self.vectorizer = TfidfVectorizer(
            analyzer="char",
            ngram_range=(3, 5),
            max_features=30000
        )
        x_vectorized = self.vectorizer.fit_transform(x)

        print("A treinar o modelo...")

        self.model = LogisticRegression(
            max_iter=2000,
            class_weight="balanced",
        )
        self.model.fit(x_vectorized, y)

        joblib.dump(self.model, MODEL_PATH)
        joblib.dump(self.vectorizer, VECTORIZER_PATH)

        print("Modelo treinado e salvo com sucesso.")

    def predict(self, url):
        if not self.model or not self.vectorizer:
            print("Modelo ou vetorizer não encontrado. Por favor, treine o modelo primeiro.")
            return None
        
        X = self.vectorizer.transform([url])
        prediction = self.model.predict(X)[0]
        probability = self.model.predict_proba(X)[0][1] # Probabilidade de ser phishing

        return prediction, probability