from django.db import models

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