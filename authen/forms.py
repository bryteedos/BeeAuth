import email
from logging import PlaceHolder
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class editprofileform(UserChangeForm):
    password=forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model=User
        fields=('email','first_name','last_name','password')

class signupform(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)

    class Meta:
        model=User
        fields=('username', 'email','first_name', 'last_name', 'password1', 'password2')