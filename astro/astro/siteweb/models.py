from django.db import models

# Create your models here.
class Home(models.Model):
    descriptions = models.TextField()
    image_un = models.FileField(upload_to ='image_site')
    image_deux = models.FileField(upload_to='image_site')
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.descriptions
    
    
    
class About(models.Model):
    description = models.TextField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.description
    
    
class Website(models.Model):
    copyright = models.CharField(max_length=200)
    nom_Site = models.CharField(max_length=200)
    titre_Home = models.CharField(max_length=200)
    titre_About = models.CharField(max_length=200)
    email = models.EmailField()
    numero = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return self.nom_Site
    
    
class Gallery(models.Model):
    image = models.FileField(upload_to='image_site')
    description = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.description