from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "name", "description", "measurement_unit", "stock"]

    def get_stock(self, product):
        return product.transaction_set.get_stock(product=product)
