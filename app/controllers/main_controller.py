from flask import Blueprint, render_template, jsonify, session
from app.services.book_service import BookService
from app.services.reservation_service import ReservationService
from app.utils.decorators import login_required
from app.utils.helpers import get_library_stats

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    """Homepage"""
    books = BookService.get_featured_books(limit=6)
    stats = get_library_stats()
    return render_template('main/index.html', books=books, stats=stats)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user_id = session['user_id']
    
    # Get user reservations
    user_reservations = ReservationService.get_user_reservations(user_id)
    
    # Get user stats
    user_stats = ReservationService.get_user_stats(user_id)
    
    # Get recent books for recommendations
    recent_books = BookService.get_featured_books(limit=4)
    
    return render_template('user/dashboard.html', 
                         reservations=user_reservations[:5], 
                         books=recent_books,
                         stats=user_stats)

@main_bp.route('/api/stats')
def api_stats():
    """API endpoint for library statistics"""
    stats = get_library_stats()
    return jsonify(stats) 