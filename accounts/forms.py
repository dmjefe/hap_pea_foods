from django import forms
#from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #first_name = forms.CharField(max_length=100)
    #last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        #field order on the form
        fields = (
         'email',
         'first_name',
         'last_name',
         'username',
         'password1',
         'password2'
    )

class Profile(forms.ModelForm):

    class Meta:
        model = models.Profile
        #field order on the form
        fields = (
        'dob',
        'address',
        'city',
        'state',
    )
