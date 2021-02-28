from django.db import models

# Create your models here.

class Contactos(models.Model):
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	codigo_pais = models.IntegerField(max_length=3)
	codigo_area = models.IntegerField(max_length=5)
	numero	= models.IntegerField(max_length=15)

	def __str__(self):
		tex = "{0}-{1}-{2}-{3}-{4}"
		return tex.format(self.nombre, self.apellido, self.codigo_pais, self.codigo_area, self.numero)