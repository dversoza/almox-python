from rest_framework import permissions

from apps.core.permissions import IsOwnerOrReadOnly
from apps.core.viewset import AlmoxModelViewSet

from .models import Stand
from .serializers import StandSerializer


class StandViewSet(AlmoxModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """

    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
