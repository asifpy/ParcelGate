from django.urls import path
from .views import BrokerListCreateAPIView, BrokerRetrieveUpdateDestroyAPIView

app_name = 'core'

urlpatterns = [
    path('brokers/', BrokerListCreateAPIView.as_view(), name='broker-list'),
    path('brokers/<int:pk>/', BrokerRetrieveUpdateDestroyAPIView.as_view(), name='broker-detail')
]