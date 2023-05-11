from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**args):
    #help func for creating a new user
    return get_user_model().objects.create_user(**args)


class PublicUserApiTests(TestCase):
    def test_create_user(self):
        credentials = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'test',
        }
        result = self.client.post(CREATE_USER_URL, credentials)

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=credentials['email'])
        self.assertTrue(user.check_password(credentials['password']))

    def test_user_exisiting_email(self):
        #testing for unique emails
        credentials = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'test',
        }

        create_user(**credentials)
        result = self.client.post(CREATE_USER_URL, credentials)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)