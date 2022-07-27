from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime
from book.models import Book, BookCategory

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.FloatField(_("price"),null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        """Meta definition for Cart."""
        verbose_name = "Cart"
        verbose_name_plural = "Carts"
    
    def __str__(self):
        """Unicode representation of Cart."""
        return str(self.user)

class CartItem(models.Model):
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"),default=1)
    price = models.FloatField(_("price"),null=True, blank=True)
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    

    class Meta:
        verbose_name = "CartItem"
        verbose_name_plural = "CartItems"

    def __str__(self):
        """Unicode representation of CartItem."""
        return self.product.title