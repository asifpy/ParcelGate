from django.urls import reverse

from rest_framework import status

from .base import TestBaseAPIView
from ..parcel.models import Parcel
from ..broker.models import Broker
from ..offer.models import Offer
from ..offer.serializers import OfferSerializer

class TestOfferAPIView(TestBaseAPIView):

    def setUp(self):

        self.parcel = Parcel.objects.create(
            block_number="A1",
            neighbourhood="Example Neighbourhood",
            subdivision_number="S1",
            land_use_group="residential",
            description="A beautiful residential plot"
        )
        self.broker_data = {
            "name": "Broker 8",
            "type": "Individual",
            "phone_number": '888-888-8888',
            "email": "broker8@example.com",
            "bio": "Specializes in commercial real estate"
        }
        self.broker = Broker.objects.create(**self.broker_data)
        self.offer_data = {
            "title": "Offer 1",
            "description": "Offer description 1",
            "broker": self.broker.id,
            "parcels": [self.parcel.id],
            "price_per_meter": '1000.00'
        }
        
        return super().setUp()
    
    @property
    def create_offer(self):
        """Create offer record"""
        self.offer_data.pop("broker")
        self.offer_data.pop("parcels")
        self.offer = Offer(**self.offer_data)
        self.offer.broker = self.broker
        self.offer.save()
        self.offer.parcels.add(self.parcel)
        return self.offer

    def test_create_offer_failed(self):
        """Test create endpoint handles bad request"""

        self.offer_data.pop("broker")
        self.offer_data.pop("parcels")
        url = reverse('offer:offer-list')
        response = self.client.post(url, self.offer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_offer(self):
        """
        Ensure we can create a new offer object.
        """
        url = reverse('offer:offer-list')
        response = self.client.post(url, self.offer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 1)
        self.assertEqual(Offer.objects.get().title, 'Offer 1')
        self.assertEqual(Offer.objects.get().broker.name, 'Broker 8')
    
    def test_list_offers(self):
        """Test list of offers endpoint"""

        url = reverse('offer:offer-list')
        _ = self.create_offer
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['results'],
            OfferSerializer(Offer.objects.all(), many=True).data
        )
    
    def test_update_offer(self):
        """Test update offer endpoint"""

        offer = self.create_offer
        # update the offer fields
        self.offer_data['title'] = "Updated title"
        self.offer_data['broker'] = self.broker.id
        self.offer_data['parcels'] = [self.parcel.id]

        url = reverse('offer:offer-detail', args=[offer.id])
        response = self.client.put(url, self.offer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated title")

    def test_details_offer(self):
        """Test offer details endpoint"""
        offer = self.create_offer
        url = reverse('offer:offer-detail', args=[offer.id])
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OfferSerializer(offer).data)


