from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    eventTitle = models.CharField(max_length=25,)
    eventDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    address = models.CharField(max_length=25,)
    city = models.CharField(max_length=25,)
    state = models.CharField(max_length=25,)
    zip = models.CharField(max_length=5,)

class Position(models.Model):
    positionTitle = models.CharField(max_length=100)
    eventID = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return '{} ID# {}'.format(self.positionTitle, self.id)

class ClaimedPosition(models.Model):
    positionID = models.ForeignKey(Position, default=None, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
