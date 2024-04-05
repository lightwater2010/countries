from django import forms

from all_countries.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from all_countries.models import Users
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Form_countries(forms.ModelForm):

    class Meta:
        model = Countries
        fields = ('name',)

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин',max_length=30)
    email = forms.CharField(label='Email',max_length=100)
    password1 = forms.CharField(label='Пароль',max_length=12,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение Пароля',max_length=12,widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class Log_in(AuthenticationForm):
    username = forms.CharField(max_length=30,label='Логин')
    password = forms.CharField(max_length=30,label='Пароль',widget=forms.PasswordInput)

