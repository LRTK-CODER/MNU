from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os
from config import get_config

def create_app(config_name=None):
    """Application factory pattern"""
    app = Flask(__name__)

    # Load configuration
    config_obj = get_config(config_name)
    app.config.from_object(config_obj)

    return app

# Create app instance
app = create_app()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'version': '1.0.0',
        'environment': os.environ.get('FLASK_ENV', 'production'),
        'debug': app.config.get('DEBUG', False)
    })

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple authentication logic (for demo purposes)
        if username and password:
            return jsonify({'message': 'Login successful', 'user': username})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/config')
def debug_config():
    """Debug endpoint to show configuration (for development only)"""
    if not app.config.get('DEBUG') or os.environ.get('FLASK_ENV') != 'development':
        return jsonify({'error': 'Access denied'}), 403

    # Only expose non-sensitive configuration
    safe_config = {
        'DEBUG': app.config.get('DEBUG'),
        'TESTING': app.config.get('TESTING'),
        'UPLOAD_FOLDER': app.config.get('UPLOAD_FOLDER', 'Not set'),
        'MAX_CONTENT_LENGTH': app.config.get('MAX_CONTENT_LENGTH', 'Not set')
    }

    return jsonify(safe_config)

@app.route('/api/internal/debug')
def internal_debug():
    """Internal debug endpoint - DISABLED for security"""
    return jsonify({'error': 'Endpoint disabled for security reasons'}), 403

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': '2025-06-24T10:30:00Z',
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Get configuration
    config_name = os.environ.get('FLASK_ENV', 'development')
    debug_mode = app.config.get('DEBUG', False)

    print(f"Starting Flask app in {config_name} mode...")
    print(f"Debug mode: {debug_mode}")

    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
