from django.db import models
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

# Create your models here.

class Organization(models.Model):
    orgName = models.CharField(max_length=25,)
    address = models.CharField(max_length=25,)
    city = models.CharField(max_length=25,)
    state = models.CharField(max_length=25,)
    zip = models.CharField(max_length=25,)
    email = models.CharField(max_length=25,)
    website = models.CharField(max_length=25,)
    FOOD_BANK = 'Food Bank'
    GROCERY_STORE = 'Grocery Store'
    RESTAURANT = 'Restaurant'
    DISTRIBUTION_CENTER = 'Distribution Center'
    OTHER = 'Other'
    TYPE_OF_ORG = (
        (FOOD_BANK, 'Food Bank'),
        (GROCERY_STORE, 'Grocery Store'),
        (RESTAURANT, 'Restaurant'),
        (DISTRIBUTION_CENTER, 'Distribution Center'),
        (OTHER, 'Other'),
    )
    typeOfOrg = models.CharField(max_length=25, choices=TYPE_OF_ORG, default=FOOD_BANK)

    def __str__(self):
        return self.orgName

class Donation(models.Model):
    userName = models.CharField(max_length=25,verbose_name='Your User Name')
    donationDate = models.DateField(verbose_name='Date of Donation')
    locationName = models.CharField(max_length=25, verbose_name='Location of Donation')
    createdBy = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #claimed = models.BooleanField(default=False)

    def __str__(self):
        return 'ID Number: {}'.format(self.id)

class ClaimedDonation(models.Model):
    contact = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    donationClaimed = models.ForeignKey(Donation, default=None, on_delete=models.CASCADE)
    #contact = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    claimingOrg = models.ForeignKey(Organization, default=None, verbose_name='Organization Name', on_delete=models.CASCADE)
    pickupDate = models.DateField(verbose_name='Date of Pickup')


class Item(models.Model):
    COUNT = 'ct'
    GALLON = 'gal'
    POUND = 'lb'
    LITER = 'liter'
    BOX = 'box'
    DOZEN = 'doz'
    CASE = 'case'
    TYPE_OF_MEASURE_CHOICES = (
        (COUNT, 'Count'),
        (GALLON, 'Gallon'),
        (POUND, 'Pound'),
        (LITER, 'Liter'),
        (BOX, 'Box'),
        (DOZEN, 'Dozen'),
        (CASE, 'Case'),
    )
    itemName = models.CharField(max_length=100)
    number = models.SmallIntegerField()
    typeOfMeasure = models.CharField(max_length=5, choices=TYPE_OF_MEASURE_CHOICES, default=COUNT)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)

class Location(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
