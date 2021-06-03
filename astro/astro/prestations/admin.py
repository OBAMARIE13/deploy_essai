from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'mail', 'company', 'date_add', 'date_update', 'status')
