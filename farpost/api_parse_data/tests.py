import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farpost.settings')
django.setup()


from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Advertisement


class AuthTests(APITestCase):
    def setUp(self):
        # Создаем пользователя для тестов
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_token_obtain(self):
        url = reverse('auth:token_obtain_pair')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.access_token = response.data['access']

    def tearDown(self):
        User.objects.all().delete()


class AdvertisementTests(APITestCase):
    def setUp(self):
        # Создаем пользователя и получаем токен
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token_url = reverse('auth:token_obtain_pair')
        self.token_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        self.token_response = self.client.post(self.token_url, self.token_data, format='json')
        self.access_token = self.token_response.data['access']

        # Создаем тестовое объявление
        self.ad = Advertisement.objects.create(
            title="Test Ad",
            advertisement_id=123456789,
            author="Test Author",
            views=100,
            position=1
        )
        self.api_url = reverse('api:advertisement-detail', kwargs={'advertisement_id': self.ad.advertisement_id})

    def test_get_advertisement(self):
        # Тестируем доступ к защищенному API
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.ad.title)
        self.assertEqual(response.data['advertisement_id'], self.ad.advertisement_id)
        self.assertEqual(response.data['author'], self.ad.author)
        self.assertEqual(response.data['views'], self.ad.views)
        self.assertEqual(response.data['position'], self.ad.position)

    def tearDown(self):
        User.objects.all().delete()
        Advertisement.objects.all().delete()
