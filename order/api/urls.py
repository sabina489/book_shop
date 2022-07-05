from django.urls import path

from order.api.views import (
    OrderDetailCreateAPIView,
    OrderDetailListAPIView,
    OrderDetailRetrieveAPIView,
    OrderDetailUpdateAPIView,
    OrderDetailDeleteAPIView,
    OrderItemCreateAPIView,
    OrderItemRetrieveAPIView,
    OrderItemUpdateAPIView,
    OrderItemDeleteAPIView,
    OrderItemListAPIView,
)

urlpatterns = [
    path("create/", OrderDetailCreateAPIView.as_view(), name="order-detail-create"),
    path("list/", OrderDetailListAPIView.as_view(), name="order-detail-list"),
    path("<int:pk>/", OrderDetailRetrieveAPIView.as_view(), name="order-detail-retrieve"),
    path("<int:pk>/update/", OrderDetailUpdateAPIView.as_view(), name="order-detail-update"),
    path("<int:pk>/delete/", OrderDetailDeleteAPIView.as_view(), name="order-detail-delete"),
    path("item/create/", OrderItemCreateAPIView.as_view(), name="order-item-create"),
    path("item/list", OrderItemListAPIView.as_view(), name="order-item-list"),
    path("item/<int:pk>/", OrderItemRetrieveAPIView.as_view(), name="order-item-retrieve"),
    path("item/<int:pk>/update/", OrderItemUpdateAPIView.as_view(), name="order-item-update"),
    path("item/<int:pk>/delete/", OrderItemDeleteAPIView.as_view(), name="order-item-delete"),

]
