- Creer un projet poetry:
poetry init

- Crer l'environnement virtuel
poetry install

- Installer un package
poetry add

- activer l'environnement virtuel
poetry shell

- créer un fichier requirements:
poetry export -f requirements.txt --output requirements.txt

- build l'image:
docker build -t api_example:latest .  

- run le container en mappant les parts
docker run -p 1234:8000  api_example:latest

- run le container en mappant les ports et créant un volume bdd
docker run -p 8000:8000 -v "./app/data:/app/data"  sqlite_api

- run le container en mappant les ports et créant un volume en mode dev
docker run -p 8000:8000 -v "./app/data:/app/data"  -v ".:/app" sqlite_api
