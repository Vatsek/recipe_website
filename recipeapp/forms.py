from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['date_addition']
        labels = {'title': 'Наименование',
                  'description': 'Описание',
                  'cooking_steps': 'Шаги приготовления',
                  'cooking_time': 'Время приготовления',
                  'image': 'Изображение',
                  'author': 'Автор'}

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
