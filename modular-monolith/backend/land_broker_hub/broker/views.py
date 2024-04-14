from django.http import Http404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Broker
from .serializers import BrokerSerializer

class BrokerListCreateAPIView(generics.ListCreateAPIView):
    """Factory Broker viewset for list and create endpoints.
    Configured filters are for `type` and `name` fields.
    Enabled pagination to return 10 objects per page
    """

    queryset = Broker.objects.all()
    serializer_class = BrokerSerializer
    filterset_fields = ['type', 'name']
    permission_classes = [IsAuthenticated]


class BrokerDetail(APIView):
    """Endpoint to return broker details for the given PK"""

    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Broker.objects.get(pk=pk)
        except Broker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BrokerSerializer(snippet)
        return Response(serializer.data)