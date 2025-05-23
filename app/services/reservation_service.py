import datetime
from flask import session
from app.models.reservation import Reservation
from app.models.book import Book
from app.models.user import User

class ReservationService:
    """Service class for reservation operations"""
    
    @staticmethod
    def create_reservation(user_id, book_id):
        """Create a new book reservation"""
        try:
            # Check if book exists and is available
            book = Book.find_by_id(book_id)
            if not book:
                return False, "Kitap bulunamadı."
            
            if not book.is_available():
                return False, "Bu kitap şu anda mevcut değil."
            
            # Check if user already has this book reserved
            if Reservation.user_has_active_reservation(user_id, book_id):
                return False, "Bu kitabı zaten rezerve etmişsiniz."
            
            # Create reservation
            reservation = Reservation(user_id=user_id, book_id=book_id)
            
            if reservation.save():
                # Update book availability
                book.reserve()
                
                # Update user stats
                user = User.find_by_id(user_id)
                if user:
                    user.total_reservations += 1
                    user.save()
                
                return True, "Kitap başarıyla rezerve edildi!"
            else:
                return False, "Rezervasyon sırasında hata oluştu."
                
        except Exception as e:
            return False, f"Rezervasyon hatası: {str(e)}"
    
    @staticmethod
    def return_reservation(reservation_id, user_id=None):
        """Return a book reservation"""
        try:
            reservation = Reservation.find_by_id(reservation_id)
            if not reservation:
                return False, "Rezervasyon bulunamadı."
            
            # Check ownership if user_id provided
            if user_id and reservation.user_id != user_id:
                return False, "Bu rezervasyon size ait değil."
            
            if reservation.status != 'active':
                return False, "Bu rezervasyon zaten iade edilmiş."
            
            # Return the book
            if reservation.return_book():
                return True, "Kitap başarıyla iade edildi!"
            else:
                return False, "İade sırasında hata oluştu."
                
        except Exception as e:
            return False, f"İade hatası: {str(e)}"
    
    @staticmethod
    def get_user_reservations(user_id):
        """Get all reservations for a user"""
        return Reservation.find_by_user(user_id)
    
    @staticmethod
    def get_all_reservations(status=None):
        """Get all reservations with optional status filter"""
        return Reservation.find_all(status=status)
    
    @staticmethod
    def get_reservation_by_id(reservation_id):
        """Get a single reservation by ID"""
        return Reservation.find_by_id(reservation_id)
    
    @staticmethod
    def get_user_active_reservation_for_book(user_id, book_id):
        """Get user's active reservation for a specific book"""
        reservations = Reservation.find_by_user(user_id)
        for reservation in reservations:
            if reservation.book_id == book_id and reservation.status == 'active':
                return reservation
        return None
    
    @staticmethod
    def get_reservation_stats():
        """Get reservation statistics"""
        all_reservations = Reservation.find_all()
        
        stats = {
            'total_reservations': len(all_reservations),
            'active_reservations': len([r for r in all_reservations if r.status == 'active']),
            'returned_reservations': len([r for r in all_reservations if r.status == 'returned']),
            'overdue_reservations': len([r for r in all_reservations if r.is_overdue()])
        }
        
        return stats
    
    @staticmethod
    def get_user_stats(user_id):
        """Get reservation statistics for a specific user"""
        user_reservations = Reservation.find_by_user(user_id)
        
        stats = {
            'total_reservations': len(user_reservations),
            'active_reservations': len([r for r in user_reservations if r.status == 'active']),
            'returned_reservations': len([r for r in user_reservations if r.status == 'returned']),
            'overdue_reservations': len([r for r in user_reservations if r.is_overdue()])
        }
        
        return stats
    
    @staticmethod
    def get_overdue_reservations():
        """Get all overdue reservations"""
        all_reservations = Reservation.find_all(status='active')
        return [r for r in all_reservations if r.is_overdue()]
    
    @staticmethod
    def extend_reservation(reservation_id, days=7):
        """Extend a reservation due date"""
        try:
            reservation = Reservation.find_by_id(reservation_id)
            if not reservation:
                return False, "Rezervasyon bulunamadı."
            
            if reservation.status != 'active':
                return False, "Sadece aktif rezervasyonlar uzatılabilir."
            
            # Extend due date
            reservation.due_date += datetime.timedelta(days=days)
            
            if reservation.save():
                return True, f"Rezervasyon {days} gün uzatıldı!"
            else:
                return False, "Rezervasyon uzatılırken hata oluştu."
                
        except Exception as e:
            return False, f"Rezervasyon uzatma hatası: {str(e)}"
    
    @staticmethod
    def can_user_reserve_book(user_id, book_id):
        """Check if user can reserve a specific book"""
        # Check if book exists and is available
        book = Book.find_by_id(book_id)
        if not book or not book.is_available():
            return False, "Kitap mevcut değil."
        
        # Check if user already has this book
        if Reservation.user_has_active_reservation(user_id, book_id):
            return False, "Bu kitabı zaten rezerve etmişsiniz."
        
        # Check user's active reservation count (optional limit)
        user_reservations = Reservation.find_by_user(user_id)
        active_count = len([r for r in user_reservations if r.status == 'active'])
        
        if active_count >= 5:  # Maximum 5 active reservations per user
            return False, "Maksimum rezervasyon sayısına ulaştınız (5)."
        
        return True, "Kitap rezerve edilebilir."
    
    @staticmethod
    def get_recent_reservations(limit=10):
        """Get recent reservations for admin dashboard"""
        all_reservations = Reservation.find_all()
        # Sort by reservation date, most recent first
        all_reservations.sort(key=lambda x: x.reservation_date, reverse=True)
        return all_reservations[:limit] 