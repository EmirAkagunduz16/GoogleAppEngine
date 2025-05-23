// Digital Library Management System - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Search functionality
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            const searchInput = document.getElementById('search');
            if (searchInput && searchInput.value.trim() === '') {
                e.preventDefault();
                searchInput.focus();
            }
        });
    }

    // Book reservation confirmation
    const reserveButtons = document.querySelectorAll('.btn-reserve');
    reserveButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Bu kitabı rezerve etmek istediğinizden emin misiniz?')) {
                e.preventDefault();
            }
        });
    });

    // Book return confirmation
    const returnButtons = document.querySelectorAll('.btn-return');
    returnButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Bu kitabı iade etmek istediğinizden emin misiniz?')) {
                e.preventDefault();
            }
        });
    });

    // Delete confirmation
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Bu işlemi gerçekleştirmek istediğinizden emin misiniz? Bu işlem geri alınamaz.')) {
                e.preventDefault();
            }
        });
    });

    // Form validation
    const forms = document.querySelectorAll('.needs-validation');
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Real-time search for books
    const bookSearchInput = document.getElementById('bookSearch');
    if (bookSearchInput) {
        let searchTimeout;
        bookSearchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(function() {
                performBookSearch(bookSearchInput.value);
            }, 300);
        });
    }

    // Category filter
    const categorySelect = document.getElementById('categoryFilter');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            const searchQuery = document.getElementById('bookSearch') ? 
                document.getElementById('bookSearch').value : '';
            performBookSearch(searchQuery, this.value);
        });
    }

    // Statistics refresh
    const refreshStatsBtn = document.getElementById('refreshStats');
    if (refreshStatsBtn) {
        refreshStatsBtn.addEventListener('click', function() {
            refreshLibraryStats();
        });
    }
});

// Book search function
function performBookSearch(query, category = 'all') {
    const bookContainer = document.getElementById('bookContainer');
    if (!bookContainer) return;

    // Show loading
    bookContainer.innerHTML = '<div class="text-center"><div class="loading"></div> Kitaplar yükleniyor...</div>';

    // Build URL
    const params = new URLSearchParams();
    if (query) params.append('search', query);
    if (category && category !== 'all') params.append('category', category);

    fetch(`/books/api?${params.toString()}`)
        .then(response => response.json())
        .then(books => {
            displayBooks(books);
        })
        .catch(error => {
            console.error('Error:', error);
            bookContainer.innerHTML = '<div class="alert alert-danger">Kitaplar yüklenirken hata oluştu.</div>';
        });
}

// Display books function
function displayBooks(books) {
    const bookContainer = document.getElementById('bookContainer');
    if (!bookContainer) return;

    if (books.length === 0) {
        bookContainer.innerHTML = '<div class="col-12"><div class="alert alert-info">Arama kriterlerinize uygun kitap bulunamadı.</div></div>';
        return;
    }

    let html = '';
    books.forEach(book => {
        html += `
            <div class="col-md-4 col-lg-3 mb-4">
                <div class="card book-card h-100">
                    <div class="card-img-top">
                        <i class="fas fa-book"></i>
                    </div>
                    <div class="card-body d-flex flex-column">
                        <h6 class="card-title">${escapeHtml(book.title)}</h6>
                        <p class="card-text text-muted small">${escapeHtml(book.author)}</p>
                        <p class="card-text small">${escapeHtml(book.category)}</p>
                        <div class="mt-auto">
                            <div class="d-flex justify-content-between align-items-center">
                                <small class="text-muted">${book.available_copies}/${book.total_copies} mevcut</small>
                                <a href="/books/${book.id}" class="btn btn-sm btn-primary">Detay</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    });

    bookContainer.innerHTML = html;
}

// Refresh library statistics
function refreshLibraryStats() {
    const statsContainer = document.getElementById('statsContainer');
    if (!statsContainer) return;

    fetch('/api/stats')
        .then(response => response.json())
        .then(stats => {
            updateStatsDisplay(stats);
        })
        .catch(error => {
            console.error('Error refreshing stats:', error);
        });
}

// Update statistics display
function updateStatsDisplay(stats) {
    const statElements = {
        'totalBooks': stats.total_books,
        'totalUsers': stats.total_users,
        'activeReservations': stats.active_reservations,
        'availableBooks': stats.available_books
    };

    Object.keys(statElements).forEach(key => {
        const element = document.getElementById(key);
        if (element) {
            element.textContent = statElements[key];
        }
    });
}

// Utility function to escape HTML
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// Loading state management
function showLoading(element) {
    element.innerHTML = '<div class="text-center"><div class="loading"></div> Yükleniyor...</div>';
}

function hideLoading() {
    const loadingElements = document.querySelectorAll('.loading');
    loadingElements.forEach(el => el.remove());
}

// Notification system
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    const container = document.querySelector('.container-fluid') || document.body;
    container.insertBefore(alertDiv, container.firstChild);

    // Auto-hide after 5 seconds
    setTimeout(() => {
        if (alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 5000);
}

// Form submission with loading state
function submitFormWithLoading(form, button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading"></span> İşleniyor...';
    button.disabled = true;

    // Re-enable button after 3 seconds (fallback)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
    }, 3000);
}

// Initialize form loading states
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                submitFormWithLoading(form, submitButton);
            }
        });
    });
}); 