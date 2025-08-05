from django.urls import path
from .views import RecipeList, ReviewCreateView, RecipeReviewList, RecipeDetail, RecipeCreateView, \
    RetrieveUpdateDestroyRecipe, RetrieveUpdateDestroyReview

urlpatterns = [
    #api_views
    path('api/recipes/',RecipeList.as_view(), name='list-recipes'), # returns all recipes
    path('api/recipes/<int:id>',RecipeDetail.as_view(), name='recipe-detail'), # returns a specific recipe
    path('api/recipes/<int:recipe_id>/reviews',RecipeReviewList.as_view(), name='recipe-reviews'), # returns the reviews for a recipe using the id,
    path('api/recipes/create', RecipeCreateView.as_view(), name='create-recipe'), # create review
    path('api/recipes/<int:id>/edit/', RetrieveUpdateDestroyRecipe.as_view(), name='edit-recipe'),
    path('api/recipes/<int:recipe_id>/create-review', ReviewCreateView.as_view(), name='create-review'), # create review
    path('api/recipes/<int:id>/edit-review/', RetrieveUpdateDestroyReview.as_view(), name='edit-recipe'),
]

