from rest_flex_fields import FlexFieldsModelSerializer

from .models import Broker

class BrokerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Broker
        fields = '__all__'