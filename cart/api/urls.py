from django.urls import path

from cart.api.views import (
    CartItemCreateAPIView,
    CartCreateAPIView,
)

urlpatterns = [
    path("create/", CartCreateAPIView.as_view(), name="cart-create"),
    path("item/create/", CartItemCreateAPIView.as_view(), name='cart-item-create'),
]
