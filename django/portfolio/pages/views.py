from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HomePage, Blog
from .forms import BlogForm,BlogModelForm
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


def blog_create(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            # # do something useful
            # print('form is valid')
            # print(form.cleaned_data)
            # print('Title:', form.cleaned_data['title'])
            # print('Paragraph:', form.cleaned_data['paragraph'])
            # return HttpResponse('success')
            Blog.objects.create(**form.cleaned_data)
            #form.save()
            return redirect('/blog')
        else:
             print('form is not valid')
             print(form.errors)
             return HttpResponse('error')
    else:
        form = BlogModelForm()

    return render(request, 'blogs/blog_create.html', {'form': form})

def blog_update(request,id):
    blog = Blog.objects.get(id=id)
    print(blog.title)
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            #Blog.objects.filter(id=id).update(**form.cleaned_data)
            form.save()
            #return redirect('/blog')
            return redirect('/blog_detail/'+str(form.instance.id))
        else:
            print('form is not valid')
            print(form.errors)
            return HttpResponse('error')
    else:
        form = BlogModelForm(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})



#delete blog
def blog_delete(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('/blog')