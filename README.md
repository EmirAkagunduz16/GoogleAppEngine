# 📚 Dijital Kütüphane Yönetim Sistemi
## Digital Library Management System

Bu proje, Google App Engine üzerinde çalışan modern bir dijital kütüphane yönetim sistemidir. Flask framework'ü kullanılarak geliştirilmiş olup, MVC (Model-View-Controller) mimarisi ile yapılandırılmıştır.

## 🚀 Proje Özellikleri

### ✨ Kullanıcı Özellikleri
- **Kullanıcı Kimlik Doğrulama**: Güvenli kayıt ve giriş sistemi
- **Kitap Arama ve Filtreleme**: Gelişmiş arama motoru
- **Kitap Rezervasyonu**: Tek tıkla kitap rezerve etme
- **Kişisel Dashboard**: Rezervasyon takibi ve istatistikler
- **Responsive Tasarım**: Mobil uyumlu modern arayüz

### 🔧 Admin Özellikleri
- **Kitap Yönetimi**: Ekleme, düzenleme, silme
- **Kullanıcı Yönetimi**: Kullanıcı ve rezervasyon takibi
- **İstatistikler**: Detaylı raporlar ve analitik
- **Sistem Yönetimi**: Kapsamlı admin paneli

### 🛠️ Teknik Özellikler
- **Serverless Mimari**: Google App Engine
- **NoSQL Veritabanı**: Firestore
- **Modern Framework**: Flask + Bootstrap 5
- **Güvenlik**: Hash'lenmiş şifreler, session yönetimi
- **API Entegrasyonu**: RESTful API'ler
- **Real-time Updates**: Otomatik veri güncellemeleri

## 📋 Gereksinimler

- Python 3.9+
- Google Cloud Platform hesabı
- Google Cloud SDK (`gcloud`)
- Firestore veritabanı


## 🏗️ MVC Mimarisi

Proje, temiz kod prensipleri ve sürdürülebilirlik için MVC (Model-View-Controller) mimarisi kullanılarak yeniden yapılandırılmıştır:

### 📁 Proje Yapısı

```
GoogleAppEngineProject/
├── app/                          # Ana uygulama paketi
│   ├── __init__.py              # Flask uygulama fabrikası
│   ├── config.py                # Uygulama konfigürasyonu
│   │
│   ├── models/                  # Model katmanı (M)
│   │   ├── __init__.py
│   │   ├── user.py             # Kullanıcı modeli
│   │   ├── book.py             # Kitap modeli
│   │   └── reservation.py      # Rezervasyon modeli
│   │
│   ├── controllers/             # Controller katmanı (C)
│   │   ├── __init__.py
│   │   ├── main_controller.py  # Ana sayfa ve dashboard
│   │   ├── auth_controller.py  # Kimlik doğrulama
│   │   ├── book_controller.py  # Kitap işlemleri
│   │   └── admin_controller.py # Admin işlemleri
│   │
│   ├── services/               # İş mantığı katmanı
│   │   ├── __init__.py
│   │   ├── auth_service.py     # Kimlik doğrulama servisi
│   │   ├── book_service.py     # Kitap servisi
│   │   └── reservation_service.py # Rezervasyon servisi
│   │
│   ├── views/                  # View katmanı (V)
│   │   ├── layouts/
│   │   │   └── base.html       # Ana şablon
│   │   ├── main/
│   │   │   └── index.html      # Ana sayfa
│   │   ├── auth/
│   │   │   ├── login.html      # Giriş sayfası
│   │   │   └── register.html   # Kayıt sayfası
│   │   ├── books/
│   │   │   ├── index.html      # Kitap listesi
│   │   │   └── detail.html     # Kitap detayı
│   │   ├── user/
│   │   │   └── dashboard.html  # Kullanıcı paneli
│   │   └── admin/
│   │       ├── dashboard.html  # Admin paneli
│   │       ├── books.html      # Kitap yönetimi
│   │       ├── add_book.html   # Kitap ekleme
│   │       └── reservations.html # Rezervasyon yönetimi
│   │
│   ├── static/                 # Statik dosyalar
│   │   ├── css/
│   │   │   └── main.css        # Ana CSS dosyası
│   │   ├── js/
│   │   │   └── main.js         # Ana JavaScript dosyası
│   │   └── images/             # Resim dosyaları
│   │
│   └── utils/                  # Yardımcı araçlar
│       ├── __init__.py
│       ├── decorators.py       # Dekoratörler
│       └── helpers.py          # Yardımcı fonksiyonlar
│
├── main.py                     # Uygulama giriş noktası
├── app.yaml                    # Google App Engine konfigürasyonu
├── requirements.txt            # Python bağımlılıkları
├── seed_data.py               # Örnek veri oluşturucu
└── README.md                  # Bu dosya
```

