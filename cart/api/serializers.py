from rest_framework import serializers

from cart.models import Cart, CartItem

class CartCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart."""
    class Meta:
        model = Cart
        fields = (
            "id",
            "user",
        )

class CartItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a cart item."""
    class Meta:
        model = CartItem
        fields = (
            "id",    
            "product", 
            "quantity", 
            "cart",
        )