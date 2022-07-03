from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from book.models import Book, BookCategory, BookInventory, User
from rest_framework import generics
from book.api.serializers import (
    BookCreateSerializer,
    BookRetrieveSerializer,
    BookUpdateSerializer,
    BookDeleteSerializer,
    BookCategoryCreateSerializer,
    BookInventoryCreateSerializer,
    UserCreateSerializer,

)
from rest_framework.permissions import AllowAny,IsAuthenticated

# from ..filters import BookFilter

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)



from book.api.serializers import (
    BookCreateSerializer,
    BookCategoryCreateSerializer,
    BookCategoryRetrieveSerializer,
    BookCategoryUpdateSerializer,
    BookCategoryDeleteSerializer,
    BookRetrieveSerializer,
    BookUpdateSerializer,
    BookDeleteSerializer,
    BookInventoryCreateSerializer,
    BookInventoryRetrieveSerializer,
    BookInventoryUpdateSerializer,
    BookInventoryDeleteSerializer,

    UserCreateSerializer,


)

class BookCreateAPIView(CreateAPIView):
    """View for creating a book."""
    permission_classes = [AllowAny]
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()

class BookListAPIView(ListAPIView):
    """View for listing all books."""
    permission_classes = [AllowAny]
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()
    # filterset_class = BookFilter

class BookRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a book."""
    permission_classes = [AllowAny]
    serializer_class = BookRetrieveSerializer
    queryset = Book.objects.all()

class BookUpdateAPIView(UpdateAPIView):
    """View for updating a book."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookUpdateSerializer
    queryset = Book.objects.all()

class BookDeleteAPIView(DestroyAPIView):
    """View for deleting a book."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookDeleteSerializer
    queryset = Book.objects.all()

class BookCategoryCreateAPIView(CreateAPIView):
    """View for creating a book category."""
    permission_classes = [AllowAny]
    serializer_class = BookCategoryCreateSerializer

class BookCategoryListAPIView(ListAPIView):
    """View for listing all book categories."""
    permission_classes = [AllowAny]
    serializer_class = BookCategoryRetrieveSerializer
    queryset = BookCategory.objects.all()

class BookCategoryRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a book category."""
    permission_classes = [AllowAny]
    serializer_class = BookCategoryRetrieveSerializer
    queryset = BookCategory.objects.all()

class BookCategoryUpdateAPIView(UpdateAPIView):
    """View for updating a book category."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookCategoryUpdateSerializer
    queryset = BookCategory.objects.all()

class BookCategoryDeleteAPIView(DestroyAPIView):
    """View for deleting a book category."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookCategoryDeleteSerializer
    queryset = BookCategory.objects.all()

class BookInventoryCreateAPIView(CreateAPIView):
    """View for creating a book inventory."""
    permission_classes = [AllowAny]
    serializer_class = BookInventoryCreateSerializer
    queryset = BookInventory.objects.all()

class BookInventoryListAPIView(ListAPIView):
    """View for listing all book inventories."""
    permission_classes = [AllowAny]
    serializer_class = BookInventoryRetrieveSerializer
    queryset = BookInventory.objects.all()

class BookInventoryRetrieveAPIView(RetrieveAPIView):
    """View for retrieving a book inventory."""
    permission_classes = [AllowAny]
    serializer_class = BookInventoryRetrieveSerializer
    queryset = BookInventory.objects.all()

class BookInventoryUpdateAPIView(UpdateAPIView):
    """View for updating a book inventory."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookInventoryUpdateSerializer
    queryset = BookInventory.objects.all()

class BookInventoryDeleteAPIView(DestroyAPIView):
    """View for deleting a book inventory."""
    permission_classes = [IsAuthenticated]
    serializer_class = BookInventoryDeleteSerializer
    queryset = BookInventory.objects.all()



class UserCreateAPIView(CreateAPIView):
    """View for creating a user."""
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
