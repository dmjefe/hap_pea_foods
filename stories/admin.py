from django.contrib import admin
from .models import Story



class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['title', 'date']
    search_fields = ['title', 'date']


admin.site.register(Story, StoryAdmin)
