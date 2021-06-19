from django.contrib.contenttypes.fields import GenericForeignKey, ContentType
from django.db import models
from core.models import Category


class CategorySlot(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min = models.SmallIntegerField()
    max = models.SmallIntegerField()
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey()

    def __str__(self):
        return f"{self.category.name}: {self.min}-{self.max}"
