from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('Homepage')
    return render(request, 'homepage.html')

def about(request):
    #return HttpResponse('About')
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def find_help(request):
    return render(request, 'find_help.html')

def partners(request):
    return render(request, 'partners.html')

def stories(request):
    return render(request, 'stories.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def portal(request):
    return render(request, 'portal.html')

def loutoutlanding(request):
    return render(request, 'logoutlanding.html')
