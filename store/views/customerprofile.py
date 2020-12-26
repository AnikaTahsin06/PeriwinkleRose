from django.shortcuts import render, redirect
from django.views.generic import TemplateView
  

class CustomerProfile(TemplateView):
    template_name = "customerprofile.html"