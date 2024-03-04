from django.urls import path
from . import views


urlpatterns = [
    path('recipe/<int:recipe_id>/', views.get_recipe_by_id, name='get_recipe'),
]
