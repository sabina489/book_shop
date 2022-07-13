from django.urls import path

from cart.api.views import (
    CartItemCreateAPIView,
    CartItemListAPIView,
    CartCreateAPIView,
)

urlpatterns = [
    path("create/", CartCreateAPIView.as_view(), name="cart-create"),
    path("item/create/", CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path("item/list/", CartItemListAPIView.as_view(), name='cart-item-list'),
]
