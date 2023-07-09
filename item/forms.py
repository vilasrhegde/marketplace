from django import forms 

from . models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('image','category','name','description','price')

        widgets = {
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
        }

# edit

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('image','name','description','price', 'is_sold')

        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
        }