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
        fields = ["id", "name", "is_business", "phone", "document", "stand", "user"]

    def get_user(self, person):
        return (
            {
                "id": person.user.id,
                "username": person.user.username,
                "email": person.user.email,
            }
            if person.user
            else None
        )


class ManagerSerializer(BaseSerializer):
    class Meta:
        model = Person
        exclude = ["stand"]
