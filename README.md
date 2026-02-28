# Emotion Aware AI System

Dit project detecteert een gezicht via de webcam, schat een emotie met een eenvoudige heuristiek
(helderheid/contrast) en geeft daar passend advies bij. Het is een proof-of-concept dat later
vervangen kan worden door een echt getraind model (bijv. FER+, Mini-Xception, etc.).

## Vereisten

- Python 3.10 (aanbevolen)
- Webcam
- Zie `requirements.txt` voor Python-packages

## Installatie

# bash
`git clone https://github.com/<jouw-gebruikersnaam>/emotion-aware-ai-system.git`
`cd emotion-aware-ai-system`
`python -m venv .venv`
# Windows:
`.\.venv\Scripts\activate`
# macOS/Linux:
`source .venv/bin/activate`

`pip install -r requirements.txt`


## Runnen van de codes
- Runnen (real-time webcam): `python main.py`
- Runnen (Streamlit web-UI): `streamlit run ui.py`
