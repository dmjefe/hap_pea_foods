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
    question = models.ForeignKey('survey.Question', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.text
    
    @property
    def vote(self):
        return self.answer_set.count()

class Answer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text

