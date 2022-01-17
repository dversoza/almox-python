from rest_framework import viewsets, permissions

from measurement_units.models import MeasurementUnit
from measurement_units.serializers import MeasurementUnitSerializer


class MeasurementUnitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows measurement units to be viewed or edited.
    """

    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
