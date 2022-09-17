from django.views import View
from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import MeasurementUnit, Product
from .serializers import (
    MeasurementUnitSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)


class MeasurementUnitViewSet(AlmoxModelViewSet):
    """
    API endpoint that allows measurement units to be viewed or edited.
    """

    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(AlmoxModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "retrieve":
            return ProductDetailSerializer

        return ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)

        query = self.request.query_params.get("query")
        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset

    def perform_destroy(self, instance):
        instance.active = False
        instance.save()
