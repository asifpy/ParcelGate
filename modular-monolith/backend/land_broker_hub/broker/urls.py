from django.urls import path
from .views import BrokerListCreateAPIView, BrokerDetail

app_name = 'broker'

urlpatterns = [
    path('', BrokerListCreateAPIView.as_view(), name='broker-list'),
    path('<int:pk>/', BrokerDetail.as_view(), name='broker-detail')
]