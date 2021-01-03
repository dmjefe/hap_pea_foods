
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'stories'

urlpatterns = [

    url(r'^$', views.stories_list, name="stories"),
    url(r'^(?P<slug>[\w-]+)/$', views.story_detail, name="detail"),
]
