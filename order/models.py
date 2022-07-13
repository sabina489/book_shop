from django.db import models
from decimal import Decimal
from django.utils.translation import gettext_lazy as _


# # payments methods
# METHOD = (
#     ('COD', 'Cash on Delivery'),

#     ('Esewa',Esewa),
# )

class Order_Detail(models.Model):
    """Model for book order details."""
    user_id = models.CharField(_("user_id"),max_length = 100)
    book_id = models.CharField(_("book_id"),max_length = 100)
    total = models.DecimalField(
        _("total"), max_digits=5, decimal_places=2, default=Decimal("2.0")
    )
    order_date = models.DateTimeField(_("order_date"),auto_now_add=True)
    class Meta:
        verbose_name = "Order_detail"
        verbose_name_plural = "Order_details"
        ordering = ["id"]
    def __str__(self):
        """Unicode representation of Order_details."""
        return self.user_id

class Order_Items(models.Model):
    """Model for book order items."""
    order_id = models.CharField(_("order_id"),max_length = 100)
    book_id = models.CharField(_("book_id"),max_length = 100)
    quantity = models.ForeignKey(
        Order_Detail,
        verbose_name=_("quantity"),
        related_name="quantity",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = "Order_items"
        verbose_name_plural = "Order_items"

    def __str__(self):
        """Unicode representation of Order_items."""
        return self.order_id
