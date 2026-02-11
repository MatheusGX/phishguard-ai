# PhishingGuard AI
### Plataforma de Deteçao de Phishing Baseada em Inteligencia Artificial

PhishGuard AI é um software com um sistema que permite analisar URLs suspeitos e
classifica-los como legitimos ou potenciamente maliciosos (phishing), combinando heuristicas e técnicas de inteligencia artificial.

## Objetivo

O objetivo do projeto é demonstrar a arquitetura e implementaçao de um sistema modular de deteçao de phishing, integrando:

- Análise heurística de URLs
- Extração de features
- Sistema de Risk Scoring
- (Opcional) Modelo de Machine Learning (TF-IDF + Logistic Regression)
- (Opcional) Integração com VirusTotal para threat intelligence externa

O sistema não pretende substituir soluções comerciais, mas sim demonstrar conceitos técnicos e arquiteturais aplicados à cibersegurança.

## Arquitetura do Sistema

O sistema segue uma arquitetura modular composta por:

- **Frontend** – Interface para inserção do URL e visualização do resultado
- **Backend** – Processamento da requisição e coordenação da análise
- **Módulo de Análise** – Extração de features e cálculo do risco
- **Módulo de IA** – Classificação baseada em Machine Learning
- **Integração Externa (opcional)** – Consulta ao VirusTotal

## Funcionalidades

- Validação de URL
- Análise de padrões suspeitos
- Identificação de palavras-chave maliciosas
- Cálculo de Risk Score (0–100)
- Classificação:
  - 🟢 Legítimo
  - 🟡 Suspeito
  - 🔴 Phishing provável

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Scikit-learn
- HTML / CSS / JavaScript
- API VirusTotal

## Estrutura do Projeto

phishguard-ai/
│
├── backend/
├── frontend/
├── docs/
├── tests/
├── requirements.txt
└── README.md

## Como executar o Projeto

### 1 Clonar o repositorio

git clone https://github.com/MatheusGX/phishguard-ai.git

### Criar ambiente virtual

python -m venv venv
venv\Scripts\acvivate

### Instalar dependencias

pip install -r requirements.txt

### Executar aplicaçao

python backend/app.py

Aceder a: http://127.0.0.1:5000