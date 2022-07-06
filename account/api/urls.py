from django.urls import path

from account.api.views import (
    ProfileCreateAPIView,
    ProfileListAPIView,
    ProfileRetrieveAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
)

urlpatterns = [
    path("create/", ProfileCreateAPIView.as_view(), name="account-create"),
    path("list/", ProfileListAPIView.as_view(), name="account-list"),
    path("profile<int:pk>/", ProfileRetrieveAPIView.as_view(), name="account-retrieve"),
    path("profile<int:pk>/update/", ProfileUpdateAPIView.as_view(), name="account-update"),
    path("profile<int:pk>/delete/", ProfileDeleteAPIView.as_view(), name="account-delete"),
]
