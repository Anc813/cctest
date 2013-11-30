from django.contrib import admin
from .models import People, HTTPRequest

# Register your models here.
admin.site.register(People)
admin.site.register(HTTPRequest)