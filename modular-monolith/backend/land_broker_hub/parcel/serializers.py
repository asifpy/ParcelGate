from rest_flex_fields import FlexFieldsModelSerializer

from .models import Parcel

class ParcelSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'