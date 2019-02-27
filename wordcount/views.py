from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'title': 'Django Word Count App'})

def count(request):
    fulltext = request.GET['fulltext']
    return render(request, 'count.html', {'fulltext': fulltext})