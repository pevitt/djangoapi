from rest_framework import serializers
from .models import Editorial, Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=True)
    editorial = EditorialSerializer(required=True)

    class Meta:
        model = Book
        fields = '__all__'
