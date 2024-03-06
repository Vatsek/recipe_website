from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('recipe/<int:recipe_id>/', views.get_recipe_by_id, name='recipe'),
    path('recipe/update/<int:recipe_id>/', views.recipe_update_form, name='recipe_update'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),

    path('delete_recipe/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('delete_recipe_question/<int:recipe_id>', views.delete_recipe_question, name='delete_recipe_question'),

    path('all_recipes', views.all_recipes, name='all_recipes'),
    path('search_recipes', views.search_recipes, name='search_recipes'),
    path('recipes_by_categories/<int:category_id>/', views.recipes_by_categories, name='recipes_by_categories'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)