from django.shortcuts import render, redirect
from . import models 
# from prestations import models as models_prestations


# Create your views here.
def index(request):
    home = models.Home.objects.filter(status=True).first()
    about = models.About.objects.filter(status=True).first()
    gallery = models.Gallery.objects.filter(status=True)
    return render(request, 'index.html', locals())