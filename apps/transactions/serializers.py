from rest_framework import serializers

from apps.core.serializers import BaseSerializer
from apps.persons.serializers import PersonSerializer
from apps.products.serializers import ProductSerializer
from apps.stands.serializers import StandSerializer

from .models import Transaction, TransactionType


class TransactionTypeSerializer(BaseSerializer):
    class Meta:
        model = TransactionType
        fields = ["id", "operation", "name", "description"]


class TransactionSerializer(BaseSerializer):
    person = PersonSerializer(read_only=True)
    person_id = serializers.IntegerField(write_only=True)

    stand = StandSerializer(read_only=True)
    stand_id = serializers.IntegerField(write_only=True)

    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    type = TransactionTypeSerializer(read_only=True)
    type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"
