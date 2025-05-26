# Python 3.9 slim base image kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sistem bağımlılıklarını yükle
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıklarını kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Port ortam değişkenini ayarla
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Uygulamayı başlat - wsgi.py içindeki application'ı kullanıyoruz
CMD exec gunicorn --bind 0.0.0.0:$PORT --log-level info wsgi:application