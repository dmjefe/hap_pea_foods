from django.db import models

# Create your models here.

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
