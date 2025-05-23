#!/usr/bin/env python3
"""
Database seeding script for the Digital Library Management System
This script populates the database with sample data for demonstration purposes.
"""

import datetime
from werkzeug.security import generate_password_hash
from google.cloud import firestore

def seed_database():
    """Seed the database with sample data"""
    
    # Initialize Firestore client
    try:
        db = firestore.Client()
        print("✅ Firestore client initialized successfully")
    except Exception as e:
        print(f"❌ Error initializing Firestore: {e}")
        return False
    
    # Sample users data
    users_data = [
        {
            'email': 'admin@library.com',
            'password_hash': generate_password_hash('admin123'),
            'full_name': 'Admin Kullanıcı',
            'phone': '+90 555 123 4567',
            'is_admin': True,
            'created_at': datetime.datetime.now(),
            'total_reservations': 0
        },
        {
            'email': 'user@library.com',
            'password_hash': generate_password_hash('user123'),
            'full_name': 'Ahmet Yılmaz',
            'phone': '+90 555 987 6543',
            'is_admin': False,
            'created_at': datetime.datetime.now(),
            'total_reservations': 0
        },
        {
            'email': 'mehmet@library.com',
            'password_hash': generate_password_hash('user123'),
            'full_name': 'Mehmet Özkan',
            'phone': '+90 555 111 2233',
            'is_admin': False,
            'created_at': datetime.datetime.now(),
            'total_reservations': 0
        },
        {
            'email': 'ayse@library.com',
            'password_hash': generate_password_hash('user123'),
            'full_name': 'Ayşe Kaya',
            'phone': '+90 555 444 5566',
            'is_admin': False,
            'created_at': datetime.datetime.now(),
            'total_reservations': 0
        }
    ]
    
    # Sample books data
    books_data = [
        {
            'title': '1984',
            'author': 'George Orwell',
            'isbn': '978-0-452-28423-4',
            'category': 'Roman',
            'description': 'Dystopian sosyal bilim kurgu romanı. Totaliter rejimin bireyler üzerindeki etkilerini anlatan klasik eser.',
            'publisher': 'Penguin Books',
            'publication_year': 1949,
            'total_copies': 3,
            'available_copies': 3,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Suç ve Ceza',
            'author': 'Fyodor Dostoyevski',
            'isbn': '978-975-13-0123-4',
            'category': 'Roman',
            'description': 'Rus edebiyatının en önemli eserlerinden biri. Psikolojik gerilim ve ahlaki sorgulamalar içeren derin roman.',
            'publisher': 'İş Bankası Yayınları',
            'publication_year': 1866,
            'total_copies': 2,
            'available_copies': 2,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Sapiens: İnsan Türünün Kısa Tarihi',
            'author': 'Yuval Noah Harari',
            'isbn': '978-975-08-3438-4',
            'category': 'Tarih',
            'description': 'İnsanlığın tarihsel gelişimini ve toplumsal evrimini inceleyen çok satan popüler bilim kitabı.',
            'publisher': 'Kolektif Kitap',
            'publication_year': 2011,
            'total_copies': 4,
            'available_copies': 4,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Python Programlama',
            'author': 'John Zelle',
            'isbn': '978-1-59059-519-0',
            'category': 'Teknoloji',
            'description': 'Python programlama dili için kapsamlı rehber. Başlangıçtan ileri seviyeye programlama teknikleri.',
            'publisher': 'No Starch Press',
            'publication_year': 2016,
            'total_copies': 5,
            'available_copies': 5,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Kısa Bir Tarih: Neredeyse Her Şey Hakkında',
            'author': 'Bill Bryson',
            'isbn': '978-0-7679-0818-4',
            'category': 'Bilim',
            'description': 'Evrenin doğuşundan günümüze bilimin gelişimini anlatan eğlenceli ve öğretici popüler bilim kitabı.',
            'publisher': 'Broadway Books',
            'publication_year': 2003,
            'total_copies': 2,
            'available_copies': 2,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Düşüncenin Gücü',
            'author': 'Norman Vincent Peale',
            'isbn': '978-975-21-0123-8',
            'category': 'Felsefe',
            'description': 'Pozitif düşüncenin yaşam üzerindeki etkilerini inceleyen klasik kişisel gelişim kitabı.',
            'publisher': 'Epsilon Yayınevi',
            'publication_year': 1952,
            'total_copies': 3,
            'available_copies': 3,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Sanat Tarihi',
            'author': 'Ernst Gombrich',
            'isbn': '978-975-511-456-2',
            'category': 'Sanat',
            'description': 'Mağara resimlerinden günümüze sanat tarihinin kapsamlı ve anlaşılır sunumu.',
            'publisher': 'Remzi Kitabevi',
            'publication_year': 1950,
            'total_copies': 2,
            'available_copies': 2,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'isbn': '978-0-441-17271-9',
            'category': 'Bilim Kurgu',
            'description': 'Çöl gezegeni Arrakis\'te geçen epik bilim kurgu romanı. Politik entrikalar ve mistik güçlerle dolu.',
            'publisher': 'Ace Books',
            'publication_year': 1965,
            'total_copies': 3,
            'available_copies': 3,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Görünmez Adam',
            'author': 'H.G. Wells',
            'isbn': '978-0-486-27071-6',
            'category': 'Bilim Kurgu',
            'description': 'Görünmezlik serumu keşfeden bilim insanının hikayesi. Klasik bilim kurgu edebiyatı.',
            'publisher': 'Dover Publications',
            'publication_year': 1897,
            'total_copies': 2,
            'available_copies': 2,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Türk Edebiyatı Tarihi',
            'author': 'Ahmet Hamdi Tanpınar',
            'isbn': '978-975-13-0456-7',
            'category': 'Edebiyat',
            'description': 'Türk edebiyatının tarihsel gelişimini inceleyen akademik ve eleştirel değerlendirme.',
            'publisher': 'Dergah Yayınları',
            'publication_year': 1982,
            'total_copies': 2,
            'available_copies': 2,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'Veri Bilimi ve Makine Öğrenmesi',
            'author': 'Andreas Müller',
            'isbn': '978-1-449-36941-5',
            'category': 'Teknoloji',
            'description': 'Python ile veri bilimi ve makine öğrenmesi uygulamaları. Pratik örnekler ve kodlar içerir.',
            'publisher': 'O\'Reilly Media',
            'publication_year': 2016,
            'total_copies': 4,
            'available_copies': 4,
            'created_at': datetime.datetime.now()
        },
        {
            'title': 'İnsan Hakları Evrensel Beyannamesi',
            'author': 'Birleşmiş Milletler',
            'isbn': '978-975-16-2345-9',
            'category': 'Felsefe',
            'description': 'İnsan haklarının evrensel ilkelerini belirleyen tarihsel belge ve yorumları.',
            'publisher': 'Ankara Üniversitesi Yayınları',
            'publication_year': 1948,
            'total_copies': 1,
            'available_copies': 1,
            'created_at': datetime.datetime.now()
        }
    ]
    
    # Add users to database
    print("👥 Adding users to database...")
    user_ids = {}
    for user_data in users_data:
        try:
            _, doc_ref = db.collection('users').add(user_data)
            user_ids[user_data['email']] = doc_ref.id
            print(f"   ✅ Added user: {user_data['full_name']} ({user_data['email']})")
        except Exception as e:
            print(f"   ❌ Error adding user {user_data['email']}: {e}")
    
    # Add books to database
    print("\n📚 Adding books to database...")
    book_ids = []
    for book_data in books_data:
        try:
            _, doc_ref = db.collection('books').add(book_data)
            book_ids.append(doc_ref.id)
            print(f"   ✅ Added book: {book_data['title']} by {book_data['author']}")
        except Exception as e:
            print(f"   ❌ Error adding book {book_data['title']}: {e}")
    
    # Add some sample reservations
    print("\n📝 Adding sample reservations...")
    if book_ids and user_ids:
        sample_reservations = [
            {
                'user_id': user_ids.get('user@library.com'),
                'book_id': book_ids[0],  # 1984
                'reservation_date': datetime.datetime.now() - datetime.timedelta(days=5),
                'due_date': datetime.datetime.now() + datetime.timedelta(days=9),
                'status': 'active'
            },
            {
                'user_id': user_ids.get('mehmet@library.com'),
                'book_id': book_ids[2],  # Sapiens
                'reservation_date': datetime.datetime.now() - datetime.timedelta(days=3),
                'due_date': datetime.datetime.now() + datetime.timedelta(days=11),
                'status': 'active'
            },
            {
                'user_id': user_ids.get('ayse@library.com'),
                'book_id': book_ids[1],  # Suç ve Ceza
                'reservation_date': datetime.datetime.now() - datetime.timedelta(days=20),
                'due_date': datetime.datetime.now() - datetime.timedelta(days=6),
                'status': 'returned',
                'return_date': datetime.datetime.now() - datetime.timedelta(days=6)
            }
        ]
        
        for reservation in sample_reservations:
            if reservation['user_id'] and reservation['book_id']:
                try:
                    db.collection('reservations').add(reservation)
                    
                    # Update book availability for active reservations
                    if reservation['status'] == 'active':
                        book_ref = db.collection('books').document(reservation['book_id'])
                        book_doc = book_ref.get()
                        if book_doc.exists:
                            book_data = book_doc.to_dict()
                            new_available = book_data.get('available_copies', 1) - 1
                            book_ref.update({'available_copies': max(0, new_available)})
                    
                    # Update user total reservations
                    user_ref = db.collection('users').document(reservation['user_id'])
                    user_doc = user_ref.get()
                    if user_doc.exists:
                        user_data = user_doc.to_dict()
                        new_total = user_data.get('total_reservations', 0) + 1
                        user_ref.update({'total_reservations': new_total})
                    
                    print(f"   ✅ Added reservation for user {reservation['user_id']}")
                except Exception as e:
                    print(f"   ❌ Error adding reservation: {e}")
    
    print(f"\n🎉 Database seeding completed successfully!")
    print(f"   📊 Added {len(users_data)} users")
    print(f"   📚 Added {len(books_data)} books")
    print(f"   📝 Added sample reservations")
    print("\n📋 Demo Login Credentials:")
    print("   Admin: admin@library.com / admin123")
    print("   User:  user@library.com  / user123")
    
    return True

if __name__ == '__main__':
    print("🌱 Starting database seeding process...")
    success = seed_database()
    
    if success:
        print("\n✅ Database seeding completed successfully!")
    else:
        print("\n❌ Database seeding failed!") 