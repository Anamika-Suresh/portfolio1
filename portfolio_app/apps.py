from django.apps import AppConfig
import sys

class PortfolioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_app'

    def ready(self):
        # Avoid running during management commands like makemigrations
        if 'manage.py' in sys.argv and any(arg in sys.argv for arg in ['makemigrations', 'migrate', 'collectstatic', 'check']):
            return
        
        try:
            from portfolio_app.models import Project
            if not Project.objects.filter(title='WhatsApp AI Chatbot').exists():
                import update_db_resume
                update_db_resume.update_db()
        except Exception:
            pass
