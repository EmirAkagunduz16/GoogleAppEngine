from app.models.book import Book
from app.models.user import User

class BookService:
    """Service class for book operations"""
    
    @staticmethod
    def get_all_books(limit=None, search_query=None, category=None):
        """Get all books with optional filtering"""
        return Book.find_all(limit=limit, search_query=search_query, category=category)
    
    @staticmethod
    def get_book_by_id(book_id):
        """Get a single book by ID"""
        return Book.find_by_id(book_id)
    
    @staticmethod
    def get_featured_books(limit=6):
        """Get featured books for homepage"""
        return Book.find_all(limit=limit)
    
    @staticmethod
    def get_categories():
        """Get all available book categories"""
        return Book.get_categories()
    
    @staticmethod
    def create_book(title, author, isbn='', category='', description='',
                   publisher='', publication_year=None, total_copies=1, created_by=None):
        """Create a new book"""
        try:
            book = Book(
                title=title,
                author=author,
                isbn=isbn,
                category=category,
                description=description,
                publisher=publisher,
                publication_year=publication_year,
                total_copies=total_copies,
                available_copies=total_copies,
                created_by=created_by
            )
            
            if book.save():
                return True, "Kitap başarıyla eklendi!", book
            else:
                return False, "Kitap eklenirken hata oluştu.", None
                
        except Exception as e:
            return False, f"Kitap ekleme hatası: {str(e)}", None
    
    @staticmethod
    def update_book(book_id, **kwargs):
        """Update an existing book"""
        try:
            book = Book.find_by_id(book_id)
            if not book:
                return False, "Kitap bulunamadı.", None
            
            # Update fields
            for key, value in kwargs.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            
            if book.save():
                return True, "Kitap başarıyla güncellendi!", book
            else:
                return False, "Kitap güncellenirken hata oluştu.", None
                
        except Exception as e:
            return False, f"Kitap güncelleme hatası: {str(e)}", None
    
    @staticmethod
    def delete_book(book_id):
        """Delete a book"""
        try:
            book = Book.find_by_id(book_id)
            if not book:
                return False, "Kitap bulunamadı."
            
            if book.delete():
                return True, "Kitap başarıyla silindi!"
            else:
                return False, "Kitap silinirken hata oluştu."
                
        except Exception as e:
            return False, f"Kitap silme hatası: {str(e)}"
    
    @staticmethod
    def search_books(query, category=None):
        """Search books by title, author, or ISBN"""
        return Book.find_all(search_query=query, category=category)
    
    @staticmethod
    def get_books_by_category(category):
        """Get books filtered by category"""
        return Book.find_all(category=category)
    
    @staticmethod
    def get_library_stats():
        """Get library statistics"""
        all_books = Book.find_all()
        
        stats = {
            'total_books': len(all_books),
            'available_books': len([book for book in all_books if book.is_available()]),
            'out_of_stock': len([book for book in all_books if not book.is_available()]),
            'total_copies': sum(book.total_copies for book in all_books),
            'available_copies': sum(book.available_copies for book in all_books)
        }
        
        # Category distribution
        category_stats = {}
        for book in all_books:
            category = book.category or 'Belirsiz'
            category_stats[category] = category_stats.get(category, 0) + 1
        
        stats['category_distribution'] = category_stats
        
        return stats
    
    @staticmethod
    def validate_book_data(title, author, total_copies):
        """Validate book data before creation/update"""
        errors = []
        
        if not title or len(title.strip()) < 2:
            errors.append("Kitap adı en az 2 karakter olmalıdır.")
        
        if not author or len(author.strip()) < 2:
            errors.append("Yazar adı en az 2 karakter olmalıdır.")
        
        try:
            copies = int(total_copies)
            if copies < 1 or copies > 100:
                errors.append("Kopya sayısı 1-100 arasında olmalıdır.")
        except (ValueError, TypeError):
            errors.append("Geçerli bir kopya sayısı giriniz.")
        
        return len(errors) == 0, errors 