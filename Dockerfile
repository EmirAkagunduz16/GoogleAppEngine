FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run seed_data.py during build
RUN python seed_data.py

ENV PORT=8080

CMD ["gunicorn", "--bind", ":${PORT}", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]
