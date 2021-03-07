from django.contrib import admin
from .models import Donation, Item, Organization, ClaimedDonation

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['orgName', 'location', 'website', 'typeOfOrg']
    list_filter = ['orgName', 'typeOfOrg']
    search_fields = ['orgName', 'city', 'state', 'typeOfOrg']

    def location(self, obj):
        return"{}, {}".format(obj.city, obj.state)

class DonationAdmin(admin.ModelAdmin):
    list_display = ['userName', 'locationName', 'donationDate', 'createdBy']
    list_filter = ['userName', 'locationName', 'donationDate', 'createdBy']
    search_fields = ['userName', 'locationName', 'donationDate', 'createdBy']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['itemName', 'number','typeOfMeasure']
    list_filter = ['itemName', 'typeOfMeasure']
    search_fields = ['itemName', 'number','typeOfMeasure']

class ClaimedDonationAdmin(admin.ModelAdmin):
    list_display = ['donationClaimed', 'contact', 'get_name','pickupDate']
    list_filter = ['contact', 'pickupDate']
    search_fields = ['contact', 'claimingOrg','pickupDate']

    def get_name(self, obj):
        return obj.claimingOrg.orgName
    get_name.admin_order_field  = 'claimingOrg'  #Allows column order sorting
    get_name.short_description = 'Organization Name'  #Renames column head


admin.site.register(Donation, DonationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ClaimedDonation, ClaimedDonationAdmin)
