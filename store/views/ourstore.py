from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class OurStore(View):
    def get(self,request):
        return render(request,'ourstore.html')
