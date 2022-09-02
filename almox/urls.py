from apps.persons.views import PersonViewSet
from apps.products.views import MeasurementUnitViewSet, ProductViewSet
from apps.stands.views import StandViewSet
from apps.transactions.views import TransactionTypeViewSet, TransactionViewSet
from apps.users.views import AlmoxAuthTokenView, UserViewSet
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"stands", StandViewSet, basename="stands")
router.register(r"users", UserViewSet, basename="users")
router.register(r"persons", PersonViewSet, basename="persons")
router.register(r"products", ProductViewSet, basename="products")
router.register(r"transactions", TransactionViewSet, basename="transactions")
router.register(
    r"transaction-types", TransactionTypeViewSet, basename="transaction-types"
)
router.register(
    r"measurement-units", MeasurementUnitViewSet, basename="measurement-units"
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/", include(router.urls)),
    path("api/auth/", AlmoxAuthTokenView.as_view(), name="api-token-auth"),
]