## 🚀 Özellikler

### 👤 Kullanıcı Yönetimi
- Kullanıcı kaydı ve giriş sistemi
- Güvenli şifre hashleme (Werkzeug)
- Oturum yönetimi
- Rol tabanlı erişim kontrolü (Admin/Kullanıcı)

### 📚 Kitap Yönetimi
- Kitap ekleme, düzenleme, silme (Admin)
- Gelişmiş arama ve filtreleme
- Kategori bazlı sınıflandırma
- Stok takibi (toplam/mevcut kopya sayısı)

### 📋 Rezervasyon Sistemi
- Kitap rezervasyonu yapma
- 14 günlük ödünç alma süresi
- Otomatik gecikme hesaplama
- Rezervasyon geçmişi
- Admin tarafından rezervasyon yönetimi

### 📊 Dashboard ve İstatistikler
- Kullanıcı dashboard'u
- Admin yönetim paneli
- Gerçek zamanlı istatistikler
- Rezervasyon durumu takibi

### 🎨 Modern Arayüz
- Bootstrap 5 ile responsive tasarım
- Font Awesome ikonları
- Özel CSS animasyonları
- Mobil uyumlu tasarım

## 🛠️ Teknoloji Yığını

### Backend
- **Python 3.9+**
- **Flask 2.3.3** - Web framework
- **Google Cloud Firestore** - NoSQL veritabanı
- **Werkzeug** - Şifre hashleme ve güvenlik

### Frontend
- **Bootstrap 5.3.2** - CSS framework
- **Font Awesome 6.4.0** - İkonlar
- **JavaScript ES6+** - İnteraktif özellikler
- **Google Fonts** - Tipografi

### Cloud & DevOps
- **Google App Engine** - Serverless hosting
- **Google Cloud Firestore** - Veritabanı
- **Python Virtual Environment** - Bağımlılık yönetimi

## 📦 Kurulum

### 1. Projeyi İndirin
```bash
git clone <repository-url>
cd GoogleAppEngineProject
```

### 2. Virtual Environment Oluşturun
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate     # Windows
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

## 🚀 Deployment (Google App Engine)

### 1. Deployment
```bash
gcloud app deploy
```

### 2. Canlı URL'yi Açma
```bash
gcloud app browse
```

## 🐳 Deployment (Google Cloud Run)

Google Cloud Run, daha esnek bir containerized deployment seçeneği sunar. Bu yöntem ile uygulamanızı Docker container olarak çalıştırabilirsiniz.

### 📋 Hızlı Başlangıç Kontrol Listesi

Deployment öncesi gerekli adımlar:

- [ ] ✅ Google Cloud hesabı var
- [ ] ✅ Billing hesabı aktif
- [ ] ✅ Google Cloud SDK kurulu (`gcloud`)
- [ ] ✅ Docker kurulu (yerel test için)
- [ ] ✅ Proje dosyaları hazır

### 0. Önkoşullar Kontrolü

