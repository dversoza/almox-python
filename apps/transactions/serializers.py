from rest_framework import serializers

from apps.core.serializers import BaseSerializer
from apps.persons.serializers import PersonSerializer
from apps.products.serializers import ProductSerializer
from apps.stands.serializers import StandSerializer

from .models import Transaction, TransactionType


class TransactionTypeSerializer(BaseSerializer):
    default_from_stand = StandSerializer(read_only=True)
    default_to_stand = StandSerializer(read_only=True)

    class Meta:
        model = TransactionType
        fields = [
            "id",
            "operation",
            "name",
            "description",
            "default_from_stand",
            "default_to_stand",
        ]


class TransactionSerializer(BaseSerializer):
    person = PersonSerializer(read_only=True)
    person_id = serializers.IntegerField(write_only=True)

    from_stand = StandSerializer(read_only=True)
    from_stand_id = serializers.IntegerField(write_only=True)
    to_stand = StandSerializer(read_only=True)
    to_stand_id = serializers.IntegerField(write_only=True)

    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    type = TransactionTypeSerializer(read_only=True)
    type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction
        exclude = ["stand"]
