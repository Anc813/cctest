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

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name)

    @models.permalink
    def get_absolute_url(self):
        if self.pk==1:
            return ('main:home', [])
        else:
            return ('main:view', [self.pk])

class HTTPRequest(models.Model):
    # https://docs.djangoproject.com/en/1.6/ref/request-response/#django.http.HttpRequest
    path = models.CharField(max_length=8192, null=True, blank=True)
    path_info = models.CharField(max_length=8192, null=True, blank=True)
    method = models.CharField(max_length=4)
    encoding = models.CharField(max_length=32, null=True, blank=True)
    GET = models.TextField(null=True, blank=True)
    POST = models.TextField(null=True, blank=True)
    COOKIES = models.TextField(null=True, blank=True)
    FILES = models.TextField(null=True, blank=True)
    META = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    session = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    priority = models.IntegerField(default=0)

    def __unicode__(self):
        return '%s %s %s' % (self.timestamp, self.method, self.path)

    class Meta:
        ordering = ['-priority', '-timestamp']

class SignalProcessor(models.Model):
    ACTION_CHOICES = (
        ('C', 'object created'),
        ('U', 'object updated'),
        ('D', 'object deleted')
    )

    app_name = models.CharField(max_length=64)
    model_name = models.CharField(max_length=64)
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    object_pk = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s %s:%s pk:%s %s' % (self.timestamp, self.app_name, self.model_name, self.pk, self.action)