```bash
# Google Cloud SDK kurulu mu?
gcloud version

# Docker kurulu mu?
docker --version

# Proje dizinine git
cd /path/to/GoogleAppEngineProject
```

### 1. Dockerfile Oluşturma

Proje kök dizininde `Dockerfile` dosyası oluşturun:

```dockerfile
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

# Uygulamayı başlat
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
```

### 2. Google Cloud Ayarları

```bash
# Google Cloud SDK kurulumu (eğer yoksa)
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Proje oluşturma ve ayarlama
gcloud projects create your-project-id
gcloud config set project your-project-id

# Gerekli API'leri etkinleştirme
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable firestore.googleapis.com

# Firestore veritabanı etkinleştirme
gcloud firestore databases create --region=europe-west1
```

#### 🌐 Alternatif: Google Cloud Console'dan Kurulum

**Yeni Proje Oluşturma:**
- https://console.cloud.google.com/projectcreate
- Proje adını girin ve billing hesabınızı seçin

**API'leri Etkinleştirme:**
- Cloud Run API: https://console.cloud.google.com/apis/library/run.googleapis.com
- Cloud Build API: https://console.cloud.google.com/apis/library/cloudbuild.googleapis.com  
- Firestore API: https://console.cloud.google.com/apis/library/firestore.googleapis.com

**Firestore Database:**
- https://console.cloud.google.com/firestore
- "Create database" → "Native mode" → Location: "europe-west1"

#### 🔧 Proje Ayarları

```bash
# Gcloud'u yeni projeye bağlama
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login

# Gunicorn bağımlılığını ekleme
echo "gunicorn==21.2.0" >> requirements.txt

# Örnek verileri yükleme
python seed_data.py
```

### 3. Container Image Oluşturma ve Deploy

```bash
# Container image'ı Google Container Registry'ye build et
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/digital-library

# Cloud Run'a deploy et
gcloud run deploy digital-library \
    --image gcr.io/YOUR_PROJECT_ID/digital-library \
    --platform managed \
    --region europe-west1 \
    --allow-unauthenticated \
    --memory 512Mi \
    --cpu 1 \
    --max-instances 100
```

### 4. Ortam Değişkenlerini Ayarlama (Opsiyonel)

```bash
# Secret key ayarlama
gcloud run services update digital-library \
    --region europe-west1 \
    --set-env-vars SECRET_KEY="your-secret-key-here"
```

### 5. Custom Domain Ayarlama (Opsiyonel)

```bash
# Domain mapping oluşturma
gcloud run domain-mappings create \
    --service digital-library \
    --domain your-domain.com \
    --region europe-west1
```

### 6. Deployment Sonrası Kontrol

#### ✅ Cloud Run Console'dan Monitoring
- https://console.cloud.google.com/run
- Service durumunu, logs'ları ve metrics'leri izleyebilirsiniz
- Environment variables ve scaling ayarlarını güncelleyebilirsiniz

#### 🧪 Uygulama Testi
Deploy edilen URL'yi ziyaret edin ve test edin:
- Ana sayfa yüklenmelidir
- Demo hesaplarla giriş yapabilmelidir:
  - Admin: `admin@kutuphane.com` / `admin123`
  - Kullanıcı: `ahmet@example.com` / `user123`

#### 📊 Service URL'ini Alma
```bash
# Deploy edilen servisin URL'ini öğrenme
gcloud run services describe digital-library \
    --region europe-west1 \
    --format="value(status.url)"
```

### 🔧 Cloud Run Konfigürasyon Seçenekleri

#### CPU ve Memory Ayarları
```bash
# Performans ayarları
gcloud run services update digital-library \
    --region europe-west1 \
    --memory 1Gi \
    --cpu 2 \
    --concurrency 80 \
    --max-instances 100 \
    --min-instances 0
```

#### Traffic Splitting (Blue/Green Deployment)
```bash
# Yeni revision'a %50 traffic yönlendirme
gcloud run services update-traffic digital-library \
    --region europe-west1 \
    --to-revisions REVISION_NAME=50,LATEST=50
```

