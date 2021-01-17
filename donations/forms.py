from django import forms
from django.forms import modelformset_factory
from . import models

class CreateItem(forms.ModelForm):
    class Meta:
        model = models.Item
        #fields= ['itemName']
        fields= ['itemName','typeOfMeasure', 'number']
        def __str__(self):
            return self.itemName

class CreateDonation(forms.ModelForm):
    class Meta:
        model = models.Donation
        fields = ('userName', )
        labels = {
            'userName': 'Your Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name here'
                }
            )
        }
ItemFormset = modelformset_factory(
    models.Item,
    fields=('itemName','number','typeOfMeasure', ),
    extra=1,
    widgets={
        'itemName': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Author Name here'
            }
        )
    }
)
