from rest_framework import permissions

from django.db.models import Q

from apps.core.viewset import AlmoxModelViewSet

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(AlmoxModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """

    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Person.objects.all()

        query = self.request.query_params.get("query")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(stand__name__icontains=query)
            )

        return queryset
