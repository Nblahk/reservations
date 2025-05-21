# catalogue/models/show.py
from django.db import models
from django.utils import timezone
from .location import Location

class Show(models.Model):
    slug         = models.CharField(max_length=60, unique=True)
    title        = models.CharField(max_length=191)
    description  = models.TextField(max_length=191, null=True, blank=True)
    poster_url   = models.CharField(max_length=191, null=True, blank=True)
    duration     = models.PositiveSmallIntegerField(null=True, blank=True)
    # on le déclare sans auto_now_add
    created_in = models.DateField(auto_now_add=True)
    location   = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='shows')
    bookable     = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # si c'est une création (pas de pk encore) et que created_in n'est pas fourni,
        # on le fixe à l'année actuelle
        if not self.pk and not self.created_in:
            self.created_in = timezone.now().year
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "shows"
