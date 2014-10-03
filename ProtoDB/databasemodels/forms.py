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

##    def save(self):
##        instance = super(ProtocolForm, self).save(commit=False)
##        instance.slug = orig = slugify(instance.title)
##
##        for x in itertools.count(1):
##            if not Protocol.objects.filter(slug=instance.slug).exists():
##                break
##            instance.slug = '%s-%d' % (orig,x)
##        instance.save()
##
##        return instance
