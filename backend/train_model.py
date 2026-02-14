from models.phishing_model import PhishingModel

model = PhishingModel()
model.train("backend/data/URLdataset.csv")