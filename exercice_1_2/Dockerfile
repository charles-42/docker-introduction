# Exemple simple de Dockerfile pour une application Python
FROM python:3.12-slim
# crée un dossier /app dans mon container et le défini comme répertoire de travail: là ou s'execute les commandes
WORKDIR /app 
# copie le code depuis le dossier ou est mon dockerfile vers le dossier /app de mon container
COPY . /app

CMD ["python", "main.py"]