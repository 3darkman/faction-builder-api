from rest_framework import serializers

from core import models


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ability
        fields = '__all__'
