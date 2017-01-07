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
	

class Document(models.Model):
	titulo = models.CharField(max_length=100)
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='document/%Y/%m/%d')



'''

https://blog.enriqueoriol.com/2014/07/upload-de-imagenes-con-django.html
'''
