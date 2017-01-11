from django.db import models
from usuario.models import usuario
# Create your models here.
''' 

nombre
'''


class Cursos(models.Model):
	name = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(usuario,null=True, blank=True)
	imagen = models.ImageField(upload_to='imagenes/')
	codigo = models.CharField(max_length=5)
	

class Document(models.Model):
	titulo = models.CharField(max_length=100)
	codigo = models.CharField(max_length=5)
	descripcion = models.CharField(max_length=100)
	filename = models.CharField(max_length=100)
	curso = models.ForeignKey(Cursos,null=True, blank=True)
	docfile = models.FileField(upload_to='document/')



'''

https://blog.enriqueoriol.com/2014/07/upload-de-imagenes-con-django.html
'''
