from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from rest_framework.permissions import AllowAny, IsAuthenticated
from order.models import Order_Detail, Order_Items

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from order.api.serializers import (
    OrderDetailCreateSerialier,
    OrderDetailRetrieveSerialier,
    OrderDetailUpdateSerialier, 
    OrderDetailDeleteSerialier,
    OrderItemCreateSerialier,
    OrderItemRetrieveSerialier,
    OrderItemUpdateSerialier,
    OrderItemDeleteSerialier,
)



class OrderDetailCreateAPIView(CreateAPIView):
    """View for creating a order_detail."""
    permission_classes = [AllowAny]
    serializer_class = OrderDetailCreateSerialier
    queryset = Order_Detail.objects.all()

class OrderDetailListAPIView(ListAPIView):
    """View for listing all order_details."""
    permission_classes = [AllowAny]
    serializer_class = OrderDetailRetrieveSerialier
    queryset = Order_Detail.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    
class OrderDetailRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a order_detail."""
    permission_classes = [AllowAny]
    serializer_class = OrderDetailRetrieveSerialier
    queryset = Order_Detail.objects.all()

class OrderDetailUpdateAPIView(UpdateAPIView):
    """View for updating a order_detail."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailUpdateSerialier
    queryset = Order_Detail.objects.all()


class OrderDetailDeleteAPIView(DestroyAPIView):
    """View for deleting a order_detail."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderDetailDeleteSerialier
    queryset = Order_Detail.objects.all()

class OrderItemCreateAPIView(CreateAPIView):
    """View for creating a order_item."""
    permission_classes = [AllowAny]
    serializer_class = OrderItemCreateSerialier
    queryset = Order_Items.objects.all()

class OrderItemListAPIView(ListAPIView):
    """View for listing all order_items."""
    permission_classes = [AllowAny]
    serializer_class = OrderItemRetrieveSerialier
    queryset = Order_Items.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

class OrderItemRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a order_item."""
    permission_classes = [AllowAny]
    serializer_class = OrderItemRetrieveSerialier
    queryset = Order_Items.objects.all()

class OrderItemUpdateAPIView(UpdateAPIView):
    """View for updating a order_item."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemUpdateSerialier
    queryset = Order_Items.objects.all()

class OrderItemDeleteAPIView(DestroyAPIView):
    """View for deleting a order_item."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderItemDeleteSerialier
    queryset = Order_Items.objects.all()