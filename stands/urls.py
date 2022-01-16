from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from stands import views

urlpatterns = [
    path("", views.StandList.as_view(), name="stand-list"),
    path("<int:pk>/", views.StandDetail.as_view(), name="stand-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
