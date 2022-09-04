from rest_framework import serializers

from apps.core.serializers import BaseSerializer

from .models import Stand


class StandSerializer(BaseSerializer):
    manager = serializers.SerializerMethodField()
    manager_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Stand
        fields = "__all__"
        depth = 1

    def get_manager(self, stand):
        return (
            {
                "id": stand.manager.id,
                "name": stand.manager.name,
            }
            if stand.manager
            else None
        )


class StandDetailSerializer(StandSerializer):
    stock = serializers.SerializerMethodField()

    def get_stock(self, stand):
        return stand.transaction_set.get_stock_for_stand_grouped_by_product(stand=stand)
