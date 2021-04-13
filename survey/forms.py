from django import forms
from django.forms import ModelForm
from .models import Questionnaire


class QuestionnaireForm(ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']
