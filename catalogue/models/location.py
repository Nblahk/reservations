from django.db import models
from .locality import Locality

class Location(models.Model):
    slug        = models.CharField(max_length=60, unique=True)
    designation = models.CharField(max_length=255)
    address     = models.CharField(max_length=255, blank=True)
    locality    = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='locations')
    website     = models.URLField(max_length=200, blank=True, null=True)
    phone       = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.designation

    class Meta:
        db_table = 'locations'
        constraints = [
            models.UniqueConstraint(fields=['slug', 'website'], name='unique_slug_website'),
        ]