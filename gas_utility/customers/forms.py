from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
