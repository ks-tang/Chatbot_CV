from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Monte les fichiers HTML et CSS
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Charge les questions et réponses
questions_df = pd.read_csv("../data/questions.csv")
reponses_df = pd.read_csv("../data/reponses.csv")
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