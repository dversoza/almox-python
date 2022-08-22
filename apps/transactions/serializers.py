from rest_framework import serializers

from apps.persons.serializers import PersonSerializer
from apps.products.serializers import ProductSerializer
from apps.stands.serializers import StandSerializer

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    stand = StandSerializer()
    product = ProductSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
