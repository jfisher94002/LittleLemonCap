# 

This project is licensed under the MIT License.

## License

7. Submit a pull request
8. Push to the branch: `git push origin feature-name`
9. Commit your changes: `git commit -am 'Add feature'`
10. Run the CI checks: `./ci-check.sh`
11. Make your changes
12. Create a feature branch: `git checkout -b feature-name`
13. Fork the repository

## Contributing

- Proper database credentials configured
- `mysql-connector-python` package installed
- MySQL server running
   For production, uncomment the MySQL configuration in `settings.py` and ensure you have:

### Production (MySQL)

The project is configured to use SQLite for development and testing.

### Development (SQLite)

## Database Configuration

The CI pipeline runs on every push and pull request to `main` and `develop` branches.

- **Formatting**: Ensures consistent code formatting
- **Security**: Automated security vulnerability scanning
- **Linting**: Code style and syntax checking
- **Testing**: Runs on Python 3.9, 3.10, 3.11, and 3.12

This project uses GitHub Actions for continuous integration:

## CI/CD

```md
./ci-check.sh
# All checks at once

bandit -r . -x ./venv,./env,./.venv
# Security check

flake8 .
# Run linting

isort .
# Sort imports

black .
# Format code
```bash


- **safety**: Dependency vulnerability checking
- **bandit**: Security analysis
- **flake8**: Linting and style checking
- **isort**: Import sorting
- **Black**: Code formatting

This project uses several tools to maintain code quality:


## Development

```

./ci-check.sh

```bash
Run local CI checks (includes linting, formatting, security checks):

```

python manage.py test

```bash
Run the test suite:

## Testing

- `/auth/` - Authentication endpoints (via Djoser)
- `/restaurant/booking/` - Booking management API
- `/restaurant/menu/` - Menu items API
- `/restaurant/` - Restaurant homepage
- `/admin/` - Django admin interface

## API Endpoints

The API will be available at `http://localhost:8000/`

```

python manage.py runserver

```bash
6. Start the development server:

```

python manage.py createsuperuser

```bash
5. Create a superuser (optional):

```

python manage.py migrate

```bash
4. Run migrations:

```

pip install -r requirements.txt

```bash
3. Install dependencies:

```

source venv/bin/activate  # On Windows: venv\Scripts\activate
python -m venv venv

```bash
2. Create a virtual environment:

```

cd littlelemon
git clone <repository-url>

```bash
1. Clone the repository:


- pip package manager
- Python 3.9 or higher


## Getting Started

- **Testing**: Django's built-in testing framework
- **Authentication**: Token-based authentication via DRF
- **Database**: SQLite (development), MySQL (production)
- **Backend**: Django 4.2+, Django REST Framework

## Tech Stack

- Comprehensive test suite
- RESTful API endpoints
- User authentication with token-based auth
- Booking system
- Menu item management

## Features

A Django REST API for the Little Lemon restaurant management system.
 Little Lemon Restaurant API
```