from django.contrib.auth.models import User
from django import forms
from .models import getinformation

class getinformationForm(forms.ModelForm):

    class Meta:
        model = getinformation
        fields = ['Search_by_HS_Code','Search_by_Name']


#class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    #class Meta:
        #model = User
        #fields = ['username', 'email', 'password']
