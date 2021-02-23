from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [

    url(r'^$', views.create_event, name='create_event'),
    url(r'volunteer/^$', views.volunteer, name='volunteer'),
    url(r'^(?P<event_id>\d+)/$', views.add_positions, name='positions'),
    url(r'^event_positions/$', views.event_positions, name='event_positions'),
]
