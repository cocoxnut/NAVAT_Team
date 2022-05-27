from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team


class TeamTests(APITestCase):
    BASE_URL = 'http://127.0.0.1:8000/'
    def test_get_all_posts(self):
        url = self.BASE_URL + 'api/v1/team/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # if response.status == status.201
    # return ok
    # else:
    # return assertError
    # assert response.status == status.200

    def test_create_team(self):
        data = {
            'id': 50,
            'name': 'test_name',
            'description': 'test_description'
        }
        url = self.BASE_URL + 'api/v1/team/'  # api/v1/post_create
        response = self.client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self):
        Team.objects.create(id=50,
                            name='test_name',
                            description='test_description', )

        url = self.BASE_URL + 'api/v1/team/50'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_post(self):
        Team.objects.create(id=50,
                            name='test_name',
                            description='test_description', )
        data = {
            'id': 50,
            'name': 'test_name',
            'description': 'test_description'
        }
        url = self.BASE_URL + 'api/v1/team/50'  # api/v1/post_create
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
