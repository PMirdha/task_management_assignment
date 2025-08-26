# Dockerfile for FastAPI backend
FROM python:3.11-slim-bookworm

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get upgrade -y && apt-get clean \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
