from django import forms 
from django.contrib.auth.models import User
from item.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        