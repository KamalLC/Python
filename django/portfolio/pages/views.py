from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context  = {
    'title': 'Hi, I am Kamal, a student to be a fullstack developer',
    'para1':'I am currently learning Django and Python to be a fullstack python developer. I want to master the technique to make unique and fully responsive personal and business websites using python, django, html, css andjavascript,react.',
    'para2':' As a programming student, I love learning new technologies and involving myself in solving different problems using programming. I am doing everything that i can do to make my career in programming.',
    'skills_list':' HTML, CSS,Bootstrap, Javascript, jQuery, Git, Github, Python, Django, Django REST, React, Nodejs, Postgres, MongoDb, Docker',
    'softwares_list':'VsCode,Chrome,Firefox,Linux, Fedora, Postman,etc',
    'mail':'klamichhane08@gmail.com',
    }
    return render(request, "pages/index.html", context)

def blogs(request):
    blogs_list = [
        {   'id':1,
            'title':'HTML',
            'subtitle':'The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.',
            'date':'15 Feb 2022',
            'image':'Images/html.png',
            'btntext':'Read more about this blog.↗',
            'paragraph':"HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentatio (CSS) or functionality/behavior (JavaScript). <br> <br> Hypertext refers to links that connect web pages to one another, either within a single website or between websites. Links are a fundamental aspect of the Web. By uploading content to the Internet and linking it to pages created by other people, you become an active participant in the World Wide Web."
        },
         {
            'id':2,
            'title':'Web Servers',
            'subtitle':'Web servers are programs that provide documents to requesting browsers identified using URLs. Servers are slave Programs.',
            'date':'15 Mar 2022',
            'image':'Images/forest.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':"Web servers are programs that provide documents to requesting browsers identified using URLs. Servers are slave Programs : They act only when requests are made to them by browser running on others computers on the Internet. The most commonly used Web servers are Apache , which runs under Windows operating systems.<br><br> First, Web browsers initiate network communications with servers by sending URLs. One of two different things can be specified by URL: the address of data file stored on the server or a stored program on the server that clients wants executed and the output of the program returned to the client. The standard Web protocol HTTP(Hypertext Transfer Protocol), is responsible for all the communication between Web client and Web servers. When Web server begins execution , it informs the operating system under which it is running that it is now ready to accept incoming network connections through a specific port on the machine. In this running state , the server runs as a background process in the operating system. Then a network connection is established between Web client or browser and Web server. And sends information requests and possibly data to the server, receives information from the server and close the connection.<br><br>Document root is he file structure of the serer has two separate directories. The root of one of this is document root. Server root is another root directory of web server file structure. Virtual document tree: Many servers allow a part of the servable document stored out side of the document root this is called virtual document tree. Virtual hosts: many servers can support more than one site on a computer potentially reducing the cost of each site and makes their maintenance more convenient. such secondary hosts are called virtual hosts. Proxy server: some servers can serve documents that are in the document root of the other machines are on the web are called proxy servers. Web servers not only support HTTP but also ftp, Gopher, News and mail."
        },
        {
            'id':3,
            'title':'Computational Simulation',
            'subtitle':'A computational simulation is a dynamic, process-oriented model instantiated on a computer. These can range from traditional economic models (expressed as equations) to more abstract constructs and processes.',
            'date':'15 Apr 2022',
            'image':'Images/tiger2.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':"OOP framework is different from the traditional conventional behavior of computer. Traditional model can be viewed as the computer is a data manager, following some pattern of instructions, wandering through memory, pulling values out of various memory transforming them in some manner, and pushing the results back into other memory<br><br>The behavior of a computer executing a program is a process-state or pigeon-hole model. By examining the values in the slots, one can determine the state of the machine or the results produced by a computation. This model may be a more or less accurate picture of what takes place inside a computer. Real word problem solving is difficult in the traditional model.In Object Oriented Model we speak of objects, messages, and responsibility for some action. We never mention memory addresses, variables, assignments, or any of the conventional programming terms. This model is process of creating a host of helpers that forms a community and assists the programmer in the solution of a problem (Like in flower example)."

        }
    ]
    context = {
        'blogs_list':blogs_list,
    }
    return render(request, "blogs/blogs.html", context)

