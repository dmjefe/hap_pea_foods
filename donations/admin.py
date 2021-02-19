from django.contrib import admin
from .models import Donation, Item, Organization, ClaimedDonation

# Register your models here.
admin.site.register(Donation)
admin.site.register(Item)
admin.site.register(Organization)
admin.site.register(ClaimedDonation)
