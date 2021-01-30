from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Item, Donation
from . import forms

# Create your views here.
@login_required(login_url="/accounts/login/")
def donation_create(request):
    if request.method == 'POST':
        form = forms.CreateDonation(request.POST) #Use if no images on form
        if form.is_valid():
            form.save()
            #redirect('home')
    else:
        form = forms.CreateDonation()
    return render(request, 'donations/donations.html', {'form':form})

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
