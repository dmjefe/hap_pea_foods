from django.contrib import admin
from .models import Event, Position, ClaimedPosition

admin.site.register(Event)
admin.site.register(Position)
admin.site.register(ClaimedPosition)
