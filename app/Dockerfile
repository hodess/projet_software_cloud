# Utiliser une image Python officielle et légère
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt d'abord (pour optimiser le cache Docker)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY main.py .

# Exposer le port 3000 (par défaut)
EXPOSE 5000

# Variable d'environnement pour le port
ENV PORT=5000

# Commande pour démarrer l'application
CMD ["python", "main.py"]

