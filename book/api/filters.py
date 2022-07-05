# from rest_framework import generics
# from django_filters import rest_framework as filters


# from book.models import Book

# class BookFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

#     class Meta:
#         model = Book
#         fields = {"price": ["gt", "lt"], "category": ["exact"], "title": ["icontains"]}

import django_filters
from book.models import Book    

class BookFilter(django_filters.FilterSet):
    """Filter for courses."""

    class Meta:
        model = Book
        fields = {"price": ["gt", "lt"], "category": ["exact"], "title": ["icontains"]}