from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from core.models import Domain, CategorySlot, StartingProfile


class FactionType(models.Model):
    name = models.CharField(max_length=250)
    is_default = models.BooleanField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    age = models.SmallIntegerField()

    slots = GenericRelation(CategorySlot)
    starting_profile = GenericRelation(StartingProfile)

    def __str__(self):
        return self.name
