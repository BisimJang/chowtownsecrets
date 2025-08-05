from rest_framework import serializers
from .models import Recipe, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'text', 'rating', 'created_at']
        read_only_fields = ['user', 'created_at']

class RecipeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'image', 'reviews', 'created_at']
