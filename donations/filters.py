from .models import Donation
import django_filters

class DonationFilter(django_filters.FilterSet):
    class Meta:
        model = Donation
        fields = ['locationName', 'createdBy', 'donationDate', 'userName' ]
        #fields = ['createdBy', 'locationName', 'donationDate', 'claimed', ]
