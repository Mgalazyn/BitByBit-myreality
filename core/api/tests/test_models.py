from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    #testing models

    def test_creating_user(self):
        #Testing creating a user
        email = 'test@example.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_email_error(self):
        #testing if user without email raise error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpassword123')

    def test_creating_superuser(self):
        #testing creating super user
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
