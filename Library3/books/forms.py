from django import forms

# class AddbookForm(forms.Form):
#     Title=forms.CharField(max_length=50)
#     Author=forms.CharField(max_length=50)
#     Price=forms.IntegerField()
#     Page=forms.IntegerField()
#     Language_choices = [('english', 'English'), ('french', 'French'), ('malayalam', 'Malayalam'), ('hindi', 'Hindi')]
#     Language = forms.ChoiceField(choices=Language_choices)
#     Image=forms.ImageField()
from books.models import Book
class AddbookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"