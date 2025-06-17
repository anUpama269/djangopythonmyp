from django import forms
from django.db.models import Choices


class AdditionForm(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()

#Factorial
class FactorialForm(forms.Form):    #form structure definition
    number=forms.IntegerField()


#BMI
class BMIForm(forms.Form):    #form structure definition
    Height=forms.IntegerField()
    Weight=forms.IntegerField()


class SignupForm(forms.Form):
    user_name=forms.CharField(max_length=50)
    password= forms.CharField(max_length=50,widget=forms.PasswordInput)
    email=forms.EmailField()
    gender_choices = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

    role_choices = [('admin', 'Admin'), ('student', 'Student')]
    role = forms.ChoiceField(choices=role_choices)

class CalorieForm(forms.Form):
    gender_choices = [('male', 'Male'), ('female', 'Female')]
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)
    Height = forms.IntegerField()
    Weight = forms.IntegerField()
    Age=forms.IntegerField()
    activity_choices = [(1.2, 'Sedentary'), (1.375, 'Lightly active (light exercise/sports 1-3 days/week)'),(1.55,'moderately active (moderate exercise/sports 3-5 days/week)'),(1.725,"very active (hard exercise/sports 6-7 days a week)"),(1.9,"extra active (very hard exercise/sports & physical job or 2x training)"),]
    Activity = forms.ChoiceField(choices=activity_choices)


