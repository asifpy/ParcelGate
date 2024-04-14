import uuid
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ..broker.models import Broker

class TestBrokerAPIView(APITestCase):

    def setUp(self):
        # handle auth
        fake_email = f"{str(uuid.uuid4())}@email.com"
        self.user = User.objects.create(
            email=str(uuid.uuid4()),
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

        self.data = {
            "name": "Broker 8",
            "type": "Individual",
            "phone_number": '888-888-8888',
            "email": "broker8@example.com",
            "bio": "Specializes in commercial real estate"
        }
        
        return super().setUp()

    def test_create_broker(self):
        """
        Ensure we can create a new broker object.
        """
        url = reverse('broker:broker-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Broker.objects.count(), 1)
        self.assertEqual(Broker.objects.get().name, 'Broker 8')
    
    def test_list_brokers(self):
        """Test list of brokers endpoint"""

        url = reverse('broker:broker-list')
        Broker.objects.create(**self.data)
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], "Broker 8")
    
    def test_details_broker(self):
        """Test broker details endpoint"""
        
