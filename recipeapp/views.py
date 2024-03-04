from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe, Author
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def index(request):
    title = 'Кушайте много, кушайте вкусно'
    heading = '5 случайных рецептов'
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'recipeapp/index.html', {'recipes': recipes, 'title': title, 'heading': heading})


def all_recipes(request):
    title = 'Все рецепты'
    heading = 'Все рецепты'
    recipes = Recipe.objects.all()
    return render(request, 'recipeapp/index.html', {'recipes': recipes, 'title': title, 'heading': heading})



def get_recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipeapp/recipe.html', {'recipe': recipe})


def add_recipe(request):
    title = 'Добавление рецепта'
    input_value = 'Добавить'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save()
            return redirect('get_recipe', new_recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipeapp/recipe_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value})


