import os
import django

# Setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from django.contrib.auth.models import User
from portfolio_app.models import Profile, Skill, Project, Certification, TimelineItem

def update_db():
    print("Starting database update with resume data...")

    # Create Superuser if not exists
    if not User.objects.filter(username='admin').exists():
        print("Creating superuser 'admin'...")
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Superuser created successfully! (User: admin, Pass: adminpassword)")
    else:
        print("Superuser 'admin' already exists. Resetting password to 'adminpassword'...")
        admin_user = User.objects.get(username='admin')
        admin_user.set_password('adminpassword')
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.save()

    # Clear previous seed data (except contacts and admin user)
    print("Clearing previous database contents...")
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Certification.objects.all().delete()
    TimelineItem.objects.all().delete()

    # 1. Create Profile
    print("Creating Profile for 'Anamika Suresh'...")
    Profile.objects.create(
        name="Anamika Suresh",
        title="AI/ML Engineer, Data Scientist",
        bio=(
            "B.Tech IT graduate with hands-on experience in end-to-end application development "
            "and deployment, including REST API development using Flask and FastAPI, and model "
            "integration via Python-based backend systems. Proficient in Python and SQL, with "
            "practical exposure to software development lifecycle concepts and DevOps tools "
            "including Docker and Git. Experienced in building and deploying data-driven "
            "applications with a focus on system integration and API-based data exchange. "
            "Strong written and spoken communication skills with a growth-oriented, "
            "collaborative approach to enterprise problem-solving."
        ),
        profile_image='profile_images/profile_pic.jpg',
        location="Calicut, India",
        github_url="https://github.com/Anamika-Suresh",
        linkedin_url="https://linkedin.com/in/anamika-suresh-it"
    )

    # 2. Create Skills
    print("Creating Technical Skills...")
    skills_data = [
        # Programming Languages
        ('Python', 92, 'Languages'),
        ('SQL', 85, 'Languages'),
        # Frameworks & Libraries
        ('Flask', 88, 'Frameworks'),
        ('FastAPI', 82, 'Frameworks'),
        ('Pandas', 85, 'Frameworks'),
        ('NumPy', 80, 'Frameworks'),
        # Web Technologies
        ('HTML', 85, 'Web'),
        ('CSS', 80, 'Web'),
        ('JavaScript', 75, 'Web'),
        # DevOps & Tools
        ('Docker', 70, 'DevOps'),
        ('Git/GitHub', 88, 'DevOps'),
        ('REST API Development', 85, 'DevOps'),
        # Databases
        ('PostgreSQL', 82, 'Databases'),
        ('MySQL', 80, 'Databases'),
        ('SQLite', 85, 'Databases'),
        # Concepts
        ('Software Development Life Cycle (SDLC)', 85, 'Concepts'),
        ('API Integration', 85, 'Concepts'),
        ('Data Access & Processing', 88, 'Concepts'),
        ('System Integration', 82, 'Concepts')
    ]
    
    for name, prof, cat in skills_data:
        Skill.objects.create(name=name, proficiency=prof, category=cat)
    print(f"Created {len(skills_data)} skills.")

    # 3. Create Timeline Items (Experience and Education)
    print("Creating Education and Experience timeline...")
    # Experience
    TimelineItem.objects.create(
        title="Python Programming Intern",
        institution="Verveox Technologies",
        period="Jul 2025 - Aug 2025",
        item_type="Experience",
        order=1,
        description=(
            "• Engineered Python applications leveraging core programming constructs and optimised "
            "data structures to support analytical workflows; implemented ML models using Scikit-learn "
            "for foundational AI solutions.\n"
            "• Architected and deployed data-driven web applications using Flask framework for real-time "
            "analytical output delivery; managed source code and collaborative development workflows via "
            "Git and GitHub."
        )
    )

    TimelineItem.objects.create(
        title="FAB Lab Intern",
        institution="CUSAT (Cochin University of Science and Technology)",
        period="June 2023",
        item_type="Experience",
        order=2,
        description="Engaged in hands-on training, prototyping, and project development focusing on 3D designing, CAD modeling, and foundational robotics."
    )

    # Education
    TimelineItem.objects.create(
        title="B.Tech in Information Technology",
        institution="Cochin University of Science and Technology",
        period="2020 - 2024",
        item_type="Education",
        order=3,
        description="CGPA: 8.33/10 (Graduated with Distinction)"
    )
    print("Timeline created successfully.")

    # 4. Create Certifications
    print("Creating Certifications...")
    certifications_data = [
        {
            'title': 'Data Science with Generative AI',
            'authority': 'Entri Elevate | Illinois Tech | NSDC',
            'date_earned': 'Apr 2026',
            'description': (
                "Completed an industry-relevant program covering Python-based data analysis, "
                "statistical inference, and predictive modeling using Machine Learning, Deep Learning, "
                "and Generative AI techniques. Executed hands-on projects on real-world datasets, "
                "applying end-to-end data workflows from extraction to insight generation."
            ),
            'credential_url': 'https://www.credly.com/badges/37b815ca-e97a-40db-9581-4dd7d04e840d/linked_in?t=tf46k4'
        },
        {
            'title': 'Introduction to Generative AI',
            'authority': 'Google Cloud',
            'date_earned': 'Aug 2025',
            'description': (
                "Analyzed core concepts of Generative AI including large language models, use-case "
                "applications, and responsible AI principles. Evaluated ethical considerations and "
                "business implications of AI-generated content in analytical workflows."
            )
        },
        {
            'title': 'Python | Machine Learning | Deep Learning',
            'authority': 'Kaggle',
            'date_earned': 'Mar 2023',
            'description': (
                "Built practical proficiency in Python, ML algorithms, and deep learning architectures "
                "through structured, competition-grade exercises."
            )
        }
    ]
    for cert in certifications_data:
        Certification.objects.create(**cert)
    print(f"Created {len(certifications_data)} certifications.")

    # 5. Create Projects
    print("Creating Projects...")
    projects_data = [
        {
            'title': 'Heart Failure Prediction System',
            'description': (
                "Designed and developed a full-stack web application following end-to-end SDLC principles, "
                "integrating a Flask backend with a PostgreSQL database to manage, store, and retrieve "
                "structured clinical data, and embedded a KNN-based classification model achieving 80.97% "
                "accuracy for real-time patient risk prediction.\n\n"
                "Implemented RESTful API endpoints using Flask to enable seamless data exchange between the "
                "ML inference layer, PostgreSQL backend, and frontend interface, demonstrating "
                "enterprise-style system integration and modular application architecture.\n\n"
                "Developed a responsive frontend using HTML, CSS, and JavaScript to present prediction "
                "outcomes and clinical insights clearly to non-technical users, ensuring cross-functional "
                "usability and clean separation of application layers."
            ),
            'image': 'project_images/heart_predict.png',
            'github_link': 'https://github.com/Anamika-Suresh/Heart_Failure_Prediction_System',
            'live_demo_link': '',
            'category': 'Data Science'
        },
        {
            'title': 'NOx Emission Prediction System',
            'description': (
                "Developed and deployed a data-driven web application using Flask, exposing a RESTful API "
                "endpoint that integrates a regression model achieving 88.6% accuracy for real-time NOx "
                "emission forecasting from gas turbine sensor data.\n\n"
                "Implemented a structured data access and preprocessing pipeline using Pandas, NumPy, "
                "and Scikit-learn to clean, transform, and manage raw sensor data, ensuring high data quality "
                "for reliable model inference and application output.\n\n"
                "Designed an end-to-end application workflow from data ingestion and ML model integration "
                "to RESTful API response and frontend display, applying SDLC principles and modular code design "
                "for maintainable, scalable application development."
            ),
            'image': 'project_images/nox_predict.png',
            'github_link': 'https://github.com/Anamika-Suresh/Gas-Turbine-NOX-Emission',
            'live_demo_link': '',
            'category': 'Data Science'
        },
        {
            'title': 'Ice Pellet Catcher',
            'description': (
                "Designed and developed a fully functional application in Python following end-to-end "
                "Software Development Life Cycle (SDLC) principles, from requirement gathering and design "
                "to implementation, testing, and deployment.\n\n"
                "Implemented core application logic including real-time collision detection, object state "
                "management, and scoring systems using object-oriented programming principles, demonstrating "
                "structured and modular code design. Managed source code versioning and project collaboration "
                "using Git/GitHub."
            ),
            'image': 'project_images/ice_catcher.png',
            'github_link': 'https://github.com/Anamika-Suresh/ice-pellet-catcher-game',
            'live_demo_link': '',
            'category': 'Game Dev'
        },
        {
            'title': 'AI Chatbot using LLAMA Model and Streamlit',
            'description': (
                "Explored and implemented a locally-deployed LLM-based conversational AI system using "
                "the LLAMA model via Ollama, demonstrating active participation in learning and applying "
                "new generative AI technologies.\n\n"
                "Extracted and managed conversational context across multi-turn interactions, applying NLP "
                "techniques to maintain coherent, stateful dialogue to translating technical model capabilities "
                "into a usable product. Built an interactive Streamlit frontend to present AI responses clearly "
                "to end users, demonstrating ability to communicate model outputs to non-technical stakeholders "
                "through intuitive UI design."
            ),
            'image': 'project_images/ai_chatbot.png',
            'github_link': 'https://github.com/Anamika-Suresh/llama-model-AI-assistant',
            'live_demo_link': '',
            'category': 'AI/NLP'
        },
        {
            'title': 'Interview Assistant: Facial Emotion Detection',
            'description': (
                "Architected a real-time Facial Emotion Recognition system across 7 emotion classes, "
                "achieving 61.6% accuracy, a strong benchmark for multi-class deep learning classification tasks.\n\n"
                "Integrated OpenCV-based webcam input with a Flask backend for live inference, enabling real-time "
                "emotion analysis from both uploaded images and video streams. Designed a user-facing web "
                "interface displaying emotion prediction results with confidence feedback, enhancing model "
                "interpretability for end users."
            ),
            'image': 'project_images/emotion_detect.png',
            'github_link': 'https://github.com/Anamika-Suresh/Interview-assistant-facial-emotion-detector',
            'live_demo_link': '',
            'category': 'Deep Learning'
        },
        {
            'title': 'Retail Sales Time Series Forecasting',
            'description': (
                "Engineered time-based features from raw retail sales data — isolating weekly and yearly "
                "seasonality, handling missing values, and quantifying promotional impact — producing a "
                "clean dataset for model training.\n\n"
                "Benchmarked ARIMA against Facebook Prophet for daily sales forecasting; Prophet outperformed "
                "ARIMA with 39% lower MAE (44.95 vs 73.65) and 38% lower RMSE (59.02 vs 95.54).\n\n"
                "Delivered comparative visualisations of forecast outputs and residual errors using Matplotlib "
                "and Seaborn, translating model results into decision-ready insights."
            ),
            'image': 'project_images/sales_forecast.png',
            'github_link': 'https://github.com/Anamika-Suresh/time-series-forcasting',
            'live_demo_link': '',
            'category': 'Forecasting'
        },
        {
            'title': 'Loan Default Risk Prediction',
            'description': (
                "Trained a Random Forest classification model on financial data achieving 89% accuracy "
                "for automated loan default risk assessment.\n\n"
                "Resolved class imbalance through targeted feature engineering and preprocessing, improving "
                "model robustness and reducing false-negative risk in predictions. Deployed a Flask RESTful "
                "API with an interactive web interface delivering real-time risk scores to non-technical "
                "end users."
            ),
            'image': 'project_images/loan_risk.png',
            'github_link': 'https://github.com/Anamika-Suresh/Loan-risk-prediction-app',
            'live_demo_link': '',
            'category': 'Data Science'
        },
        {
            'title': 'AI Career Mentor & Resume Optimizer',
            'description': (
                "A Personal Career Mentor platform utilizing Retrieval-Augmented Generation (RAG) "
                "concepts to help fresh graduates and job seekers prepare for interviews, optimize "
                "resumes, and analyze hiring patterns. Implements text chunking, ChromaDB vector store "
                "indexing, and customized mentor prompts with Google Gemini & OpenAI LLM backends to "
                "render conversational advice along with citations and retrieved source files."
            ),
            'image': 'project_images/career_mentor.png',
            'github_link': 'https://github.com/Anamika-Suresh/AI-Career-Mentor',
            'live_demo_link': 'https://ai-career-mentor-5vsbprjw8pfaj9r4ubc52q.streamlit.app/',
            'category': 'AI/NLP'
        }
    ]
    for proj in projects_data:
        Project.objects.create(**proj)
    print(f"Created {len(projects_data)} projects.")
    
    print("Database seeding completed with resume details!")

if __name__ == '__main__':
    update_db()
