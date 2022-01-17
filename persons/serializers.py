from rest_framework import serializers

from persons.models import Person
from stands.serializers import StandSerializer
from users.serializers import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    stand = StandSerializer()

    class Meta:
        model = Person
        fields = ["id", "name", "is_business", "phone", "document", "stand", "user"]
