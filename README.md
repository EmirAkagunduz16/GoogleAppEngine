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

## 🚀 Hızlı Başlangıç

### 1. Projeyi Klonlayın
```bash
git clone <repository-url>
cd GoogleAppEngineProject
```

### 2. Sanal Ortam Oluşturun
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

### 4. Google Cloud Projesini Ayarlayın
```bash
# Google Cloud SDK kurulumu (eğer yoksa)
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Giriş yapın
gcloud auth login

# Proje oluşturun
gcloud projects create your-project-id

# Projeyi aktif yapın
gcloud config set project your-project-id

# Firestore'u aktifleştirin
gcloud firestore databases create --location=europe-west1
```

### 5. Veritabanını Başlatın
```bash
python seed_data.py
```

### 6. Yerel Geliştirme
```bash
python main.py
```

Uygulama http://localhost:8080 adresinde çalışacaktır.

## 🌐 Deployment (Google App Engine)

### 1. App Engine'i Etkinleştirin
```bash
gcloud app create --region=europe-west1
```

### 2. Uygulamayı Deploy Edin
```bash
gcloud app deploy
```

### 3. Uygulamayı Açın
```bash
gcloud app browse
```

## 📊 Demo Verileri

Sistem demo kullanıcıları ve kitaplar ile önceden doldurulmuştur:

### 👥 Kullanıcılar
- **Admin**: `admin@library.com` / `admin123`
- **Kullanıcı**: `user@library.com` / `user123`

### 📚 Örnek Kitaplar
- 1984 (George Orwell)
- Suç ve Ceza (Dostoyevski)
- Sapiens (Yuval Noah Harari)
- Python Programlama
- ve daha fazlası...

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

### 4. Google Cloud Ayarları
```bash
# Google Cloud SDK kurulumu (eğer yoksa)
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Proje oluşturma ve ayarlama
gcloud projects create your-project-id
gcloud config set project your-project-id
gcloud app create --region=europe-west1

# Firestore veritabanı etkinleştirme
gcloud firestore databases create --region=europe-west1
```

### 5. Örnek Veri Yükleme
```bash
python seed_data.py
```

### 6. Yerel Çalıştırma
```bash
python main.py
```

Uygulama http://localhost:8080 adresinde çalışacaktır.

## 🚀 Deployment (Google App Engine)

### 1. Deployment
```bash
gcloud app deploy
```

### 2. Canlı URL'yi Açma
```bash
gcloud app browse
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

## �� Sorun Giderme

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

## 📈 Performans Optimizasyonları

- Firestore sorgu optimizasyonları
- Statik dosya önbellekleme
- Lazy loading ile sayfa yükleme hızı
- Bootstrap ve Font Awesome CDN kullanımı

## 🔒 Güvenlik Özellikleri

- Werkzeug ile güvenli şifre hashleme
- CSRF koruması
- Oturum güvenliği
- Rol tabanlı erişim kontrolü
- Input validasyonu

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 👨‍💻 Geliştirici

Bu proje, Google App Engine ve modern web teknolojileri kullanılarak geliştirilmiş kapsamlı bir kütüphane yönetim sistemidir.

---

**Not:** Bu sistem eğitim amaçlı geliştirilmiştir ve production ortamında kullanılmadan önce ek güvenlik önlemleri alınmalıdır. # GoogleAppEngine
# GoogleAppEngine
