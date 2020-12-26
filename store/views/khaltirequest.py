from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from store.models.orders import Order

class KhaltiRequest(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, "khaltirequest.html", context)
