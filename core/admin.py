from django.contrib import admin
from .models import *

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'telefono', 'mensaje')
    ordering = ['id']
    
admin.site.register(DatosContacto, ContactoAdmin)
