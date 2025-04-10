import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

# Charger les questions/réponses
questions_df = pd.read_csv('data/questions.csv')  
reponses_df = pd.read_csv('data/reponses.csv') 

# Préparer un dictionnaire des réponses par mot-clé
reponses_dict = dict(zip(reponses_df['keyword'], reponses_df['answer']))

# Vectoriser les questions
vectorizer = TfidfVectorizer()
# Entraîner le modèle TF-IDF sur les questions
tfidf_matrix = vectorizer.fit_transform(questions_df['question'])


# Fonction pour trouver la réponse en fonction de la question
def find_answer(user_question):
    # Transformer la question utilisateur en vecteur
    user_question_tfidf = vectorizer.transform([user_question])

    # Calcul de la similarité entre la question de l'utilisateur et les questions de la base
    similarities = cosine_similarity(user_question_tfidf, tfidf_matrix)

    # Trouver l'index de la question la plus similaire
    most_similar_index = similarities.argmax()

    # Récupérer le mot-clé associé à la question la plus similaire
    keyword = questions_df.iloc[most_similar_index]['keyword']

    # Récupérer la réponse à ce mot-clé
    return reponses_dict[keyword]




if __name__ == "__main__":

    while True:
        user_question = input("Pose une question (exit pour arrêter): ")

        if user_question.lower() in ['exit', 'quitter']:
            print("Au revoir!")
            break

        response = find_answer(user_question)
        print(response)