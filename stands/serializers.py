from rest_framework import serializers

from stands.models import Stand


class StandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True, allow_blank=False)
    active = serializers.BooleanField(default=True)
    created_by = serializers.ReadOnlyField(source="created_by.username")
    updated_by = serializers.ReadOnlyField(source="updated_by.username")

    def create(self, validated_data):
        """
        Create and return a new `Stand` instance, given the validated data.
        """
        return Stand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Stand` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
