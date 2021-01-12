from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Item
from . import forms

# Create your views here.
def donations(request):
    form = forms.CreateDonation()
    return render(request, 'donations/donations.html', {'form':form})
