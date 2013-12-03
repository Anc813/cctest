from django.contrib import admin
from .models import People, HTTPRequest, SignalProcessor

class SignalProcessorAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'model_name', 'action', 'object_pk', 'timestamp')

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'birth_date', 'email', 'jabber', 'skype')

# Register your models here.
admin.site.register(People, PeopleAdmin)
admin.site.register(HTTPRequest)
admin.site.register(SignalProcessor, SignalProcessorAdmin)