
from django import forms
from .models import  usuario


class FormularioRegistro(forms.ModelForm):
	
	class Meta:
		model = usuario
		fields = ['username','password','email','first_name','last_name','dni','gender']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}
		
class FormularioContacto(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField()

