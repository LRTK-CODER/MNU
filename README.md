# SecureApp - Modern Flask Web Application

A secure, modern web application built with Flask featuring comprehensive authentication, dashboard analytics, and robust security configurations.

## 🚀 Features

- **Secure Authentication System**: Industry-standard login with session management
- **Interactive Dashboard**: Real-time analytics and charts with Chart.js
- **RESTful API**: Clean API endpoints for system status and configuration
- **Responsive Design**: Bootstrap-powered responsive UI
- **Security Best Practices**: CSRF protection, secure sessions, input validation
- **Environment-based Configuration**: Separate configs for development, testing, and production
- **Comprehensive Logging**: Structured logging for monitoring and debugging

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd secureapp
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
cp .env.example .env
# Edit .env file with your configuration values
```

### 5. Initialize Database (if using database features)
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## ⚙️ Configuration

The application supports multiple environments:

- **Development**: Debug mode enabled, SQLite database
- **Production**: Security hardened, PostgreSQL recommended
- **Testing**: In-memory database, CSRF disabled

### Environment Variables

Key configuration options in `.env`:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
MAIL_SERVER=smtp.gmail.com
REDIS_URL=redis://localhost:6379/0
```

See `.env.example` for complete configuration options.

## 🚀 Usage

### Development Mode
```bash
export FLASK_ENV=development
python app.py
```

Or using Flask CLI:
```bash
flask run --debug
```

### Production Mode
```bash
export FLASK_ENV=production
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

The application will be available at `http://localhost:5000`

## 📚 API Endpoints

### Public Endpoints
- `GET /` - Home page
- `GET /login` - Login page
- `POST /login` - Authentication
- `GET /dashboard` - User dashboard
- `GET /api/status` - System status
- `GET /health` - Health check

### Debug Endpoints (Development Only)
- `GET /api/config` - Configuration info
- `GET /api/internal/debug` - Internal debug info

## 🔒 Security Features

- **Session Security**: Secure, HTTP-only cookies with SameSite protection
- **CSRF Protection**: Cross-site request forgery protection
- **Input Validation**: Server-side input validation and sanitization
- **Secure Headers**: Security headers for XSS and clickjacking protection
- **Environment Separation**: Separate configurations for each environment
- **Password Security**: Secure password hashing with bcrypt

## 🏗️ Architecture

```
secureapp/
├── app.py              # Main application file
├── config.py           # Configuration classes
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
├── templates/         # Jinja2 templates
│   ├── base.html      # Base template
│   ├── index.html     # Home page
│   ├── login.html     # Login page
│   └── dashboard.html # Dashboard
└── static/           # Static assets (CSS, JS, images)
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

With coverage:
```bash
python -m pytest --cov=app tests/
```

## 📈 Monitoring

The application includes several monitoring endpoints:

- `/health` - Basic health check
- `/api/status` - Detailed system status
- Comprehensive logging to files and console

## 🔧 Development

### Adding New Features

1. Create feature branch: `git checkout -b feature/new-feature`
2. Make changes and add tests
3. Ensure all tests pass: `pytest`
4. Submit pull request

### Code Style

- Follow PEP 8 standards
- Use meaningful variable names
- Add docstrings to functions and classes
- Write unit tests for new features

## 📝 Changelog

### v1.0.0 (2025-06-24)
- Initial release
- Basic authentication system
- Dashboard with charts
- RESTful API endpoints
- Security configurations

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Review the documentation
3. Contact the development team

## 🙏 Acknowledgments

- Flask community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Chart.js for beautiful charts
- Contributors and testers

---

**Note**: This application is designed with security in mind, but always follow security best practices when deploying to production environments.