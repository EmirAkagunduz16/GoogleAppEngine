import os
from google.cloud import firestore

class Config:
    """Application configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Firestore configuration
    try:
        FIRESTORE_DB = firestore.Client(database='new-default')
    except Exception:
        # For local development
        FIRESTORE_DB = None
    
    # Application settings
    DEBUG = os.environ.get('FLASK_DEBUG', False)
    TESTING = False
    
    # Pagination
    BOOKS_PER_PAGE = 12
    RESERVATIONS_PER_PAGE = 10
    
    # Reservation settings
    DEFAULT_RESERVATION_DAYS = 14
    MAX_RESERVATIONS_PER_USER = 5

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    FIRESTORE_DB = None  # Use mock database for testing

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
} 