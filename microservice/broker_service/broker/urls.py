from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('broker.core.urls', namespace='core')),
]