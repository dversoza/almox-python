from rest_framework import serializers

from measurement_units.serializers import MeasurementUnitSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    measurement_unit = MeasurementUnitSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "measurement_unit"]
