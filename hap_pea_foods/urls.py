"""hap_pea_foods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views


#styling changes to ADMIN site
admin.site.site_header = 'HAP-PEA FOODS' # changes blue banner
admin.site.index_title = 'ADMIN DASHBOARD' # changes title under blue banner
admin.site.site_title = 'Hap-Pea Foods Admin' # changes browser tab title

urlpatterns = [
    path('admin/', admin.site.urls),
    url('about/', views.about, name="about"),
    url('donate/', include('donations.urls')),
    url('survey/', include('survey.urls')),
    url('find_help/', views.find_help, name="find_help"),
    url('partners/', views.partners, name="partners"),
    url('accounts/', include('accounts.urls')),
    url('stories/', include('stories.urls')),
    url('events/', include('events.urls')),
    url('volunteer/', views.volunteer, name="volunteer"),
    url('portal/', views.portal, name="portal"),
    url('contact/', views.contact, name="contact"),
    url('createevent/', views.createevent, name="createevent"),
    url('moneydonations/', views.moneydonations, name="moneydonations"),
    url('organizations/', views.organizations, name="organizations"),
    url('mycalendar/', views.mycalendar, name="mycalendar"),
    url('non_disc_stmt/', views.non_disc_stmt, name="non_disc_stmt"),
    url('privacy/', views.privacy, name="privacy"),
    url('facts/', views.facts, name="facts"),
    url('terms_cond/', views.terms_cond, name="terms_cond"),
    #path('', include('qr_code.urls', namespace='qr_code')),
    url('', views.homepage, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
