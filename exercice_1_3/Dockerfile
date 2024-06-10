# Exemple simple de Dockerfile pour une application Python
FROM python:3.12-slim

RUN pip install pandas

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]