"""App views"""
from django.shortcuts import render

def frontpage(request):
    """Home page"""
    return render(request, 'frontpage.html')
