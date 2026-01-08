"""
Tests for the tasks application.
"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Task, UserProfile


class TaskModelTest(TestCase):
    """Test cases for Task model."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            priority='high',
            due_date=timezone.now().date() + timedelta(days=7)
        )
    
    def test_task_creation(self):
        """Test task is created correctly."""
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.priority, 'high')
        self.assertEqual(self.task.status, 'pending')
    
    def test_task_str(self):
        """Test task string representation."""
        self.assertEqual(str(self.task), 'Test Task')
    
    def test_mark_completed(self):
        """Test marking task as completed."""
        self.task.mark_completed()
        self.assertEqual(self.task.status, 'completed')
        self.assertIsNotNone(self.task.completed_at)
    
    def test_mark_pending(self):
        """Test marking task as pending."""
        self.task.mark_completed()
        self.task.mark_pending()
        self.assertEqual(self.task.status, 'pending')
        self.assertIsNone(self.task.completed_at)
    
    def test_is_overdue(self):
        """Test overdue task detection."""
        # Task in future - not overdue
        self.assertFalse(self.task.is_overdue)
        
        # Task in past - overdue
        self.task.due_date = timezone.now().date() - timedelta(days=1)
        self.task.save()
        self.assertTrue(self.task.is_overdue)
        
        # Completed task - not overdue
        self.task.mark_completed()
        self.assertFalse(self.task.is_overdue)
    
    def test_is_completed(self):
        """Test completed status check."""
        self.assertFalse(self.task.is_completed)
        self.task.mark_completed()
        self.assertTrue(self.task.is_completed)


class TaskViewTest(TestCase):
    """Test cases for Task views."""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description'
        )
    
    def test_home_view(self):
        """Test home page view."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/home.html')
    
    def test_task_list_view_requires_login(self):
        """Test task list requires authentication."""
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_task_list_view_authenticated(self):
        """Test task list view with authentication."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, 'Test Task')
    
    def test_task_create_view(self):
        """Test task creation."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task-create'), {
            'title': 'New Task',
            'description': 'New Description',
            'priority': 'medium',
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())
    
    def test_task_update_view(self):
        """Test task update."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('task-update', kwargs={'pk': self.task.pk}),
            {
                'title': 'Updated Task',
                'description': 'Updated Description',
                'priority': 'high',
                'status': 'in_progress'
            }
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.priority, 'high')
    
    def test_task_delete_view(self):
        """Test task deletion."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('task-delete', kwargs={'pk': self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
    
    def test_task_toggle_view(self):
        """Test task toggle completion."""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('task-toggle', kwargs={'pk': self.task.pk})
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, 'completed')


class UserProfileTest(TestCase):
    """Test cases for UserProfile model."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpass123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            bio='Test Bio',
            phone_number='1234567890'
        )
    
    def test_profile_creation(self):
        """Test user profile is created correctly."""
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.bio, 'Test Bio')
    
    def test_profile_str(self):
        """Test profile string representation."""
        self.assertEqual(str(self.profile), "testuser's Profile")
    
    def test_full_name_property(self):
        """Test full name property."""
        self.user.first_name = 'John'
        self.user.last_name = 'Doe'
        self.user.save()
        self.assertEqual(self.profile.full_name, 'John Doe')
