from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    # overrides created_by and updated_by fields to display only user email keeping the rest of the fields intact
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.email

    def get_updated_by(self, obj):
        return obj.updated_by.email
