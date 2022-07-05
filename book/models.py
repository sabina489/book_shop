import email
from django.db import models
from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BookCategory(models.Model):
    """Model for course category."""

    category_name = models.CharField(
        _("category_name"),
        max_length=100,
    )
    image = models.ImageField(upload_to='book/',blank = True, null=True)
    description = models.CharField(_("description"),max_length = 500, blank=True, null=True)
    
    class Meta:
        """Meta definition for CourseCategory."""

        verbose_name = "BookCategory"
        verbose_name_plural = "BookCategorys"
        ordering = ["id"]

    def __str__(self):
        """Unicode representation of BookCategory."""
        return self.category_name

class Book(models.Model):
    """Model for book."""
    title  = models.CharField(_("title"),max_length = 200)
    author = models.CharField(_("author"),max_length = 200)
    description = models.CharField(_("description"),max_length = 500, blank=True, null=True)
    price = models.FloatField(_("price"),null=True, blank=True)
    # image_url = models.CharField(_("image_url"),max_length = 2083, blank=True, null=True)
    image = models.ImageField(upload_to='book/',blank = True, null=True)
    follow_author = models.CharField(_("follow_author"),max_length=2083, blank=True, null=True)  
    book_available = models.BooleanField(_("book_available"),default=False)
    category = models.ForeignKey(
        BookCategory,
        verbose_name=_("category"),
        related_name="books",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        
    

    def __str__(self):
        """Unicode representation of Book."""
        return self.title

class BookInventory(models.Model):
    """Model for book inventory."""
    book = models.ForeignKey(
        Book,
        verbose_name=_("book"),
        related_name="book_inventory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    quantity = models.IntegerField(default=0,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    class Meta:
        verbose_name = "BookInventory"
        verbose_name_plural = "BookInventories"
        

    def __str__(self):
        """Unicode representation of BookInventory."""
        return self.book.title




