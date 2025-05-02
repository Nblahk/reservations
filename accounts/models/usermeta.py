# catalogue/models/usermeta.py
from django.db import models
from django.conf import settings

class UserMeta(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meta'
    )
    langue = models.CharField(max_length=2, choices=[
        ("fr", "Français"),
        ("en", "English"),
        ("nl", "Nederlands"),
    ], blank=True)

    def __str__(self):
        return f"{self.user.username} → {self.get_langue_display()}"
