from django.db import models

class Broker(models.Model):
    """Model to capture Broker related fields"""

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-id']

