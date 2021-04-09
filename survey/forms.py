from django import forms
from django.forms import ModelForm
from .models import Question, Choice, Answer


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
