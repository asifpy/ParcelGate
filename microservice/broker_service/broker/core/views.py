from rest_framework import generics
from .models import Broker
from .serializers import BrokerSerializer

class BrokerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer

class BrokerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer