from django.contrib.auth.models import User
from django import forms
from .models import addresources, addmatchingresources, editresources, Technologies

class addresourcesForm(forms.ModelForm):

    class Meta:
        model = addresources
        fields = ['Name_of_Resource', 'HS_Code']

class addmatchingresourcesForm(forms.ModelForm):

    class Meta:
        model = addmatchingresources
        fields = ['Name_of_Matching_Resource', 'Matching_HS_Code','Extraction_rate','Check_if_matches_interchangeable']

class editresourcesForm(forms.ModelForm):

    class Meta:
        model = editresources
        fields = ['Name_of_Resource', 'HS_Code']

class TechnologiesForm(forms.ModelForm):

    class Meta:
        model = Technologies
        fields = ['Method', 'Process']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
