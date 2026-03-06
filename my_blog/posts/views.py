import re

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
# Create your views here.

class HelloWorld(View):
    def get(self, request):
        return render(request, 'helloworld.html', {'message': 'Hello World!'})