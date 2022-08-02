from requests import delete
from rest_framework import serializers
from django.db import transaction
# from stripe import Order
from cart.api.serializers import ResultCreateSerializer
from decimal import Decimal

from order.models import Order_Detail, Order_Items
from book.models import Book

from cart.models import Cart, CartItem

class OrderDetailCreateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "total",
            "order_date",
        )
        read_only_fields = ("user_id","total", "id", "order_date")

    @transaction.atomic
    def create(self, validated_data):
        cart = Cart.objects.get(user=self.context["request"].user)
        # print("************", cart.total)

        order_detail = Order_Detail.objects.create(
            total=cart.total,
            user_id = self.context["request"].user,
        )
        order_detail.save()
    
        if cart:
            for item in cart.cart_items.all():
                order_item = Order_Items.objects.create(
                    order_product = item.product,
                    order_price = item.price,
                    order_quantity = item.quantity,
                    order_id = order_detail

                )
                order_item.save()
                item.delete()
    
        return order_detail

class OrderDetailListSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "total",
            "order_date",
        )
        read_only_fields = ("user_id","total", "id", "order_date")

class FinalOrderSerializer(serializers.ModelSerializer):
    """Serializer for producnt."""

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



class OrderDetailUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "total",
            "order_date",
        )

class OrderDetailDeleteSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "order_date",
            "total",
        )
class OrderItemCreateSerialier(serializers.ModelSerializer):
    
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "order_product",
            "order_price",
            "order_quantity",
        
        )
        read_only_fields = ("id","order_id")
    
    @transaction.atomic
    def create(self, validated_data):
        cart = Cart.objects.get(user=self.context["request"].user)
        instance = super().create(validated_data)
        instance.save()
        if cart:
            for item in cart:
                Order_Items.order_id = instance.id
                Order_Items.order_product.user_id = instance.user_id
                Order_Items.total = instance.total
                item.save()
        return instance  

class OrderItemRetrieveSerialier(serializers.ModelSerializer):
    # order = FinalOrderSerializer(read_only=True)
    order_product = FinalOrderSerializer(read_only=True)
    
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "order_product",
            "order_price",
            "order_quantity",
            # "order",
        )
class OrderDetailRetrieveSerializer(serializers.ModelSerializer):
    order_items = OrderItemRetrieveSerialier(read_only=True, many=True)
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "total",
            "order_date",
            "order_items",
        )
class OrderItemUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "order_product",
            "order_quantity",
            "order_price",
        )
    
    # def update(self,instance,validated_data):
    #     """Update an order item."""
    #     instance.order_product = validated_data.get("order_product", instance.order_product)
    #     instance.order_price = validated_data.get("order_price", instance.order_price)
    #     instance.order_quantity = validated_data.get("order_quantity", instance.order_quantity)
    #     instance.save()
    #     return instance

class OrderItemDeleteSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "order_quantity",
            "order_price", 
            "order_product",
        )
    
    # def delete(self, instance):
    #     """Delete a order item."""
    #     instance.delete()
    #     return instance

class OrderDetailRetrieveSerialier(serializers.ModelSerializer):
    """Serializer for retrieving a order."""
    order_items = OrderItemRetrieveSerialier(read_only=True, many=True)
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "total",
            "order_date",
            "order_items",
        )