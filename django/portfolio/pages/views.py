from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def blogs(request):
    return render(request, "blogs/blogs.html")

def contact(request):
    return render(request, "pages/contact.html")
