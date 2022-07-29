from rest_framework import serializers

from order.models import Order_Detail, Order_Items

class OrderDetailCreateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            # "book_id",
            "total",
            "order_date",
        )

class OrderDetailRetrieveSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            # "book_id",
            "total",
            "order_date",
        )

class OrderDetailUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            # "book_id",
            "total",
            "order_date",
        )

class OrderDetailDeleteSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = (
            "id",
            "user_id",
            "book_id",
            "total",
            # "order_date",
        )

class OrderItemCreateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "book_id",
            "quantity",
        )

class OrderItemRetrieveSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "book_id",
            "quantity",
        )

class OrderItemUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "book_id",
            "quantity",
        )

class OrderItemDeleteSerialier(serializers.ModelSerializer):
    class Meta:
        model = Order_Items
        fields = (
            "id",
            "order_id",
            "book_id",
            "quantity",
        )
