from django.contrib import admin

from book.models import Book, BookCategory, BookInventory, User
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "description",
        "price",
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

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


