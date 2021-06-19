from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from django.utils.translation import gettext_lazy as _


class Size(models.TextChoices):
    SMALL = 'S', _('Small')
    MEDIUM = 'M', _('Medium')
    LARGE = 'L', _('Large')
    EXTRA_LARGE = 'XL', _('Extra Large')
    HUGE = 'H', _('Huge')
    COLOSSAL = 'C', _('Colossal')


class StartingProfile(models.Model):
    strength = models.SmallIntegerField()
    toughness = models.SmallIntegerField()
    movement = models.SmallIntegerField()
    martial = models.SmallIntegerField()
    ranged = models.SmallIntegerField()
    defense = models.SmallIntegerField()
    discipline = models.SmallIntegerField()
    willpower = models.SmallIntegerField()
    command = models.SmallIntegerField()
    wounds = models.SmallIntegerField()
    attacks = models.SmallIntegerField()
    size = models.CharField(max_length=2, choices=Size.choices)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()
