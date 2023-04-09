from django.contrib import admin
from .models import Schedule
from django.db import models

# Register your models here
class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    
    list_display = ('patient', 'student','meeting_date', 'finished',)
    list_filter = ('finished',)
    
    fieldsets = ( # Creation form fields
        (None, {'fields': ('patient', 'student','meeting_date',)}),
        
        ('Status', {'fields': ('finished',)}),
    )
    
    search_fields = ('patient','student','meeting_date',)
    ordering = ('meeting_date',)

admin.site.register(Schedule, ScheduleAdmin)