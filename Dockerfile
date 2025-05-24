FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

CMD python seed_data.py && gunicorn --bind :${PORT} --workers 1 --threads 8 --timeout 0 main:app