from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Transaction, TransactionType
from .serializers import TransactionSerializer, TransactionTypeSerializer


class TransactionViewSet(AlmoxModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransactionTypeViewSet(AlmoxModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
