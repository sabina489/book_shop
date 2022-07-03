from rest_framework import serializers

from book.models import Book, BookCategory, BookInventory, User


class BookCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a book."""
    class Meta:
        model = Book
        fields = (
            "id",    
            "title", 
            "author", 
            "description", 
            "price", 
            "image_url", 
            "follow_author", 
            "book_available", 
            "category",
        )
    


class BookRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving a book."""
    class Meta:
        model = Book
        fields = (
            "id",    
            "title", 
            "author", 
            "description", 
            "price", 
            "image_url", 
            "follow_author", 
            "book_available", 
            "category",
        )

class BookUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating a book."""
    class Meta:
        model = Book
        fields = (
            "id",    
            "title", 
            "author", 
            "description", 
            "price", 
            "image_url", 
            "follow_author", 
            "book_available", 
            "category",
        )

class BookDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting a book."""
    class Meta:
        model = Book
        fields = (
            "id",    
            "title", 
            "author", 
            "description", 
            "price", 
            "image_url", 
            "follow_author", 
            "book_available", 
            "category",
        )

class BookCategoryCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating book category."""
    class Meta:
        model = BookCategory
        fields = (
            "id",    
            "category_name", 
            "description",
        )
    


class BookCategoryRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving book category."""
    class Meta:
        model = BookCategory
        fields = (
            "id",    
            "category_name", 
            "description",
        )

class BookCategoryUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating book category."""
    class Meta:
        model = BookCategory
        fields = (
            "id",    
            "category_name", 
            "description",
        )

class BookCategoryDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting book category."""
    class Meta:
        model = BookCategory
        fields = (
            "id",    
            "category_name", 
            "description",
        )

class BookInventoryCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating bookinventory."""
    class Meta:
        model = BookInventory
        fields = (
            "id",    
            "book", 
            "quantity",
        )

class BookInventoryRetrieveSerializer(serializers.ModelSerializer):
    """Serializer for retrieving bookinventory."""
    class Meta:
        model = BookInventory
        fields = (
            "id",    
            "book", 
            "quantity",
        )

class BookInventoryUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating bookinventory."""
    class Meta:
        model = BookInventory
        fields = (
            "id",    
            "book", 
            "quantity",
        )

class BookInventoryDeleteSerializer(serializers.ModelSerializer):
    """Serializer for deleting bookinventory."""
    class Meta:
        model = BookInventory
        fields = (
            "id",    
            "book", 
            "quantity",
        )

class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating user."""
    class Meta:
        model = User
        fields = (
            "id",    
            "username",
            # "middlename"
            # "lastname", 
            "password",
            "email",
        )
