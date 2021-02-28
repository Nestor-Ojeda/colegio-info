from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Contactos)
class ContactoAdmin(admin.ModelAdmin):
	pass
