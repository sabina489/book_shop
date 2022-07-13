from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from cart.models import Cart, CartItem

from rest_framework.permissions import AllowAny,IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from cart.api.serializers import (
    CartItemCreateSerializer,
    CartItemRetrieveSerializer,
    CartCreateSerializer,
)

class CartCreateAPIView(CreateAPIView):
    """View for creating a cart."""
    permission_classes = [AllowAny]
    serializer_class = CartCreateSerializer
    queryset = Cart.objects.all()

class CartItemCreateAPIView(CreateAPIView):
    """View for creating a cart item."""
    permission_classes = [AllowAny]
    serializer_class = CartItemCreateSerializer
    queryset = CartItem.objects.all()
    def perform_create(self, serializer):
        serializer.save(cart=self.request.user.cart)

class CartItemListAPIView(ListAPIView):
    """View for listing all cart items."""
    permission_classes = [AllowAny]
    serializer_class = CartItemRetrieveSerializer
    queryset = CartItem.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]