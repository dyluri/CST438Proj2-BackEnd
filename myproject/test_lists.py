from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from base.models import Lists

class ListsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list = Lists.objects.create(user_id=1, list_name='Test List', item_list='1,2,3')

    def test_get_lists(self):
        response = self.client.get('/lists')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_items(self):
        response = self.client.get('/list', {'list_id': self.list.list_id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['list_name'], 'Test List')

    def test_get_all_items(self):
        response = self.client.get('/list/items', {'user_id': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('1', response.data)
        self.assertIn('2', response.data)
        self.assertIn('3', response.data)

    def test_add_list(self):
        response = self.client.post('/list/add', {'user_id': 1, 'list_name': 'New List', 'item_list': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['list_name'], 'New List')

    def test_add_item(self):
        response = self.client.post('/list/addItem', {'user_id': 1, 'list_id': self.list.list_id, 'item_id': '4'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('4', response.data['item_list'])

    def test_delete_item(self):
        response = self.client.post('/list/deleteItem', {'user_id': 1, 'list_id': self.list.list_id, 'item_id': '2'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotIn('2', response.data['item_list'])

    def test_delete_list(self):
        response = self.client.delete('/list/delete', {'user_id': 1, 'list_id': self.list.list_id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lists.objects.filter(list_id=self.list.list_id).exists())
