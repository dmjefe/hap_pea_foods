from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [

    url(r'^$', views.volunteer, name='volunteer'),
    url(r'^create_event/$', views.create_event, name='create_event'),
]
