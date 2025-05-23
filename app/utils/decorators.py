from functools import wraps
from flask import redirect, url_for, flash
from app.services.auth_service import AuthService

def login_required(f):
    """Decorator to require user login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        is_logged_in, message = AuthService.require_login()
        if not is_logged_in:
            flash(message, 'warning')
            return redirect(url_for('auth_bp.login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin privileges"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        is_admin, message = AuthService.require_admin()
        if not is_admin:
            flash(message, 'error')
            if AuthService.is_logged_in():
                return redirect(url_for('main_bp.dashboard'))
            else:
                return redirect(url_for('auth_bp.login'))
        return f(*args, **kwargs)
    return decorated_function 