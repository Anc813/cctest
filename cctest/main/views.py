from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView
from .models import People, HTTPRequest
from django.core.urlresolvers import reverse
from .widgets import JQueryUIDateWidget
from django.forms.models import modelform_factory

# Create your views here.

class HomeView(DetailView):
    model = People
    template_name = "main/home.html"

class HTTPRequestView(ListView):
    model = HTTPRequest
    template_name = "main/requests.html"

    def get_queryset(self):
        return HTTPRequest.objects.all()[:10]

class HomeEditView(UpdateView):
    model = People
    template_name = "main/edit.html"
    form_class =  modelform_factory(People,
                                    widgets={"birth_date": JQueryUIDateWidget })
