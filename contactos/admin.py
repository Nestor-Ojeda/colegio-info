from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Contacto)
class EmpleadoAdmin(admin.ModelAdmin):
	pass


