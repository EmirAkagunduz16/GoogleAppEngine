from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.book_service import BookService
from app.services.reservation_service import ReservationService
from app.utils.decorators import admin_required
from app.utils.helpers import get_library_stats

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/')
@admin_required
def dashboard():
    """Admin dashboard"""
    # Get comprehensive stats
    stats = get_library_stats()
    
    # Get recent reservations
    recent_reservations = ReservationService.get_recent_reservations(limit=10)
    
    return render_template('admin/dashboard.html', 
                         stats=stats, 
                         recent_reservations=recent_reservations)

@admin_bp.route('/books')
@admin_required
def books():
    """Admin books management"""
    all_books = BookService.get_all_books()
    return render_template('admin/books.html', books=all_books)

@admin_bp.route('/books/add', methods=['GET', 'POST'])
@admin_required
def add_book():
    """Add new book"""
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn', '')
        category = request.form.get('category')
        description = request.form.get('description', '')
        publisher = request.form.get('publisher', '')
        publication_year = request.form.get('publication_year')
        total_copies = request.form.get('total_copies')
        
        # Validate required fields
        if not title or not author or not category:
            flash('Tüm zorunlu alanları doldurunuz.', 'error')
            return render_template('admin/add_book.html', categories=BookService.get_categories())
        
        # Validate book data
        is_valid, errors = BookService.validate_book_data(title, author, total_copies)
        if not is_valid:
            for error in errors:
                flash(error, 'error')
            return render_template('admin/add_book.html', categories=BookService.get_categories())
        
        # Convert publication year
        try:
            publication_year = int(publication_year) if publication_year else None
        except ValueError:
            publication_year = None
        
        # Convert total copies
        try:
            total_copies = int(total_copies)
        except ValueError:
            total_copies = 1
        
        # Create book
        success, message, book = BookService.create_book(
            title=title,
            author=author,
            isbn=isbn,
            category=category,
            description=description,
            publisher=publisher,
            publication_year=publication_year,
            total_copies=total_copies,
            created_by=session['user_id']
        )
        
        if success:
            flash(message, 'success')
            return redirect(url_for('admin_bp.books'))
        else:
            flash(message, 'error')
    
    categories = BookService.get_categories()
    return render_template('admin/add_book.html', categories=categories)

@admin_bp.route('/reservations')
@admin_required
def reservations():
    """Admin reservations management"""
    all_reservations = ReservationService.get_all_reservations()
    return render_template('admin/reservations.html', reservations=all_reservations)

@admin_bp.route('/reservations/<reservation_id>/return', methods=['POST'])
@admin_required
def return_reservation(reservation_id):
    """Admin force return a reservation"""
    success, message = ReservationService.return_reservation(reservation_id)
    
    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')
    
    return redirect(url_for('admin_bp.reservations')) 