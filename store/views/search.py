from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView
from store.models.products import Product

class Search(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Product.objects.filter( Q(name__icontains=kw)  | Q(description__icontains=kw) )
        context["results"] = results
        return context