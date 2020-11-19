from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient

class UserTestCase(TestCase):
  def setUp(self):
    self.credentials = {
        'username': 'testUser',
        'password': 'testpassword'}
    User.objects.create_user(**self.credentials)
    self.token = ''

  def test_get_token(self):
    c = self.client
    response = c.post('/api/token-auth/' , self.credentials)
    self.token = response.data['token']
    self.assertTrue('token' in response.data)

  def test_verify_token(self):
    c = self.client
    header = {
      'Authorization': 'JWT {}'.format(self.token)
    }
    response = c.post('/api/token-verify/' ,data = {'token': self.token}, **header)
    print(response.data)
    # self.assertTrue('token' in response.data)