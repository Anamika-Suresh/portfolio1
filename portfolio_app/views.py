from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .models import Profile, Skill, Project, Contact, Certification, TimelineItem
from .forms import ContactForm, ProjectForm

def ensure_db_updated():
    try:
        if not Project.objects.filter(title='AI Agent using LangChain').exists():
            Project.objects.get_or_create(
                title='WhatsApp AI Chatbot',
                defaults={
                    'description': (
                        "Developed an intelligent WhatsApp AI Chatbot integrating natural language processing and automated messaging capabilities for real-time conversational responses.\n\n"
                        "Built modular backend workflows utilizing Python API integrations, processing user inquiries dynamically and delivering context-aware automated solutions.\n\n"
                        "Designed end-to-end conversation flows with robust error handling, webhook management, and scalable API architecture for seamless messaging interaction."
                    ),
                    'image': 'project_images/whatsapp_chatbot.jpg',
                    'github_link': 'https://github.com/Anamika-Suresh/whatsapp-chatbot',
                    'live_demo_link': '',
                    'category': 'AI/NLP'
                }
            )
            Project.objects.get_or_create(
                title='AI Agent using LangChain',
                defaults={
                    'description': (
                        "Architected an autonomous AI Agent framework powered by LangChain, enabling LLM-driven reasoning, multi-step problem solving, and tool execution.\n\n"
                        "Implemented agentic workflows with custom tool integration, vector store memory retrieval, and dynamic prompt orchestration to resolve complex user queries.\n\n"
                        "Leveraged Python, LangChain, and state-of-the-art LLMs to create structured agent memory pipelines and automated task execution graphs."
                    ),
                    'image': 'project_images/ai_agent_langchain.jpg',
                    'github_link': 'https://github.com/Anamika-Suresh/AI-Agent-Langchain',
                    'live_demo_link': '',
                    'category': 'AI/NLP'
                }
            )
        
        if not TimelineItem.objects.filter(title='AI/ML Intern', institution='Ladder7 Nextstep Solutions LLP').exists():
            TimelineItem.objects.create(
                title="AI/ML Intern",
                institution="Ladder7 Nextstep Solutions LLP",
                period="Sep 2026 - Present",
                item_type="Experience",
                order=1,
                description=(
                    "• Started an AI/ML internship focused on developing and experimenting with machine learning solutions, "
                    "data preprocessing, model development, and AI-based applications.\n"
                    "• Working with Python, Pandas, NumPy, Scikit-learn, TensorFlow, and PyTorch while collaborating with the R&D "
                    "team on practical AI/ML projects and technical problem-solving."
                )
            )
    except Exception as e:
        print(f"Auto-sync error: {e}")

def home_view(request):
    ensure_db_updated()
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            name="Jane Doe",
            title="Python & Django Developer",
            bio="Passionate software engineer building elegant, performant, and secure web applications.",
            location="New York, NY"
        )
    projects = Project.objects.order_by('-created_at')[:3]
    return render(request, 'portfolio_app/home.html', {'profile': profile, 'projects': projects})

def about_view(request):
    ensure_db_updated()
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            name="Jane Doe",
            title="Python & Django Developer",
            bio="Passionate software engineer building elegant, performant, and secure web applications.",
            location="New York, NY"
        )
    skills = Skill.objects.all()
    # Group skills by category for the about page UI
    skills_by_category = {}
    for choice_val, choice_lbl in Skill.CATEGORY_CHOICES:
        # Category field holds choice_val, e.g., 'Languages'
        skills_by_category[choice_lbl] = skills.filter(category=choice_val)
        
    experience_items = TimelineItem.objects.filter(item_type='Experience')
    education_items = TimelineItem.objects.filter(item_type='Education')
    certifications = Certification.objects.all()
    
    return render(request, 'portfolio_app/about.html', {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'experience_items': experience_items,
        'education_items': education_items,
        'certifications': certifications
    })

def projects_view(request):
    ensure_db_updated()
    projects = Project.objects.all().order_by('-created_at')
    # Fetch unique categories of projects currently in the database to show filter pills
    categories = Project.objects.values_list('category', flat=True).distinct()
    category_choices = dict(Project.CATEGORY_CHOICES)
    categories_list = [{'value': cat, 'label': category_choices.get(cat, cat)} for cat in categories if cat]
    return render(request, 'portfolio_app/projects.html', {
        'projects': projects,
        'categories_list': categories_list
    })

def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio_app/project_detail.html', {'project': project})

def contact_view(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            name="Anamika Suresh",
            title="AI/ML Engineer, Data Scientist",
            bio="B.Tech IT graduate with hands-on experience in Python systems.",
            location="Calicut, India"
        )
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save()
            # Send simulated email (Challenge extension)
            try:
                send_mail(
                    subject=f"New Portfolio Message from {contact_instance.name}",
                    message=f"From: {contact_instance.name} <{contact_instance.email}>\n\nMessage:\n{contact_instance.message}",
                    from_email='webmaster@localhost',
                    recipient_list=['anamika.suresh963@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                # Fallback print if email configuration fails
                print(f"Error sending email: {e}")
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/contact.html', {'form': form, 'profile': profile})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'portfolio_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have logged out successfully.")
    return redirect('home')

@login_required
def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Project added successfully!")
            return redirect('projects')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProjectForm()
    return render(request, 'portfolio_app/add_project.html', {'form': form})
