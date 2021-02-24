from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Event, Position, ClaimedPosition
from .filters import EventFilter, PositionFilter
from django.urls import reverse
from urllib.parse import urlencode
from . import forms

def volunteer(request):
    return render(request, 'events/volunteer.html',)

def create_event(request):
    if request.method == 'POST':
        form = forms.CreateEvent(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            #instance.createdBy = request.user
            instance.save()
            pk = instance.pk
            url = str(pk) + '/'
            return redirect(url)
    else:
        form = forms.CreateEvent()
    return render(request, 'events/create_event.html', {'form':form})

@login_required(login_url="/accounts/login/")
def add_positions(request, event_id):
    event = Event.objects.get(pk=event_id)
    PositionFormset = inlineformset_factory(Event, Position, fields=('positionTitle',), extra=1,)

    if request.method == 'POST':
        formset = PositionFormset(request.POST, instance=event)
        if formset.is_valid():
            formset.save()

    formset = PositionFormset(instance=event)

    return render(request, 'events/add_positions.html', {'formset' : formset})

def event_positions(request):
    if request.method == 'POST':
        form = forms.ClaimPosition(request.POST) #Use if no images on form
        if form.is_valid():
            instance = form.save(commit=False)
            instance.userID = request.user
            instance.save()
            #pk = instance.pk
            #Should probably redirect to a "success" page or something.
            return redirect('home')
    else:
        inner_qs = ClaimedPosition.objects.all()
        #available_positions_list = Position.objects.exclude(eventID_id = inner_qs)
        available_positions_list = Position.objects.exclude(queryset = None)
        position_filter = PositionFilter(request.GET, queryset=available_positions_list)
        form = forms.ClaimPosition()
        #return render(request, 'events/event_positions.html', {'filter': position_filter})
        return render(request, 'events/event_positions.html', {'filter': position_filter, 'form': form})


#all_persons = Person.objects.all().values_list('car__id', flat=True)
#auto_without_pers = Automobile.objects.exclude(id__in=all_persons)
