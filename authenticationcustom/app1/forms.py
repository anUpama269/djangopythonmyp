from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# class SignupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['username','password','email','first_name','last_name']
from app1.models import CustomUser
class SignupForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['username','password1','password2','email','first_name','last_name','phone','address']



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()