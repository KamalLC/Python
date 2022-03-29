from django.shortcuts import render
from django.http import HttpResponse
from .models import HomePage, Blog
# Create your views here.

def index(request):
    # homepage_data = HomePage.objects.all()
    # print(homepage_data)
    # print(type(homepage_data))
    homepage_data = HomePage.objects.get(id=1)
    context = {
        'title':homepage_data.title,
        'para1':homepage_data.para1,
        'para2':homepage_data.para2,
        'skills_list':homepage_data.skills_list,
        'softwares_list':homepage_data.softwares_list,
        'mail':homepage_data.mail,
    }
    return render(request, "pages/index.html",context)

def contact(request):
    #return HttpResponse("Hello, world. You're at the portfolio contact.")
    return render(request, "pages/contact.html")

def blog(request):
    blogs_list = Blog.objects.all()
    print(blogs_list)
    
    context = {
        'blogs_list':blogs_list,
    }
    
    return render(request, "blogs/blogs.html",context)

def blog_detail(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request, "blogs/blog_detail.html",context)