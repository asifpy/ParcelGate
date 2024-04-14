from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Parcel
from .serializers import ParcelSerializer

class ParcelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

class ParcelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]