from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return HttpResponse("Hello, world. You're at the portfolio contact.")
