# Generated by Django 5.0.2 on 2024-03-04 11:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('date_of_reg', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное имя')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cooking_steps', models.TextField(verbose_name='Шаги приготовления')),
                ('cooking_time', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')),
                ('date_addition', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.author', verbose_name='Автор')),
            ],
        ),
    ]
