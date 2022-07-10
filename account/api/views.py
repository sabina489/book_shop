# import imp
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics,status,permissions,mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from account.models import User,Profile
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import (
    CreateAPIView,

)


from account.api.serializers import (
    ProfileCreateSerializer,
    RegisterSerializer,
)

from multiprocessing import context
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(CreateAPIView):
    """Register a new user."""
    serializer_class = RegisterSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':'Invalid data'})
        serializer.save()

        user = User.objects.get(username = request.data['username'])
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200,
        'payload': serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token), 'message': 'Your data is saved'})



class ProfileCreateAPIView(CreateAPIView):
    """View for creating a account."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()

    

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }