# PhishingGuard AI
### Plataforma de Detecção de Phishing Baseada em Inteligencia Artificial

PhishGuard AI é um projeto acadêmico de uma aplicação web para analise de URLs suspeitos, combinando análise heurística e um modelo de Machine Learning treinado com dataset público de larga escala.

O sistema classifica URLs como:
🟢 Legítimo
🟡 Suspeito
🔴 Phishing Provável

## Objetivo

O objetivo do projeto é demonstrar a arquitetura e implementação de um sistema modular de detecção de phishing, baseado em:

- Análise heurística de URLs
- Extração de features
- Sistema de Risk Scoring heurístico
- Modelo supervisionado (TF-IDF + Logistic Regression)
- Arquitetura hibrida de decisão

O projeto tem finalidade académica e demonstra conceitos aplicados à cibersegurança e inteligencia artificial.

## Arquitetura do Sistema

O sistema segue uma arquitetura modular composta por:

- **Frontend** – Interface para inserção do URL e visualização do resultado
- **Backend** – Processamento da requisição e coordenação da análise
- **Security Layer** - Validação e coordenação
- **Módulo de Análise** – Extração de features e cálculo do risco
- **Risk Scoring** - Sistema Heurístico
- **ML Module** – Classificação baseada em Machine Learning
- **Logging** - Registo de análises

## Machine Learning

Modelo treinado com dataset público contendo 6 milhões de URLs maliciosas mas só 200000 foram utilizadas

Configuração:
- TF-IDF com análise por caracteres (n-grams 3-5)
- Logistic Regression
- Balanceamento manual das classes
- Threshold conservador para reduzir falsos positivos

O ML auxilia a heurística

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Scikit-learn
- HTML / tailwind / JavaScript
- Pandas

## Estrutura do Projeto

PhishGuard-ai/
├── backend/
│   ├── models/
│   ├── services/
│   ├── security/
│   └── routes/
├── frontend/
│   ├── templates/
│   └── static/
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
