from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.api_root),
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("stands/", include("stands.urls")),
    path("users/", include("users.urls")),
]
