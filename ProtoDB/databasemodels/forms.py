from django import forms
from django.contrib.auth.models import User
from databasemodels.models import UserDescription
from databasemodels.models import Protocol


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        exclude = ["publisher","keywords"]
        #fields = ('title', 'description', 'keywords', 'text')
##    def create_view(request, **kwargs):
##        if request.method == "POST"
##            aaa = request.user
##            form = ProtocolForm(request.POST)
##            if form.is_valid():
##                bbb = form.save(commit = False)
##                bbb.key_field = aaa
##                bbb.save()
##                

##    def clean_publisher(self):
##        if not self.cleaned_data['publisher']:
##            return User()
##            #print('cleanp')
##        return self.cleaned_data['publisher']
##        #print('cleanp')
        
