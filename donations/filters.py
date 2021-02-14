from .models import Donation
import django_filters

class DonationFilter(django_filters.FilterSet):
    class Meta:
        model = Donation
        fields = ['locationName', 'claimed', ]
        #fields = ['createdBy', 'locationName', 'donationDate', 'claimed', ]
