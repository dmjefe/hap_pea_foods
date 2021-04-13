from django.db import models


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
