from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse(request, 'home.html', {'title': 'Django Word Count'})