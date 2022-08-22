from rest_framework import serializers

from .models import Stand


class StandSerializer(serializers.ModelSerializer):
    manager = serializers.SerializerMethodField()

    class Meta:
        model = Stand
        fields = "__all__"
        depth = 1

    def get_manager(self, obj):
        # ignore stand attribute from manager to avoid circular reference
        from persons.serializers import ManagerSerializer

        return ManagerSerializer(obj.manager).data
