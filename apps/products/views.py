from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import MeasurementUnit, Product
from .serializers import MeasurementUnitSerializer, ProductSerializer


class MeasurementUnitViewSet(AlmoxModelViewSet):
    """
    API endpoint that allows measurement units to be viewed or edited.
    """

    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(AlmoxModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
