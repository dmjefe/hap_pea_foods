from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Item, Donation, ClaimedDonation
from .filters import DonationFilter
from django.urls import reverse
from urllib.parse import urlencode
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def donation_create(request):
    if request.method == 'POST':
        form = forms.CreateDonation(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.createdBy = request.user
            instance.save()
            pk = instance.pk
            url = str(pk) + '/'
            return redirect(url)
    else:
        form = forms.CreateDonation()
    return render(request, 'donations/donations.html', {'form':form})

@login_required(login_url="/accounts/login/")
def add_items(request, donation_id):
    donation = Donation.objects.get(pk=donation_id)
    ItemFormset = inlineformset_factory(Donation, Item, fields=('itemName','number','typeOfMeasure',), extra=1,)

    if request.method == 'POST':
        formset = ItemFormset(request.POST, instance=donation)
        if formset.is_valid():
            formset.save()
            #return redirect('items', donation_id=donation.pk)

    formset = ItemFormset(instance=donation)

    return render(request, 'donations/items.html', {'formset' : formset})


def search(request):
    #display only unclaimed donations.
    if request.method == 'POST':
        form = forms.ClaimedDonation(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.contact = request.user
            instance.save()
            pk = instance.pk
            #Should probably redirect to a "success" page or something.
            return redirect('home')
    else:
        donation_list = Donation.objects.filter(claimeddonation = None)
        donation_filter = DonationFilter(request.GET, queryset=donation_list)
        form = forms.ClaimedDonation()
        return render(request, 'donations/donations_list.html', {'filter': donation_filter, 'form':form})
