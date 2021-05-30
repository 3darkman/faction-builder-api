from rest_framework import generics

from core.models import Category
from genesys import serializers


class TraitListView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        queryset = None
        domain = self.request.query_params.get('domain')
        category = self.request.query_params.get('category')

        if domain is not None:
            queryset = Category.objects.filter(domain__id=domain)
        if category is not None:
            queryset = Category.objects.filter(id=category)
        if queryset is None:
            queryset = Category.objects.filter(tn_parent__isnull=True)
        return queryset
