from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        full_name = request.form.get('full_name')
        phone = request.form.get('phone', '')
        
        # Basic validation
        if not email or not password or not full_name:
            flash('Tüm zorunlu alanları doldurunuz.', 'error')
            return render_template('auth/register.html')
        
        # Register user
        success, message = AuthService.register_user(email, password, full_name, phone)
        
        if success:
            flash(message, 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash(message, 'error')
    
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Basic validation
        if not email or not password:
            flash('E-posta ve şifre gerekli.', 'error')
            return render_template('auth/login.html')
        
        # Authenticate user
        success, message = AuthService.login_user(email, password)
        
        if success:
            flash(message, 'success')
            return redirect(url_for('main_bp.dashboard'))
        else:
            flash(message, 'error')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    """User logout"""
    message = AuthService.logout_user()
    flash(message, 'info')
    return redirect(url_for('main_bp.index')) 