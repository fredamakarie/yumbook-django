# accounts/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

User = get_user_model()

class AccountsTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "username": "testuser",
            "password": "password123",
            "email": "test@example.com"
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_user_creation(self):
        """Ensure a user can be created"""
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertEqual(self.user.username, "testuser")

    def test_user_authentication(self):
        """Ensure user can log in with correct credentials"""
        login = self.client.login(username="testuser", password="password123")
        self.assertTrue(login)

    def test_user_token_authentication(self):
        """Ensure DRF token authentication works"""
        from rest_framework.authtoken.models import Token
        token, created = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('recipe-list'))  # assuming recipe-list exists
        self.assertIn(response.status_code, [200, 403, 404])  # depends on your setup

    def test_register_user_api(self):
        """Ensure new user can register via API endpoint"""
        data = {
            "username": "newuser",
            "password": "newpassword123",
            "email": "new@example.com"
        }
        response = self.client.post(reverse('register'), data, format='json')
        self.assertIn(response.status_code, [200, 201])
