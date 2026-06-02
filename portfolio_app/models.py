from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Languages', 'Programming Languages'),
        ('Frameworks', 'Frameworks & Libraries'),
        ('Web', 'Web Technologies'),
        ('DevOps', 'DevOps & Tools'),
        ('Databases', 'Databases'),
        ('Concepts', 'Concepts'),
    ]
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(default=80)  # Value between 0 and 100
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Languages')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Web Dev', 'Web Development'),
        ('Data Science', 'Data Science & ML'),
        ('AI/NLP', 'AI & NLP'),
        ('Deep Learning', 'Deep Learning & CV'),
        ('Game Dev', 'Game Development'),
        ('Forecasting', 'Time Series Forecasting'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Web Dev')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class Certification(models.Model):
    title = models.CharField(max_length=200)
    authority = models.CharField(max_length=150)
    date_earned = models.CharField(max_length=50)  # e.g., "April 2026"
    description = models.TextField(blank=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.authority}"

class TimelineItem(models.Model):
    TYPE_CHOICES = [
        ('Experience', 'Professional Experience / Internship'),
        ('Education', 'Education'),
    ]
    title = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)  # Company or school name
    period = models.CharField(max_length=100)       # e.g., "2020 - 2024"
    description = models.TextField(blank=True)      # Bullet points / details
    item_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Experience')
    order = models.IntegerField(default=0)          # Control sorting order

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} at {self.institution} ({self.period})"

