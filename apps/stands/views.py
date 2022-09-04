from rest_framework import permissions

from apps.core.permissions import IsOwnerOrReadOnly
from apps.core.viewset import AlmoxModelViewSet

from .models import Stand
from .serializers import StandDetailSerializer, StandSerializer


class StandViewSet(AlmoxModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "retrieve":
            return StandDetailSerializer

        return StandSerializer

    def get_queryset(self):
        queryset = Stand.objects.all()

        query = self.request.query_params.get("query")
        if query:
            queryset = queryset.filter(name__icontains=query)

        return queryset
