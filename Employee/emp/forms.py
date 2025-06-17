from django import forms
from emp.models import Employe
class AddemployeeForm(forms.ModelForm):
    class Meta:
        model=Employe
        fields=['Name','Age','Salary','Designation','place','Image','Department_name']