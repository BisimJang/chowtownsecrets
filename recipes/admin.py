from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Recipe, Review
from accounts.models import CustomUser


admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(CustomUser)

