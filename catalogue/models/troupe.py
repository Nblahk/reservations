from django.db import models

class Troupe(models.Model):
    id       = models.BigAutoField(primary_key=True)
    name     = models.CharField(max_length=60, unique=True)
    logo_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "troupes"
