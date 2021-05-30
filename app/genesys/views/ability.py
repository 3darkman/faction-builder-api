from rest_framework import viewsets

from genesys import serializers
from core.models import Ability


class AbilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ability.objects.all()
    serializer_class = serializers.AbilitySerializer