### 📊 Cloud Run vs App Engine Karşılaştırması

| Özellik | Cloud Run | App Engine |
|---------|-----------|------------|
| **Container Support** | ✅ Native Docker | ❌ Runtime specific |
| **Cold Start** | ~100-500ms | ~1-3s |
| **Pricing** | Pay per request | Pay per instance hour |
| **Scalability** | 0-1000 instances | Automatic |
| **Custom Runtime** | ✅ Any language | ❌ Supported runtimes |
| **Memory Limit** | Up to 8GB | Up to 1GB |
| **CPU** | Up to 4 vCPU | Up to 2.4GHz |
| **HTTP/2** | ✅ Native | ✅ Supported |
| **WebSocket** | ✅ Full support | ❌ Limited |
| **Background Tasks** | ❌ Request-scoped | ✅ Supported |

### ⚠️ Cloud Run Specific Considerations

#### 1. **Stateless Design**
- Cloud Run containers are stateless
- Use external storage for persistent data
- Session data should be stored in Firestore or Redis

#### 2. **Request Timeout**
- Maximum request timeout: 3600 seconds
- Default timeout: 300 seconds
- Configure based on your needs

#### 3. **File System**
- File system is read-only except `/tmp`
- Use Cloud Storage for file uploads
- Temporary files in `/tmp` are lost on scale-down

#### 4. **Environment Variables**
```bash
# Production environment variables
gcloud run services update digital-library \
    --region europe-west1 \
    --set-env-vars \
    FLASK_ENV=production,\
    SECRET_KEY=your-secret-key,\
    GOOGLE_CLOUD_PROJECT=your-project-id
```

### 🛠️ Local Development with Docker

```bash
# Local olarak Docker ile test etme
docker build -t digital-library .
docker run -p 8080:8080 \
    -e GOOGLE_CLOUD_PROJECT=your-project-id \
    -e SECRET_KEY=dev-secret-key \
    digital-library

# Docker Compose ile (opsiyonel)
# docker-compose.yml dosyası oluşturun:
```

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8080:8080"
    environment:
      - GOOGLE_CLOUD_PROJECT=your-project-id
      - SECRET_KEY=dev-secret-key
      - FLASK_ENV=development
    volumes:
      - .:/app
    command: python main.py
```

### 🔄 CI/CD Pipeline (Cloud Build)

**cloudbuild.yaml** dosyası oluşturun:

```yaml
steps:
  # Build the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/digital-library:$COMMIT_SHA', '.']
  
  # Push the container image to Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/digital-library:$COMMIT_SHA']
  
  # Deploy container image to Cloud Run
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
    - 'run'
    - 'deploy'
    - 'digital-library'
    - '--image'
    - 'gcr.io/$PROJECT_ID/digital-library:$COMMIT_SHA'
    - '--region'
    - 'europe-west1'
    - '--platform'
    - 'managed'
    - '--allow-unauthenticated'

images:
  - 'gcr.io/$PROJECT_ID/digital-library:$COMMIT_SHA'
