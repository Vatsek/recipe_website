from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RecipeForm, SearchForm
from .models import Recipe, Category


def index(request):
    title = 'Кушайте много, кушайте вкусно'
    heading = '5 случайных рецептов'
    categories = Category.objects.all()
    recipes = Recipe.objects.filter(is_active=True).order_by('?')[:5]
    return render(request, 'recipeapp/index.html', {'recipes': recipes,
                                                    'title': title,
                                                    'heading': heading,
                                                    'categories': categories})


def all_recipes(request):
    title = 'Все рецепты'
    heading = 'Все рецепты'
    categories = Category.objects.all()
    recipes = Recipe.objects.filter(is_active=True).all()
    return render(request, 'recipeapp/index.html', {'recipes': recipes,
                                                    'title': title,
                                                    'heading': heading,
                                                    'categories': categories})



def get_recipe_by_id(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    categories = Category.objects.all()
    return render(request, 'recipeapp/recipe.html', {'recipe': recipe, 'categories': categories})


@login_required
def add_recipe(request):
    title = 'Добавление рецепта'
    input_value = 'Добавить'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe', recipe.pk)
    else:
        form = RecipeForm()
        categories = Category.objects.all()
    return render(request, 'recipeapp/recipe_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value,
                   'categories': categories})


@login_required()
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
            recipe.category = form.cleaned_data['category']
            if form.cleaned_data['image'] != None:
                recipe.image = form.cleaned_data['image']
            recipe.save()
            return redirect('recipe', recipe_id)

    else:
        form = RecipeForm(instance=Recipe.objects.get(pk=recipe_id))
        categories = Category.objects.all()

    return render(request, 'recipeapp/recipe_form.html',
                  {'form': form,
                   'title': title,
                   'input_value': input_value,
                   'categories': categories})

@login_required()
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.is_active = False
    recipe.save()
    return render(request, 'recipeapp/delete_recipe_complete.html')


@login_required()
def delete_recipe_question(request, recipe_id):
    categories = Category.objects.all()
    return render(request, 'recipeapp/delete_recipe_question.html', {'recipe_id': recipe_id, 'categories': categories})


def search_recipes(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            recipes = Recipe.objects.all().filter(title=title, is_active=True)
            title = 'Результат поиска'
            heading = 'Результат поиска'
            categories = Category.objects.all()
            return render(request, 'recipeapp/index.html', {'recipes': recipes,
                                                            'title': title,
                                                            'heading': heading,
                                                            'categories': categories})
    else:
        form = SearchForm()
        categories = Category.objects.all()
    return render(request, 'recipeapp/search_recipes_form.html',
                  {'form': form, 'categories': categories})


def recipes_by_categories(request, category_id):
    title = 'Рецепты по категории'
    heading = 'Все рецепты выбранной категории'
    recipes = Recipe.objects.filter(category=category_id)
    categories = Category.objects.all()
    return render(request, 'recipeapp/index.html', {'recipes': recipes,
                                                    'title': title,
                                                    'heading': heading,
                                                    'categories': categories})
