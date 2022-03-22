from django.contrib import admin
from django.urls import path

from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blogs', views.blogs, name='blogs'),
    # path('contact', views.contact, name='contact'),
]