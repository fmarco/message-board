from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from .views import MessageViewSet
import json


class MessageViewSetTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='user@foo.com', email='user@foo.com', password='top_secret')
        self.token = Token.objects.get(user=self.user)


    def test_token_auth(self):
        request = self.factory.get('/messages')
        force_authenticate(request, user=self.user, token=self.token)
        view = MessageViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.render().content)


    def test_message_creation(self):
        request = self.factory.post('/messages/', json.dumps({'message': 'hello!'}), content_type='application/json')
        force_authenticate(request, user=self.user, token=self.token)
        view = MessageViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.render().content)
        self.assertIn('message', json_response)
        self.assertEqual(json_response['message'], 'hello!')