from django.urls import path
from .views import OfferListCreateAPIView, OfferRetrieveUpdateDestroyAPIView

app_name = 'offer'

urlpatterns = [
    path('', OfferListCreateAPIView.as_view(), name='offer-list'),
    path('<int:pk>/', OfferRetrieveUpdateDestroyAPIView.as_view(), name='offer-detail')
]