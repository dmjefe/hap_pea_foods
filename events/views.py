from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#from django.forms import inlineformset_factory
from .models import Event, Position, ClaimedPosition
#from .filters import DonationFilter
from django.urls import reverse
#from urllib.parse import urlencode
from . import forms

def volunteer(request):
    return render(request, 'events/volunteer.html',)

def create_event(request):
    if request.method == 'POST':
        form = forms.CreateEvent(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.createdBy = request.user
            instance.save()
            pk = instance.pk
            url = str(pk) + '/'
            return redirect(url)
    else:
        form = forms.CreateEvent()
    return render(request, 'events/create_event.html', {'form':form})
