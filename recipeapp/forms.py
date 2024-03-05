from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'test1', 'placeholder': 'Название блюда'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'test2', 'placeholder': 'Описание'}))
    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'test2', 'placeholder': 'Шаги приготовления'}))
    cooking_time = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'test2', 'placeholder': 'Время приготовления'}))


    class Meta:
        model = Recipe
        exclude = ['date_addition', 'author']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = True
        self.fields['image'].required = False







class SearchForm(forms.Form):
    title = forms.CharField(max_length=50)