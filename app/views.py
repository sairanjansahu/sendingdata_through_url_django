from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def url(request,name):
    return HttpResponse(f'hi how are u {name}')