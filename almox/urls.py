from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from measurement_units.views import MeasurementUnitViewSet
from persons.views import PersonViewSet
from products.views import ProductViewSet
from stands.views import StandViewSet
from transactions.views import TransactionViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"stands", StandViewSet)
router.register(r"users", UserViewSet)
router.register(r"persons", PersonViewSet)
router.register(r"products", ProductViewSet)
router.register(r"transactions", TransactionViewSet)
router.register(r"measurement-units", MeasurementUnitViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(router.urls)),
]
