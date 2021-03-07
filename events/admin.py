from django.contrib import admin
from .models import Event, Position, ClaimedPosition


class EventAdmin(admin.ModelAdmin):
    list_display = ['eventTitle', 'eventDate', 'location']
    list_filter = ['eventTitle', 'eventDate']
    search_fields = ['eventDate', 'city', 'state', 'eventTitle']

    def location(self, obj):
        return"{}, {}".format(obj.city, obj.state)


class ClaimedPositionAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'positionID']

    def get_name(self, obj):
        return obj.userID.username
    get_name.admin_order_field  = 'userID'  #Allows column order sorting
    get_name.short_description = 'User Name'  #Renames column head

admin.site.register(Event, EventAdmin)
admin.site.register(Position)
admin.site.register(ClaimedPosition, ClaimedPositionAdmin)
