from rest_framework import generics, permissions

from almox.permissions import IsOwnerOrReadOnly
from stands.models import Stand
from stands.serializers import StandSerializer


class StandList(generics.ListCreateAPIView):
    """
    List all stands, or create a new stand.
    """

    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class StandDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a stand instance.
    """

    queryset = Stand.objects.all()
    serializer_class = StandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
