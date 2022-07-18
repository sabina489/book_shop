from pipes import Template
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from book.models import Book, BookCategory, BookInventory
from rest_framework import generics


from rest_framework.permissions import AllowAny,IsAuthenticated

from book.api.paginations import LargeResultsSetPagination
# from book import Book
from .filters import BookFilter

# stripe 
import stripe
from django.conf import settings
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse,JsonResponse
from book.models import Book

# stripe.api_key = settings.STRIPE_SECRET_KEY

stripe.api_key = 'sk_test_51LLNkJEAORkPsj554dMme1PijaWgUW8yUkdM0kmvo9GtaleCC0242Guu4f4JQPC9tSEjIk9i65u3Xe5dorGq67SC00TjIrihE2'


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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    pagination_class = LargeResultsSetPagination
    # search_fields = ['category','price','title']
    search_fields = ['title']
    filterset_class = BookFilter

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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]

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
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]


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


class ProductLandingPageView(TemplateView):
    template_name = "product.html"

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Book.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'title': product.title,
                            'description': product.description,
                            'images': [product.image],     
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })



