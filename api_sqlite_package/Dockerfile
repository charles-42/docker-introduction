FROM python:3.12-slim

RUN mkdir -p /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r app/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]