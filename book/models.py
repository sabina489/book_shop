import email
from django.db import models
from decimal import Decimal

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BookCategory(models.Model):
    """Model for course category."""

    category_name = models.CharField(
        _("name"),
        max_length=100,
    )
    description = models.CharField(max_length = 500, blank=True, null=True)
    
    class Meta:
        """Meta definition for CourseCategory."""

        verbose_name = "BookCategory"
        verbose_name_plural = "BookCategorys"
        ordering = ["id"]

    def __str__(self):
        """Unicode representation of BookCategory."""
        return self.name

class Book(models.Model):
    """Model for book."""
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, blank=True, null=True)
    follow_author = models.CharField(max_length=2083, blank=True, null=True)  
    book_available = models.BooleanField(default=False)
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
    quantity = models.IntegerField(default=0)
    class Meta:
        verbose_name = "BookInventory"
        verbose_name_plural = "BookInventories"
        

    def __str__(self):
        """Unicode representation of BookInventory."""
        return self.book.quantity




class User(models.Model):

    username = models.CharField(max_length = 100)
    # middlename = models.CharField(max_length = 100,blank=True,null=True)
    # lastname = models.CharField(max_length = 100)
    # user_email = models.CharField
    email = models.EmailField(_("email address"), unique=True)
    # password = models.PasswordField(_("password"), max_length=128)
    password = models.CharField(
        _("password"),
        max_length=128,
        help_text=_(
            "Use'[algo]$[salt]$[hexdigest]' or use the \
                < a href=\"password/\">change password form</a>."
        ),
        blank=True,
        null=True,
    )

    

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.user_firstname

    