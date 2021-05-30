from django.db import models


class Ability(models.Model):
    """Ability to be choosed to creating a faction"""
    name = models.CharField(max_length=255,)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
