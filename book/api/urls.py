from django.urls import path

from book.api.views import (
    BookCreateAPIView,
    BookListAPIView,
    BookRetrieveAPIView,
    BookUpdateAPIView,
    BookDeleteAPIView,

    BookCategoryCreateAPIView,
    BookCategoryRetrieveAPIView,
    BookCategoryUpdateAPIView,
    BookCategoryListAPIView,
    BookCategoryDeleteAPIView,

    BookInventoryCreateAPIView,
    BookInventoryRetrieveAPIView,
    BookInventoryUpdateAPIView,
    BookInventoryListAPIView,
    BookInventoryDeleteAPIView,

    CreateCheckoutSessionView,
    ProductLandingPageView,

)

urlpatterns = [
    path("create/", BookCreateAPIView.as_view(), name='book-create'),
    path("list/", BookListAPIView.as_view(), name='book-list'),
    path("book<int:pk>/", BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path("book<int:pk>/update/", BookUpdateAPIView.as_view(), name='book-update'),
    path("book<int:pk>/delete/", BookDeleteAPIView.as_view(), name='book-delete'),

    path("category/create/", BookCategoryCreateAPIView.as_view(), name='book-category-create'),
    path("category/list/", BookCategoryListAPIView.as_view(), name='book-category-list'),
    path("category/<int:pk>/", BookCategoryRetrieveAPIView.as_view(), name='book-category-retrieve'),
    path("category/<int:pk>/update/", BookCategoryUpdateAPIView.as_view(), name='book-category-update'),
    path("category/<int:pk>/delete/", BookCategoryDeleteAPIView.as_view(), name='book-category-delete'),

    path("book/inventory/create/", BookInventoryCreateAPIView.as_view(), name='book-inventory-create'),
    path("book/inventory/list/", BookInventoryListAPIView.as_view(), name='book-inventory-list'),
    path("book/inventory/<int:pk>/", BookInventoryRetrieveAPIView.as_view(), name='book-inventory-retrieve'),
    path("book/inventory/<int:pk>/update/", BookInventoryUpdateAPIView.as_view(), name='book-inventory-update'),
    path("book/inventory/<int:pk>/delete/", BookInventoryDeleteAPIView.as_view(), name='book-inventory-delete'),

    path("book/checkout/create/", CreateCheckoutSessionView.as_view(), name='book-checkout-create'),
    path("product/", ProductLandingPageView.as_view(), name='product-landing-page'),
]

    