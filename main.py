# main.py (dans /Chatbot_CV)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Chatbot_CV_v1.app.main import app as app_v1
from Chatbot_CV_v2.app.main import app as app_v2

app = FastAPI(title="Chatbot CV")

# CORS (facultatif selon ton usage web)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monter les deux versions sous des chemins distincts
app.mount("/v1", app_v1)
app.mount("/v2", app_v2)
