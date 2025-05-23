from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.services.book_service import BookService
from app.services.reservation_service import ReservationService
from app.utils.decorators import login_required

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/')
def index():
    """Books listing page"""
    search_query = request.args.get('search', '')
    category = request.args.get('category', 'all')
    
    # Get all books with filters
    all_books = BookService.get_all_books(search_query=search_query, category=category)
    
    # Get categories for filter dropdown
    categories = BookService.get_categories()
    
    return render_template('books/index.html', 
                         books=all_books, 
                         search_query=search_query,
                         selected_category=category,
                         categories=categories)

@book_bp.route('/<book_id>')
def detail(book_id):
    """Book detail page"""
    book = BookService.get_book_by_id(book_id)
    
    if not book:
        flash('Kitap bulunamadı.', 'error')
        return redirect(url_for('book_bp.index'))
    
    # Check if user has active reservation for this book
    user_reservation = None
    if 'user_id' in session:
        user_reservation = ReservationService.get_user_active_reservation_for_book(
            session['user_id'], book_id
        )
    
    return render_template('books/detail.html', book=book, user_reservation=user_reservation)

@book_bp.route('/<book_id>/reserve', methods=['POST'])
@login_required
def reserve(book_id):
    """Reserve a book"""
    user_id = session['user_id']
    
    # Check if user can reserve this book
    can_reserve, message = ReservationService.can_user_reserve_book(user_id, book_id)
    
    if not can_reserve:
        flash(message, 'warning')
        return redirect(url_for('book_bp.detail', book_id=book_id))
    
    # Create reservation
    success, message = ReservationService.create_reservation(user_id, book_id)
    
    if success:
        flash(message, 'success')
        return redirect(url_for('main_bp.dashboard'))
    else:
        flash(message, 'error')
        return redirect(url_for('book_bp.detail', book_id=book_id))

@book_bp.route('/reservation/<reservation_id>/return', methods=['POST'])
@login_required
def return_book(reservation_id):
    """Return a book"""
    user_id = session['user_id']
    
    success, message = ReservationService.return_reservation(reservation_id, user_id)
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    
    return redirect(url_for('main_bp.dashboard'))

@book_bp.route('/api')
def api_books():
    """API endpoint for books"""
    search = request.args.get('search', '')
    category = request.args.get('category', 'all')
    
    books = BookService.get_all_books(search_query=search, category=category)
    
    # Convert books to dictionaries for JSON serialization
    books_data = []
    for book in books:
        book_dict = book.to_dict()
        book_dict['id'] = book.id
        
        # Convert datetime objects to strings
        if book_dict.get('created_at'):
            book_dict['created_at'] = book_dict['created_at'].isoformat()
        
        books_data.append(book_dict)
    
    return jsonify(books_data) 