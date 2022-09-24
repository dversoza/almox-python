from django.urls import path

from apps.reports.views import ExportCSVStands, ExportCSVProducts, ExportStockCSV


urlpatterns = [
    path("products/", ExportCSVProducts.as_view(), name="products-report"),
    path("stands/", ExportCSVStands.as_view(), name="stands-report"),
    path("stock/", ExportStockCSV.as_view(), name="transactions-report"),
]
