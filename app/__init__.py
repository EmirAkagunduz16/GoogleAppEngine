from flask import Flask
from app.config import Config
import os
from datetime import datetime

def create_app(config_class=Config):
    """Application factory pattern"""
    # Set the template folder to the views directory
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'views'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(config_class)
    
    # Add datetime to Jinja2 template context
    app.jinja_env.globals['datetime'] = datetime
    app.jinja_env.globals['now'] = datetime.now
    
    # Register Blueprints (Controllers)
    from app.controllers.main_controller import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.book_controller import book_bp
    from app.controllers.admin_controller import admin_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(book_bp, url_prefix='/books')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app 