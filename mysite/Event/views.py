from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """the function incharge of the home page"""
    return render(request, 'Event/base.html', {})

def detail(request, Event_detail,):
    """returning the event detail"""
    return HttpResponse("<h2> details for event:" + str(Event_detail) + "</h2>")

