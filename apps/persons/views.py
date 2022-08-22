from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(AlmoxModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
