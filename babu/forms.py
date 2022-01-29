from operator import length_hint
from django import forms
from .models import student
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class myForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ["name", "dob",  "mobile","note"]
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control","placeholder": "Enter Fullname"}),
            'dob': forms.DateInput(attrs={'class': "col form-control", 'type': "date"}),
            'mobile': forms.TextInput(attrs={'class': "form-control", "maxlength":"8","placeholder": "Enter Mobile number"}),
            'note': forms.TextInput(attrs={'class': "form-control","placeholder": "Enter Note"}),
            
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1","password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control" ,"placeholder": "Enter Username"}),
            'first_name': forms.TextInput(attrs={'class': "form-control mb-4","placeholder": "Enter Firstname"}),
            'last_name': forms.TextInput(attrs={'class': "form-control mb-4","placeholder": "Enter Lastname"}),
            'email': forms.EmailInput(attrs={'class': "form-control mb-4","placeholder": "Enter Email"}),
            'password1': forms.PasswordInput( attrs={'class': "form-control","placeholder": "Enter Password"}),
            'password2': forms.PasswordInput( attrs={'class': "form-control","placeholder": "Enter Confirm Password"}),
        }
