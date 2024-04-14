from django.urls import path
from .views import ParcelListCreateAPIView, ParcelRetrieveUpdateDestroyAPIView

app_name = 'parcel'

urlpatterns = [
    path('', ParcelListCreateAPIView.as_view(), name='parcel-list'),
    path('<int:pk>/', ParcelRetrieveUpdateDestroyAPIView.as_view(), name='parcel-detail')
]