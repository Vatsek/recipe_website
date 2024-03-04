from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('recipe/<int:recipe_id>/', views.get_recipe_by_id, name='get_recipe'),
    path('add_recipe/', views.add_recipe, name='add_recipe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)