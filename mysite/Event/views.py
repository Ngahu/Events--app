from django.shortcuts import render

def index(request):
    """the function incharge of the home page"""
    return render(request, 'Event/index.html', {})
