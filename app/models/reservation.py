import datetime
from flask import current_app
from .user import User
from .book import Book

class Reservation:
    """Reservation model for the digital library system"""
    
    def __init__(self, user_id, book_id, reservation_id=None, reservation_date=None, 
                 due_date=None, return_date=None, status='active'):
        self.id = reservation_id
        self.user_id = user_id
        self.book_id = book_id
        self.reservation_date = reservation_date or datetime.datetime.now()
        self.due_date = due_date or (self.reservation_date + datetime.timedelta(days=14))
        self.return_date = return_date
        self.status = status  # 'active', 'returned', 'overdue'
        
        # Cache for related objects
        self._user = None
        self._book = None
    
    def to_dict(self):
        """Convert reservation object to dictionary"""
        return {
            'user_id': self.user_id,
            'book_id': self.book_id,
            'reservation_date': self.reservation_date,
            'due_date': self.due_date,
            'return_date': self.return_date,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data, reservation_id=None):
        """Create reservation object from dictionary"""
        return cls(
            reservation_id=reservation_id,
            user_id=data.get('user_id'),
            book_id=data.get('book_id'),
            reservation_date=data.get('reservation_date'),
            due_date=data.get('due_date'),
            return_date=data.get('return_date'),
            status=data.get('status', 'active')
        )
    
    @classmethod
    def find_by_id(cls, reservation_id):
        """Find reservation by ID"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return None
            
        try:
            doc = db.collection('reservations').document(reservation_id).get()
            if doc.exists:
                reservation_data = doc.to_dict()
                return cls.from_dict(reservation_data, doc.id)
        except Exception:
            pass
        
        return None
    
    @classmethod
    def find_by_user(cls, user_id):
        """Find all reservations for a user"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return []
            
        reservations_ref = db.collection('reservations')
        query = reservations_ref.where('user_id', '==', user_id)
        
        reservations = []
        for doc in query.stream():
            reservation_data = doc.to_dict()
            reservation = cls.from_dict(reservation_data, doc.id)
            reservations.append(reservation)
        
        return reservations
    
    @classmethod
    def find_by_book(cls, book_id):
        """Find all reservations for a book"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return []
            
        reservations_ref = db.collection('reservations')
        query = reservations_ref.where('book_id', '==', book_id)
        
        reservations = []
        for doc in query.stream():
            reservation_data = doc.to_dict()
            reservation = cls.from_dict(reservation_data, doc.id)
            reservations.append(reservation)
        
        return reservations
    
    @classmethod
    def find_all(cls, status=None):
        """Find all reservations with optional status filter"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return []
            
        reservations_ref = db.collection('reservations')
        
        if status:
            query = reservations_ref.where('status', '==', status)
        else:
            query = reservations_ref
        
        reservations = []
        for doc in query.stream():
            reservation_data = doc.to_dict()
            reservation = cls.from_dict(reservation_data, doc.id)
            reservations.append(reservation)
        
        return reservations
    
    @classmethod
    def user_has_active_reservation(cls, user_id, book_id):
        """Check if user has active reservation for a book"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return False
            
        reservations_ref = db.collection('reservations')
        query = reservations_ref.where('user_id', '==', user_id)\
                                .where('book_id', '==', book_id)\
                                .where('status', '==', 'active')
        
        docs = list(query.stream())
        return len(docs) > 0
    
    @property
    def user(self):
        """Get the user object for this reservation"""
        if self._user is None:
            self._user = User.find_by_id(self.user_id)
        return self._user
    
    @property
    def book(self):
        """Get the book object for this reservation"""
        if self._book is None:
            self._book = Book.find_by_id(self.book_id)
        return self._book
    
    def is_overdue(self):
        """Check if reservation is overdue"""
        if self.status != 'active':
            return False
        return datetime.datetime.now().date() > self.due_date.date()
    
    def days_remaining(self):
        """Get number of days remaining"""
        if self.status != 'active':
            return 0
        delta = self.due_date.date() - datetime.date.today()
        return max(0, delta.days)
    
    def days_overdue(self):
        """Get number of days overdue"""
        if not self.is_overdue():
            return 0
        delta = datetime.date.today() - self.due_date.date()
        return delta.days
    
    def save(self):
        """Save reservation to database"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return False
            
        try:
            if self.id:
                # Update existing reservation
                db.collection('reservations').document(self.id).update(self.to_dict())
            else:
                # Create new reservation
                _, doc_ref = db.collection('reservations').add(self.to_dict())
                self.id = doc_ref.id
            return True
        except Exception:
            return False
    
    def return_book(self):
        """Mark reservation as returned"""
        self.status = 'returned'
        self.return_date = datetime.datetime.now()
        
        # Update book availability
        book = self.book
        if book:
          book.return_copy()
        
        return self.save()
    
    def delete(self):
        """Delete reservation from database"""
        db = current_app.config['FIRESTORE_DB']
        if not db or not self.id:
            return False
            
        try:
            db.collection('reservations').document(self.id).delete()
            return True
        except Exception:
            return False
    
    def __repr__(self):
        return f'<Reservation {self.id}: {self.user_id} -> {self.book_id}>' 