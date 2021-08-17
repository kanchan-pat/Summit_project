from django import forms
from store.models import Categories


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'