```

## 🔐 Demo Hesapları

Sistem örnek verilerle birlikte gelir:

### Admin Hesabı
- **E-posta:** admin@kutuphane.com
- **Şifre:** admin123

### Kullanıcı Hesapları
- **E-posta:** ahmet@example.com / **Şifre:** user123
- **E-posta:** ayse@example.com / **Şifre:** user123
- **E-posta:** mehmet@example.com / **Şifre:** user123

## 🏛️ MVC Mimarisi Detayları

### Model Katmanı (app/models/)
- **User Model:** Kullanıcı verilerini ve kimlik doğrulama işlemlerini yönetir
- **Book Model:** Kitap bilgilerini ve stok durumunu yönetir
- **Reservation Model:** Rezervasyon işlemlerini ve durumlarını yönetir

### Controller Katmanı (app/controllers/)
- **MainController:** Ana sayfa ve dashboard rotalarını yönetir
- **AuthController:** Giriş, kayıt ve çıkış işlemlerini yönetir
- **BookController:** Kitap görüntüleme ve rezervasyon işlemlerini yönetir
- **AdminController:** Admin paneli işlemlerini yönetir

### Service Katmanı (app/services/)
- **AuthService:** Kimlik doğrulama iş mantığı
- **BookService:** Kitap işlemleri iş mantığı
- **ReservationService:** Rezervasyon işlemleri iş mantığı

### View Katmanı (app/views/)
- Jinja2 şablonları ile HTML renderı
- Modüler şablon yapısı
- Responsive tasarım

## 📊 API Endpoints

### Genel API'ler
- `GET /api/stats` - Kütüphane istatistikleri
- `GET /books/api` - Kitap listesi (JSON)

### Kullanıcı Rotaları
- `GET /` - Ana sayfa
- `GET /dashboard` - Kullanıcı dashboard'u
- `GET /books/` - Kitap listesi
- `GET /books/<id>` - Kitap detayı
- `POST /books/<id>/reserve` - Kitap rezervasyonu
- `POST /books/reservation/<id>/return` - Kitap iadesi

### Kimlik Doğrulama
- `GET/POST /auth/login` - Giriş
- `GET/POST /auth/register` - Kayıt
- `GET /auth/logout` - Çıkış

### Admin Rotaları
- `GET /admin/` - Admin dashboard
- `GET /admin/books` - Kitap yönetimi
- `GET/POST /admin/books/add` - Kitap ekleme
- `GET /admin/reservations` - Rezervasyon yönetimi

## 🔧 Konfigürasyon

### Ortam Değişkenleri
```bash
export SECRET_KEY="your-secret-key"
export FLASK_DEBUG=True  # Sadece geliştirme için
```

### Firestore Konfigürasyonu
- Proje otomatik olarak Google Cloud Firestore'a bağlanır
- Yerel geliştirme için emülatör kullanılabilir

## 🧪 Test Etme

### Yerel Test
```bash
python main.py
```

### Fonksiyonel Test Senaryoları
1. Kullanıcı kaydı ve girişi
2. Kitap arama ve filtreleme
3. Kitap rezervasyonu
4. Admin paneli işlemleri
5. Rezervasyon iade işlemi

## 📋 Sorun Giderme

### ⚠️ Yaygın Deployment Sorunları

#### 1. **App.yaml Dosyası Bulunamadı Hatası**
```bash
ERROR: An app.yaml (or appengine-web.xml) file is required to deploy this directory
```

**Çözüm:**
```bash
# Doğru proje dizinine gidin
cd /path/to/GoogleAppEngineProject

# Dizinin doğru olduğunu kontrol edin
ls -la  # app.yaml dosyasının burada olması gerekir

# Şimdi deploy işlemini tekrar deneyin
gcloud app deploy
```

#### 2. **Google Cloud Project Kurulum Sorunları**

**Adım 1: Billing Hesabı Aktifleştirme (Zorunlu)**
```bash
# Billing hesabınızı Google Cloud Console'dan aktifleştirin
# https://console.cloud.google.com/billing
```

**Adım 2: App Engine Uygulaması Oluşturma Sorunları**
```bash
# Komut satırından app oluşturmaya çalışın
gcloud app create --region=europe-west1

# Eğer "App already exists" hatası alırsanız:
gcloud app describe

# Eğer yukarıdaki komut hata verirse, manuel olarak oluşturun:
```

**Manuel App Engine Oluşturma (Önerilen):**
1. https://console.cloud.google.com/appengine adresine gidin
2. "Create Application" butonuna tıklayın
3. Region olarak "europe-west1" seçin
4. "Create" butonuna tıklayın

**Adım 3: Gerekli API'leri Etkinleştirme**
```bash
# App Engine API'yi etkinleştirin
gcloud services enable appengine.googleapis.com

