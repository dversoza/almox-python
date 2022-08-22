from apps.measurement_units.views import MeasurementUnitViewSet
from apps.persons.views import PersonViewSet
from apps.products.views import ProductViewSet
from apps.stands.views import StandViewSet
from apps.transactions.views import TransactionViewSet
from apps.users.views import AlmoxAuthTokenView, UserViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

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
    path("api/auth/", AlmoxAuthTokenView.as_view(), name="api-token-auth"),
]
