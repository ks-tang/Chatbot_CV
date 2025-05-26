import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sys

# Pour pouvoir importer les scripts
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.rag_engine import ask  # ou ton nom de script exact

app = FastAPI()

# Définir les chemins vers templates et static
base_dir = os.path.dirname(__file__)
static_dir = os.path.join(base_dir, "static")
templates_dir = os.path.join(base_dir, "templates")

# Monter les fichiers statiques de la version 2
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Définir le dossier des templates
templates = Jinja2Templates(directory=templates_dir)

# Routes
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask", response_class=HTMLResponse)
async def post_question(request: Request):
    form = await request.form()
    question = form["question"]
    response = ask(question)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question,
        "response": response
    })
