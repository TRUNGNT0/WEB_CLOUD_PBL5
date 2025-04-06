from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass
# Compare this snippet from green_house/accounts/models.py: