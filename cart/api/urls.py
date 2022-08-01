from django.urls import path

from cart.api.views import (
    CartItemCreateAPIView,
    CartItemListAPIView,
    CartCreateAPIView,
    CartRetrieveAPIView,
    CartItemRetrieveAPIView,
    CartItemDeleteAPIView,
)

urlpatterns = [
    path("create/", CartCreateAPIView.as_view(), name="cart-create"),
    path("retrieve/", CartRetrieveAPIView.as_view(), name="cart-retrieve"),
    path("item/create/", CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path("item/list/", CartItemListAPIView.as_view(), name='cart-item-list'),
    path("item/retrieve/<int:pk>", CartItemRetrieveAPIView.as_view(), name='cart-item-retrieve'),
    path("item/delete/<int:pk>", CartItemDeleteAPIView.as_view(), name='cart-item-delete'),
]
