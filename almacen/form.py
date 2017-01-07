from django import forms
from .models import Cursos

class cursos(forms.ModelForm):
	class Meta:
		model=Cursos
		fields=['name','descripcion','imagen']

