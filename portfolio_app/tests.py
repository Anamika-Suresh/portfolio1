from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile, Project, Contact, Skill, Certification, TimelineItem

class PortfolioTestCase(TestCase):
    def setUp(self):
        # Create user
        self.user = User.objects.create_user(username='testdeveloper', password='password123')
        
        # Create Profile
        self.profile = Profile.objects.create(
            name="Test Developer",
            title="Tester",
            bio="Just testing things.",
            location="Test City"
        )
        
        # Create Skill
        self.skill = Skill.objects.create(
            name="Testing Skill",
            proficiency=99,
            category="Languages"
        )
        
        # Create Project
        self.project = Project.objects.create(
            title="Test Project",
            description="Testing project description.",
            github_link="https://github.com",
            live_demo_link="https://demo.com",
            category="Web Dev"
        )

        # Create Timeline Item
        self.timeline_item = TimelineItem.objects.create(
            title="Test Internship",
            institution="Test Company",
            period="2025",
            item_type="Experience",
            order=1,
            description="Built test suites."
        )

        # Create Certification
        self.certification = Certification.objects.create(
            title="Test Certification",
            authority="Test Authority",
            date_earned="2026",
            description="Earned test credential."
        )

    def test_anonymous_access_views(self):
        """Verify standard pages load with 200 OK for anonymous visitors."""
        pages = ['home', 'about', 'projects', 'contact', 'login']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200)

    def test_about_page_dynamic_content(self):
        """Verify that dynamic timeline items and certifications display on About page."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.timeline_item.title)
        self.assertContains(response, self.timeline_item.institution)
        self.assertContains(response, self.certification.title)
        self.assertContains(response, self.certification.authority)

    def test_project_detail_view(self):
        """Verify project detail page loads successfully with 200 OK."""
        response = self.client.get(reverse('project_detail', args=[self.project.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.project.title)

    def test_contact_form_submission(self):
        """Verify submitting the contact form saves to database and redirects."""
        data = {
            'name': 'John Tester',
            'email': 'john@test.com',
            'message': 'This is a test message from unit tests.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertEqual(Contact.objects.count(), 1)
        
        saved_msg = Contact.objects.first()
        self.assertEqual(saved_msg.name, 'John Tester')
        self.assertEqual(saved_msg.email, 'john@test.com')

    def test_add_project_anonymous_redirect(self):
        """Verify adding a project redirects anonymous users to login page."""
        response = self.client.get(reverse('add_project'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_add_project_authenticated_access(self):
        """Verify authenticated users can access the add project page."""
        self.client.login(username='testdeveloper', password='password123')
        response = self.client.get(reverse('add_project'))
        self.assertEqual(response.status_code, 200)
        
    def test_add_project_submission(self):
        """Verify authenticated users can submit a project successfully."""
        self.client.login(username='testdeveloper', password='password123')
        data = {
            'title': 'New Dynamic Project',
            'description': 'A new project added from web interface.',
            'github_link': 'https://github.com/new',
            'live_demo_link': 'https://newdemo.com',
            'category': 'Web Dev'
        }
        response = self.client.post(reverse('add_project'), data)
        self.assertEqual(response.status_code, 302)  # Redirects back to projects list
        self.assertEqual(Project.objects.count(), 2)  # 1 from setUp + 1 new
        
        new_proj = Project.objects.get(title='New Dynamic Project')
        self.assertEqual(new_proj.category, 'Web Dev')
