from django import forms
#from django.forms import modelformset_factory
from . import models

class CreateDonation(forms.ModelForm):
    class Meta:
        model = models.Donation
        fields = ['userName', 'locationName', 'donationDate' ]
