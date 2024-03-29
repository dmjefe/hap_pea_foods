from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    eventTitle = models.CharField(max_length=25,verbose_name='Title of Event',)
    eventDate = models.DateField(verbose_name='Date of Event',)
    startTime = models.TimeField(verbose_name='Start Time (hh:mm)')
    endTime = models.TimeField(verbose_name='End Time (hh:mm)')
    address = models.CharField(max_length=25,)
    city = models.CharField(max_length=25,)
    state = models.CharField(max_length=25,)
    zip = models.CharField(max_length=5,)
    def __str__(self):
        return 'Title: {}, Date: {}'.format(self.eventTitle, self.eventDate)

class Position(models.Model):
    positionTitle = models.CharField(max_length=100,verbose_name='Title of Position')
    eventID = models.ForeignKey(Event, default=None, verbose_name='Event',on_delete=models.CASCADE)
    def __str__(self):
        return 'Position: {}, Event: {}'.format(self.positionTitle, self.eventID.eventTitle)

class ClaimedPosition(models.Model):
    positionID = models.ForeignKey(Position, default=None, verbose_name='Position', on_delete=models.CASCADE)
    userID = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
