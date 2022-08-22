from rest_framework import serializers

from .models import Stand


class StandSerializer(serializers.ModelSerializer):
    manager = serializers.SerializerMethodField()

    class Meta:
        model = Stand
        fields = "__all__"
        depth = 1

    def get_manager(self, stand):
        # ignore stand attribute from manager to avoid circular reference
        from apps.persons.serializers import ManagerSerializer

        return ManagerSerializer(stand.manager).data


class StandDetailSerializer(StandSerializer):
    stock = serializers.SerializerMethodField()

    def get_stock(self, stand):
        return stand.transaction_set.get_stock_for_stand(stand=stand)
