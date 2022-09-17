from django.db.models import Q
from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Transaction, TransactionType
from .serializers import TransactionSerializer, TransactionTypeSerializer


class TransactionViewSet(AlmoxModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Transaction.objects.all()

        query = self.request.query_params.get("query")
        if query:
            queryset = queryset.filter(
                Q(product__name__icontains=query)
                | Q(person__name__icontains=query)
                | Q(stand__name__icontains=query)
                | Q(type__name__icontains=query)
                | Q(details__icontains=query)
            )

        year = self.request.query_params.get("year")
        if year:
            queryset = queryset.filter(datetime__year=year)

        return queryset


class TransactionTypeViewSet(AlmoxModelViewSet):
    serializer_class = TransactionTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = TransactionType.objects.all()

        query = self.request.query_params.get("query", None)
        if query is not None:
            queryset = queryset.filter(name__icontains=query)

        return queryset
