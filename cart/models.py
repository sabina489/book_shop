from decimal import Decimal
from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from book.models import Book

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.DecimalField(_("total"), max_digits=5, decimal_places=2,default=Decimal(0.0))
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        """Meta definition for Cart."""
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
    
    def __str__(self):
        """Unicode representation of Cart."""
        return str(self.created_at)

class CartItem(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,blank=True, null=True)
    price = models.DecimalField(_("price"),max_digits=5, decimal_places=2,default=Decimal("0.0"))
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    
    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    def __str__(self):
        """Unicode representation of CartItem."""
        # return self.product.title
        return f"{self.cart} {self.product}"    