from rest_framework import permissions

from apps.core.viewset import AlmoxModelViewSet

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(AlmoxModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
