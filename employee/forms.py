from django import forms
from employee.models import Employee
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "desig": forms.TextInput(attrs={"class": "form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.TextInput(attrs={"class":"form-control"})
        }
