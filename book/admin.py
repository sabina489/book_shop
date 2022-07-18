from django.contrib import admin
from book.api.views import CreateCheckoutSessionView

from book.models import Book, BookCategory, BookInventory
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "description",
        "price",
        "category",
        )

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = (
        "id",
        "category_name",
        "description",
    )

@admin.register(BookInventory)
class BookInventoryAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)






