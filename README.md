# Developer Portfolio & Project Management System

A premium, glassmorphic developer portfolio website built with Django. It features dynamic content rendering from a database (SQLite), a timeline for education and experience, a credentials/certifications grid, and an administrative login for real-time project management.

## 🚀 Live Demo
**Website:** [https://portfolio1-iv6j.onrender.com/](https://portfolio1-iv6j.onrender.com/)

---

## ✨ Features

- **Responsive Modern Design**: Elegant glassmorphic UI with micro-interactions, responsive grids, and premium HSL color tokens.
- **Dynamic Dark/Light Mode**: User-controlled theme toggling with persistent state (stored in local storage) for consistent viewing.
- **Interactive Project Filter**: Dynamic client-side project filtering by category with smooth opacity transitions.
- **Database-Driven Resume**: 
  - **Profile Card**: Displays name, title, profile picture, location, and social links.
  - **Resume Timeline**: Chronological vertical timeline for education and industry experience.
  - **Technical Skills**: Visual progress bars categorized by programming languages, frameworks, web technologies, DevOps, databases, and general concepts.
  - **Certifications**: Showcase credentials with direct Credly verification links.
- **Secure Contact Form**: A validated, interactive contact form that stores submissions in the database and prints notification emails to the terminal console (or sends via configured SMTP).
- **Developer Access & Management**: 
  - Administrative login portal for the site owner.
  - Secure `/login/` view redirecting to a dashboard where you can add new projects directly from the web interface.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django 5.2
- **Frontend**: HTML5, Vanilla CSS3 (Custom design system), JavaScript (ES6), Bootstrap Icons
- **Database**: SQLite3 (Development & Production)
- **Deployment & Hosting**: Gunicorn (WSGI Server), WhiteNoise (Static asset hosting), Render cloud platform

---

## 📂 Directory Structure

```text
portfolio/
├── media/                     # User-uploaded profile & project images
│   ├── profile_images/
│   └── project_images/
├── portfolio_app/             # Main portfolio Django application
│   ├── templates/             # HTML templates (base, home, about, projects, contact, etc.)
│   ├── models.py              # Profile, Skill, Project, Contact, Certification, Timeline models
│   ├── views.py               # View controllers (rendering, auth, project management)
│   ├── forms.py               # Project management & Contact form definitions
│   └── urls.py                # App routing
├── portfolio_project/         # Django core configuration folder
│   ├── settings.py            # Global project configurations (security, DB, WhiteNoise, Static)
│   └── urls.py                # Root routing
├── static/                    # Frontend assets
│   ├── css/
│   │   └── style.css          # Premium style tokens, animations & layout designs
│   └── js/
│       └── main.js            # Theme toggle, client-side filtering, form validation
├── populate_db.py             # Initial database seeder script
├── update_db_resume.py        # Updated database seeder reflecting LaTeX resume details
├── requirements.txt           # Python package dependencies
├── .python-version            # Python version rule for Render
└── manage.py                  # Django CLI entrypoint
```

---

## 💻 Local Setup & Running Instructions

### Prerequisites
Make sure you have **Python 3.11+** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/Anamika-Suresh/portfolio1.git
cd portfolio1
```

### 2. Create and Activate Virtual Environment
On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
Create and initialize database tables for your models:
```bash
python manage.py migrate
```

### 5. Seed the Resume & Project Data
Run the database update script to pre-populate the profile, skills, timeline, certifications, and project lists matching your resume:
```bash
python update_db_resume.py
```
*Note: This will also automatically ensure that a developer superuser (`admin`) is created or reset with the password `adminpassword`.*

### 6. Start the Development Server
```bash
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser.

---

## 🔑 Administrative Access

To add projects or manage resume contents directly:
1. Go to **`/login/`** (or click the **Login** button in the header navigation).
2. Enter the default developer credentials:
   - **Username**: `admin`
   - **Password**: `adminpassword`
3. Once logged in, you will be redirected to the home page with an administrative privilege level, allowing you to add new projects via the form interface.
