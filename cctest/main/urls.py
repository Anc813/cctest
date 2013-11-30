from django.conf.urls import patterns, include, url
from .views import HomeView, HTTPRequestView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home', kwargs={'pk' : '1'}),
    url(r'^http_responses$', HTTPRequestView.as_view(), name='requests-list'),
)
