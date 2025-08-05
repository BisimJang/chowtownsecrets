from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from .models import Recipe, Review
from .serializers import RecipeSerializer, ReviewSerializer


# Create your views here.
# List recipe endpoint
# CRUD recipe endpoint
# CRUD review endpoint
# User auth and registration
# Pagination
# Searching and Filtering


# List the recipes
class RecipeList(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# List a particular recipe
class RecipeDetail(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'

# create a particular recipe
class RecipeCreateView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Retrieve, update, delete a Recipe
class RetrieveUpdateDestroyRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# List out the reviews for a particular recipe
class RecipeReviewList(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Review.objects.filter(recipe_id=recipe_id)

# create a new review
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        serializer.save(user=self.request.user, recipe=recipe)

    def get_queryset(self):
        recipe_id = self.kwargs['recipe_id']
        return Review.objects.filter(recipe_id=recipe_id)

# Retrieve, update and delete a review
class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().user:
            raise PermissionDenied("You can only edit your own review.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise PermissionDenied("You can only delete your own review.")
        instance.delete()
