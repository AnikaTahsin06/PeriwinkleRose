from django.shortcuts import render, redirect
from django.views.generic import TemplateView
 
from store.models.customer import Customer
from django.views import View

class CustomerProfile(TemplateView):
    template_name = "search.html"

  

     

    