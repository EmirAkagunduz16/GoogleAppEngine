from app.services.book_service import BookService
from app.services.reservation_service import ReservationService
from flask import current_app

def get_library_stats():
    """Get comprehensive library statistics"""
    db = current_app.config.get('FIRESTORE_DB')
    if not db:
        return {
            'total_books': 0,
            'total_users': 0,
            'active_reservations': 0,
            'total_reservations': 0
        }
    
    try:
        # Get book stats
        book_stats = BookService.get_library_stats()
        
        # Get reservation stats
        reservation_stats = ReservationService.get_reservation_stats()
        
        # Count users
        users = list(db.collection('users').stream())
        user_count = len(users)
        
        # Combine stats
        stats = {
            'total_books': book_stats['total_books'],
            'total_users': user_count,
            'active_reservations': reservation_stats['active_reservations'],
            'total_reservations': reservation_stats['total_reservations'],
            'available_books': book_stats['available_books'],
            'out_of_stock': book_stats['out_of_stock'],
            'overdue_books': reservation_stats['overdue_reservations']
        }
        
        return stats
        
    except Exception:
        return {
            'total_books': 0,
            'total_users': 0,
            'active_reservations': 0,
            'total_reservations': 0
        }

def format_date(date_obj, format_str='%d.%m.%Y'):
    """Format datetime object to string"""
    if date_obj:
        return date_obj.strftime(format_str)
    return 'Bilinmiyor'

def is_overdue(due_date):
    """Check if a date is overdue"""
    if not due_date:
        return False
    
    from datetime import date
    return due_date.date() < date.today()

def days_until_due(due_date):
    """Calculate days until due date"""
    if not due_date:
        return 0
    
    from datetime import date
    delta = due_date.date() - date.today()
    return max(0, delta.days) 