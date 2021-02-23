from .models import Event, Position
import django_filters

class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['eventTitle', 'eventDate', 'city', 'startTime' ]
        #fields = ['createdBy', 'locationName', 'donationDate', 'claimed', ]

class PositionFilter(django_filters.FilterSet):
    class Meta:
        model = Position
        fields = ['eventID', 'positionTitle', ]
