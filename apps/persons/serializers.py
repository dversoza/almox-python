from apps.core.serializers import BaseSerializer
from apps.stands.serializers import StandSerializer
from rest_framework import serializers

from .models import Person


class PersonSerializer(BaseSerializer):
    user = serializers.SerializerMethodField()
    stand = StandSerializer(read_only=True)
    stand_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Person
        fields = [
            "id",
            "name",
            "is_business",
            "phone",
            "document",
            "user",
            "stand",
            "stand_id",
        ]

    def get_user(self, person):
        if person.user:
            return {
                "id": person.user.id,
                "username": person.user.username,
                "email": person.user.email,
            }
        return None


class ManagerSerializer(BaseSerializer):
    class Meta:
        model = Person
        exclude = ["stand"]
