from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import People
# Create your views here.

class HomeView(DetailView):
    model = People
    template_name = "main/home.html"
