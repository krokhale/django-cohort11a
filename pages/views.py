from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
#     html / json / xml
    template_name = 'home.html'

# def homePageView(TemplateView):
#     template_name = 'home.html'
#     return HttpResponse('Hello, World!')