def contact(request):
    return render(request, "pages/contact.html")

def blogDetail(request, id):
    blogs_list = [
        {   'id':1,
            'title':'HTML',
            'subtitle':'The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.',
            'date':'15 Feb 2022',
            'image':'Images/html.png',
            'btntext':'Read more about this blog.↗',
            'paragraph':"HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content. Other technologies besides HTML are generally used to describe a web page's appearance/presentatio (CSS) or functionality/behavior (JavaScript). <br> <br> Hypertext refers to links that connect web pages to one another, either within a single website or between websites. Links are a fundamental aspect of the Web. By uploading content to the Internet and linking it to pages created by other people, you become an active participant in the World Wide Web."
        },
         {
            'id':2,
            'title':'Web Servers',
            'subtitle':'Web servers are programs that provide documents to requesting browsers identified using URLs. Servers are slave Programs.',
            'date':'15 Mar 2022',
            'image':'Images/forest.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':"Web servers are programs that provide documents to requesting browsers identified using URLs. Servers are slave Programs : They act only when requests are made to them by browser running on others computers on the Internet. The most commonly used Web servers are Apache , which runs under Windows operating systems.<br><br> First, Web browsers initiate network communications with servers by sending URLs. One of two different things can be specified by URL: the address of data file stored on the server or a stored program on the server that clients wants executed and the output of the program returned to the client. The standard Web protocol HTTP(Hypertext Transfer Protocol), is responsible for all the communication between Web client and Web servers. When Web server begins execution , it informs the operating system under which it is running that it is now ready to accept incoming network connections through a specific port on the machine. In this running state , the server runs as a background process in the operating system. Then a network connection is established between Web client or browser and Web server. And sends information requests and possibly data to the server, receives information from the server and close the connection.<br><br>Document root is he file structure of the serer has two separate directories. The root of one of this is document root. Server root is another root directory of web server file structure. Virtual document tree: Many servers allow a part of the servable document stored out side of the document root this is called virtual document tree. Virtual hosts: many servers can support more than one site on a computer potentially reducing the cost of each site and makes their maintenance more convenient. such secondary hosts are called virtual hosts. Proxy server: some servers can serve documents that are in the document root of the other machines are on the web are called proxy servers. Web servers not only support HTTP but also ftp, Gopher, News and mail."
        },
        {
            'id':3,
            'title':'Computational Simulation',
            'subtitle':'A computational simulation is a dynamic, process-oriented model instantiated on a computer. These can range from traditional economic models (expressed as equations) to more abstract constructs and processes.',
            'date':'15 Apr 2022',
            'image':'Images/tiger2.jpg',
            'btntext':'Read more about this blog.↗',
            'paragraph':"OOP framework is different from the traditional conventional behavior of computer. Traditional model can be viewed as the computer is a data manager, following some pattern of instructions, wandering through memory, pulling values out of various memory transforming them in some manner, and pushing the results back into other memory<br><br>The behavior of a computer executing a program is a process-state or pigeon-hole model. By examining the values in the slots, one can determine the state of the machine or the results produced by a computation. This model may be a more or less accurate picture of what takes place inside a computer. Real word problem solving is difficult in the traditional model.In Object Oriented Model we speak of objects, messages, and responsibility for some action. We never mention memory addresses, variables, assignments, or any of the conventional programming terms. This model is process of creating a host of helpers that forms a community and assists the programmer in the solution of a problem (Like in flower example)."

        }
    ]
    for blog in blogs_list:
        if blog['id'] == int(id):
            context = {
                'blog':blog,
            }
    return render(request, "blogs/blog-detail.html", context)