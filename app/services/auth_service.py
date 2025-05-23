from flask import session, flash
from app.models.user import User

class AuthService:
    """Service class for authentication operations"""
    
    @staticmethod
    def register_user(email, password, full_name, phone=''):
        """Register a new user"""
        try:
            # Check if user already exists
            existing_user = User.find_by_email(email)
            if existing_user:
                return False, "Bu e-posta adresi zaten kayıtlı."
            
            # Create new user
            user = User(
                email=email,
                full_name=full_name,
                phone=phone,
                is_admin=False
            )
            user.set_password(password)
            
            if user.save():
                return True, "Kayıt başarıyla tamamlandı!"
            else:
                return False, "Kayıt sırasında bir hata oluştu."
                
        except Exception as e:
            return False, f"Kayıt sırasında hata: {str(e)}"
    
    @staticmethod
    def login_user(email, password):
        """Authenticate user login"""
        try:
            user = User.find_by_email(email)
            
            if user and user.check_password(password):
                # Set session data
                session['user_id'] = user.id
                session['user_email'] = user.email
                session['user_name'] = user.full_name
                session['is_admin'] = user.is_admin
                
                return True, f"Hoş geldiniz, {user.full_name}!"
            else:
                return False, "Geçersiz e-posta veya şifre."
                
        except Exception as e:
            return False, f"Giriş sırasında hata: {str(e)}"
    
    @staticmethod
    def logout_user():
        """Log out the current user"""
        session.clear()
        return "Başarıyla çıkış yaptınız."
    
    @staticmethod
    def get_current_user():
        """Get the currently logged-in user"""
        if 'user_id' in session:
            return User.find_by_id(session['user_id'])
        return None
    
    @staticmethod
    def is_logged_in():
        """Check if user is logged in"""
        return 'user_id' in session
    
    @staticmethod
    def is_admin():
        """Check if current user is admin"""
        return session.get('is_admin', False)
    
    @staticmethod
    def require_login():
        """Check if user is logged in, return error message if not"""
        if not AuthService.is_logged_in():
            return False, "Bu sayfaya erişmek için giriş yapmalısınız."
        return True, None
    
    @staticmethod
    def require_admin():
        """Check if user is admin, return error message if not"""
        is_logged_in, message = AuthService.require_login()
        if not is_logged_in:
            return False, message
        
        if not AuthService.is_admin():
            return False, "Bu sayfaya erişim yetkiniz yok."
        
        return True, None 