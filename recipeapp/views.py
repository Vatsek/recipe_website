from django.shortcuts import render, redirect
from .forms import RecipeForm, SearchForm
from .models import Recipe, RecipeCategories


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
    recipe_categories = RecipeCategories.objects.get(recipes=recipe_id)
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipeapp/recipe.html', {'recipe': recipe, 'recipe_categories': recipe_categories})


def add_recipe(request):
    title = 'Добавление рецепта'
    input_value = 'Добавить'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            new_recipe = form.save()
            return redirect('recipe', new_recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipeapp/recipe_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value})


def recipe_update_form(request, recipe_id):
    title = 'Изменение рецепта'
    input_value = 'Изменить'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe.title = form.cleaned_data['title']
            recipe.description = form.cleaned_data['description']
            recipe.cooking_steps = form.cleaned_data['cooking_steps']
            recipe.cooking_time = form.cleaned_data['cooking_time']
            recipe.author = form.cleaned_data['author']
            a = recipe.image
            # recipe.image = form.cleaned_data['image']
            b = recipe.image
            recipe.save()
            if form.cleaned_data['image'] != None:
                recipe.image = form.cleaned_data['image']
                recipe.save()
            return redirect('recipe', recipe_id)

    else:
        form = RecipeForm(instance=Recipe.objects.get(pk=recipe_id))
    return render(request, 'recipeapp/recipe_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value})


def search_recipes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            recipes = Recipe.objects.all().filter(title=title)
            title = 'Результат поиска'
            heading = 'Результат поиска'
            return render(request, 'recipeapp/index.html', {'recipes': recipes, 'title': title, 'heading': heading})
    else:
        form = SearchForm()
    return render(request, 'recipeapp/search_recipes_form.html',
                  {'form': form})


def categories(request):
    title = 'Категории'
    heading = 'Категории'
    categories = RecipeCategories.objects.all()
    return render(request, 'recipeapp/categories.html', {'categories': categories, 'title': title, 'heading': heading})


def recipes_by_categories(request, category_id):
    title = 'Рецепты по категории'
    heading = 'Все рецепты выбранной категории'
    category = RecipeCategories.objects.get(pk=category_id)
    recipes_lst = category.get_recipes()
    return render(request, 'recipeapp/index.html', {'recipes': recipes_lst, 'title': title, 'heading': heading})
