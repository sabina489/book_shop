from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from account.models import Profile

from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from account.api.serializers import (
    ProfileCreateSerializer,
    ProfileRetrieveSerializer,
    ProfileUpdateSerializer,
    ProfileDeleteSerializer,
)

class ProfileCreateAPIView(CreateAPIView):
    """View for creating a profile."""
    permission_classes = [AllowAny]
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileListAPIView(ListAPIView):
    """View for listing all profiles."""
    permission_classes = [AllowAny]
    serializer_class = ProfileRetrieveSerializer
    queryset = Profile.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

class ProfileRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a profile."""
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileRetrieveSerializer
    queryset = Profile.objects.all()

class ProfileUpdateAPIView(UpdateAPIView):
    """View for updating a profile."""
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()

class ProfileDeleteAPIView(DestroyAPIView):
    """View for deleting a profile."""
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileDeleteSerializer
    queryset = Profile.objects.all()