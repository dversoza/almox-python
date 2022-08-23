from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers

from apps.core.serializers import BaseSerializer
from apps.stands.serializers import StandSerializer

from .models import Person


class PersonSerializer(BaseSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
    stand = StandSerializer(read_only=True)

    class Meta:
        model = Person
        fields = ["id", "name", "is_business", "phone", "document", "stand", "user_id"]


class ManagerSerializer(BaseSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "is_business", "phone", "document"]
