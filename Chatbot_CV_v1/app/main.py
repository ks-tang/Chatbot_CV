import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 🔧 Base paths
BASE_DIR = os.path.dirname(__file__)  # /Chatbot_CV_v1/app
ROOT_DIR = os.path.dirname(BASE_DIR)  # /Chatbot_CV_v1

# 📁 Static files (optionnel mais nécessaire si dossier vide)
static_path_v1 = os.path.join(os.path.dirname(__file__), "Chatbot_CV_v1", "app", "static")
# static_path = os.path.join(BASE_DIR, "static")
if os.path.isdir(static_path_v1):
    app.mount("/static_v1", StaticFiles(directory=static_path_v1), name="static_v1")

# 📁 Templates
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# 📄 Chargement des données
questions_path = os.path.join(ROOT_DIR, "data", "questions.csv")
reponses_path = os.path.join(ROOT_DIR, "data", "reponses.csv")

questions_df = pd.read_csv(questions_path)
reponses_df = pd.read_csv(reponses_path)
reponses_dict = dict(zip(reponses_df["keyword"], reponses_df["answer"]))

# 🔍 Vectorisation TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions_df["question"])

# 🌐 Page d'accueil
@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 🔁 Réponse à la question
@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, question: str = Form(...)):
    vect = vectorizer.transform([question])
    similarities = cosine_similarity(vect, tfidf_matrix)
    best_match_index = similarities.argmax()
    best_match_key = questions_df.iloc[best_match_index]["keyword"]
    response = reponses_dict.get(best_match_key, "Désolé, je n’ai pas compris.")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "question": question,
        "response": response
    })
