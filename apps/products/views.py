from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(AlmoxModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
