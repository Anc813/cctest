from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import People, HTTPRequest
# Create your views here.

class HomeView(DetailView):
    model = People
    template_name = "main/home.html"

class HTTPRequestView(ListView):
    model = HTTPRequest
    template_name = "main/requests.html"

    def get_queryset(self):
        return HTTPRequest.objects.all()[:10]