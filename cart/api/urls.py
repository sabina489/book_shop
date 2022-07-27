from django.urls import path

from cart.api.views import (
    CartItemCreateAPIView,
    CartItemListAPIView,
    CartCreateAPIView,
    CartRetrieveAPIView,
    CartItemRetrieveAPIView,
)

urlpatterns = [
    path("create/", CartCreateAPIView.as_view(), name="cart-create"),
    path("item/create/", CartItemCreateAPIView.as_view(), name='cart-item-create'),
    path("item/list/", CartItemListAPIView.as_view(), name='cart-item-list'),
    path("retrieve/", CartRetrieveAPIView.as_view(), name='cart-retrieve'),
    path("item/<int:pk>/", CartItemRetrieveAPIView.as_view(), name='cart-item-detail'),
]
