from django.shortcuts import render
from .models import Recipe, Author
from django.http.response import HttpResponse


def index(request):
    return render(request, 'recipeapp/index.html')


def get_recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipeapp/recipe.html', {'recipe': recipe})
