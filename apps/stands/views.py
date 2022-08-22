from rest_framework import permissions

from apps.core.permissions import IsOwnerOrReadOnly
from apps.core.viewset import AlmoxModelViewSet

from .models import Stand
from .serializers import StandDetailSerializer, StandSerializer


class StandViewSet(AlmoxModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """

    queryset = Stand.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "retrieve":
            return StandDetailSerializer

        return StandSerializer
