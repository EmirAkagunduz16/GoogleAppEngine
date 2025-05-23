import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app

class User:
    """User model for the digital library system"""
    
    def __init__(self, email, full_name, phone='', is_admin=False, user_id=None, 
                 created_at=None, total_reservations=0, password_hash=None):
        self.id = user_id
        self.email = email
        self.full_name = full_name
        self.phone = phone
        self.is_admin = is_admin
        self.created_at = created_at or datetime.datetime.now()
        self.total_reservations = total_reservations
        self.password_hash = password_hash
    
    def set_password(self, password):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check password against hash"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'email': self.email,
            'full_name': self.full_name,
            'phone': self.phone,
            'is_admin': self.is_admin,
            'created_at': self.created_at,
            'total_reservations': self.total_reservations,
            'password_hash': self.password_hash
        }
    
    @classmethod
    def from_dict(cls, data, user_id=None):
        """Create user object from dictionary"""
        return cls(
            user_id=user_id,
            email=data.get('email'),
            full_name=data.get('full_name'),
            phone=data.get('phone', ''),
            is_admin=data.get('is_admin', False),
            created_at=data.get('created_at'),
            total_reservations=data.get('total_reservations', 0),
            password_hash=data.get('password_hash')
        )
    
    @classmethod
    def find_by_email(cls, email):
        """Find user by email"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return None
            
        users_ref = db.collection('users')
        docs = users_ref.where('email', '==', email).stream()
        
        for doc in docs:
            user_data = doc.to_dict()
            return cls.from_dict(user_data, doc.id)
        
        return None
    
    @classmethod
    def find_by_id(cls, user_id):
        """Find user by ID"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return None
            
        try:
            doc = db.collection('users').document(user_id).get()
            if doc.exists:
                user_data = doc.to_dict()
                return cls.from_dict(user_data, doc.id)
        except Exception:
            pass
        
        return None
    
    def save(self):
        """Save user to database"""
        db = current_app.config['FIRESTORE_DB']
        if not db:
            return False
            
        try:
            if self.id:
                # Update existing user
                db.collection('users').document(self.id).update(self.to_dict())
            else:
                # Create new user
                doc_ref = db.collection('users').add(self.to_dict())
                self.id = doc_ref[1].id
            return True
        except Exception:
            return False
    
    def delete(self):
        """Delete user from database"""
        db = current_app.config['FIRESTORE_DB']
        if not db or not self.id:
            return False
            
        try:
            db.collection('users').document(self.id).delete()
            return True
        except Exception:
            return False
    
    def __repr__(self):
        return f'<User {self.email}>' 