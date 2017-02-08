
from django import forms
from .models import  usuario


class FormularioRegistro(forms.ModelForm):
	
	class Meta:
		model = usuario
		fields = ['username','password','email','first_name','last_name','dni','gender']    
		widgets = {
			'password':forms.PasswordInput(attrs = {'placeholder': 'Password','pattern':'.{7,32}','oninvalid':'this.setCustomValidity("Ingrese una contraseña mayor a 7 caracteres")'}),
            'username' : forms.TextInput(attrs = {'placeholder': 'Username','pattern':'[a-zA-Z0-9]{3,32}'}),
            'email'    : forms.EmailInput(attrs = {'placeholder': 'E-Mail','pattern':'[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{1,5}'}),
            'first_name':forms.TextInput(attrs = {'placeholder': 'Nombre','pattern':'[a-zA-Z0-9]{3,32}'}),
            'last_name':forms.TextInput(attrs = {'placeholder': 'Apellidos','pattern':'[a-zA-Z0-9]{3,32}'}),
            'dni':forms.NumberInput(attrs = {'placeholder': 'DNI','oninvalid':'this.setCustomValidity("Por favor ingrese  8 caracteres")','max':'99999999','min':'9999999'}),

		}

	def save(self, commit=True):
		user = super(FormularioRegistro, self).save(commit=False)
		if commit:
			user.is_active = False # No está activo hasta que active el vínculo de verificación
			user.save()	
		return user   

'''
YESNO = (
    ('Yes','Yes'),
    ('No', 'No'),
)'''
class FormularioContacto(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class':'form-control'}))
	correo = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class':'form-control'}))
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Mensaje a enviar','class':'form-control','rows':'5'}))
	#this is test
	#like = forms.ChoiceField(widget=forms.RadioSelect, choices=YESNO)
'''	
	correo = forms.EmailField()
	mensaje = forms.CharField()
'''

 
