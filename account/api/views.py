from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics,status,permissions,mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from account.models import User,Profile
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    GenericAPIView,
    ListAPIView,

)

from account.api.serializers import (
    ProfileCreateSerializer,
    ProfileRetrieveSerializer,
    RegisterSerializer,
    UserSerializer,
)

from multiprocessing import context
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from cart.models import Cart

class RegisterView(CreateAPIView):
    """Register a new user."""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    
    # user = None
    # access_token = None
    # token = None
    # authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':'Invalid data'})
        serializer.save()

        user = User.objects.get(username = request.data['username'])
        cart = Cart.objects.create(user = user)
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200,
        'payload': serializer.data,
        'refresh': str(refresh),
        # 'username': user.username,
        # 'email': user.email,
        # 'id': user.id,
        'access': str(refresh.access_token), 'message': 'Your data is saved'})

    # def get_object(self):
    #     username = self.request.data.get("username", None)
    #     return get_object_or_404(self.queryset, username=username)


class ProfileCreateAPIView(CreateAPIView):
    """View for creating a account."""
    # authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()

    

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class ProfileRetrieveAPIView(GenericAPIView):
    """View for retrieving a profile."""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        return Response({'status': 200, 'data': self.serializer_class(request.user).data})
        

    def get_queryset(self):
        print(self.queryset)
        return self.request.user

    # def get_object(self):
    #     profile = self.request.data.get("username", None)
    #     return get_object_or_404(self.queryset,user=profile)




# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email,
#             'username': user.username,
#         })

