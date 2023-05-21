"""The tests for all user-related endpoints goes here"""

from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status


USER_REGISTER_URL = reverse("register")

def create_user(**args):
    return get_user_model().objects.create_user(**args)

class PublicUserAPITests(TestCase):
    """The tests for the public user api view"""

    def setUp(self):
        self.client = APIClient()

    def test_user_with_email_already_exists(self):
        payload = {
            "email": "test@example.com",
            "password": "testpassword"
        }

        create_user(**payload)
        response = self.client.post(USER_REGISTER_URL, payload)
        self.assertContains(response, "user with this email already exists")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)