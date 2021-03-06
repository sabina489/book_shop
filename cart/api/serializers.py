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
        read_only_fields = ("id", "cart")
    def create(self, validated_data):
        """Create a new cart item."""
        with transaction.atomic():
            cart, _ = Cart.objects.get_or_create(user=self.context["request"].user)
            product = validated_data.get("product")
            cart_item_with_product = cart.cart_items.filter(product=product).first()
            if cart_item_with_product:
                cart_item_with_product.quantity += validated_data.get("quantity")
                cart_item_with_product.save()
                return cart_item_with_product
            cart_item = CartItem.objects.create(cart=cart, **validated_data)
            return cart_item

class CartItemDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting a cart item."""
    class Meta:
        model = CartItem
        fields = (
            "id",
            "product",
            "quantity",
            "cart",
            )
        read_only_fields = ("id",)

    def delete(self, instance):
        """Delete a cart item."""
        instance.delete()
        return instance
    
  

class CartItemRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a cart item."""
    product = ResultCreateSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = (
            "id",    
            "product", 
            "quantity",
            # "cart", 
        )

class CartRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a cart."""
    cart_items = CartItemRetrieveSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = (
            "id",
            "cart_items",
            "total",
            "created_at",
        )

