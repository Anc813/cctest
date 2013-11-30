from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    birth_date = models.DateField()
    bio = models.TextField()
    #Contacts
    email = models.EmailField()
    jabber = models.EmailField(null=True, blank=True)
    skype = models.CharField(max_length=32, null=True, blank=True)
    other_contacts = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name)

class HTTPRequest(models.Model):
    # https://docs.djangoproject.com/en/1.6/ref/request-response/#django.http.HttpRequest
    body = models.TextField(null=True)
    path = models.CharField(max_length=8192, null=True)
    path_info = models.CharField(max_length=8192, null=True)
    method = models.CharField(max_length=4)
    encoding = models.CharField(max_length=32, null=True)
    GET = models.TextField(null=True)
    POST = models.TextField(null=True)
    COOKIES = models.TextField(null=True)
    FILES = models.TextField(null=True)
    META = models.TextField(null=True)
    user = models.ForeignKey(User, null=True)
    session = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s %s %s' % (self.timestamp, self.method, self.path)

    class Meta:
        ordering = ['-timestamp']