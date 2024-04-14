from django.db import models

from ..broker.models import Broker
from ..parcel.models import Parcel

class Offer(models.Model):
    """Model to capture Offer related fields"""

    title = models.CharField(max_length=100)
    description = models.TextField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE)
    parcels = models.ManyToManyField(Parcel)
    price_per_meter = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
