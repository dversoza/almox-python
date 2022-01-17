from rest_framework import permissions, viewsets

from almox.permissions import IsOwnerOrReadOnly
from stands.models import Stand
from stands.serializers import StandSerializer


class StandViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """

    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
