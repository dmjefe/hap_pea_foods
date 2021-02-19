from django.db import models
from django.contrib.auth.models import User


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

class Donation(models.Model):
    userName = models.CharField(max_length=25,)
    donationDate = models.DateField()
    locationName = models.CharField(max_length=25,)
    createdBy = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    #claimed = models.BooleanField(default=False)

class ClaimedDonation(models.Model):
    donationClaimed = models.ForeignKey(Donation, default=None, on_delete=models.CASCADE)
    contact = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    claimingOrg = models.ForeignKey(Organization, default=None, on_delete=models.CASCADE)
    pickupDate = models.DateField()


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
