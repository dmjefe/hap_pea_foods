from django.contrib import admin
from .models import Question, Choice, Answer, Questionnaire

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass
