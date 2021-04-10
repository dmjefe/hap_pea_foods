from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.survey_list_view, name='list'),
    path('create', views.survey_create_view, name='create'),
    path('choice', views.question_choice_view, name='choice'),
    path('answer/<questionnaire_id>/', views.answer_view, name='answer'),
    path('results/<questionnaire_id>/', views.results_view, name='results'),
]
