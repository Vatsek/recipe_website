from django import forms
from .models import Recipe


class ProductForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['date_product_add']
        labels = {'title': 'Наименование',
                  'description': 'Описание',
                  'price': 'Стоимость',
                  'quantity_of_product': 'количество',
                  'image': 'Изображение'}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False