from django import forms  # Formularios de Django
from django.contrib.auth.forms import AuthenticationForm
from .models import User

class LoginForm(AuthenticationForm): # Clase creada que hereda de AuthenticationForm, pero con los componentes personalizados

    username = forms.CharField(
        label = 'Username',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
        
    )


    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )


    class Meta:

        model = User
        fields = ['username', 'password']