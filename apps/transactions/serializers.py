from apps.core.serializers import BaseSerializer
from apps.persons.serializers import PersonSerializer
from apps.products.serializers import ProductSerializer
from apps.stands.serializers import StandSerializer

from .models import Transaction, TransactionType


class TransactionTypeSerializer(BaseSerializer):
    class Meta:
        model = TransactionType
        fields = ["id", "name", "description"]


class TransactionSerializer(BaseSerializer):
    person = PersonSerializer()
    stand = StandSerializer()
    product = ProductSerializer()
    type = TransactionTypeSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
