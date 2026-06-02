import os
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio_app.models import Profile, Skill, Project

def populate():
    print("Starting database population script...")

    # 1. Create Superuser if not exists
    if not User.objects.filter(username='admin').exists():
        print("Creating superuser 'admin'...")
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Superuser created successfully! (User: admin, Pass: adminpassword)")
    else:
        print("Superuser 'admin' already exists.")

    # 2. Create Profile if not exists
    if not Profile.objects.exists():
        print("Creating profile for 'Anamika Suresh'...")
        profile = Profile.objects.create(
            name="Anamika Suresh",
            title="Python & Django Developer | AI Engineer",
            bio="I am a passionate software engineer specializing in Python development, web systems, and data-driven artificial intelligence. I enjoy solving complex logic problems, optimizing database queries, and designing beautiful responsive user interfaces.",
            location="Kochi, India",
            github_url="https://github.com/Anamika-Suresh",
            linkedin_url="https://linkedin.com/in/anamika-suresh"
        )
        print("Profile created!")
    else:
        print("Profile already exists.")

    # 3. Create Skills if not exists
    if not Skill.objects.exists():
        print("Creating skills...")
        skills_data = [
            # Languages
            ('Python', 90, 'Languages'),
            ('JavaScript', 80, 'Languages'),
            ('HTML5 & CSS3', 85, 'Languages'),
            ('SQL', 80, 'Languages'),
            # Backend
            ('Django', 88, 'Backend'),
            ('FastAPI', 75, 'Backend'),
            ('PostgreSQL', 78, 'Backend'),
            # Frontend
            ('Bootstrap', 85, 'Frontend'),
            ('React', 60, 'Frontend'),
            # Tools
            ('Git & GitHub', 85, 'Tools/Other'),
            ('Docker', 70, 'Tools/Other'),
        ]
        for name, prof, cat in skills_data:
            Skill.objects.create(name=name, proficiency=prof, category=cat)
        print(f"Created {len(skills_data)} skills!")
    else:
        print("Skills already exist.")

    # 4. Create Projects if not exists
    if not Project.objects.exists():
        print("Creating projects...")
        projects_data = [
            {
                'title': 'Heart Failure Prediction System',
                'description': 'A machine learning system integrated with a Django dashboard that predicts heart failure risk based on patient clinical indicators. Features real-time parameter analysis, visual health statistics, and downloadable report summaries.',
                'github_link': 'https://github.com/Anamika-Suresh/Heart_Failure_Prediction_System',
                'live_demo_link': 'https://heart-prediction.example.com',
                'category': 'Data Science'
            },
            {
                'title': 'AI Career Mentor & Resume Optimizer',
                'description': 'A web application built using Django and Generative AI that analyzes resume files against job descriptions. Provides actionable feedback on key achievements, keyword density, and schedules reminders for application followups.',
                'github_link': 'https://github.com/Anamika-Suresh/AI_Career_Mentor',
                'live_demo_link': 'https://career-mentor.example.com',
                'category': 'Web Dev'
            },
            {
                'title': 'E-Commerce Analytics Engine',
                'description': 'A real-time sales and stock reporting dashboard. Implements Django Celery for asynchronous billing processing, custom chart aggregations, and csv export integrations.',
                'github_link': 'https://github.com/Anamika-Suresh/Ecommerce_Analytics',
                'live_demo_link': 'https://sales-analytics.example.com',
                'category': 'Web Dev'
            }
        ]
        for proj in projects_data:
            Project.objects.create(**proj)
        print(f"Created {len(projects_data)} projects!")
    else:
        print("Projects already exist.")

    print("Database population completed successfully!")

if __name__ == '__main__':
    populate()
