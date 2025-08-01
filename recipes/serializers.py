from rest_framework import serializers
from .models import Recipe


class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'ingredients', 'image']
