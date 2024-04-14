from rest_flex_fields import FlexFieldsModelSerializer

from .models import Offer
from ..broker.serializers import BrokerSerializer
from ..parcel.serializers import ParcelSerializer

class OfferSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'
        expandable_fields = {
          'parcels': (ParcelSerializer, {'many': True}),
          'broker': BrokerSerializer
        }