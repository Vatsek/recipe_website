from django.contrib import admin
from .models import Recipe, Author, Category

@admin.register(Author)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'date_of_reg', 'full_name']
    list_filter = ['date_of_reg']
    readonly_fields = ['id', 'date_of_reg']
    fieldsets = ((None, {'fields': ['first_name', 'last_name']}),
                 ('Контакты', {'fields': ['email']}))
    search_fields = ['email']
    search_help_text = 'Поиск по почте'


@admin.register(Recipe)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'cooking_steps', 'cooking_time', 'image', 'author', 'category', 'is_active']
    fieldsets = (None, {'fields': ['title', 'description', 'cooking_steps', 'cooking_time', 'image', 'author', 'category']}),
    readonly_fields = ['id', 'date_addition']


@admin.register(Category)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['title']