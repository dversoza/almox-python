from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path("", views.UserList.as_view(), name="user-list"),
    path("<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("groups/", views.GroupList.as_view(), name="group-list"),
    path("groups/<int:pk>/", views.GroupDetail.as_view(), name="group-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
