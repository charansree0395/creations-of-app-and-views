from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sai(request):
    return HttpResponse("This is an django Framework")

def king(request):
    return HttpResponse("King is always an super ")

def india(request):
    return HttpResponse("India has many states and states have many districts !!.....")