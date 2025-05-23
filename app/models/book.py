import datetime
from flask import current_app

class Book:
    """Book model for the digital library system"""
    
    def __init__(self, title, author, isbn='', category='', description='', 
                 publisher='', publication_year=None, total_copies=1, 
                 available_copies=None, book_id=None, created_at=None, created_by=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.description = description
        self.publisher = publisher
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = available_copies if available_copies is not None else total_copies
        self.created_at = created_at or datetime.datetime.now()
        self.created_by = created_by
    
    def to_dict(self):
        """Convert book object to dictionary"""
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category,
            'description': self.description,
            'publisher': self.publisher,
            'publication_year': self.publication_year,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'created_at': self.created_at,
            'created_by': self.created_by
        }
    
    @classmethod
    def from_dict(cls, data, book_id=None):
        """Create book object from dictionary"""
        return cls(
            book_id=book_id,
            title=data.get('title'),
            author=data.get('author'),
            isbn=data.get('isbn', ''),
            category=data.get('category', ''),
            description=data.get('description', ''),
            publisher=data.get('publisher', ''),
            publication_year=data.get('publication_year'),
            total_copies=data.get('total_copies', 1),
            available_copies=data.get('available_copies'),
            created_at=data.get('created_at'),
            created_by=data.get('created_by')
        )
    
    @classmethod
    def find_by_id(cls, book_id):
        """Find book by ID"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return None
            
        try:
            doc = db.collection('books').document(book_id).get()
            if doc.exists:
                book_data = doc.to_dict()
                return cls.from_dict(book_data, doc.id)
        except Exception:
            pass
        
        return None
    
    @classmethod
    def find_all(cls, limit=None, search_query=None, category=None):
        """Find all books with optional filters"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return []
            
        books_ref = db.collection('books')
        query = books_ref
        
        if category and category != 'all':
            query = query.where('category', '==', category)
        
        books = []
        for doc in query.stream():
            book_data = doc.to_dict()
            book = cls.from_dict(book_data, doc.id)
            
            # Search filtering
            if search_query:
                search_lower = search_query.lower()
                if (search_lower not in book.title.lower() and 
                    search_lower not in book.author.lower() and
                    search_lower not in book.isbn.lower()):
                    continue
            
            books.append(book)
        
        # Sort by title
        books.sort(key=lambda x: x.title)
        
        if limit:
            books = books[:limit]
        
        return books
    
    @classmethod
    def get_categories(cls):
        """Get all unique categories"""
        return ['Bilim Kurgu', 'Roman', 'Tarih', 'Bilim', 'Felsefe', 'Sanat', 'Teknoloji', 'Edebiyat']
    
    def save(self):
        """Save book to database"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return False
            
        try:
            if self.id:
                # Update existing book
                db.collection('books').document(self.id).update(self.to_dict())
            else:
                # Create new book
                _, doc_ref = db.collection('books').add(self.to_dict())
                self.id = doc_ref.id
            return True
        except Exception:
            return False
    
    def delete(self):
        """Delete book from database"""
        db = current_app.config['FIRESTORE_DB']
        if not db or not self.id:
            return False
            
        try:
            db.collection('books').document(self.id).delete()
            return True
        except Exception:
            return False
    
    def is_available(self):
        """Check if book is available for reservation"""
        return self.available_copies > 0
    
    def reserve(self):
        """Reserve a copy of the book"""
        if self.available_copies > 0:
            self.available_copies -= 1
            return self.save()
        return False
    
    def return_copy(self):
        """Return a copy of the book"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return self.save()
        return False
    
    def __repr__(self):
        return f'<Book {self.title} by {self.author}>' 