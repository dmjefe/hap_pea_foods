from django.shortcuts import render
from django.http import HttpResponse
from .models import Story

# Create your views here.
def stories_list(request):
    stories = Story.objects.all().order_by('date')
    return render(request, 'stories/stories_list.html', {'stories':stories})

def story_detail(request, slug):
    #return HttpResponse(slug)
    story = Story.objects.get(slug=slug)
    return render(request, 'stories/story_detail.html', {'story':story})
