from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from book.models import Book
from cart.models import Cart


# payments methods
METHOD = (
    ("Esewa","Esewa"),
)

class OrderStatus:
    PENDING = "pending"
    SUCCESS = "success"
    CHOICES = [
        (PENDING, "pending"),
        (SUCCESS, "success")
    ]


class Order_Detail(models.Model):
    """Model for book order details."""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    total = models.DecimalField(
        _("total"), max_digits=5, decimal_places=2, default=Decimal("0.0")
    )
    order_date = models.DateTimeField(_("order_date"),auto_now_add=True)
    order_status = models.CharField(choices=OrderStatus.CHOICES,default=OrderStatus.PENDING, max_length=32)
    class Meta:
        verbose_name = "Order_detail"
        verbose_name_plural = "Order_details"
        ordering = ["id"]
    def __str__(self):
        """Unicode representation of Order_details."""
        return self.user_id

class Order_Items(models.Model):
    """Model for book order items."""
    order_product = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(default=0,blank=True, null=True)
    order_price = models.DecimalField(_("order_price"),max_digits=5, decimal_places=2,default=Decimal("0.0"))
    order_id = models.ForeignKey(Order_Detail, on_delete=models.CASCADE, related_name="order_items")

    class Meta:
        verbose_name = "Order_items"
        verbose_name_plural = "Order_items"

    def __str__(self):
        """Unicode representation of Order_items."""
        return f"{self.order_cart} {self.order_product}"

