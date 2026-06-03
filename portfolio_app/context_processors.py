from .models import Profile

def profile_context(request):
    profile = Profile.objects.first()
    # Provide a fallback if profile hasn't been seeded yet
    if not profile:
        profile = Profile(
            name="Anamika Suresh",
            title="AI/ML Engineer, Data Scientist",
            location="Calicut, India",
            github_url="https://github.com/Anamika-Suresh",
            linkedin_url="https://linkedin.com/in/anamika-suresh-it"
        )
    return {
        'global_profile': profile
    }
