from django.shortcuts import render, redirect
from .models import Question, Answer, Choice, Questionnaire
from .forms import CreateQuestionForm, CreateChoiceForm, SelectChoiceForm, QuestionnaireForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def survey_create_view(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your survey question was created succesfully!')
            return redirect('list')
    else:
        form = QuestionnaireForm()
    return render(request, 'survey/create.html', {'form':form})

def survey_list_view(request): # list view
    questions = Questionnaire.objects.all()
    return render(request, 'survey/list.html', {'questions':questions})

def answer_view(request, questionnaire_id):
    question = Questionnaire.objects.get(pk=questionnaire_id)
    if request.method == "POST":
        selected_option = request.POST['answer']
        if selected_option == "option1":
            question.option_one_count += 1
        elif selected_option == "option2":
            question.option_two_count += 1
        elif selected_option == "option3":
            question.option_three_count += 1
        elif selected_option == "option4":
            question.option_four_count += 1
        question.save()
        messages.success(request, f'Your answer was submitted succesfully!')
        return redirect('list')
    return render(request, 'survey/answer.html', {'question':question})

@login_required
def results_view(request, questionnaire_id): # for admin only
    result = Questionnaire.objects.get(pk=questionnaire_id)
    return render(request, 'survey/results.html', {'result':result})

def qrCode(request): # list view
    return render(request, 'survey/qrCode.html')

# def question_choice_view(request):
#     if request.method == 'POST':
#         form = CreateChoiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your choice was created succesfully!')
#             return redirect('list')
#     else:
#         form = CreateChoiceForm()
#     return render(request, 'survey/choice.html', {'form':form})
