
from django import forms
from .models import  usuario


class FormularioRegistro(forms.ModelForm):
	
	class Meta:
		model = usuario
		fields = ['username','password','email','first_name','last_name','dni','gender']    




		widgets = {
			'password':forms.PasswordInput(),
			
		}

	def save(self, commit=True):
		user = super(FormularioRegistro, self).save(commit=False)
		if commit:
			user.is_active = False # No está activo hasta que active el vínculo de verificación
			user.save()	
		return user   


class FormularioContacto(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField()

