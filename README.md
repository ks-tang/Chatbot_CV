# 🤖 Chatbot CV – Kévin Tang

Bienvenue sur mon projet **Chatbot CV**, un assistant interactif permettant de découvrir mon parcours, mes compétences et mes projets sous forme de conversation.  
Le chatbot est accessible en deux versions :

- 🔹 **Version 1** : Basée sur TF-IDF et similarité cosinus
- 🔸 **Version 2** : Basée sur un modèle de langage local via RAG (Retrieval-Augmented Generation)

---

## 🧠 Objectifs

- Présenter mon profil de manière interactive.
- Proposer une interface conversationnelle personnalisée à partir de mon CV
- Utiliser différentes approches du NLP : TF-IDF et modèle de langage (LLM local via RAG).
- Déployer deux versions du chatbot accessibles via une interface web

---

## ✨ Fonctionnalités

🔹 Version 1 (TF-IDF)
- Répond à des questions précises
- Basée sur un fichier .csv de Q/R
- Approche NLP classique (vectorisation TF-IDF, similarité cosinus)
- Lien vers LinkedIn et GitHub

🔸 Version 2 (LLM + RAG)
- Recherche d'information dans mon CV (cv.txt)
- Indexation vectorielle avec FAISS
- Génération de réponse via LLM local (Mistral)
- Architecture modulaire pour intégrer d’autres documents ou modèles

---

## 🧰 Technologies utilisées

Composant	Technologies
Backend	: FastAPI, LangChain, FAISS
NLP	: TF-IDF (sklearn), LLM local via Ollama
Frontend : HTML, CSS (templates Jinja2)
Serveur LLM :	Ollama (Mistral 7B)
Vectorisation :	FAISS
Conteneurisation : Docker
Déploiement local : Uvicorn
Déploiement cloud : Render

---

Le chatbot est disponible ici (si actif) : https://chatbot-cv.onrender.com/
