import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'

    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Mail configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # API Keys and Secrets
    STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')

    # OAuth Configuration
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

    # Redis Configuration
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'

    # Security Configuration
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'your-password-salt'

    # JWT Configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-string'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # File Upload Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

    # Development database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///dev.db'

    # Disable CSRF for development
    WTF_CSRF_ENABLED = False

    # Development API credentials from environment variables
    DEV_API_KEY = os.environ.get('DEV_API_KEY')
    DEV_WEBHOOK_SECRET = os.environ.get('DEV_WEBHOOK_SECRET')

    # Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

    # Production database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # Enhanced security for production
    SESSION_COOKIE_SECURE = True
    WTF_CSRF_ENABLED = True

    # Logging configuration
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'logs/app.log'

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True

    # Test database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Disable CSRF for testing
    WTF_CSRF_ENABLED = False

    # Speed up password hashing for tests
    BCRYPT_LOG_ROUNDS = 4

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(config_name=None):
    """Get configuration based on environment"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    return config.get(config_name, config['default'])
