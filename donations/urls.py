from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'donations'

urlpatterns = [

    url(r'^$', views.donations, name="donations"),

]
