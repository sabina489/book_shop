from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import filters
from cart.models import Cart, CartItem

from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
)


from cart.api.serializers import (
    CartItemCreateSerializer,
    CartItemRetrieveSerializer,
    CartCreateSerializer,
    CartRetrieveSerializer,
    CartItemRetrieveSerializer,
)

class CartCreateAPIView(CreateAPIView):
    """View for creating a cart."""
    permission_classes = [IsAuthenticated]
    serializer_class = CartCreateSerializer
    queryset = Cart.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemCreateAPIView(CreateAPIView):
    """View for creating a cart item."""
    permission_classes = [AllowAny]
    serializer_class = CartItemCreateSerializer
    queryset = CartItem.objects.all()
    
class CartItemListAPIView(ListAPIView):
    """View for listing all cart items."""
    permission_classes = [AllowAny]
    serializer_class = CartItemRetrieveSerializer
    queryset = CartItem.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

class CartItemRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a cart item."""
    permission_classes = [AllowAny]
    serializer_class = CartItemRetrieveSerializer
    queryset = CartItem.objects.all()
    
class CartRetrieveAPIView(GenericAPIView):
    """View for retrieving a cart."""
    permission_classes = [AllowAny]
    serializer_class = CartRetrieveSerializer
    queryset = Cart.objects.all()

    def get_object(self):
        return self.get_queryset().get(user=self.request.user)
    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)
