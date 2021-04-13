from django.contrib import admin
from .models import  Questionnaire

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    pass
