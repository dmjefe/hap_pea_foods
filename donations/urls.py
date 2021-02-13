from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [

    url(r'^$', views.donation_create, name="donations"),
    url(r'^(?P<donation_id>\d+)/$', views.add_items, name="items"),
    url('donations_list/', views.donations_list, name="donations_list"),
    #url('items/', views.add_items, name="items"),

]
