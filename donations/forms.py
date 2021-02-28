from django import forms
#from django.forms import modelformset_factory
from . import models
from .models import Item, Donation, ClaimedDonation

class CreateDonation(forms.ModelForm):
    class Meta:
        model = models.Donation
        fields = ['userName', 'locationName', 'donationDate' ]

class ClaimedDonation(forms.ModelForm):
    donation_list = Donation.objects.filter(claimeddonation = None)
    donationClaimed = forms.ModelChoiceField(queryset=donation_list)
    class Meta:
        model = models.ClaimedDonation
        fields = ['donationClaimed', 'claimingOrg', 'pickupDate',]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.queryset = ClaimedDonation.objects.filter(Donation.objects.filter(claimeddonation = None))
