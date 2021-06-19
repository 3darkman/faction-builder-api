from django.db import models

from core.models import FactionType, User


class Faction(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='factions', blank=True, null=True)
    type = models.ForeignKey(FactionType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
