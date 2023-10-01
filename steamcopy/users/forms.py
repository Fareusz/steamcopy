from django import forms
from . import models

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    username = forms.CharField(max_length=64, required=True)

    class Meta:
        model = models.profile
        fields = ['username', 'displayname', 'password']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=64, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = models.profile
        fields = ['username', 'password']