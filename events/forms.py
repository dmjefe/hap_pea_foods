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
    inner_qs = ClaimedPosition.objects.all()
    available_positions_list = Position.objects.exclude(id__in=inner_qs)
    positionID = forms.ModelChoiceField(queryset=available_positions_list)
    class Meta:
        model = models.ClaimedPosition
        fields = ['positionID', 'id',]
