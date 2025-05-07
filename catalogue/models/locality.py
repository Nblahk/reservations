from django.db import models

class Locality(models.Model):
    postal_code = models.CharField(max_length=6)
    locality    = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.postal_code} {self.locality}"

    class Meta:
        db_table = "localities"
