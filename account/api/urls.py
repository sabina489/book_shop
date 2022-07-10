from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from account.api.views import (
    ProfileCreateAPIView,
    RegisterView,
)

urlpatterns = [
    path("register/",RegisterView.as_view(), name = 'register'),
    path("create/", ProfileCreateAPIView.as_view(), name = 'profile-create'),
    path("login/",TokenObtainPairView.as_view(),name = 'token_obtain_pair'),
    path("login/refresh/",TokenRefreshView.as_view(),name = 'token_refresh'),
]
