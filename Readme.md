# Smart Inventory System

## Overview
Smart Inventory System is a Flask-based web application for managing products, tracking inventory levels, recording sales, and generating inventory and sales reports. The project is built to demonstrate practical backend development skills, including authentication, database modeling, and maintainable application architecture.

## Features
* User authentication and session management
* Product and inventory CRUD operations
* Sales recording with automatic stock deduction
* Low-stock monitoring
* Inventory and sales reporting
* Admin-restricted management routes
* Database migrations using Alembic

## Tech Stack
### Backend

* Python 3
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* Flask-Migrate (Alembic)
* Flask-Login
* Flask-WTF
* python-dotenv

### Frontend
* Server-rendered HTML with Jinja2
* Bootstrap (via Bootstrap-Flask)

### Database
* Relational database managed through SQLAlchemy



## Project Structure
smart-inventory-system/
│
├── app/
│   ├── __init__.py        # Application factory and extensions
│   ├── models/            # Database models
│   ├── routes/            # Blueprint-based routes
│   ├── templates/         # Jinja2 templates
│   └── static/            # Static assets
│
├── migrations/             # Database migration scripts
├── instance/               # Instance-specific configuration
├── config.py               # Application configuration
├── run.py                  # Application entry point
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
└── .gitignore


## Architecture
The application follows a modular MVC-style architecture:
* **Models**: SQLAlchemy ORM models representing users, products, inventory, and sales
* **Views**: Server-rendered HTML templates using Jinja2
* **Controllers**: Flask routes organized using Blueprints

The Flask Application Factory pattern is used to support scalability and clean separation of concerns.


## Environment Variables
Create a `.env` file in the project root with the following variables:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-connection-string
```


## Installation and Local Setup
### Prerequisites
* Python 3.9 or higher
* pip
* Virtual environment tool (venv or virtualenv)

### Setup Steps
```bash
# Clone the repository
git clone <repository-url>
cd smart-inventory-system

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
flask db upgrade

# Start the application
python run.py
```

The application will be available at:http://127.0.0.1:5000


## Database Migrations
Database schema changes are managed using Flask-Migrate.
```bash
flask db migrate -m "migration message"
flask db upgrade
```

## Authentication and Authorization
* Session-based authentication using Flask-Login
* Login required for protected routes
* Administrative routes restricted to authorized users


## Deployment
For production deployment:

* Use a WSGI server such as Gunicorn or uWSGI
* Place the application behind a reverse proxy (Nginx or Apache)
* Disable debug mode
* Manage secrets using environment variables


## License
No license file is included in this repository.

## Author
Richard Onyango
