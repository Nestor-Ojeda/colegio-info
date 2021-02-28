from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TutorA, TutorB, Alumno )
class AlumnoAdmin(admin.ModelAdmin):
    pass







