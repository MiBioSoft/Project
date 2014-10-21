from django import forms
from django.contrib.auth.models import User
from databasemodels.models import UserDescription
from databasemodels.models import Protocol
from django.utils.text import slugify
import itertools

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        exclude = ["publisher","keywords","slug"]

