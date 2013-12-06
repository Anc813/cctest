from django.contrib import admin
from .models import People, HTTPRequest, SignalProcessor


class SignalProcessorAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'model_name', 'action', 'object_pk',
                    'timestamp')


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'birth_date', 'email', 'jabber',
                    'skype')


class HTTPRequestsAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'priority', 'path', 'method', 'GET', 'POST',
                    'COOKIES', 'FILES', 'user', 'session')
    list_filter = ('priority', 'path', 'user')


admin.site.register(People, PeopleAdmin)
admin.site.register(HTTPRequest, HTTPRequestsAdmin)
admin.site.register(SignalProcessor, SignalProcessorAdmin)
