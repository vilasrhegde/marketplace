from django import forms 

from . models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border dark:text-white dark:bg-gray-900'
SIZE_CHOICES = [
        ('','None'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]
COLOR_CHOICES = [
        ('','None'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Violet', 'Violet'),
        ('Orange', 'Orange'),
        ('Black', 'Black'),
        ('Green', 'Green'),
        ('White', 'White'),
    ]

GENDER_CHOICES = [
        ('','Not specified'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

class NewItemForm(forms.ModelForm):

    # size = forms.ChoiceField(choices=SIZE_CHOICES)
    class Meta:
        model = Item
        fields = ('image','category','name','price','size','color','gender','description',)

        widgets = {
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES,
                'rows':4
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
            'size':forms.Select(attrs={
                'class':INPUT_CLASSES
            },choices=SIZE_CHOICES),
            'color':forms.SelectMultiple(attrs={
                'class':INPUT_CLASSES
            },choices=COLOR_CHOICES),
            'gender':forms.Select(attrs={
                'class':INPUT_CLASSES
            },choices=GENDER_CHOICES),
        }
        empty_label = 'Select category'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select category'
        self.fields['category'].initial = ''


# edit

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('is_sold','image','name','size','color','description',)

        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSES,
                'rows':4
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
            'size':forms.Select(attrs={
                'class':INPUT_CLASSES
            },choices=SIZE_CHOICES),
            'color':forms.SelectMultiple(attrs={
                'class':INPUT_CLASSES
            },choices=COLOR_CHOICES),
            'is_sold':forms.CheckboxInput(attrs={
                'class':'text-left accent-emerald-500/25 w-5 h-5'
            }),
        }