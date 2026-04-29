FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip 
    && pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 3000

CMD ["sh", "-c", "python -m app.seed && uvicorn app.main:app --host 0.0.0.0 --port 3000"]
