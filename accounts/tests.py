from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomUserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='test@gmail.com', username='test',password='1234')
        self.superuser = get_user_model().objects.create(email='admin@gmail.com', password='admin123', username='admin', is_staff=True, is_superuser=True)
    
    def test_user_creation_data(self):
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertEqual(self.user.username, 'test')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)
        
    def test_superuser_creation(self):
        self.assertEqual(self.superuser.email, 'admin@gmail.com')
        self.assertEqual(self.superuser.username, 'admin')
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    
    