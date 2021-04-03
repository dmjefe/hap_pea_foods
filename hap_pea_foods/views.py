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

def contact(request):
    return render(request, 'contact.html')

def survey(request):
    return render(request, 'survey.html')

def surveyresults(request):
    return render(request, 'surveyresults.html')

def createevent(request):
    return render(request, 'createevent.html')

def facts(request):
    return render(request, 'facts.html')

def moneydonations(request):
    return render(request, 'moneydonations.html')

def mycalendar(request):
    return render(request, 'mycalendar.html')

def non_disc_stmt(request):
    return render(request, 'non_disc_stmt.html')

def organizations(request):
    return render(request, 'organizations.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms_cond(request):
    return render(request, 'terms_cond.html')

def googleb992673f1334124f.html(request):
    return render(request, 'googleb992673f1334124f.html')
