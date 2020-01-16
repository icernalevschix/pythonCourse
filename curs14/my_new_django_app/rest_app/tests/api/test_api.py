from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
import json

from rest_app.models import FancyCat

class ListApiTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('fancy_cats_list')
        FancyCat.objects.create(name='Alex', age=2)
        FancyCat.objects.create(name='Oscar', age=1)

    def test_get_method(self):

        # user = User.objects.create_superuser(username="admin", password="adminadmin",
        #     email="admin@example.com")
        # self.client.force_login(user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {'id': 1, 'name': 'Alex'},
            {'id': 2, 'name': 'Oscar'}
        ])
    
    def test_post_method(self):
        data = {'name': 'Mary'}
        user = User.objects.create_superuser(username="admin", password="adminadmin",
            email="admin@example.com")
        self.client.force_login(user)
        response = self.client.post(self.url, data = data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['name'], 'Mary')
        self.assertEqual(FancyCat.objects.count(), 3)

    def test_not_authenticated(self):
        data = {'name': 'Mary'}
        response = self.client.post(self.url, data = {'name': 'Mary'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_bad_request(self):
        data = {}
        user = User.objects.create_superuser(username="admin", password="adminadmin",
            email="admin@example.com")
        self.client.force_login(user)
        response = self.client.post(self.url, data = data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_get_single_auth(self):
        user = User.objects.create_superuser('admin', None, 'adminadmin')
        self.client.force_login(user)
        self.url = reverse('fancy_cats_detail', kwargs={'pk':2} )
        response = self.client.get(self.url)

        self.assertJSONEqual(response.content, {'id': 2, 'name': 'Oscar'})
        # print(type(response.content))
        # print(type(response.data))

    def test_get_single_nonAuth(self):
        self.url = reverse('fancy_cats_detail', kwargs={'pk':1})
        response = self.client.get(self.url)

        # self.assertJSONEqual(response.content, {'id': 1, 'name': 'Alex'})  # **** fails if permission_classes are commented out
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_auth(self):
        user = User.objects.create_superuser('admin', None, 'adminadmin')
        self.client.force_login(user)
        self.url = reverse('fancy_cats_detail', kwargs={'pk':1})
        data = {'name': 'Patrunjel'}
        response = self.client.put(self.url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Patrunjel')
        self.assertEqual(response.data['id'], 1)

    def test_put_nonAuth(self):
        self.url = reverse('fancy_cats_detail', kwargs={'pk':1})
        data = {'name': 'Patrunjel'}
        response = self.client.put(self.url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_auth(self):
        user = User.objects.create_superuser('admin', None, 'adminadmin')
        self.client.force_login(user)
        self.url = reverse('fancy_cats_detail', kwargs={'pk':1})
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FancyCat.objects.count(), 1)

    def test_delete_nonAuth(self):
        self.url = reverse('fancy_cats_detail', kwargs={'pk':1})
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)