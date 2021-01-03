from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Story
from . import forms

# Create your views here.
def stories_list(request):
    stories = Story.objects.all().order_by('date')
    return render(request, 'stories/stories_list.html', {'stories':stories})

def story_detail(request, slug):
    #return HttpResponse(slug)
    story = Story.objects.get(slug=slug)
    return render(request, 'stories/story_detail.html', {'story':story})

@login_required(login_url="/accounts/login/")
def story_create(request):
    if request.method == 'POST':
        #form = forms.CreateStory(request.POST, request.FILES) #use this if you have thumbnails on form
        form = forms.CreateStory(request.POST) #Use if no images on form
        if form.is_valid():
            form.save()
            #redirect('home')
    else:
        form = forms.CreateStory()
    return render(request, 'stories/story_create.html', {'form':form})
