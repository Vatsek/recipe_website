from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe, Author
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def index(request):
    return render(request, 'recipeapp/index.html')


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


