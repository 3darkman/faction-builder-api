from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=255)
    branch_of_life_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
