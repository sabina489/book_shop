from rest_framework import serializers
from django.db import transaction
from book.models import Book

from cart.models import Cart, CartItem

class CartCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart."""
    class Meta:
        model = Cart
        fields = (
            "id",
            )   



class ResultCreateSerializer(serializers.ModelSerializer):
    """Serializer for product."""
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "description",
            "book_available",
            "image",
            "price",
            "category",
        )

class CartItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart item."""
    # product = ResultCreateSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = (
            "id",    
            "product", 
            "quantity",
            "cart",
        )
  

class CartItemRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a cart item."""
    product = ResultCreateSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = (
            "id",    
            "product", 
            "quantity",
     
            "cart",
            
        )

class CartRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a cart."""
    cart_items = CartItemRetrieveSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = (
            "id",
            "cart_items",
            "total",
            "created_at",
        )

