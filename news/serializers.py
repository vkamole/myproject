from rest_framework import serializers
from .models import Author, Category, News


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'content',
                  'created_at', 'author', 'categories')
