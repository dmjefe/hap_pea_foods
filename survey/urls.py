from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.survey_list_view, name='list'),
    path('create', views.survey_create_view, name='create'),
    path('answer/<questionnaire_id>/', views.answer_view, name='answer'),
    path('results/<questionnaire_id>/', views.results_view, name='results'),    
    path('qrCode/', views.qrCode, name='qrCode'),
]
