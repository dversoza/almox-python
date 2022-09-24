from datetime import datetime

from django.db.models import Q
from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Transaction, TransactionType
from .serializers import TransactionSerializer, TransactionTypeSerializer


class TransactionViewSet(AlmoxModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Transaction.objects.all()

        query = self.request.query_params.get("query")
        if query:
            queryset = queryset.filter(
                Q(product__name__icontains=query)
                | Q(person__name__icontains=query)
                | Q(from_stand__name__icontains=query)
                | Q(to_stand__name__icontains=query)
                | Q(type__name__icontains=query)
                | Q(details__icontains=query)
            )

        transaction_type = self.request.query_params.get("type")
        if transaction_type:
            queryset = queryset.filter(type__id=transaction_type)

        start_date = self.request.query_params.get("start_date")
        if start_date:
            start_date = datetime.fromisoformat(start_date)
            queryset = queryset.filter(datetime__gte=start_date)

        end_date = self.request.query_params.get("end_date")
        if end_date:
            end_date = datetime.fromisoformat(end_date)
            queryset = queryset.filter(datetime__lte=end_date)

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
