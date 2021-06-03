from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('descriptions', 'image_un', 'image_deux', 'date_add', 'date_update', 'status')
    
    
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_add', 'date_update', 'status')
    
    
@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('copyright', 'nom_Site', 'titre_Home', 'titre_About', 'email', 'numero', 'date_add', 'date_update', 'status')



@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'date_add', 'date_update', 'status')