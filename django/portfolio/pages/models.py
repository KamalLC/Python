from django.db import models

# Create your models here.
class HomePage(models.Model):
    title = models.CharField(max_length=200)
    para1 = models.TextField()
    para2 = models.TextField()
    skills_list = models.TextField()
    softwares_list = models.TextField()
    mail = models.EmailField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', default='images/html.png')
    #image_path = models.CharField(max_length=200)
    # btntext = models.CharField(max_length=200)
    paragraph = models.TextField()

    def __str__(self):
        return self.title