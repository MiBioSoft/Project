from django import forms
from django.contrib.auth.models import User
from databasemodels.models import UserDescription

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
