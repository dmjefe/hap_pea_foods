from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    dob = forms.DateField()
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)
    zip = forms.CharField(max_length=9)


    class Meta:
        model = User
        #field order on the form
        fields = (
        'first_name',
        'middle_name',
        'last_name',
        'dob',
        'phone',
        'address',
        'city',
        'state',
        'zip',
        'email',
        'username',
        'password1',
        'password2')