# Firestore API'yi etkinleştirin
gcloud services enable firestore.googleapis.com

# Cloud Build API'yi etkinleştirin (deployment için)
gcloud services enable cloudbuild.googleapis.com
```

#### 3. **Firestore Veritabanı Kurulumu**
```bash
# Firestore Native modunda oluşturun
gcloud firestore databases create --location=europe-west1

# Eğer hata alırsanız, Google Cloud Console'dan manuel olarak oluşturun:
# https://console.cloud.google.com/firestore
```

#### 4. **Proje ID ve Authentication Sorunları**
```bash
# Aktif projeyi kontrol edin
gcloud config get-value project

# Proje ID'yi ayarlayın
gcloud config set project YOUR_PROJECT_ID

# Authentication'ı yenileyin
gcloud auth login
gcloud auth application-default login
```

### 🔧 Deployment Öncesi Kontrol Listesi

Deployment yapmadan önce aşağıdakileri kontrol edin:

- [ ] ✅ Google Cloud Project oluşturuldu
- [ ] ✅ Billing hesabı aktifleştirildi
- [ ] ✅ App Engine uygulaması oluşturuldu
- [ ] ✅ Firestore veritabanı oluşturuldu
- [ ] ✅ Gerekli API'ler etkinleştirildi
- [ ] ✅ Doğru proje dizininde bulunuyorsunuz
- [ ] ✅ `app.yaml` dosyası mevcut
- [ ] ✅ `requirements.txt` dosyası mevcut
- [ ] ✅ `gcloud` authentication yapılmış

### 📋 Adım Adım Deployment Süreci

#### Cloud Shell Kullanıyorsanız:

1. **Proje dosyalarını Cloud Shell'e yükleyin:**
```bash
# Dosyaları zip olarak yükleyin ve açın
unzip GoogleAppEngineProject.zip
cd GoogleAppEngineProject
```

2. **Proje ayarlarını yapılandırın:**
```bash
# Proje ID'yi ayarlayın
gcloud config set project YOUR_PROJECT_ID

# Gerekli API'leri etkinleştirin
gcloud services enable appengine.googleapis.com
gcloud services enable firestore.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

3. **App Engine uygulamasını oluşturun:**
```bash
# Manuel olarak Google Cloud Console'dan oluşturmanız önerilir
# https://console.cloud.google.com/appengine
```

4. **Firestore veritabanını oluşturun:**
```bash
gcloud firestore databases create --location=europe-west1
```

5. **Örnek verileri yükleyin:**
```bash
python seed_data.py
```

6. **Deploy edin:**
```bash
gcloud app deploy
```

### Yaygın Sorunlar

1. **Firestore Bağlantı Hatası**
   ```bash
   gcloud auth application-default login
   ```

2. **Port Çakışması**
   ```bash
   # Farklı port kullanın
   python main.py --port 8081
   ```

3. **Bağımlılık Hataları**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

4. **App Engine Region Hatası**
   ```bash
   # Eğer farklı region kullanmak istiyorsanız
   gcloud app create --region=us-central1
   ```

5. **Deployment Timeout**
   ```bash
   # Daha uzun timeout ile deneyin
   gcloud app deploy --timeout=1200
   ```

### 🆘 Acil Durum Çözümleri

#### Tüm Ayarları Sıfırlama:
```bash
# Proje konfigürasyonunu sıfırlayın
gcloud config unset project
gcloud config set project YOUR_PROJECT_ID

# Authentication'ı yenileyin
gcloud auth revoke
gcloud auth login
gcloud auth application-default login
```

#### Alternatif Deployment Yöntemi:
```bash
# App.yaml'ı belirterek deploy edin
gcloud app deploy app.yaml --quiet

# Veya manuel dosya yolu ile
gcloud app deploy /full/path/to/GoogleAppEngineProject/app.yaml
```

