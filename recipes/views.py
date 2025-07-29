from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import Recipe, Review
from .forms import RegisterForm, CustomLoginForm, ReviewForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def home_page(request):
    recipes = Recipe.objects.all()
    reviews = Review.objects.select_related('recipe', 'user').order_by('-created_at')
    paginator = Paginator(recipes, 4)  # 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    review_paginator = Paginator(reviews, 2)  # Show 5 reviews per page
    review_page_number = request.GET.get('page')
    review_page_obj = review_paginator.get_page(review_page_number)
    return render(request, 'recipes/index.html', {
        'recipes': page_obj,
        'reviews': reviews,
        'page_obj': review_page_obj,
    })


def login_signup(request):
    register_form = RegisterForm()
    login_form = CustomLoginForm()

    if request.method == 'POST':
        if 'signup' in request.POST:
            # Handle registration
            register_form = RegisterForm(request.POST)
            login_form = CustomLoginForm()  # Empty login form for context
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, "Account created successfully!")
                return redirect('recipes-home')
            else:
                messages.error(request, "Please correct the errors below.")

        elif 'login' in request.POST:
            # Handle login
            login_form = CustomLoginForm(request, data=request.POST)
            register_form = RegisterForm()  # Empty signup form for context
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('recipes-home')
            else:
                print(login_form.errors)
                messages.error(request, "Invalid login credentials.")

    else:
        # GET request
        register_form = RegisterForm()
        login_form = CustomLoginForm()

    return render(request, 'recipes/login_signup.html', {
        'register_form': register_form,
        'login_form': login_form,
    })


@login_required
def create_review(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = ReviewForm(request.POST)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.recipe = recipe
            review.save()
            return redirect('recipe-detail', recipe_id=recipe.id)
        else:
            form = ReviewForm()

    return render(request, 'recipes/review_form.html', {'form': form, 'recipe': recipe})

@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('recipe-detail', pk=review.recipe.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'recipes/review_form.html', {'form': form, 'recipe': review.recipe})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    recipe_id = review.recipe.id
    if request.method == 'POST':
        review.delete()
        return redirect('recipe-detail', recipe_id=recipe_id)
    return render(request, 'recipes/review_confirm_delete.html', {'review': review})

def all_reviews(request):
    reviews_list = Review.objects.select_related('recipe', 'user').order_by('-created_at')
    paginator = Paginator(reviews_list, 5)  # Show 5 reviews per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/all_reviews.html', {'page_obj': page_obj})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/recipe_detail.html', context=context)


def all_recipes(request):
    query = request.GET.get('q')

    if query:
        recipes = Recipe.objects.filter(
            Q(title__icontains=query)
        )
    else:
        recipes = Recipe.objects.all()

    paginator = Paginator(recipes, 6)  # 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/all_recipes.html', {
        'recipes': page_obj,
        'query': query,
        'no_results': query and not recipes.exists()
    })

def custom_logout(request):
    logout(request)
    return render(request, 'recipes/logout.html')
