from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [

    url(r'^$', views.donation_create, name="donations"),
    url(r'^(?P<donation_id>\d+)/$', views.add_items, name="items"),
    #url('items/', views.add_items, name="items"),

]
