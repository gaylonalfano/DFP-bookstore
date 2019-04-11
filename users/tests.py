# users/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        """Test creating a new user is successful"""
        user = get_user_model().objects.create_user(
            username='test',
            email='test@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test creating a new superuser is successful"""
        user = get_user_model().objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )

        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
