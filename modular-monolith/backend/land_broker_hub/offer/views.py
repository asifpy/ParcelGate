from rest_framework import generics
from rest_flex_fields import is_expanded
from rest_framework.permissions import IsAuthenticated

from .models import Offer
from .serializers import OfferSerializer

class OfferListCreateAPIView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filterset_fields = ['broker__type', 'broker__name']
    permit_list_expands = ['parcels', 'broker']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Offer.objects.all()
        if is_expanded(self.request, 'broker'):
            queryset = queryset.select_related('broker')
        if is_expanded(self.request, 'parcels'):
            queryset = queryset.prefetch_related('parcels')
        return queryset

class OfferRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]