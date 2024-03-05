from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=u'Имя')
    last_name = models.CharField(max_length=50, verbose_name=u'Фамилия')
    email = models.EmailField(verbose_name=u'Почта')
    date_of_reg = models.DateField(auto_now_add=True, verbose_name=u'Дата регистрации')
    full_name = models.CharField(max_length=100, verbose_name=u'Полное имя')

    def __str__(self):
        return str(self.full_name)

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Название')
    description = models.TextField(verbose_name=u'Описание')
    cooking_steps = models.TextField(verbose_name=u'Шаги приготовления')
    cooking_time = models.IntegerField(default=0, validators=[MinValueValidator(1)], verbose_name=u'Время приготовления')
    image = models.ImageField(upload_to='images', blank=True, verbose_name=u'Изображение')
    date_addition = models.DateField(auto_now_add=True, verbose_name=u'Дата добавления')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_NULL,
                               null=True,
                               default=None,
                               related_name='recipe',
                               verbose_name=u'Автор')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default='1', verbose_name=u'Категория')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name=u'Название категории')

    def __str__(self):
        return self.title
