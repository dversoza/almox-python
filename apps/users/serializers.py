from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "is_staff",
            "groups",
            "person",
        ]

    def get_person(self, user):
        try:
            return {
                "id": user.person.id,
                "name": user.person.name,
            }
        except User.person.RelatedObjectDoesNotExist:
            return {
                "id": None,
                "name": user.first_name,
            }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]
