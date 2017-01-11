from django import forms
from .models import Cursos,Document

class cursos(forms.ModelForm):
	class Meta:
		model=Cursos
		fields=['name','descripcion','imagen']

class capitulos(forms.ModelForm):
	class Meta:
		model=Document
		fields=['titulo','filename','descripcion','docfile']


