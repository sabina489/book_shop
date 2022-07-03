import django_filters

from book.models import Book

class Book(django_filters.FilterSet):
    """Filter for book."""

    class Meta:
        model = Book
        fields = {"title": ["icontains"]}