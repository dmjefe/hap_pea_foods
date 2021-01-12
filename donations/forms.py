from django import forms
from . import models

class CreateDonation(forms.ModelForm):
    class Meta:
        model = models.Item
        #fields= ['itemName']
        fields= ['itemName','typeOfMeasure', 'number']
        def __str__(self):
            return self.itemName
