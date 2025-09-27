from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# This is the serializer class of the book with the validation override
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate(self, attrs):
        try:
            year = int(attrs['publication_year'])
        except ValueError:
            raise serializers.ValidationError("Publication year must be a valid number")

        if year > datetime.now().year:
            raise serializers.ValidationError("The publish year must not be in the future")

        return attrs
        
# This is the serializer class of the author including the books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ["name", "books"]
        
        