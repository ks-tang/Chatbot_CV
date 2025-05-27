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


# Répertoire courant = app/
BASE_DIR = os.path.dirname(__file__)

# Chemins vers static et templates
static_path = os.path.join(BASE_DIR, "static")
templates_path = os.path.join(BASE_DIR, "templates")

# Montage du dossier static à l’URL "/static"
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Initialisation des templates
templates = Jinja2Templates(directory=templates_path)

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
