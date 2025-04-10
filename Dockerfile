# Utilise une image officielle Python
FROM python:3.13.2

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY ./app ./app
COPY ./data ./data
COPY ./scripts ./scripts
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port
EXPOSE 8000

# Lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t chatbot-image .
# docker run --name chatbot_container -d -p 8000:8000 chatbot-image 