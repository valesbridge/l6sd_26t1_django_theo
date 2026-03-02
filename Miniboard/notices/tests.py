"""Tests for the notices application."""

from django.test import TestCase, Client
from django.urls import reverse
from .models import Notice


class NoticeModelTest(TestCase):
    """Test the Notice model."""
    
    def setUp(self):
        """Create a test notice."""
        self.notice = Notice.objects.create(
            title="Test Notice",
            content="This is a test notice",
            author="Test Author",
            is_pinned=False
        )
    
    def test_notice_creation(self):
        """Test that a notice can be created."""
        self.assertEqual(self.notice.title, "Test Notice")
        self.assertEqual(self.notice.author, "Test Author")
        self.assertFalse(self.notice.is_pinned)
    
    def test_notice_str(self):
        """Test the string representation of a notice."""
        self.assertEqual(str(self.notice), "Test Notice")


class NoticeViewTest(TestCase):
    """Test the Notice views."""
    
    def setUp(self):
        """Create test data."""
        self.client = Client()
        self.notice = Notice.objects.create(
            title="Welcome",
            content="Welcome to our noticeboard",
            author="Admin"
        )
    
    def test_home_view(self):
        """Test the home view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mini Noticeboard")
    
    def test_notice_detail_view(self):
        """Test the notice detail view."""
        response = self.client.get(reverse('notice_detail', args=[self.notice.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.notice.title)
    
    def test_create_notice_view(self):
        """Test the create notice view."""
        response = self.client.get(reverse('create_notice'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_notice_post(self):
        """Test creating a notice via POST."""
        data = {
            'title': 'New Notice',
            'content': 'This is a new notice',
            'author': 'New Author',
            'is_pinned': False
        }
        response = self.client.post(reverse('create_notice'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Notice.objects.filter(title='New Notice').exists())
    
    def test_about_view(self):
        """Test the about view."""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mini Noticeboard")
