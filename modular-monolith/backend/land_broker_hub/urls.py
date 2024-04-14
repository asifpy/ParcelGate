from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brokers/', include('land_broker_hub.broker.urls', namespace='broker')),
    path('parcels/', include('land_broker_hub.parcel.urls', namespace='parcel')),
    path('offers/', include('land_broker_hub.offer.urls', namespace='offer')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]