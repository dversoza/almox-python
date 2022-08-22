from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import MeasurementUnit
from .serializers import MeasurementUnitSerializer


class MeasurementUnitViewSet(AlmoxModelViewSet):
    """
    API endpoint that allows measurement units to be viewed or edited.
    """

    queryset = MeasurementUnit.objects.all()
    serializer_class = MeasurementUnitSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
