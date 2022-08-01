from django.contrib import admin

from order.models import Order_Detail, Order_Items

# Register your models here.

@admin.register(Order_Detail)
class Order_detailAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "total",
        "order_date",
    )

@admin.register(Order_Items)
class Order_itemsAdmin(admin.ModelAdmin):
    list_display = (
        "order_id",
        "order_product",
        "order_price",
        "order_quantity",
    )
