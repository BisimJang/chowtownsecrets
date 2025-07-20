from django.http import request
from django.urls import path
from .views import home_page, login_page

urlpatterns = [
    path('', home_page, name='recipes-home'),
    path('login', login_page, name='recipes-login'),
]