from django import forms
from .models import Curso , Tema , Video ,Comment ,Categoria
#from .models import Cursos,Document,Comment

class CursoForm(forms.ModelForm):
	class Meta:
		model=Curso
		fields=['name','descripcion','imagen']

class TemaForm(forms.ModelForm):
	class Meta:
		model=Tema
		fields=['titulo','descripcion']
class VideoForm(forms.ModelForm):
	class Meta:
		model=Video
		fields=['filename','docfile']
class CategoriaForm(forms.ModelForm):
	class Meta:
		model=Categoria
		fields=['nombre']		
'''
class Formcapitulos(forms.ModelForm):
	class Meta:
		model=Document
		fields=['titulo','filename','descripcion','docfile']
'''
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user','email','body')

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user','email','body')	

'''
class Curso(models.Model):
	name = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(usuario,null=True, blank=True)
	imagen = models.ImageField(upload_to='imagenes/')
	codigo = models.CharField(max_length=5)
class Tema(models.Model):
	titulo = models.CharField(max_length=100)
	codigo = models.CharField(max_length=5)
	descripcion = models.CharField(max_length=100)
	curso = models.ForeignKey(Curso,null=True, blank=True)
class Video(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='document/')
'''