# main.py (dans /Chatbot_CV)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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



@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse("""
        <html>
        <head><title>Chatbot CV</title></head>
        <body>
            <h1>Bienvenue sur le Chatbot CV</h1>
            <p><a href="/v1">➡️ Accéder à la version 1</a></p>
            <p><a href="/v2">➡️ Accéder à la version 2</a></p>
        </body>
        </html>
    """)