from django.db import models

class Parcel(models.Model):
    """Model to capture Parcel related fields"""

    LAND_USE_CHOICES = [
        ('agricultural', 'Agricultural'),
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
    ]

    block_number = models.CharField(max_length=50)
    neighbourhood = models.CharField(max_length=100)
    subdivision_number = models.CharField(max_length=50)
    land_use_group = models.CharField(max_length=50, choices=LAND_USE_CHOICES)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.block_number} - {self.subdivision_number} ({self.neighbourhood})"
