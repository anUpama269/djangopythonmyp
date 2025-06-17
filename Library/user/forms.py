from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user import CustomUser
class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'address']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


