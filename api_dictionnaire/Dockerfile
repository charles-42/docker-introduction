FROM python:3.12-slim

ENV DATABASE_URL="sqlite:///./test.db"

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["watchmedo", "auto-restart", "--directory=.", "--pattern=*.py", "--recursive", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]