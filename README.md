# Image Gallery

A web application for uploading, viewing, and deleting images. Supports user registration, login, password reset, light/dark themes, and pagination.

## Technologies
- Python (Flask)
- HTML/CSS
- SQLite
- Jinja2
- Pillow
- python-dotenv
- itsdangerous

## Features
- User registration and login (passwords hashed)
- Optional email for password recovery
- Password reset via email (if provided)
- Upload, view, and delete your own images
- Captions for images
- Pagination
- Light/dark theme with toggle
- Responsive design (mobile-friendly)

## Installation and Run

1. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (see example below).

4. Run the application:
```bash
python app.py
```

5. Open in your browser: http://localhost:5000

## Example .env
```
SECRET_KEY=your-very-secret-key
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
EMAIL_FROM=your@email.com
```

## Project Structure
```
galerieWebSite/
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── README.md
├── TDD_SPEC.md
├── TECHNICAL_PLAN.md
├── templates/
│   ├── index.html
│   ├── image.html
│   ├── login.html
│   ├── register.html
│   ├── forgot.html
│   ├── reset.html
│   └── upload.html
├── static/
│   ├── style.css
│   ├── theme.js
│   └── uploads/
└── database.db
```

## License
MIT (add LICENSE file if needed) 