from rest_framework import viewsets, permissions

from persons.models import Person
from persons.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
