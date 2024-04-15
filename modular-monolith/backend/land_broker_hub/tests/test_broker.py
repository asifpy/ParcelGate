from django.urls import reverse

from rest_framework import status

from .base import TestBaseAPIView
from ..broker.models import Broker
from ..broker.serializers import BrokerSerializer

class TestBrokerAPIView(TestBaseAPIView):

    def setUp(self):
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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'], "Broker 8")
        self.assertEqual(
            response.data['results'],
            BrokerSerializer(Broker.objects.all(), many=True).data
        )
    
    def test_details_broker(self):
        """Test broker details endpoint"""
        broker = Broker.objects.create(**self.data)
        url = reverse('broker:broker-detail', args=[broker.id])
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, BrokerSerializer(broker).data)


