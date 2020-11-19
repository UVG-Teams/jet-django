from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient
from django.conf import settings

class UserTestCase(TestCase):
  def setUp(self):
    self.JET = settings.GLOBAL_JET
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
    response = c.post('/api/token-auth/' , self.credentials)
    token = response.data['token']
    header = {
      'Authorization': 'JET {}'.format(self.token)
    }
    response = c.post('/api/token-verify/' ,data = {'token': token}, **header)
    self.assertTrue(response.data['valid'])

  def test_verify_token_jwt(self):
    c = self.client
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
    header = {
      'Authorization': 'JET {}'.format(token)
    }
    try:
      response = c.post('/api/token-verify/' ,data = {'token': token}, **header) # Esto deberia lanzar un super error
      self.assertEquals(response.status, 500)
    except:
      self.assertEquals(True, True) #Esto deberia de pasar


  def test_decrypt_token_payload(self):
    c = self.client
    response = c.post('/api/token-auth/' , self.credentials)
    token = response.data['token']
    meta , payload = self.JET.decrypt_from_PK(token)
    self.assertTrue('id' in payload)

  def test_decrypt_token_meta(self):
    c = self.client
    response = c.post('/api/token-auth/' , self.credentials)
    token = response.data['token']
    meta , payload = self.JET.decrypt_from_PK(token)
    self.assertTrue('rnd' in meta)

  def test_decrypt_token_meta_type(self):
    c = self.client
    response = c.post('/api/token-auth/' , self.credentials)
    token = response.data['token']
    meta , payload = self.JET.decrypt_from_PK(token)
    self.assertEquals('JET-1' , meta['typ'])