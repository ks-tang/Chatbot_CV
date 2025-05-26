from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = FastAPI()

# Monte les fichiers HTML et CSS
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory="templates")

# Charge les questions et réponses
base_dir = os.path.dirname(os.path.dirname(__file__))  # remonte à Chatbot_CV_v1
questions_path = os.path.join(base_dir, "data", "questions.csv")
reponses_path = os.path.join(base_dir, "data", "reponses.csv")

questions_df = pd.read_csv(questions_path)
reponses_df = pd.read_csv(reponses_path)
reponses_dict = dict(zip(reponses_df["keyword"], reponses_df["answer"]))

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions_df["question"])

# Home endpoint
@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ask endpoint
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

@app.get("/chatbot-advanced")
def render_advanced():
    return templates.TemplateResponse("advanced.html", {"request": request})

# uvicorn app.main:app --reload