from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()

class Choice(models.Model):
    question = models.ForeignKey('survey.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

class Questionnaire(models.Model):
    question = models.TextField()
    option_one = models.CharField(null=True, max_length=30)
    option_two = models.CharField(null=True, max_length=30)
    option_three = models.CharField(null=True, max_length=30)
    option_four = models.CharField(null=True, max_length=30)
    option_one_count = models.IntegerField(default = 0)
    option_two_count = models.IntegerField(default = 0)
    option_three_count = models.IntegerField(default = 0)
    option_four_count = models.IntegerField(default = 0)
    textAnswer = models.TextField(null = True)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count
