from operator import length_hint
from django import forms
from .models import student
from django.contrib.auth.models import User


class myForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "dob",  "mobile","note"]
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'dob': forms.DateInput(attrs={'class': "col form-control", 'type': "date"}),
            'mobile': forms.TextInput(attrs={'class': "form-control", "maxlength":"8"}),
            'note': forms.TextInput(attrs={'class': "form-control"}),
            
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'last_name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': "form-control"})
        }
