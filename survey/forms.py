from django import forms
from django.forms import ModelForm
from .models import Question, Choice, Answer, Questionnaire


class CreateQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"   # if you want all the fields

class CreateChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"   # if you want all the fields

class SelectChoiceForm(ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"   # if you want all the fields

class QuestionnaireForm(ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']
        #fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four', 'textAnswer']
