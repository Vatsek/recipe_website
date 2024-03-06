from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'style': 'border-radius: 6px; '
                                                                   'width:200px; height:20px;',
                                                          'placeholder': 'Введите название'}))

    description = forms.CharField(widget=forms.Textarea(attrs={'style': 'border-radius: 6px;',
                                                               'placeholder': 'Введите краткое описание блюда'}))

    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'style': 'border-radius: 6px;',
                                                                 'placeholder': 'Введите шаги приготовления блюда'}))

    cooking_time = forms.IntegerField(widget=forms.NumberInput(attrs={
        'placeholder': 'Время приготовления'}))

    class Meta:
        model = Recipe
        exclude = ['date_addition', 'author', 'is_active']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = True
        self.fields['image'].required = False


class SearchForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Введите название блюда'}))

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['style'] = 'width:200px; height:20px; border-radius: 6px;'
