from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your username',
        'class':'w-full py-4 px-6 dark:text-black rounded-xl'
    }))   
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full py-4 px-6 dark:text-black rounded-xl'
    }))
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter your username',
        'class':'w-full py-4 px-6   dark:text-black rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email',
        'class':'w-full py-4 px-6   dark:text-black rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full py-4 px-6  dark:text-black  rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Check your password',
        'class':'w-full py-4 px-6   dark:text-black rounded-xl'
    }))