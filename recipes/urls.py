from django.http import request
from django.urls import path
from .views import home_page, login_signup, login, all_reviews, all_recipes, recipe_detail, custom_logout, \
    create_review, delete_review, update_review
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home_page, name='recipes-home'),
    path('auth/', login_signup, name='recipes-signup'),
    path('recipe-detail/<int:recipe_id>/', recipe_detail, name='recipe-detail'),
    path('add-review/<int:recipe_id>/', create_review, name='add-review'),
    path('review/<int:review_id>/edit/', update_review, name='update-review'),
    path('review/<int:review_id>/delete/', delete_review, name='delete-review'),
    path('all-reviews/', all_reviews, name='all-reviews'),
    path('all-recipes/', all_recipes, name='all-recipes'),
    path('logout/',custom_logout, name='logout'),
]