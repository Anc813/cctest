from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import HomeView, HTTPRequestView, HomeEditView


urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view(), name='home',
                           kwargs={'pk': '1'}),
                       url(r'^view/(?P<pk>\d+)$', HomeView.as_view(),
                           name='view'),
                       url(r'^http_responses$', HTTPRequestView.as_view(),
                           name='requests-list'),
                       url(r'^edit/(?P<pk>\d+)$',
                           login_required(HomeEditView.as_view()), name='edit'),
                       )
