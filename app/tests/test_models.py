from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTestCase(TestCase):
    """Testcases for the user model goes here"""

    def testing_creating_user_with_email_successful(self):
        """Testing creating user with email successful"""
        email = "test@example.com"
        password = "testpassword"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def testing_user_entered_email_normalized(self):
        """Testing whether or not email is normalized"""
        emails = [
            ["test@example.com", "test@example.com"],
            ["Test2@example.com", "Test2@example.com"],
        ]

        for email, expected_email in emails:
            user = get_user_model().objects.create_user(email=email, password="testpassword")
            self.assertEqual(user.email, email)
            self.assertTrue(user.check_password("testpassword"))

    def test_new_user_registration_without_email_raises_error(self):
        """Testing whether new user registered without email raises an error"""

        with self.assertRaises(ValueError):
            user =get_user_model().objects.create_user(email="", password="testpassword")


    def test_create_superuser(self):
        """Testing creeation of new superuser"""
        email = 'test@example.com'
        password = "testpassword"

        user =get_user_model().objects.create_superuser(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(password))



    