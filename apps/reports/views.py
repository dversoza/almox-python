import codecs
import csv

from django.http import HttpResponse
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.views import APIView

from apps.products.models import Product
from apps.stands.models import Stand


class ExportCSVProducts(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Produtos.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(
            response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL
        )

        headers = ["ID", "Produto", "Unidade de Medida"]

        writer.writerow(headers)

        products = Product.objects.filter(active=True).order_by("name")

        for product in products:
            writer.writerow([product.id, product.name, product.measurement_unit.name])

        return response


class ExportCSVStands(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication,
    ]

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Barracas.csv"'
        response.write(codecs.BOM_UTF8)

        writer = csv.writer(
            response, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL
        )

        headers = ["ID", "Barraca", "Responsável", "Contato"]

        writer.writerow(headers)

        stands = Stand.objects.filter(active=True).order_by("name")

        for stand in stands:
            writer.writerow([stand.id, stand.name, stand.manager.name, stand.contact])

        return response
