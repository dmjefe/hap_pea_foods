from django.shortcuts import render, redirect
from .models import Question, Answer, Choice
from .forms import CreateQuestionForm, CreateChoiceForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def survey_list_view(request): # list view
    questions = Question.objects.all()
    return render(request, 'survey/list.html', {'questions':questions})

def survey_create_view(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your question was created succesfully!')
            return redirect('list')
    else:
        form = CreateQuestionForm()
    return render(request, 'survey/create.html', {'form':form})

def question_choice_view(request):
    if request.method == 'POST':
        form = CreateChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your choice was created succesfully!')
            return redirect('list')
    else:
        form = CreateChoiceForm()
    return render(request, 'survey/choice.html', {'form':form})

def answer_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'survey/answer.html', {'question':question})

@login_required
def results_view(request, question_id): # for admin only
    result = Question.objects.get(pk=question_id)
    return render(request, 'survey/results.html', {'result':result})
