from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import AppUser


class RegisterForm(UserCreationForm):

    '''Form for user creation'''

    username=forms.CharField(label='Username',min_length=1,max_length=150)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Password',min_length=4,max_length=150)
    password2=forms.CharField(label='Confirm Password',min_length=4,max_length=150)


class AppUserForm(ModelForm):

    '''Forms for appuser'''

    class Meta:
        model=AppUser
        fields=('bio','location',)




