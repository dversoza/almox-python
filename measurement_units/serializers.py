from rest_framework import serializers

from measurement_units.models import MeasurementUnit


class MeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementUnit
        fields = ["id", "name", "abbreviation"]
