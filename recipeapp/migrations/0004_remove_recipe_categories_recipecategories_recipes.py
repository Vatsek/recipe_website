# Generated by Django 5.0.2 on 2024-03-05 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_remove_recipecategories_recipes_recipe_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AddField(
            model_name='recipecategories',
            name='recipes',
            field=models.ManyToManyField(to='recipeapp.recipe', verbose_name='Рецепты'),
        ),
    ]