from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Item, Donation
from django.urls import reverse
from urllib.parse import urlencode
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def donation_create(request):
    if request.method == 'POST':
        form = forms.CreateDonation(request.POST) #Use if no images on form
        if form.is_valid():
            #form.save()
            instance = form.save(commit=False)
            instance.createdBy = request.user
            instance.save()
            pk = instance.pk
            #return redirect('donations/items.html', pk = instance.objects.get(pk=pk))
            #return redirect('donations/items.html', pk = Donation.objects.last(pk=pk))
            #pk = instance.objects.get(pk=pk)
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


def donations_list(request):
    donation = Donation.objects.all().order_by('donationDate')
    return render(request, 'donations/donations_list.html', {'donation':donation})
    #donation = Donation.objects.get(claimed)
    #if donation.claimed == False :
        #return render(request, 'donations/donations_list.html', {'donation':donation})
