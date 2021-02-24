from django import forms
#from django.forms import modelformset_factory
from . import models
from .models import Event, Position, ClaimedPosition

class CreateEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['eventTitle', 'eventDate', 'startTime', 'endTime', 'address', 'city',
        'state', 'zip', ]

class ClaimPosition(forms.ModelForm):
    class Meta:
        model = models.ClaimedPosition
        fields = ['positionID', 'id']
