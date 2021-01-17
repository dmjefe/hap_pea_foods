from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from . import forms

# Create your views here.
def donations(request):
    #form = forms.CreateDonation()
    #return render(request, 'donations/donations.html', {'form':form})

    template_name = 'donation/donations.html'
    if request.method == 'GET':
        donationForm = forms.CreateDonation(request.GET or None)
        formset = forms.ItemFormset(queryset=Item.objects.none())
    elif request.method == 'POST':
        donationForm = forms.CreateDonation(request.POST)
        formset = forms.ItemFormset(request.POST)
        if donationForm.is_valid() and formset.is_valid():
            # first save this donation, as its reference will be used in `Items`
            donation = donationForm.save()
            for form in formset:
                # so that `item` instance can be attached.
                item = form.save(commit=False)
                item.donation = donation
                item.save()
            #return redirect('home')
            return redirect('store:item_list')
    return render(request, template_name, {
        'donationForm': donationForm,
        'formset': formset,
    })
